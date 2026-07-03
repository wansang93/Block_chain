import os
import jwt
import uuid
import hashlib
import requests
import urllib3
import pandas as pd
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ACCESS_KEY = os.environ.get('UPBIT_ACCESS_KEY', '')
SECRET_KEY = os.environ.get('UPBIT_SECRET_KEY', '')
SERVER_URL = 'https://api.upbit.com'
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
CSV_DIR = os.path.join(DATA_DIR, 'csv')
PARQUET_DIR = os.path.join(DATA_DIR, 'parquet')


def get_auth_header(params=None):
    payload = {
        'access_key': ACCESS_KEY,
        'nonce': str(uuid.uuid4()),
    }
    if params:
        query_string = urlencode(params).encode()
        m = hashlib.sha512()
        m.update(query_string)
        payload['query_hash'] = m.hexdigest()
        payload['query_hash_alg'] = 'SHA512'

    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    if isinstance(jwt_token, bytes):
        jwt_token = jwt_token.decode('utf-8')
    return {'Authorization': f'Bearer {jwt_token}'}


def fetch_all(endpoint, extra_params=None):
    results = []
    page = 1
    limit = 100
    while True:
        params = {'limit': limit, 'page': page}
        if extra_params:
            params.update(extra_params)
        headers = get_auth_header(params)
        res = requests.get(f'{SERVER_URL}{endpoint}', headers=headers, params=params, verify=False)
        res.raise_for_status()
        batch = res.json()
        if not batch:
            break
        results.extend(batch)
        print(f'  {endpoint} page {page}: {len(batch)}건', end='\r')
        if len(batch) < limit:
            break
        page += 1
    print()
    return results


def get_orders():
    return fetch_all('/v1/orders', {'state': 'done'})


def get_withdrawals():
    return fetch_all('/v1/withdraws')


def get_deposits():
    return fetch_all('/v1/deposits')


def save(data, name):
    os.makedirs(CSV_DIR, exist_ok=True)
    os.makedirs(PARQUET_DIR, exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(CSV_DIR, f'{name}.csv'), index=False, encoding='utf-8-sig')
    df.to_parquet(os.path.join(PARQUET_DIR, f'{name}.parquet'), index=False)
    print(f'{name}: {len(df)}건 저장 완료')


def merge_and_save(orders, withdrawals, deposits):
    df_orders = pd.DataFrame(orders)
    df_orders['type'] = 'order'

    combined = pd.concat([df_orders, pd.DataFrame(withdrawals), pd.DataFrame(deposits)], ignore_index=True)
    combined['created_at'] = pd.to_datetime(combined['created_at'], utc=True)
    combined = combined.sort_values('created_at').reset_index(drop=True)

    combined.to_csv(os.path.join(CSV_DIR, 'history_all.csv'), index=False, encoding='utf-8-sig')
    combined.to_parquet(os.path.join(PARQUET_DIR, 'history_all.parquet'), index=False)
    print(f'history_all: {len(combined)}건 저장 완료')

    export_json(combined)


def export_json(df):
    df = df.copy()
    df['created_at'] = df['created_at'].astype(str)
    df['coin'] = df['market'].str.replace('KRW-', '', regex=False).fillna(df['currency'])
    df['trade_amount'] = (df['price'].fillna(0) * df['executed_volume'].fillna(0)).round(0)
    cols = ['created_at', 'type', 'coin', 'side', 'price', 'executed_volume',
            'trade_amount', 'paid_fee', 'amount', 'currency', 'state']
    out = df[[c for c in cols if c in df.columns]].fillna('').to_dict(orient='records')

    json_dir = os.path.join(DATA_DIR, 'json')
    os.makedirs(json_dir, exist_ok=True)
    import json
    with open(os.path.join(json_dir, 'history_all.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False)
    print(f'history_all.json: {len(out)}건 저장 완료')


if __name__ == '__main__':
    if not ACCESS_KEY or not SECRET_KEY:
        print("환경변수를 설정해주세요:")
        print("  $env:UPBIT_ACCESS_KEY='your_access_key'")
        print("  $env:UPBIT_SECRET_KEY='your_secret_key'")
        exit(1)

    print('주문 내역 수집 중...')
    orders = get_orders()
    print('출금 내역 수집 중...')
    withdrawals = get_withdrawals()
    print('입금 내역 수집 중...')
    deposits = get_deposits()

    save(orders, 'orders')
    save(withdrawals, 'withdrawals')
    save(deposits, 'deposits')
    merge_and_save(orders, withdrawals, deposits)
