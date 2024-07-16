# 1. Counter : 항목들의 개수를 세는데 사용
# most_common(n) : 가장 많이 등장한 n개의 항목과 그 빈도수를 반환
from collections import Counter

text = 'Hello, World!'
char_counts = Counter(text)
print(char_counts)
print(char_counts.most_common(3))
print(type(char_counts))

# elements(): Counter 객체에 포함된 모든 항목을 반환, 각 항목은 그 빈도수만큼 반복되어 반환
numbers = [1,2,3,1,2,2]
num_counts = Counter(numbers)
print(num_counts)
print(list(num_counts.elements()))

# +, -, &, | 연산자
# + : 두 Counter 객체의 값을 더합니다.
c1 = Counter([1,2,2,3,3,3])
c2 = Counter([2, 2, 3, 3])
print(c1 + c2)

# - : 두 Counter 객체의 차를 계산합니다.
# & : 두 Counter 객체의 교집합을 계산합니다.
# | : 두 Counter 객체의 합집합을 계산합니다.
print(c1-c2)
print(c1 & c2)
print(c1 | c2)