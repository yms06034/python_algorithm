"""
데이터의 인접 요소끼리 비교하고, swap 연산을 수행하며 정렬하는 방식

두 인접한 인덱스의 크기를 비교해 정렬하는 방법
O(n^2)으로 다른 정렬 알고리즘보다 속도가 느린편

[버블정렬 과정]
1. 비교연산이 필요한 루프 범위를 설정
2. 인접한 데이터 값을 비교한다
3. swap 조건에 부합하면 swap 연산을 수행
4. 루프 범위가 끝날 때까지 2~3을 반복
5. 정렬 영역을 설정 다음 루프를 실행할 때는 이 영역을 제외
6. 비교 대상이 없을 때까지 1~5를 반복

만약 특정한 루프의 전체 영역에서 swap이 한번도 발생하지 않는다면 그 영역뒤에 있는 데이터가 모두 정렬되었다는 뜻이므로 프로세스 종료
"""

def bubble(arr):
    len_ = len(arr) - 1
    sort = False
    while not sort:
        sort = True
        for i in range(len_):
            if arr[i] > arr[i + 1]:
                sort = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        print(arr)
data = [6, 7, 8, 1, 3, 4, 7, 5, 4]
bubble(data)