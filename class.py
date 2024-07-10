"""
클래스와 객체
class -> 과자틀
object(객체) -> 과자 틀을 사용해 만든 과자
"""

# class Cookie:
#     pass
# a = Cookie()
# b = Cookie()
# print(type(a), type(b))

'''
사칙연산 클래스 만들기
- 클래스를 어떻게 만들지 구상하기
1) 사칙연산을 하려면 두 숫자를 입력받아야겠군! [setdata 메서드]
2) 나누기 기능 [div 메서드]
3) 더하기 기능 [add 메서드]
4) 빼기 기능 [sub 메서드]
5) 곱하기 기능 [mul 메서드]
먼저, a=FourCal()을 입력해서 a라는 객체를 만든다.
a=FourCal()
그런 다음, a.setdata(4,2)를 입력해서 숫자 4와 2를 a 에 지정해두자
a.setdata(4,2)
'''
# 클래스 구조 만들기 -> 아무 기능 없이 틀 만들기
class FourCal:
    pass

# 객체에 숫자 지정할 수 있게 만들기
# a.setdata(4,2)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

# 클래스 안에 구현된 함수는 다른 말로 메서드 Method 라고 부른다.
# 1) setdata메서드의 매개변수
# setdata 메서드는 매개변수로 self, first, second 3개 입력값을 받는다.
# setdata 메서드의 수행문에서 self는 전달된 객체 a이므로,
# self.first = 4 -> a.first = 4
# self.second = 2 -> a.second = 2

a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)

# 더하기 기능 만들기
# a = FourCal()
# a.setdata(4,2)
# print(a.add())
# 6
# 이런 더하기 기능을 갖춘 클래스를 만들어보자.

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    
# add 메서드를 따로 떼서 자세히 살펴보자
# add 메서드의 매개변수는 self이고, 반환값은 result 이다.
# result = self.first + self.second
# a.first + a.second

# 곱하기, 빼기, 나누기 기능 만들기

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
a.setdata(11, 5)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

# 생성자
# a = FourCal()
# print(a.add())
# FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면 오류가 발생한다.
# setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문이다.
# 이렇게 객체에 초기값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초기값을 설정하기보다는
# 생성자를 구현하는 것이 안전한 방법이다.
# def __init__(self, first, second):
#   self.first = first
#   self.second = second
# a = FourCal(4,2)
# print(a.add())

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
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
# 클래스의 상속
# 어떤 클래스를 만들 때, 다른 클래스의 기능을 물려받을 수 있게 하는 것
# FourCal 클래스를 상속하는 MoreFourCal클래스는 다음과 같이 간단하게 만들 수 있다.
class MoreFourCal(FourCal):
    pass

# 상속했으므로 모든 기능을 사용할 수 있는지 확인해보자.
a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# a의 b제곱을 계산하는 MoreFourCal 클래스를 만들어보자.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4 ,2)
print(a.pow())

# 메서드 오버라이딩
# a.FourCal(4,0) 4를 0으로 나누려고 하기 때문에 ZeroDivisionError가 발생한다.
# 다음과 같이 FourCal 클래스를 상속하는 SafeFourCal클래스를 만들어보자.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        return self.first / self.second
    
a = SafeFourCal(4, 0)
print(a.div())

# SafeFourCal클래스는 FourCal클래스에 있는 div메서드를 동일한 이름으로 다시 작성하였다.
# 이렇게 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩이라고 한다.


