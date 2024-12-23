"""
1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로
 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

"""

N,M = map(int,input().split())

min_list = []
min_num = 0

# 각 행에 대해서 min값을 미리 구해 둔 후에 그 min값만을 모아둔 list에 append 시키고 그 중에서 max값을 가져옴
for _ in range(N): # N행동안 반복
    column = list(map(int,input().split())) # M열만큼의 숫자를 입력 받아서 list로 저장
    min_num = min(column) # list에서 min값을 가져옴
    min_list.append(min_num) # min값을 min값만을 모아두는 list에 추가

print(max(min_list)) # min 값을 모아 둔 list중에서 max값을 출력
