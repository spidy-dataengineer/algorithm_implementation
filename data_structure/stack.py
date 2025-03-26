class Stack:
    def __init__(self):
        self.stack = []  # 내부 리스트를 이용해 스택 구현

    def push(self, item):
        self.stack.append(item)  # 리스트 끝에 요소 추가 (O(1))

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # 리스트 끝 요소 제거 및 반환 (O(1))
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # 스택의 마지막 요소 조회
        return None

    def is_empty(self):
        return len(self.stack) == 0  # 스택이 비었는지 확인

    def size(self):
        return len(self.stack)  # 스택 크기 반환

# 사용 예시
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # 2 (후입선출, LIFO)
