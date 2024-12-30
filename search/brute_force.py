"""
브루트 포스(Brute Force) 알고리즘, 때때로 무차별 대입법이라고도 불리는 이 방법은
문제를 해결하기 위해 가능한 모든 경우의 수를 전부 탐색해보는 방식입니다.
가장 기본적이며 직관적인 알고리즘 접근 방식 중 하나로, 복잡한 최적화 기법이나 특별한 알고리즘 지식이 필요 없이
문제의 해답을 찾을 수 있습니다.

* 완전성(Completeness): 브루트 포스는 모든 가능성을 탐색하기 때문에, 해답이 존재한다면 반드시 찾을 수 있습니다. 이러한 특성 때문에 완전 탐색 알고리즘으로도 불립니다.
* 단순성(Simplicity): 알고리즘의 구현이 비교적 간단하여, 복잡한 문제 해결 방법을 고민하기 전에 초기 접근 방식으로 사용될 수 있습니다.
* 시간 복잡도(Time Complexity): 대부분의 경우 시간 복잡도가 매우 높아, 작은 규모의 문제나 시간 제한이 크게 중요하지 않은 상황에서 주로 사용됩니다. 경우에 따라서는 계산 시간이 실용적이지 않을 수 있습니다.

* 비밀번호 크래킹: 주어진 비밀번호의 가능한 모든 조합을 시도하여 비밀번호를 찾아내는 과정에서 사용됩니다.
* 순열과 조합 문제: 데이터의 모든 순열이나 조합을 생성하여 특정 조건을 만족하는 경우를 찾을 때 활용됩니다.
* 체스 문제: 체스에서의 나이트 투어나 여덟 퀸 문제 같은 특정 조건을 만족하는 해답을 찾기 위해 사용됩니다.
* 그래프 문제: 최소 경로 문제나 해밀턴 경로 문제에서 모든 가능한 경로를 탐색하여 최적의 해답을 찾는 데 사용될 수 있습니다.

"""

def brute_force_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where target is found
    return -1  # Return -1 if target is not found

# Example usage:
arr = [2, 4, 6, 8, 10]
target = 6
result = brute_force_search(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found.")
