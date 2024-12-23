"""
N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
"""

N,K = map(int,input().split())

opr_num = 0
result = N # 굳이 새로운 변수에 N을 할당 안하고 N으로 계속 연산해나가도 된다.

while result != 1:
    if result % K == 0:
        result /= K
    else:
        result -= 1
    opr_num += 1

print(opr_num)
