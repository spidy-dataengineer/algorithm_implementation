N,M,K= map(int, input().split())

n_list = list(map(int, input().split()))

n_list.sort(reverse=True)

first = n_list[0] # 가장 큰 수
second = n_list[1] # 두 번 째로 큰 수

result = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 만큼 더할 수 있는 반복문
        if M == 0: # M이 0이면 안되지만, 0인 경우 반복문 탈출
            break
        result += first
        M -= 1 # 결과에 더해 나갈 때 마다 총 더해야 될 횟수 줄여서 루프 줄이기
    if M == 0: # 루프를 빠져나가기 위한 조건(M번 동안 결과에 더했는지 확인)
        break
    result += second # 2번째 큰 수를 첫 번째 큰 수 대신에 더함
    M -= 1 # 결과에 더해 나갈 때 마다 총 더해야 될 횟수 줄여서 루프 줄이기


"""
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기
"""

print(result)