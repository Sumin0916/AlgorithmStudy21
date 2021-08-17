# Brute Force (완전탐색)


풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

추천 문제 아닌 나머지는 나머지를 난이도 섞었습니다.

완전탐색 중 백트래킹 있었던 문제와 최대한 겹치지 않도록 했습니다.

다른 알고리즘 풀었어도 완전탐색으로 풀어보시면 좋습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7271)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |신규진| 정승훈 | 김윤형 | 강수민 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2798" target="_blank">2798</a> | <a href="https://www.acmicpc.net/problem/2798" target="_blank">블랙잭</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> | <a href="./../solution/brute_force/2798">바로가기</a> |:heavy_check_mark:
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2231" target="_blank">2231</a> | <a href="https://www.acmicpc.net/problem/2231" target="_blank">분해합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> | <a href="./../solution/brute_force/2231">바로가기</a> |:heavy_check_mark:
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/19532" target="_blank">19532</a> | <a href="https://www.acmicpc.net/problem/19532" target="_blank">수학은 비대면강의입니다</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> | <a href="./../solution/brute_force/19532">바로가기</a> |:heavy_check_mark: 
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18312" target="_blank">18312</a> | <a href="https://www.acmicpc.net/problem/18312" target="_blank">시각</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> | <a href="./../solution/brute_force/18312">바로가기</a> |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15721" target="_blank">15721</a> | <a href="https://www.acmicpc.net/problem/15721" target="_blank">번데기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/5.svg"/> | <a href="./../solution/brute_force/15721">바로가기</a> |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1969" target="_blank">1969</a> | <a href="https://www.acmicpc.net/problem/1969" target="_blank">DNA</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/1969">바로가기</a> |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2503" target="_blank">2503</a> | <a href="https://www.acmicpc.net/problem/2503" target="_blank">숫자 야구</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/2503">바로가기</a> |
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2422" target="_blank">2422</a> | <a href="https://www.acmicpc.net/problem/2422" target="_blank">한윤정이 이탈리아에 가서 아이스크림을 사먹는데</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/2422">바로가기</a> |
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17626" target="_blank">17626</a> | <a href="https://www.acmicpc.net/problem/17626" target="_blank">Four Squares</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/17626">바로가기</a> |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/5568" target="_blank">5568</a> | <a href="https://www.acmicpc.net/problem/5568" target="_blank">카드 놓기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/5568">바로가기</a> |
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18511" target="_blank">18511</a> | <a href="https://www.acmicpc.net/problem/18511" target="_blank">큰 수 구성하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/18511">바로가기</a> |
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9079" target="_blank">9079</a> | <a href="https://www.acmicpc.net/problem/9079" target="_blank">동전 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | <a href="./../solution/brute_force/9079">바로가기</a> |
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14501" target="_blank">14501</a> | <a href="https://www.acmicpc.net/problem/14501" target="_blank">퇴사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      |:heavy_check_mark:
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16937" target="_blank">16937</a> | <a href="https://www.acmicpc.net/problem/16937" target="_blank">두 스티커</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16439" target="_blank">16439</a> | <a href="https://www.acmicpc.net/problem/16439" target="_blank">치킨치킨치킨</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | <a href="./../solution/brute_force/16439">바로가기</a> |
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2615" target="_blank">2615</a> | <a href="https://www.acmicpc.net/problem/2615" target="_blank">오목</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16508" target="_blank">16508</a> | <a href="https://www.acmicpc.net/problem/16508" target="_blank">전공책</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14620" target="_blank">14620</a> | <a href="https://www.acmicpc.net/problem/14620" target="_blank">꽃길</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/12919" target="_blank">12919</a> | <a href="https://www.acmicpc.net/problem/12919" target="_blank">A와 B 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1548" target="_blank">1548</a> | <a href="https://www.acmicpc.net/problem/1548" target="_blank">부분 삼각 수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2961" target="_blank">2961</a> | <a href="https://www.acmicpc.net/problem/2961" target="_blank">도영이가 만든 맛있는 음식</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15661" target="_blank">15661</a> | <a href="https://www.acmicpc.net/problem/15661" target="_blank">링크와 스타트</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1025" target="_blank">1025</a> | <a href="https://www.acmicpc.net/problem/1025" target="_blank">제곱수 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14500" target="_blank">14500</a> | <a href="https://www.acmicpc.net/problem/14500" target="_blank">테트로미노</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/brute_force/14500">바로가기</a> |
| 24 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15686" target="_blank">15686</a> | <a href="https://www.acmicpc.net/problem/15686" target="_blank">치킨 배달</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |:heavy_check_mark:
| 25 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21278" target="_blank">21278</a> | <a href="https://www.acmicpc.net/problem/21278" target="_blank">호석이 두 마리 치킨</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 26 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21315" target="_blank">21315</a> | <a href="https://www.acmicpc.net/problem/21315" target="_blank">카드 섞기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 27 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16637" target="_blank">16637</a> | <a href="https://www.acmicpc.net/problem/16637" target="_blank">괄호 추가하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 28 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14391" target="_blank">14391</a> | <a href="https://www.acmicpc.net/problem/14391" target="_blank">종이 조각</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 29 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18808" target="_blank">18808</a> | <a href="https://www.acmicpc.net/problem/18808" target="_blank">스티커 붙이기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 30 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21943" target="_blank">21943</a> | <a href="https://www.acmicpc.net/problem/21943" target="_blank">연산 최대로</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |

출처:https://github.com/tony9402/baekjoon
