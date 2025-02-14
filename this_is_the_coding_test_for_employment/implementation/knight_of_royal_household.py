"""
8x8 좌표 평면에서 나이트는 L자 형태로만 이동 가능
수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동
수직으로 두 칸 이동한 뒤에 수평으로 한칸 이동

행은 1~8
열은 a~h로 표현

"""
input_data = input()
row = int(input_data[1]) # 행 정의 1~8 사이 값
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 열 정의 a~h 사이 값
print(row, column)

steps = [(-2,-1), (-1,-2), (1,-2), (1,2), (-1,2), (-2,1), (2,-1), (2,1)] # 나이트의 이동 경우의 수 정의

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)