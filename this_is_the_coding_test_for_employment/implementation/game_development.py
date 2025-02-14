"""
1 x 1 크기의 정사각형으로 이루어진 N x M 크기의 직사각형의 맵이 존재(육지 혹은 바다)
케릭터는 동서남북 중 한 곳을 바라 봄

맵의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수(A = 행, B는 열)

캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없음

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정함
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진. 왼쪽 방향에
가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

- 첫째 줄에 N과 M을 공백을 구분하여 입력 3<= N, M <= 50
- 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 서로 공백으로 구분하여 주어진다. 방향 d의 값으로는 4가지가 존재
0,1,2,3(북,동,남,서)
- 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어짐. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
맵의 외곽은 항상 바다로 되어 있다.
- 0,1(육지,바다)
- 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

캐릭터가 방문한 칸의 수는?

* dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 좋음
"""
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향 입력
x, y, drctn = map(int, input().split())
d[x][y] = 1 # 현재 좌표(시작 점) 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global drctn
    drctn -= 1
    if drctn == -1:
        drctn = 3

# 시뮬레이션
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[drctn]
    ny = y + dy[drctn]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[drctn]
        ny = y - dy[drctn]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다에 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)