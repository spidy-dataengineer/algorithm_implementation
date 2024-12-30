"""
이진 탐색(Binary Search)은 정렬된 배열에서 특정한 값을 효율적으로 찾는 탐색 알고리즘입니다.
이 알고리즘의 기본 원리는 탐색 범위를 반으로 줄여가며 데이터를 찾는 것이며,
이 과정을 반복함으로써 탐색의 효율성을 극대화합니다.
이진 탐색은 분할 정복(Divide and Conquer) 방식의 대표적인 예시로 볼 수 있습니다.

1. 정렬된 배열: 이진 탐색을 수행하기 전에 데이터가 정렬되어 있어야 합니다. 데이터가 정렬되어 있지 않은 경우, 이진 탐색은 올바른 결과를 보장할 수 없습니다.
2. 중간점 선택: 탐색 범위 내에서 중간 위치의 요소를 선택합니다. 배열이 0부터 시작한다고 가정할 때, 중간점의 인덱스는 (left + right) / 2로 계산할 수 있습니다.
3. 탐색 조건 비교: 중간점의 데이터와 찾고자 하는 값(target)을 비교합니다. 이 때, 세 가지 경우가 발생할 수 있습니다.
4. 중간점의 데이터가 찾고자 하는 값과 일치하는 경우: 탐색을 종료합니다.
5. 중간점의 데이터가 찾고자 하는 값보다 작은 경우: 탐색 범위의 왼쪽 부분을 버리고 오른쪽 부분을 새로운 탐색 범위로 설정합니다.
6. 중간점의 데이터가 찾고자 하는 값보다 큰 경우: 탐색 범위의 오른쪽 부분을 버리고 왼쪽 부분을 새로운 탐색 범위로 설정합니다.
7. 반복 수행: 새로운 탐색 범위를 기반으로 2번과 3번의 과정을 찾고자 하는 값이 발견되거나 탐색 범위가 더 이상 존재하지 않을 때까지 반복합니다.

* 이진 탐색은 O(log n)의 시간 복잡도를 가집니다. 대규모 데이터셋에서도 탐색 시간이 로그 시간으로 증가하기 때문에 매우 빠릅니다.

* 정렬된 데이터: 데이터가 미리 정렬되어 있어야 한다는 제한이 있습니다. 정렬되지 않은 데이터에는 적용할 수 없습니다.
* 동적 데이터셋: 데이터셋이 자주 변경되어 재정렬이 필요한 경우, 이진 탐색의 효율이 떨어질 수 있습니다.
* 배열에서의 값 탐색, 범위 내의 특정 조건을 만족하는 요소 찾기(예: 최소 또는 최대 값의 경계 찾기),
 알고리즘 문제 해결 시 탐색 범위를 좁혀나가는 과정 등 다양한 상황에서 활용
"""

# recursive
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return False

    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# iterative
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Test data
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

# Test cases
targets = [5, 15, 22, 3, 9]

# Test the recursive binary search
print("Recursive Binary Search:")
for target in targets:
    print(f"Target {target}: {binary_search_recursive(arr, target, 0, len(arr) - 1)}")

# Test the iterative binary search
print("\nIterative Binary Search:")
for target in targets:
    print(f"Target {target}: {binary_search_iterative(arr, target)}")