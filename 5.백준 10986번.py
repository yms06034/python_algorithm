"""
문제 파악

5 = 수 개수
3 = 3나눠 떨어지는 구간이 있는지
1 2 3 1 2 = 입력 수

예제 출력 = 7

손으로 계산해보면


1+2 / 1+2+3 / 1+2+3+1+2     3
2+3+1                       1
3 / 3+1+2                   2
1+2                         1

그래서 7이란는 값이 도출된것이다.
"""

"""
문제 분석
1. (A + B) % C = ((A % C) + (B % C)) % C와 같다.
특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일하다.

2. 구간 합 배열을 이용한 식 S[i] - S[j]는 원본 리스트의 j + 1부터 i까지의 구간 합

3. s[i] % M의 값과 S[j] % M의 값이 같다면 (S[i] - S[j]) % M은 0이다.
즉, 구간 합 배열의 원소를 M으로 나눈 나머지로 업데이트하고 S[i]와 S[j]가 같은 (i, j)쌍을 찾으면 
원본 리스트에서 j + 1부터 i까지의 구간 합이 M으로 나눠떨어진다는 것을 알 수 있다.
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m 
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i]*(C[i]-1) // 2) # Combination 공식 | _n C_r=\frac{n !}{r ! (n-r) !} 
        
print(answer)