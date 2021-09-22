# Dynamic Programming 2 (동적계획법 2)

다이나믹 프로그래밍 유형 문제 위주로 뽑았습니다.

다이나믹 프로그래밍은 점화식을 세우면 절반 이상은 풀었다고 볼 수 있습니다.

점화식 세우는 건 금방 익히기 힘들어 코딩테스트에 나올만한 문제들,   
다이나믹 프로그래밍을 공부할만한 문제들을 최대한 뽑았습니다.

풀어보면 좋을 문제는 추천 문제에 체크(:heavy_check_mark:) 해놨습니다.

<br>

***❗️❗️꼭 문제를 순서대로 안풀어도 됩니다.❗️❗️***

[백준 문제집](https://www.acmicpc.net/workbook/view/7021)
|          순번          |        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        풀이 링크         |신규진|  정승훈 | 김윤형 | 강수민 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |:-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15724" target="_blank">15724</a> | <a href="https://www.acmicpc.net/problem/15724" target="_blank">주지수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9084" target="_blank">9084</a> | <a href="https://www.acmicpc.net/problem/9084" target="_blank">동전</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/12865" target="_blank">12865</a> | <a href="https://www.acmicpc.net/problem/12865" target="_blank">평범한 배낭</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      || | |:heavy_check_mark:|
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9251" target="_blank">9251</a> | <a href="https://www.acmicpc.net/problem/9251" target="_blank">LCS</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/dynamic_programming_2/9251">바로가기</a> || | |:heavy_check_mark:|
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2225" target="_blank">2225</a> | <a href="https://www.acmicpc.net/problem/2225" target="_blank">합분해</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/5557" target="_blank">5557</a> | <a href="https://www.acmicpc.net/problem/5557" target="_blank">1학년</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | <a href="./../solution/dynamic_programming_2/5557">바로가기</a> |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2631" target="_blank">2631</a> | <a href="https://www.acmicpc.net/problem/2631" target="_blank">줄세우기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2624" target="_blank">2624</a> | <a href="https://www.acmicpc.net/problem/2624" target="_blank">동전 바꿔주기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2228" target="_blank">2228</a> | <a href="https://www.acmicpc.net/problem/2228" target="_blank">구간 나누기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14567" target="_blank">14567</a> | <a href="https://www.acmicpc.net/problem/14567" target="_blank">선수과목 (Prerequisite)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17485" target="_blank">17485</a> | <a href="https://www.acmicpc.net/problem/17485" target="_blank">진우의 달 여행 (Large)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2073" target="_blank">2073</a> | <a href="https://www.acmicpc.net/problem/2073" target="_blank">수도배관공사</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18427" target="_blank">18427</a> | <a href="https://www.acmicpc.net/problem/18427" target="_blank">함께 블록 쌓기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1915" target="_blank">1915</a> | <a href="https://www.acmicpc.net/problem/1915" target="_blank">가장 큰 정사각형</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2758" target="_blank">2758</a> | <a href="https://www.acmicpc.net/problem/2758" target="_blank">로또</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1520" target="_blank">1520</a> | <a href="https://www.acmicpc.net/problem/1520" target="_blank">내리막 길</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | <a href="./../solution/dynamic_programming_2/1520">바로가기</a> |
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2056" target="_blank">2056</a> | <a href="https://www.acmicpc.net/problem/2056" target="_blank">작업</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1695" target="_blank">1695</a> | <a href="https://www.acmicpc.net/problem/1695" target="_blank">팰린드롬 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20542" target="_blank">20542</a> | <a href="https://www.acmicpc.net/problem/20542" target="_blank">받아쓰기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21923" target="_blank">21923</a> | <a href="https://www.acmicpc.net/problem/21923" target="_blank">곡예 비행</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1005" target="_blank">1005</a> | <a href="https://www.acmicpc.net/problem/1005" target="_blank">ACM Craft</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> | <a href="./../solution/dynamic_programming_2/1005">바로가기</a> |
| 21 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11049" target="_blank">11049</a> | <a href="https://www.acmicpc.net/problem/11049" target="_blank">행렬 곱셈 순서</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1823" target="_blank">1823</a> | <a href="https://www.acmicpc.net/problem/1823" target="_blank">수확</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10942" target="_blank">10942</a> | <a href="https://www.acmicpc.net/problem/10942" target="_blank">팰린드롬?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |
| 24 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2629" target="_blank">2629</a> | <a href="https://www.acmicpc.net/problem/2629" target="_blank">양팔저울</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 25 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20181" target="_blank">20181</a> | <a href="https://www.acmicpc.net/problem/20181" target="_blank">꿈틀꿈틀 호석 애벌레 - 효율성</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 26 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/3687" target="_blank">3687</a> | <a href="https://www.acmicpc.net/problem/3687" target="_blank">성냥개비</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> | <a href="./../solution/dynamic_programming_2/3687">바로가기</a> |
| 27 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21942" target="_blank">21942</a> | <a href="https://www.acmicpc.net/problem/21942" target="_blank">부품 대여장</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
