# 배열에 마지막에 하나씩 추가시키고 빼오는 개념
stack = []
stack.append(5)
stack.append(1)
stack.append(5)
stack.append(6)
stack.pop()
stack.append(8)
stack.pop()


print(stack) # 최하단 부터 출력
print(stack[::-1]) # 최상단 부터 출력