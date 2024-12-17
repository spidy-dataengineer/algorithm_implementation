# 가장 큰 화폐 단위부터 거슬러 주는 알고리즘
N = int(input())
A = 0

while (N != 0):
    if N // 500 > 0:
        A += N // 500
        N %= 500
    elif N // 100 > 0:
        A += N // 100
        N %= 100
    elif N // 50 > 0:
        A += N // 50
        N %= 50
    else:
        A += N // 10
        N %= 10

print(A)
########################################
""" 시간복잡도는 화폐의 종류가 K라고 했을 때, O(K)
n = 1260
count = 0
coint_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)

"""