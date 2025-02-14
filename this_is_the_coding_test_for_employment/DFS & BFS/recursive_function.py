import time
# 자기 자신을 다시 호출하는 함수
def recursive_function(i):
    if i == 20:
        return # return은 값을 반환하지 않으며 단순히 현재 함수 호출을 종료하는 역할
    print(f"{i}번 째 재귀 함수 호출")
    time.sleep(1)
    recursive_function(i+1)
    # 재귀 함수에서 역순으로 돌아가는 이유는 함수 호출의 실행 방식인 스택(stack) 구조 때문
    # 파이썬에서 함수가 호출되면, 현재 실행 중인 함수의 상태(매개변수, 지역 변수 등)를 저장하고 새로운 함수로 넘어갑니다.
    # 이 저장된 상태는 **스택(stack)**이라는 데이터 구조에 쌓입니다.
    # 스택은 후입선출(LIFO, Last In First Out) 원칙을 따르기 때문에, 마지막에 호출된 함수가 가장 먼저 반환
    print(f"{i}번 째 재귀 함수이므로 종료")

recursive_function(1)

"""
1. recursive_function(1)  → 스택에 저장
2. recursive_function(2)  → 스택에 저장
3. recursive_function(3)  → 스택에 저장
...
20. recursive_function(20) → 스택에 저장

마지막에 스택에 추가된 함수가 먼저 반환되기 때문에, 함수가 종료될 때는 스택에 쌓인 순서의 반대 방향(역순) 으로 반환됩니다:

recursive_function(20) → 종료
recursive_function(19) → 종료
recursive_function(18) → 종료
...
recursive_function(1) → 최종 종료
"""