# 리스트 컴프리헨션
# 기본 구조 - [expression for item in iterable]

# 단순한 예) 1부터 10까지의 숫자 리스트를 생성
number = [x for x in range(1, 11)]
print(number)

# 조건 추가하기 - 짝수만 포함하는 리스트 생성
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 중첩 반복문
matrix = [ [x*y for y in range(2)] for x in range(2)]
print(matrix)

# if_else 절대값 구하기
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
absolute_values = [abs(x) for x in numbers]
print(absolute_values)

# 함수 사용하기
names = ['alice', 'bob', 'charlie', 'david']
uppercase_names = [name.upper() for name in names]
print(uppercase_names)