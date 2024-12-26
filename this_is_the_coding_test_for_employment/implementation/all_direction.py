# 완전 탐색, 시뮬레이션 유형을 모두 구현으로 묶어서 다룸
# 완전 탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

"""
N x N 크기의 정사각형 공간
L: 왼쪽으로 한 칸
R: 오른쪽으로 한 칸
U: 위로 한 칸
D: 아래 한 칸
* 공간 밖은 무시

입력 조건:
1. 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
2. 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

출력 조건:
1. 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백으로 구분하여 출력한다.

"""
N = int(input())
direction = list(map(str,input().split()))

result = [1,1]
for i in range(len(direction)):
    if direction[i] == "R" and (result[1]+1 <= N):
        result[1] += 1
    else:
        pass
    if direction[i] == "L" and (result[1]-1 >= 1):
        result[1] -= 1
    else:
        pass
    if direction[i] == "U" and (result[0]-1 >= 1):
        result[0] -= 1
    else:
        pass
    if direction[i] == "D" and (result[0]+1 <= N):
        result[0] += 1
    else:
        pass

result = ' '.join(map(str, result))
print(result)

"""
N = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1] # x좌표가 움직이는 조작을 미리 리스트(배열)에 정의
dy = [-1, 1, 0, 0] # y좌표가 움직이는 조작을 미리 리스트(배열)에 정의
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]: # 입력받은 움직이는 지시가 미리 정의해둔 움직이는 정의와 같을 때 nx, ny 공간 좌표에 반영
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
"""