# # 모듈 : 함수나 변수 또는 클래스를 모아놓은 파일
# # 모듈 만들기
# # mod1.py
# # def add(a,b):
# #   return a + b
# # def sub(a,b):
# #   return a - b

# # 모듈 불러오기

# import mod1
# print(mod1.add(2, 4))
# print(mod1.sub(4, 2))

# # from 모듈이름 import 모듈에 있는 함수

# from mod1 import add

# print(add(3, 13))

# # 모듈에 있는 여러함수 사용하기
# from mod1 import add, sub
# from mod1 import *


# if __name__ == "__main__" : 파일 내부에서만 동작함
# mod1.py을 다음과 같이 변경해보자.

# mod1.py
# def add(a,b):
#   return a + b

# def sub(a,b):
#   return a - b

# print(add(1, 4))
# print(sub(4, 2))

# 이 모듈을 불러온다면 계속 print가 실행됨
# 그래서 mod1.py 파일에 다음과 같이 추가

# if __name__ == "__main__":
#   print(add(1,4))
#   print(sub(4,2))
# 이렇게 되면 mod1 파일에서만 실행된다.

from mod1 import *

print(add(422, 522))
print(sub(122, 22))


# 클래스나 변수등을 포함한 모듈
# mod2.py
# PI = 3.141592

# class Math:
#   def solv(self, r):
#       return PI * (r**2)
#   def add(a, b):
#       return a + b

from mod2 import *
print(PI)

# 모듈에 있는 변수를 사용할 수 있다.

# mod2.py 모듈을 사용해 반지름이 5인 원의 넓이를 계산해보자.

a = Math()
print(a.solv(5))
