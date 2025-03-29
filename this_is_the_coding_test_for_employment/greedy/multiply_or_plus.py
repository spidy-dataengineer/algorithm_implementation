S = str(input())

result = int(S[0]) # 최초 수를 문자열의 제일 처음 수로 지정해두는게 포인트

for i in range(1, len(S)):
    num = int(S[i])
    # 0이나 1인 경우 더하기 수행이 이득
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)