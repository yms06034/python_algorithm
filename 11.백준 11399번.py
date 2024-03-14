"""
ATM 앞에 있는 사람 중 인출 시간이 가장 짧은 사람이 먼저 인출될 수 있도록 오름차순으로 정렬하면 끝 (그리디 방식)
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_idx = i
    insert_value = A[i]
    for j in range(i-1, -1, -1): # 뒤에서부터 반복
        if A[j] < A[i]:
            insert_idx = j+1
            break
        if j == 0:
            insert_idx = 0

    for j in range(i, insert_idx, -1):
        A[j] = A[j-1]
    A[insert_idx] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0
for i in range(0, N):
    sum += S[i]

print(sum)