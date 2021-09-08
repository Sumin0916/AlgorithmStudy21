# Binary Search (이분탐색)

[메인으로 돌아가기](https://github.com/tony9402/baekjoon)

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7277)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         | 신규진 | 정승훈 | 김윤형 | 강수민 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2417" target="_blank">2417</a> | <a href="https://www.acmicpc.net/problem/2417" target="_blank">정수 제곱근</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/binary_search/2417">바로가기</a> | :heavy_check_mark: 
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10815" target="_blank">10815</a> | <a href="https://www.acmicpc.net/problem/10815" target="_blank">숫자 카드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | <a href="./../solution/binary_search/10815">바로가기</a> | :heavy_check_mark: 
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2805" target="_blank">2805</a> | <a href="https://www.acmicpc.net/problem/2805" target="_blank">나무 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | <a href="./../solution/binary_search/2805">바로가기</a> | :heavy_check_mark: 
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1654" target="_blank">1654</a> | <a href="https://www.acmicpc.net/problem/1654" target="_blank">랜선 자르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | <a href="./../solution/binary_search/1654">바로가기</a> | :heavy_check_mark: 
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2512" target="_blank">2512</a> | <a href="https://www.acmicpc.net/problem/2512" target="_blank">예산</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | <a href="./../solution/binary_search/2512">바로가기</a> | :heavy_check_mark: 
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/19637" target="_blank">19637</a> | <a href="https://www.acmicpc.net/problem/19637" target="_blank">IF문 좀 대신 써줘</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | <a href="./../solution/binary_search/19637">바로가기</a> |:heavy_check_mark:
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11663" target="_blank">11663</a> | <a href="https://www.acmicpc.net/problem/11663" target="_blank">선분 위의 점</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |:heavy_check_mark: 
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2110" target="_blank">2110</a> | <a href="https://www.acmicpc.net/problem/2110" target="_blank">공유기 설치</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      | :heavy_check_mark: 
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/3079" target="_blank">3079</a> | <a href="https://www.acmicpc.net/problem/3079" target="_blank">입국심사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |:heavy_check_mark: 
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2470" target="_blank">2470</a> | <a href="https://www.acmicpc.net/problem/2470" target="_blank">두 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |:heavy_check_mark: 
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20444" target="_blank">20444</a> | <a href="https://www.acmicpc.net/problem/20444" target="_blank">색종이와 가위</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      | :heavy_check_mark:
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1477" target="_blank">1477</a> | <a href="https://www.acmicpc.net/problem/1477" target="_blank">휴게소 세우기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1939" target="_blank">1939</a> | <a href="https://www.acmicpc.net/problem/1939" target="_blank">중량제한</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2473" target="_blank">2473</a> | <a href="https://www.acmicpc.net/problem/2473" target="_blank">세 용액</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/13397" target="_blank">13397</a> | <a href="https://www.acmicpc.net/problem/13397" target="_blank">구간 나누기 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2412" target="_blank">2412</a> | <a href="https://www.acmicpc.net/problem/2412" target="_blank">암벽 등반</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1300" target="_blank">1300</a> | <a href="https://www.acmicpc.net/problem/1300" target="_blank">K번째 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/7453" target="_blank">7453</a> | <a href="https://www.acmicpc.net/problem/7453" target="_blank">합이 0인 네 정수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
