"""
구간 합은 합 배열을 이용하여 시간 복잡도를 더 줄이기 위해 사용하는 특수한 목적의 알고리즘
코딩 테스트에서 사용 빈도가 높다!!! (핵심)

 - 구간합 핵심 이론
 먼저 합 배열을 구해야 한다. 배열 A가 있을 때 합 배열 S는 다음과 같이 정의
 S[i] = A[0] + A[1] + A[2] + ... + A[i-1] + A[i]

 -- 도식화
 index      0   1   2   3  4  5
 배열 A     15, 13, 10, 7, 3, 12
 합 배열 B  15, 28, 38. 45, 48, 60

 빅-오의 경우 i가 0이고 j가 N인 경우로 시간 복잡도는 O(N)

 - 합 배열 S 만드는 공식
 S[i] = S[i-1] + A[i]

 - 구간합 구하는 공식
 S[j] - S[i-1]
 
 -- 예를 들어 A[2] ~ A[5] 구간 합을 합 배열로 구하는 과정
 S[5] = A[0] + A[1] + A[2] + A[3] + A[4] + A[5]
 S[1] = A[0] + A[1]
 S[5] - S[1] = A[2] + A[3] + A[4] + A[5]
"""

# 구간 합 구하기2 백준 11660번
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(n+1):
    D[i][1] = D[i-1][1] + A[i][1]
    D[1][i] = D[1][i-1] + A[1][i]
    

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1 ,y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)