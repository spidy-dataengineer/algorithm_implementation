# Time Complexity
* __Big-O__: 가장 빠르게 증가하는 항만을 고려하는 표기법
  * O(1): 상수 시간(Constant time)
  * O(logN): 로그 시간(Log time)
  * O(N): 선형 시간
  * O(NlogN): 로그 선형 시간
  * O(N제곱): 이차 시간
  * O(N세제곱): 삼차 시간
  * O(2N제곱): 지수 시간

N이 1000일 때의 연산 횟수
* O(N): 1,000 
* O(NlogN): 10,000 
* O(N제곱): 1,000,000
* O(N세제곱): 1,000,000,000

* N의 범위가 500인 경우: 시간 복잡도가 O(N세제곱)인 알고리즘 설계
* N의 범위가 2,000인 경우: 시간 복잡도가 O(N제곱)인 알고리즘 설계
* N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘 설계
* N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘 설계

____________________________
# Space Complexity
* __Big-O__: O(NlogN), O(N제곱)등으로 표기
* 메모리 사용량에도 절대적인 제한이 있고, 일반적으로 메모리 사용량 기준은 MB단위

코딩 테스트 대부분 리스트(배열)을 사용해서 풀어야 함
* int a[1000]: 4KB
* int a[1000000]: 4MB
* int a[2000][2000]: 16MB

____________________________
![알고리즘 코딩 테스트 유형 분석](https://www.hanbit.co.kr/data/editor/20200918163925_xyypndmo.png)