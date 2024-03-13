"""
Stack은 삽이과 삭제 연산이 Last in First out으로 이뤄지는 자료구조
그렇기에 삽입과 삭제가 한 쪽에서만 일어나느 특징이 있음

Python의 Stack
- top : insert와 delete가 일어난 위치
 - s.append()
 - s.pop()
 - s[-1]

 Stack는 DFS(Depth First Search), 백트래킹 종류의 코딩 테스트에서 효과적임
 개념 자체가 재귀함수 알고르즘 원리와 일맥상통하기 때문
 """

"""
Queue는 insert와 delete 연산이 FIFO(First in First out)로 이뤄지는 자료구조
새 값 추가는 Queue의 rear에서 이뤄지고 삭제는 Queue의 front(s[0])에서 이뤄진다

Python의 Queue
- rear = s.append(data)
- front = s.pipleft()
- s[0]

Queue는 Breadth Frist Search에서 자주 사용됨

// 우선 순위 큐
prioroty queue는 값이 들어간 순서와 상관없이 우선순위가 높은 데이터가 먼저 나오는 자료구조

큐 설정에 따라 front에 항상 최댓값 또는 최솟값이 위치함
우순선위 큐는 일반적으로 힙(heap)을 이용해 구현하는데 힙의 트리 종류 중 하나
"""

"""
오큰수 구하기

N(1 <= N <= 1,000,000) 이기 때문에 워스트케이스를 확인 했을시 일일이 스캔하기에는 시간복잡도가 N이기 때문에 절대 금지

그렇기에 Stack을 활용해서 문제를 푼다
- Stack에 새로 들어오는 수가 Top에 존재를 하는 수보다 크면 그 수는 오큰수가 된다.
- 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에 -1을 출력해야 한다.
"""

import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result  = ""
for i in range(n):
    result += str(ans[i]) + " "

print(result)