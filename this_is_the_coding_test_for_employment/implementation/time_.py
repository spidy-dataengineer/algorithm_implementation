"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
단순히 시각을 1씩 증가시키면서 포함되는 지 확인 -> 완전탐색 문제 86,400가지 밖에 없으므로 100만개 이하일 때는 완전 탐색이 적절
"""
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매시각 시, 분, 초 중에 3이 있기만 하면 count를 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)