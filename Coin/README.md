# Coin Market

- [Market Capitalization Ranking](https://cryptoslate.com/coins/)
- [국가별 거래량](https://www.coinhills.com/market/currency/)

## Korea Market

- [upbit](https://upbit.com/)

## Global Market

- [binance](https://www.binance.com/en/trade/BTC_USDT?layout=basic)

# BitCoin

## [비트코인 논문 해석](./bitcoin_white_paper.md)

## 비트코인의 동작 원리

- Basic principles
  - [Youtube: Techquickie Youtube: How Does Bitcoin Work?](https://www.youtube.com/watch?v=L-Qhv8kLESY&ab_channel=Techquickie)
  - [Youtube: 3Blue1Brown Youtube: But how does bitcoin actually work?](https://www.youtube.com/watch?v=bBC-nXj3Ng4&ab_channel=3Blue1Brown)
- [Youtube: How secure is 256 bit security?](https://www.youtube.com/watch?v=S9JGmA5_unY&ab_channel=3Blue1Brown)

## 비트코인의 단점

**다른 코인과 다른 치명적인 단점**

블록 생성에 대한 보상금으로 Bitcoin을 지급 -> 2140년경 모든 Bitcoin이 생성될 것으로 예측 -> 블록생성이 아닌 Trasaction fees로 보상이 바뀜 -> 블록체인의 안정성이 떨어짐
- 반론: 2140년이면 내가 저세상에 가있을 나이이다. 단점거리가 안된다.

<details>
<summary>비트코인 단점 자세히 보기</summary>
<div markdown="1">

> [출처 Googling: 비트코인의 단점](https://medium.com/@newfie7675/%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8%EC%9D%98-%EB%8B%A8%EC%A0%90-19ba5103563)

1) 속도:
비트코인을 거래하는데 소요되는 속도는 최소 10분이며, 몇 시간까지 걸리기도 한다. 그 이유는 위에서 언급한 바와 같이, 비트코인은 디지털 데이터를 화폐로 사용되기 위해, 암호해독에 참여하는 노드들이 랜덤하게 거래를 검증하는 메커니즘을 만들고, 10분에 한 번씩 검증된 작업이 장부에 기입되어 블록으로 만들어지며, 블록이 생성되면서 화폐도 발행되도록 설계되었다. 믿을 수 있는 화폐가 되기 위해 필요한 과정이지만, 이로 인해 거래 속도가 느려지게 되었다.
비트코인 네트워크의 초당 거래량(TPS: Transaction Per Second)은 6개로 페이팔의 193개와 비자의 24,000개보다 현저히 느리다.
또한 거래량이 많아지면 마치 명절의 고속도로 톨게이트처럼 병목현상이 나타나 몇 시간이 지나도 거래가 처리되지 않는 현상이 일어나고는 한다. 이러한 문제를 확장성(Scalability) 문제라고 하는데, 후에 확장성 문제와 제시된 해결책 및 각각의 장단점에 대해 살펴보도록 하겠다.

2) 가격변동성: 
위의 그림(생략)은 지난 1년간 비트코인의 가격 차트이고, 아래 그림은 달러와 원화의 환율 차트이다. 1 비트코인 최고가격인 19,818달러는 최저가격 3,227달러의 약 6배이며, 원화 1원의 최고가격 0.000949 달러는 최저가격 0.000872 달러 대비 약 8.8% 높다(비트코인에 비하면 원화가 얼마나 안정적인 화폐인지 알 수 있다.) 이처럼 비트코인의 가격은 안정적인 화폐로 사용되기에는 너무 변동폭이 크다. 이런 점 때문에 비트코인의 수많은 장점에도 불구하고 상인들은 비트코인을 지급수단으로 인정하지 않고 있다. 이런 단점을 보완하기 위해 법정화폐와 페깅된 스테이블코인(Stable Coin)이 생겨났는데 이에 대해서는 추후에 설명하도록 하겠다.

3) 프라이버시(익명성): 
개인들의 자금흐름은 정부가 개인들의 행동을 통제/감시하는데 가장 좋은 도구로 사용된다. 블록체인은 개인 명의의 계좌 대신, 익명의 주소를 사용하기 때문에 프라이버시가 보호된다고 생각되기 싶지만, 꼭 그렇지 만은 않다. 첫째, https://btc.com/ 에 모든 거래내역들이 공개되어 있기 때문에 주소만 입력하면 자산현황과 누구와 거래했고 자금의 출처가 어딘지까지 추적이 가능하다. 둘째, 익명의 주소와 개인정보를 연동하지 않았지만, 추적할 수 있는 방법이 있다. 거래를 신청한 IP주소를 추적할 수도 있고, 현금화를 위해 사용하는 거래소는 신원인증을 거치기 때문에 거래소가 제공하는 정보를 통해 출처를 알아낼 수도 있다. 2013년 FBI는 상기 방법을 이용해서 비트코인으로 마약을 거래하던 실크로드라는 웹사이트 운영자를 체포했다. 범죄자 추적에는 유리할 수 있지만 만약 일반인의 거래기록이 누구나 인터넷에서 볼 수 있도록 공개된다고 하면, 많은 사람들이 사용을 꺼릴 것이다. 이처럼 비트코인의 투명성은 많은 사람들이 사용하는 화폐가 되는데 걸림돌이 될 수 있다.

4) 에너지 소모: 
비트코인의 채굴을 위해 사용되는 컴퓨터들은 엄청난 양의 전력을 소모한다. 모건스탠리의 보고서에 따르면 가상화폐 채굴에 들어가는 전력량은 아르헨티나의 전력 소모량과 비슷하다고 한다. 일례로, 미국과 캐나다의 경계에 있는 나이아가라 폭포 주변에 마을들은, 수력발전으로 얻어진 전력을 저렴한 가격에 공급받는데, 비트코인 채굴장들이 모여들기 시작했다. 채굴장들이 소모하는 전력은 실제로 대단해서, 주민들의 전력 할당량이 부족하여 다른 지역에서 전력을 구매해야만 했다. 결국 시의회에서는 비트코인 채굴장의 영업허가를 내주지 않게 되었고, 이런 일은 전세계 여러 국가에서 일어나고 있는 일이다. 해킹이 불가능하도록 설계된 비트코인은 에너지 과다소모라는 의도치 못한 부작용을 야기했다.

- (+) 추가로 비트코인의 거래 한번은 약 300kg의 이산화탄소가 발생하고 이는 비자카드를 한번 긁는 것보다 75만 배 많은 양입니다.
- 반박: 비트코인만 그렇지 다른 코인들은 전기료를 많이 아끼게 할 수 있다. - 이더리움 만든사람

1) 느린 의사결정: 
탈중앙화된 화폐 발행은, 특정 국가나 기관 혹은 개인이 화폐정책에 대해 독단적으로 결정할 수 없다는 뜻이고, 필연적으로 정작 필요한 의사결정을 내려야 할 순간에 투표를 통해 결정해야해서, 업그레이드가 느리다는 단점이 생겼다.
위에서 설명한 것처럼 비트코인은 속도, 익명성 등 개선할 점들이 많다. ‘프로토콜’이라는 네트워크의 사용자들(노드) 간의 합의된 규칙을 바꾼다면 이러한 단점들을 개선할 수 있지만, 이를 위해서는 네트워크 참여자들간 투표를 통과해야 한다. 비트코인 개선안(BIP: Bitcoin Improvement Proposal)이 제안되면, 채굴자들은 채굴을 통해 개선안에 투표하거나 반대할 수 있다. 투표에 걸리는 시간이 길어지기 때문에, 필요한 개선안이 나와도 실제로 적용되기 까지는 상당히 오랜 시간이 걸리며, 이해관계에 의해 채택되지 않을 수도 있다.

- 소프트포크와 하드포크란?

  만약 합의에 이르게 되면, 채굴자들은 소프트웨어를 업데이트하여 채굴을 이어 나가면 되며, 네트워크는 하나로 유지된다. 이를 소프트포크(Soft fork)라고 하는데 MS 오피스 업데이트처럼 기능은 개선되지만 MS 오피스 2007에서 작성한 문서를 MS 오피스 2013에서 열람과 수정이 가능한 것과 동일한 원리이다.
  만약 합의에 이르지 못하게 되면 새로운 개선안에 찬성하지 못하는 채굴자들만 업데이트된 소프트웨어를 설치하여 채굴을 지속하게 되는데, 기존 네트워크의 프로토콜과 호환되지 못하므로 네트워크가 분리된다. 이를 하드포크(Hard fork)라고 하는데, 이렇게 되면 기존의 코인과 별도의 코인이 생성되며, 기존의 코인을 가지고 있던 사람들은 새로운 코인을 지급받게 된다. 예를 들면, 비트코인캐시는 비트코인에서 하드포크되어 나온 코인인데, 비트코인 보유자들은 1비트코인당 1비트코인캐시를 지급받았다.

6) 결말: 
이처럼 비트코인의 민주적인 의사결정 방식은 양날의 검처럼 뚜렷한 장점과 단점을 가진다. 현실세계의 여러 정치적 문제처럼, 참여자들의 이해관계로 인해 의사결정이 지연되며, 네트워크가 분리되는 것처럼 상황이 생기기도 한다.
“Democracy is the worst form of government except for all other forms that have been tried”. Winston Churchill이 말해서 유명해진 quote인데, “민주주의는 최악의 통치형태이다, 이미 시도해본 다른 통치방식을 제외하면” 정도로 해석할 수 있다.
비트코인은 탈중앙화된 governance와 보안성을 위해 속도를 포기하고, 채굴에 많은 에너지를 쓰도록 하였으며, 투표를 통해 의사결정이 되기 때문에 의사결정이 복잡하고 느리다. 그래서 화폐라고 하기에는 거래 처리속도가 아주 느리고, 정부와 같은 중앙화된 주체가 시장에 적극 개입하여 환율을 조정하거나 화폐발행을 통해 가격을 조정하지 않아서 가격 변동성 또한 높다.
누군가가 얘기한것 처럼 비트코인이 ‘가장 난해하고 우아한 사기사건’으로 후대에 회자될지, 자정능력을 통해 mainstream에 인정받는 안정적인 자산으로 자리잡을지는, 시간이 지나야만 알 수 있을 듯하다.
비트코인의 단점들을 살펴보았는데, 단점들을 보완하기 위한 코인들이 생겨났으며, 지금도 계속 생겨나고 있다. 다음 편에서는 비트코인의 후속 코인들의 소개와 어떻게 단점을 보완하는지를 알아보도록 하겠다.

</div>
</details>

# 여러가지 코인

비트코인의 단점을 개선하거나 다른 방식의 경쟁력 있는 코인들 입니다.

## 이더리움(Ethereum/ETH)

이더리움 동작 원리 -> [프로그래머스: 이더리움 입문 바이블](https://programmers.co.kr/learn/courses/7322)

## 폴카닷(Polkadot/DOT)

## 에이다(Cardano/ADA)

## 바이낸스 코인(BNB/BNB)

- 시총이 올라갈 것으로 예상되는 저만의 코인 리스트입니다.
  - 앵커(ANKR), 질리카(ZIL)

# 생각나는대로 적기

1. 저는 업으로 시드를 만들고 투자로 돈을 법니다.
2. 투자와 투기의 가장 큰 차이점은 원칙과 가치관과 지식이라고 생각합니다.
   - 저의 가치관 중 하나는 투자는 돈을 버는 것 뿐만 아니라 리스크를 줄이는 방향으로 가야합니다.
3. 코인에 대한 지식은 책과 검색으로 공부합니다.
   1. 월가의 영웅 가치투자를 읽습니다.(투자 관련 추천책)
   2. 무엇인지 알고 삽니다.(현재는 시드가 작기 때문에 리스크에 대한 공부를 합니다.)
      > DO NOT buy what you DO NOT understand.
      - 비트코인의 기술력과 장단점을 파악합니다.(논문 읽기, 기사 찾기 하루 1시간 공부)

목표: 투자로 2의 n승으로 벌 수 있습니다. [링크](https://github.com/wansang93/TIL/blob/master/2020-09/200926.md)
- 현재는 매우 비현실적인 부분입니다. 무언가의 깨닳음이 있다면 가능하다고 믿습니다.

비트코인에 대해 부정적으로 생각하는 사람들에게!

우선 왜 부정적인지에 대해 생각해야 합니다.
- 만약 막연한 거부감 때문이라면 다르게 생각해 보세요. 초창기 TV가 처음나오는 시절 연예인이나 배우라는 직업은 과거의 광대와 같은 웃음거리라는 취급을 받았다고 합니다. 하지만 20~30년 후에는 더 발전하여 K-PoP의 주역이자 Entertainer 등 멋진 직업이 되었죠. 저의 청년기에 인기였던 아프리카 VJ라는 직업은 별풍선에 의존하는 안좋은 인식들이 현재 유튜버나 VJ 등의 방송사 플랫폼을 이용하는 거대 수익이라는 꿈의 직장이 됬죠. 다음 시장은 어디일까요? 저는 비트코인이라고 생각합니다. 언젠가 비트코인 플랫폼을 만들어보고 싶습니다.
- 만약 도박이라고 생각한다면 다르게 생각해 보세요. 저의 가치관과 연결된 문제라 사람마다 생각이 다를 수 있지만 저의 생각은 이렇습니다. 현대 금융 시스템에서 화폐는 절대 가치가 존재하지 않습니다. 극단적인 예시로 한국이 전쟁이 난다면 원화는 종이조가리가 될 수 있습니다. 원화를 가지고 있는 사람들의 시스템이 붕괴되는 순간 원화를 가지고 있는 것이 오히려 가치가 없는 화폐를 가지고 있는겁니다. 비트코인은 분명히 기술력과 산업이 만난 아름다운 조합인 가 같습니다.(더 공부해 봐야함) 해결할 수 있는 부분을 블록체인이라는 기술로 해결하고 그 블록 생성자에 대한 보상으로 코인을 지급하고 이 코인이 하나의 상품의 역할을 하고 있다고 생각합니다. 다른 예시로 게임 아이템은 확률입니다. 게임 아이템을 비싸게 파는 사람들은 운이 좋아서 좋은 아이템이 나와서 비싸게 파는 것 입니다. 하지만 이는 일부이고 확률게임이 도박게임이다 라고 보는 것과 비슷하다고 생각합니다.

## 비트코인이 왜 비쌀까요?

### 전문가의 생각

- [Youtube: 비트코인이 폭등하는 이유 8가지](https://www.youtube.com/watch?v=d-HhGW5ctWQ&ab_channel=815%EB%A8%B8%EB%8B%88%ED%86%A1)
  1. 제도금융권, 가상자산(암호화폐) 시장 진입 확대: 인식이 변화된 사회, 시장의 긍정적 반응들
  2. 페이팔 효과: 지구 최대 규모의 거래 업체인 페이팔이 암호화폐 거래지원을 함
  3. 바이든 효과: 달러 가치 하락, 재정 확대 -> 유동성 급증, 저금리 기조, 부자 증세, 실질 인플레이션 증가
  4. 차기 정부, 법인세 7% 인상과 장기보유주식에 대한 양도세 증가 -> 주식 자금의 이동
  5. 자사주 매입 감소: 바이백의 매력이 떨어져 비트코인으로 자금 이동
  6. 미국 브룩스 틍화감독청장, 기존 금융과 가상자산 융합 추진
  7. 디지털화폐 도입되면 암호화폐 사용 증가 -> 양성화할 수 없는 지하자금 상존, 디지털 금으로서 가치
  8. 공급 부족: 중국의 암호호폐 장외거래 집중 단속: 채굴꾼의 74%가 암호화폐 현금화 차질, 수요 증가와 공급 감소의 동시 발생

### 개인적으로 생각

하기에 매우 이상적인 **투자 상품**(화폐x, 잠재적 화폐 기능)이기 때문입니다.
- 이유1: 수요가 늘어날 것
- 이유2: 그러나 공급량은 한정적인 것
- 이유3: 가격을 상승시키는 주체가 명확, 강력한 자금력을 갖고 있을 것

1. 수요가 늘어날 것
   
   비트코인의 구조 상 수요가 늘수 밖에 없다고 생각합니다.
   - 이유1: 비트코인은 안전자산입니다. 안전자산은 수요가 늘 수 밖에 없습니다. 안전자산이란 투자에 따른 위험이 매우 적은 금융자산을 뜻합니다.
     - 근거1: 달러는 세계 통화 중에 기축 통화를 담당하고 있습니다. 비트코인은 세계 코인중에 기축 코인을 담당합니다. 거의 대부분의 코인 마켓에서는 비트코인으로 다른 코인을 구매할 수 있습니다.(예시로 옛날엔 쌀로 모든 물건을 살 수 있는 원리와 비슷합니다.) 이러한 이유로 코인중에 제일 변동성이 작은 코인(법이 만들어 질 수 있거나 수요 층이 안정화가 된다면)이 먼 훗날 될꺼라고 생각합니다.
     - 반박근거1: 안전자산이 아닌 이유, 시장가격의 변동의 위험이 큰 상품입니다. 주식시장과 다르게 상한과 하한이 없고 수요 공급의 원칙으로 가격이 변동하기 때문에 이론적으로는 무제한으로 가격이 오르고 내릴 수 있습니다.
     - 근거2: 불안전한 금융기관에 대한 불신을 없엘 수 있는 달러의 대체제입니다.
       - 예시1: 베네수엘라나 나이지리아(2021년 기사 기준)는 자국의 금융기관에 대한 불신이 있습니다. 말이 안되는 인플레이션이나 통화 가치 평가절하를 하면 화폐의 가치가 흔들리고 위협을 받습니다. 따라서 사람들은 화폐의 기능을 상실해 자국의 화폐보다는 안전자산인 달러나 금을 선호하게 되는데 이 포지션을 훗날에는 비트코인이 담당합니다. 이유는 손쉽게 구할 수 있는 플랫폼들의 개발로 인한 접근성이 달러와 금에 비해 비교가 안되게 뛰어나기 때문입니다. 이 화폐는 거래에 있어서 기본이 되는 화폐가 됩니다.
   - 이유2: 제 3자 기관이 없는 거래 방법의 장점
     - 원리1: 비트코인의 핵심기술은 분산 서비스 시스템이기 때문에 제 3자가 관여하지 않아도 네트워크에 있는 사람들의 인증을 합리화하기 때문에 제 3자 기관이 관여하지 않는 민주적인 거래 시스템입니다.
     - 근거1: 미국의 이란의 제제나 중국의 자국보호무역에 따른 은행의 자금동결과 무역전쟁 등으로 일어난 화폐 시스템은 비민주적인 시스템입니다. 이러한 점에서 주요 글로벌 기업들은 은행에 돈을 넣는것보다 코인이라는 중간 매개체를 이용해서 자금을 이동시키기에 최적화된 방법입니다.
     - 반박근거1: 제 3자 기관이 관여하지 않기 때문에 가격 변동성이 지나치게 높아 화폐의 기능을 상실하고 오직 상품으로써의 가치만 지닐 수 있습니다.

2. 그러나 공급량은 한정적인 것
   - 비트코인의 총 공급량은 21,000,000(2천1백만)개 입니다. 금과 은처럼 공급량이 한정적입니다.

3. 가격을 상승시키는 주체가 명확, 강력한 자금력을 갖고 있을 것
   - 근거1: 코인 거래의 대부분이 미국 자본(61%)입니다. 역설로 유럽 자본(개인 및 기업)이 들어온다면 가격이 더 오를꺼라고 생각합니다. 더 나아가 20~30년 후의 경제 세계 경제 주체가 될 가능성이 있는 아프리카의 IT 발달은 코인에 대한 영향력을 더 증가할 것입니다.
   - 근거2: 테슬라가 코인을 샀습니다. 주요 미국 IT 기업들이 코인에 대한 비전을 밝게 보고 있으며 금융 쪽에서는 투자 상품화를 통해 수익을 내려고 있습니다. 2010년 이래로 10년간 최고의 금융 상품인것은 분명합니다. 현재 2021년 3월 기준 조바이든의 인사팀들은 암호화폐를 매우 긍정적으로 바라보고 있습니다.[googling: anthony scaramucci(미국 선임 경제고문) bitcoin](https://www.google.com/search?newwindow=1&biw=1331&bih=722&tbm=nws&ei=hxNLYJvAJJCmmAXp3I34BQ&q=anthony+scaramucci+bitcoin&oq=anthony+scaramucci+bitcoin&gs_l=psy-ab.3...24690.24690.0.25591.1.1.0.0.0.0.85.85.1.1.0....0...1c.1.64.psy-ab..0.0.0....0.71gHomT6jkE)
   - 근거3: (뇌피셜)부자들에게 가장 큰 이슈는 세금문제입니다. [세금 이슈 유튜브 링크](https://www.youtube.com/watch?v=VozZk8A5rhM&ab_channel=%EA%B7%B8%EB%A6%BF%EC%98%81%EC%96%B4TV) 어느날 누군가가 당신에게 20%의 돈을 때간다고 생각해보세요. 부자들은 100억, 1000억 단위의 돈이 있는데 그중에 20억, 200억이 없어진다고 생각하면 그 부자들은 자신의 돈을 지키려고 합니다. 세금을 피하는 방법은 다양하게 있습니다. 그 중에 하나가 코인시장이 될 가능성이 있습니다. 마치 금고안에 금을 현물로 보유하면 세금의 추적이 어려운 원리입니다. 이들은 강력한 자금력을 가지고 20%의 등락폭보다 적은 코인이 있다면 충분히 변동성을 감안하고도 코인에 대한 수요를 아끼지 않을 것 같습니다. 이와같은 자금추적 문제 때문에 거래소에 대한 규제와 법이 마련되었고 또 개정될 것 같습니다.
   - 근거3-2: 북한의 해커단체는 자금을 블록체인 암호화폐로 받습니다. 그 중에 모네로(Monero)라는 다크코인이 있습니다. 해커들이 가장 사랑하는 화폐 중 하나입니다. [유튜브 링크: 암호화폐 다크웹](https://www.youtube.com/watch?v=KzHh_29U5Ak&ab_channel=tvN%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8)

또다른 이유
- 이유4: 다른 투자상품보다의 과평가, 주식 시장에 대한 세금 부과에 따른 자금의 이동

## 비트코인의 사회적 시각

전문가와 법률가 등의 시각
- [Youtube: 비트코인 돌멩이인가 신화폐인가? 세미나](https://www.youtube.com/watch?v=OGgtyDrYHAs&ab_channel=%EA%B5%AD%EA%B0%80%EB%AF%B8%EB%9E%98%EC%97%B0%EA%B5%AC%EC%9B%90)

전문가가 설명하는 비트코인의 기술력과 기술 이슈들

- [Youtube: 쉽게 설명하는 블록체인 강의: 정은진 샌프란시스코 부교수](https://www.youtube.com/watch?v=kl5pkhbqz3k&ab_channel=EO)
- [Youtube: 김승주 고려대 교수, 블록체인 기술의 이해와 활용사례](https://www.youtube.com/watch?v=MDRF4PMWdsg&ab_channel=KISDI%EC%A0%95%EB%B3%B4%ED%86%B5%EC%8B%A0%EC%A0%95%EC%B1%85%EC%97%B0%EA%B5%AC%EC%9B%90)
- [Youtube: 김승주 고려대 교수, 4차 산업혁명은 왜 블록체인을 찾는가 3편 구성](https://www.youtube.com/watch?v=Qkwd1vjxG0g&ab_channel=%EB%89%B4%EC%8A%A4%EC%9B%A8%EC%9D%B4TV)
