# 팩토리얼이란 7! 처럼 나타내고 7 * 6 * 5 * 4 * 3 * 2 * 1을 나타냄
# 0! 1!는 1과 같음

def factorial_iterative(n):
    result = 1

    for i in range(1,n + 1):
        result *= i

    return result

print(factorial_iterative(4))