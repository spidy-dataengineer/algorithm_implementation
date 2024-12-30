"""
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
3개의 숫자이긴 하지만, 2번째로 "큰" 수에 부합하는건 reverse 후에 2번째 인덱스를 가져오는게 문제와 맞는 코드이긴 함
"""

A,B,C = map(int,input().split())

num_list = [A,B,C]
num_list.sort(reverse=True)
print(num_list[1])