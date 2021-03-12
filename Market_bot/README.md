# MyProject

목표: 프로젝트를 해서 좀 더 편리하고 쉽게 돈을 법니다.

- 210221 업데이트 예정
- 기본적인 API를 받아 알림 봇(Ver0.01)을 만들고 추후에 자동화 프로그램을 만든다.
- 거래소별 가격차이를 조사하고 시세차익으로 돈을 번다.
- 펀딩비를 지급하는 거래소에서 펀딩비를 받는다.

## 기술 순서

### 1. 본인 IP 주소를 알아낸다. for API에 전용 IP등록을 위해서

```pyhon
import requests
r = requests.get(r'http://jsonip.com')
ip= r.json()['ip']
print(ip)  # 182.219.90.***
```

### 2. 업비트 API KEY를 만든다. 링크 -> [https://www.upbit.com/mypage/open_api_management]

### 3. 간단한 값을 얻어온다. 시세, 계좌 조회 등등

```python
# 시세 종목 조회
import requests
url = "https://api.upbit.com/v1/market/all"
querystring = {"isDetails":"true"}
response = requests.request("GET", url, params=querystring)
print(response.text)
```

```python
# 계좌 조회
import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

payload = {
   'access_key': access_key,
   'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())
```

jwt token 이란?

- JSON Web Token의 약자
- 전자 서명 된 URL-safe (URL로 이용할 수있는 문자 만 구성된)의 JSON
> 참고 블로그 링크 -> [http://www.opennaru.com/opennaru-blog/jwt-json-web-token/](http://www.opennaru.com/opennaru-blog/jwt-json-web-token/)
