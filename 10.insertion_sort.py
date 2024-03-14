"""
이미 정렬된 데이터 범위에 정렬되지 않은 데이터를 적절한 위치에 삽입시켜 정렬하는 방식
시간복잡도 = O(n^2)

선택 데이터를 현재 정렬된 데이터 범위 내에서 적절한 위치에 삽입하는 것이 삽입정렬의 핵심

1. 현재 index에 있는 데이터 값을 선택
2. 현재 선택된 데이터가 정렬된 데이터 범위에 삽입될 위치를 탐색
3. 삽입 위치부터 index에 있는 위치까지 shift 연산을 수행
4. 삽입 위치에 현재 선택된 데이터를 삽입하고 index++ 연산을 수행
5. 전체 데이터의 크기만큼 index가 커질 때까지, 즉 선택한 데이터가 없을 때까지 반복

적절한 삽입 위치를 탐색하는 부분에서 Binary Search 등과 같이 탐색 알고리즘을 사용하면 시간 복잡도를 줄일 수 있음
O(logN)
"""

def insertion_sort(arr, len_):
    a = arr
    for i in range(0, len_):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

        print(a)

data = [6, 9, 8, 1, 3, 4, 7, 5, 4]
len_ = len(data)
insertion_sort(data, len_)

