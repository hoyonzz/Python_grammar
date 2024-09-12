# # 사칙연산 클래스 만들기

# # 클래스를 어떻게 만들지 먼저 구상하기
# """
# 어떤 클래스를 만들지 대충 그림을 그려 보자.
# setdata 메서드 : 사칙연산을 하려면 두 숫자를 입력받아야겠군!
# div 메서드 : 나누기 기능은?
# add 메서드 : 더하기 기능은?
# sub 메서드 : 빼기 기능은?
# mul 메서드 : 곱하기 기능은?
# """

# # 클래스 구조 만들기
# class FourCal:
#     pass

# a = FourCal()

# print(type(a))

# # 객체에 숫자 지정할 수 있게 만들기
# # a.setdata(4,2)

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

# # 더하기 기능 만들기
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
    

# a = FourCal()

# a.setdata(4,2)

# print(a.add())

# # 곱하기, 빼기, 나누기 기능 만들기

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
    
# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 8)
# print(a.add())
# print(a.mul())
# print(a.div())
# print(a.sub())

# print(b.add())
# print(b.mul())
# print(b.div())
# print(b.sub())

# 생성자(Constructor)
"""
FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add메서드를 수행하면 오류가 발생한다.
setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문이다.

이렇게 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는
생성자를 구현하는 것이 안전한 방법이다.

생성자란 객체가 생설될 때 자동으로 호출되는 메서드를 의미한다.
파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다. 다음과 같이 FourCal 클래스에 생성자를 추가해보자.
"""

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
# a = FourCal(4, 2)
# print(a.first)

# print(a.second)

# print(a.add())
# print(a.div())


# 클래스의 상속
# 상속이란 '물려받다'라는 뜻으로, '재산을 상속받다'라고 할 때의 상속과 같은 의미이다. 

class MoreFourCal(FourCal):
    pass


a = MoreFourCal(10, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
print(a.pow())

# 메서드 오버라이딩

