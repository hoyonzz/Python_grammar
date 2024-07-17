# 디렉토리 안에 없는 파일을 열려고 할 때, (FileNotFoundError)
# 0으로 나눌경우 - ZeroDivisionError
# 리스트 범위초과 - IndexError

# 오류 예외 처리 기법 기본 형태
# try:
#   ...
# except:
#   ...

# 1) try, except만 쓰는 방법
# try:
#   ...
# except
#   ...
# -> 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

# 2) 발생 오류만 포함한 except 문
# try:
#     ...
# except 발생오류:
#     ...
# -> except 문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록 수행

# 3) 발생 오류와 오류 메시지 변수까지 포함한 except문
# try:
#     ...
# except 발생 오류 as 오류 메시지 변수:
#     ...
# -> 이경우는 오류 메시지의 내용까지 알고 싶을 때 사용

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
    
# 앞에서 나온 3번 방법을 사용해 IndexError가 발생할 때 오류 메시지를 출력하는 소스를 작성해보자.

try:
    a = [1,2]
    print(a[2])
except IndexError as e:
    print(e)
    
# try ... finally : finally절은 try문 수행 도중 예외 발생 여부와 상관없이 항상 수행된다.
# 보통 사용한 리소스를 close 할 때 사용된다.

# f = open('foo.txt', 'w')
# try:
#     # 어떤 동작을 수행
# finally:
#     f.close()

# 여러 개의 오류 처리하기
# try:
#     ...
# except 발생 오류 1:
#     ...
# except 발생 오류 2:
#     ...
    
# try:
#     a=[1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except IndexError:
#     print('인덱싱 할 수 없습니다.')
    
# try:
#     a=[1,2,3]
#     print(a[4])
#     100/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# try:
#     a=[1,2,3]
#     print(a[4])
#     100/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)


# 오류 일부러 발생시키기
# ex) Bird클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은경우

class Bird:
    def fly(self):
        raise NotImplementedError
    
# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

class Eagle(Bird):
    def fly(self):
        print('very fast')
        
eagle = Eagle()
eagle.fly()

# 예외 만들기

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError
    print(nick)
    
say_nick('천사')
# say_nick('바보')

try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print('허용되지 않은 별명입니다.')