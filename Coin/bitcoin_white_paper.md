# Bitcoin: A Peer-to-Peer Electronic Cash System

- 21.03.12 ~ 

논문을 해석해봤습니다. 논문 링크 -> [https://bitcoin.org/en/bitcoin-paper](https://bitcoin.org/en/bitcoin-paper)

```
Satoshi Nakamoto
satoshin@gmx.com
www.bitcoin.org
```

## 3분 요약

중요한 내용이라는 부분만 요약해봤습니다.(진행 중)

```
초록
비트코인(bitcoin: P2P 방식의 전자 화폐)은 금융 기관이 없어도 거래가 가능합니다.
비트코인이 기존 은행들(디지털 서명방식)의 이중 지출 문제를 대신 해결합니다.
비트코인의 핵심 기술(해시 기반의 작업 증명(proof-of-work) 방식)을 이용해 네트워크의 기록을 생성(timestamps)하고
작업 증명 방식을 재작동하지 않으면 바꿀수 없는 기록으로 만듭니다.
가장 긴 체인(chain)은 발생된 이벤트(기록)들의 순서에 대한 증명을 합니다.
가장 긴 작업 증명 체인이 그들이 없는 동안에 발생한 일의 증거로 채택됩니다.
```

# 비트코인: P2P 전자 화폐 시스템

## Abstract(개요)

```
Abstract.
A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending.
We propose a solution to the double-spending problem using a peer-to-peer network.
The network timestamps transactions by hashing them into an ongoing chain of hash-based proof-of-work, forming a record that cannot be changed without redoing the proof-of-work. The longest chain not only serves as proof of the sequence of events witnessed, but proof that it came from the largest pool of CPU power.
As long as a majority of CPU power is controlled by nodes that are not cooperating to attack the network, they'll generate the longest chain and outpace attackers.
The network itself requires minimal structure. Messages are broadcast on a best effort basis, and nodes can leave and rejoin the network at will, accepting the longest proof-of-work chain as proof of what happened while they were gone.
```

```
순수 P2P(Peer-to-Peer) 방식의 전자 화폐는 한 쪽에서 다른 쪽으로 금융 기관 없이 온라인 거래(payments)를 가능하게 합니다.
디지털 서명(Digital signatures)은 솔루션의 일부를 제공하지만, 신뢰 가능한 제3자가 이중 지출(Double-spending)을 방지해야 하는 경우에는 이러한 주요 이점이 없어집니다.
우리는 이중 지출(Double-spending)의 문제를 P2P 방식을 사용해서 해결책을 제안합니다.
네트워크는 거래들을 해시 기반 작업의 증명의 체인(chain of hash-based proof-of-work(mining))으로 해싱해서 기록해 그 작업증명을 다시 하지 않고는 변경할 수 없는 기록을 만듭니다.
가장 긴 체인(chain)은 발생된 이벤트(기록)들의 순서에 대한 증명을 하고 또 가장 큰 CPU 파워에서 나왔다는 것을 증명합니다.
과반수의 CPU 파워가 네트워크 공격에 협력하지 않은 노드들에 의해 제어하지 않는 한(51% 공격이 없는 한) 그들(네트워크 노드들)이 가장 긴 체인을 생성하고 공격자보다 앞서나갑니다.
그 네트워크는 최소한의 구조로만을 요구합니다. 최대로 가능한 한도 내에서(on a best effort basis) 브로드캐스트(broadcast)가 되며 노드들이 마음대로 떠나거나 재가입할 수 있고, 가장 긴 작업 증명 체인이 그들이 없는 동안에 발생한 일의 증거로 채택됩니다.
```

