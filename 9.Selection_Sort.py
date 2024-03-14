"""
대상 데이터에서 최대나 최소 데이터를 데이터가 나열된 순으로 찾아가며 선택하는 방법
선택 정렬은 구현 방법이 복잡하고, 시간 복잡도도 O(n^2)으로 효율적이지 않아 코테에서 잘 사용하지 않음

최솟값 또는 최댓값을 찾고, 남은 정렬 부분의 가장 앞에 있는 데이터와 swap하는 것이 선택정렬의 핵심
"""

def selection_sort(arr, len_):
    for idx in range(len_):
        min_idx = idx
        for i in range(idx+1, len_):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        print(arr)


arr = [1,1,-2,10,13,20,50,-24, 0, 3, 44, 44, 44]
len_ = len(arr)
# selection_sort(arr, len_)

def selection_sort2(arr, size):
    for n in range(0, size):
        a = min(arr[n:])
        i = arr.index(a, n)
        arr[n], arr[i] = a, arr[n]
        print(arr)

arr = [1,1,-2,10,13,20,50,-24, 0, 3, 44, 44, 44]
size = len(arr)
selection_sort2(arr, size)