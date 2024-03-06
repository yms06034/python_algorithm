"""
python에서는 리스트가 배열의 특성도 함께 포함되어 있음

 - 배열
 배열은 메모리의 연속 공간에 값이 채워져 있는 형태의 자료구조
 1. 인덱스를 사용하여 값에 바로 접근할 수 있다.
 2. 새로운 값을 삽입하거나 특정 인덱스에 있는 값을 삭제하기 어렵다. 값을 삽입하거나 삭제하려면 해당 인덱스 주변에 있는 값을 이동시키는 과정이 필요하다
 3. 배열의 크기는 선언할 때 지정할 수 있으며, 한 번 선언하면 크기를 늘리거나 줄일 수 없다.
 4. 구조가 간단하므로 코딩 테스트에서 많이 사용된다.


 - 리스트
 리스트는 값과 포인터를 묶은 노드라는 것을 포인터로 연결한 자료구조
 1. 인덱스가 없으므로 값에 접근하려면 Head 포인터로부터 순서대로 접근해야 한다.
 다시 말해 값에 접근하는 속도가 느리다.
 2. 포인터로 연결되어 있으므로 데이터를 삽입하거나 삭제하는 연산 속도가 빠르다.
 3. 선언할 때 크기를 별도로 지정하지 않아도 된다. 다시 말해 리스트의 크기는 정해져 있지 않으며, 
 크기가 변하기 쉬운 데이터를 다룰 때 적절하다.
 4. 포인터를 저장할 공간이 필요하므로 배열보다 구조가 복잡하다.
"""

# 백준 11720번 숫자의 합 구하기
## 1번째 줄에 숫자의 개수 N(1 <= N <= 100), 2번째 줄에 숫자 N개가 공백 없이 주어진다.

### 슈도 코드 작성
"""
n값 받기
numbers 변수에 list 함수를 이용하요 숫자를 한 자리씩 나누어 받기
sum 변수 선언

for numers 탐색:
    sum 변수에 numbers에 있는 각 자릿수를 가져와 더하기

snm 출력
"""

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i)

print(sum)

"""
파이썬에서의 형 변환
1. int : int(data)      // float, bool 변환 가능
2. float : float(data)  // int, bool 변환 가능
3. str : str(data)      // int, float, bool, chr 변환 가능
4. chr : chr(data)      // int, bool 변환 가능
5. bool : bool(data)    // int, float, str, chr 변환 가능
"""