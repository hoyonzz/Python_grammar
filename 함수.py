def add(a,b):
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 결과값이 없는 함수
def add(a, b):
    print('%d, %d의 합은 %d입니다.' % (a, b, a+b))
    
add(3,4)
# 결과값은 오직 return 명령어로만 받을 수 있다.
a = add(3, 4)

print(a)

# 입력값도 결과값도 없는 함수
def say():
    print('Hi')
    
say()

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

answer = add_many(1,2,3)
print(answer)

# 여러 개의 입력을 처리할 때, def add_many(*args)처럼 매개변수로 *args만 사용할 수 있는 것은 아니다.
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
    return result

answer = add_mul('add', 1,2,3,4,5)
print(answer)
answer = add_mul('mul', 1,2,3,4,5)
print(answer)

# answer = add_mul('ad', 1,2,3,4)
# print(answer)

# 키워드 파라미터 : 매개변수 앞에 별 두개를 붙인다.
def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# return의 또다른 쓰임새 - 특별한 상황일 때, 함수를 빠져나가고 싶을 때
def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s 입니다.' % nick)
    
say_nick('야호')
say_nick('바보')
say_nick('신호등')

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a+1
    
vartest(a)
print(a)
# 매개변수는 함수밖에 변수 이름과 전혀 상관 없다.

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1
    
    
vartest()
print(a)

# lambda
add = lambda a, b: a+b
result = add(3,4)
print(result)