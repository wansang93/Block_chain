import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title='업비트 거래 대시보드', layout='wide')

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'csv', 'history_all.csv')


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['created_at'] = pd.to_datetime(df['created_at'], utc=True)
    df['date'] = df['created_at'].dt.date
    df['year_month'] = df['created_at'].dt.to_period('M').astype(str)
    df['coin'] = df['market'].str.replace('KRW-', '').fillna(df['currency'])
    df['trade_amount'] = df['price'] * df['executed_volume']
    return df


df = load_data()
orders = df[df['type'] == 'order']
deposits = df[df['type'] == 'deposit']
withdrawals = df[df['type'] == 'withdraw']

# ── 사이드바 필터 ──────────────────────────────────────────
st.sidebar.title('필터')
coins = sorted(orders['coin'].dropna().unique())
selected_coins = st.sidebar.multiselect('코인', coins, default=coins)
date_min = df['created_at'].min().date()
date_max = df['created_at'].max().date()
date_range = st.sidebar.date_input('기간', [date_min, date_max], min_value=date_min, max_value=date_max)

filtered = orders[
    orders['coin'].isin(selected_coins) &
    (orders['created_at'].dt.date >= date_range[0]) &
    (orders['created_at'].dt.date <= date_range[1])
] if len(date_range) == 2 else orders[orders['coin'].isin(selected_coins)]

# ── 상단 요약 지표 ─────────────────────────────────────────
st.title('업비트 거래 대시보드')
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric('총 주문', f"{len(filtered):,}건")
c2.metric('매수', f"{len(filtered[filtered['side']=='bid']):,}건")
c3.metric('매도', f"{len(filtered[filtered['side']=='ask']):,}건")
c4.metric('총 수수료', f"₩{filtered['paid_fee'].sum():,.0f}")
c5.metric('총 거래금액', f"₩{filtered['trade_amount'].sum():,.0f}")

st.divider()

# ── Row 1: 월별 거래금액 / 코인별 거래 비중 ──────────────────
col1, col2 = st.columns([2, 1])

with col1:
    monthly = filtered.groupby(['year_month', 'side'])['trade_amount'].sum().reset_index()
    fig = px.bar(monthly, x='year_month', y='trade_amount', color='side',
                 color_discrete_map={'bid': '#3182CE', 'ask': '#E53E3E'},
                 labels={'year_month': '월', 'trade_amount': '거래금액(KRW)', 'side': ''},
                 title='월별 거래금액 (매수/매도)')
    fig.update_layout(legend=dict(orientation='h', y=1.1),
                      xaxis_tickangle=-45, height=380)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    coin_vol = filtered.groupby('coin')['trade_amount'].sum().nlargest(10).reset_index()
    fig2 = px.pie(coin_vol, names='coin', values='trade_amount',
                  title='코인별 거래 비중 (Top 10)', hole=0.4)
    fig2.update_layout(height=380)
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: 코인별 매수/매도 횟수 / 입출금 추이 ───────────────
col3, col4 = st.columns([1, 1])

with col3:
    cnt = filtered.groupby(['coin', 'side']).size().reset_index(name='count')
    top_coins = filtered.groupby('coin').size().nlargest(12).index
    cnt = cnt[cnt['coin'].isin(top_coins)]
    fig3 = px.bar(cnt, x='coin', y='count', color='side',
                  color_discrete_map={'bid': '#3182CE', 'ask': '#E53E3E'},
                  labels={'coin': '코인', 'count': '거래 횟수', 'side': ''},
                  title='코인별 매수/매도 횟수 (Top 12)')
    fig3.update_layout(legend=dict(orientation='h', y=1.1), height=380)
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    dep_m = deposits.groupby('year_month')['amount'].sum().reset_index()
    dep_m['구분'] = '입금'
    wit_m = withdrawals.groupby('year_month')['amount'].sum().reset_index()
    wit_m['구분'] = '출금'
    flow = pd.concat([dep_m, wit_m])
    fig4 = px.bar(flow, x='year_month', y='amount', color='구분',
                  color_discrete_map={'입금': '#38A169', '출금': '#DD6B20'},
                  labels={'year_month': '월', 'amount': '금액', '구분': ''},
                  title='월별 입출금 현황 (KRW)')
    fig4.update_layout(legend=dict(orientation='h', y=1.1),
                       xaxis_tickangle=-45, height=380)
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3: 수수료 추이 / 원본 테이블 ──────────────────────────
col5, col6 = st.columns([1, 2])

with col5:
    fee_m = filtered.groupby('year_month')['paid_fee'].sum().reset_index()
    fig5 = px.line(fee_m, x='year_month', y='paid_fee', markers=True,
                   labels={'year_month': '월', 'paid_fee': '수수료(KRW)'},
                   title='월별 수수료 추이')
    fig5.update_traces(line_color='#805AD5')
    fig5.update_layout(xaxis_tickangle=-45, height=320)
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.subheader('거래 내역')
    show_cols = ['created_at', 'type', 'coin', 'side', 'price', 'executed_volume', 'trade_amount', 'paid_fee']
    st.dataframe(
        filtered[show_cols].sort_values('created_at', ascending=False).head(200),
        use_container_width=True, height=320
    )
