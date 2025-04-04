# https://wikidocs.net/233706
"""
버블 정렬(Bubble Sort)은 기본적인 정렬 알고리즘 중 하나로,
 인접한 원소들을 비교하고 필요에 따라 위치를 교환하는 방식으로 동작합니다.
 이 알고리즘은 구현이 간단하며, 이름에서 알 수 있듯이 큰 값(또는 작은 값)이 배열을 통해
 버블(거품)처럼 서서히 상단(또는 하단)으로 이동하는 과정을 거칩니다.

* 초기 상태: 배열의 처음부터 끝까지 순회를 시작합니다.
* 비교 및 교환: 현재 원소와 바로 다음에 있는 원소를 비교합니다. 정렬하려는 순서(오름차순 또는 내림차순)에 따라, 현재 원소가 다음 원소보다 크거나(오름차순 정렬) 작다면(내림차순 정렬), 두 원소의 위치를 교환합니다.
* 반복: 배열의 모든 원소에 대해 이 과정을 반복합니다. 한 번의 순회로 가장 큰(또는 가장 작은) 원소가 배열의 끝으로 이동하게 됩니다.
* 완료 조건: 배열에 더 이상 교환할 원소가 없을 때까지, 또는 정렬이 완료될 때까지 전체 과정을 반복합니다.

* 시간 복잡도: 최악의 경우와 평균적인 경우 모두 (O(n^2))의 시간 복잡도를 가집니다. 여기서 (n)은 배열의 길이입니다.
* 공간 복잡도: (O(1))의 추가 공간을 사용합니다. 즉, 제자리 정렬(In-place sorting) 알고리즘입니다.
"""
# 바로 옆자리의 수와 비교하면서 즉각 즉각 위치 변경하는 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
    return arr

# 예시 배열
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
###################################################
# optimized bubble sort
def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: # 자리의 교환이 일어나지 않은 경우, loop 종료
            break
"""
추가적으로 이미 정렬된 배열에 대한 불필요한 비교를 줄이기 위해,
한 번의 완전한 순회에서 어떠한 교환이 발생하지 않았다면 배열이 정렬되었다고 판단하고
정렬 과정을 조기에 종료하는 최적화가 가능
"""