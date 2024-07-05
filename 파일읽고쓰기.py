# 파일 생성하기
# f = open('새파일.txt', 'w')
# f.close()

# 파일 열기모드
'''
'r' - 읽기모드:파일을 잃기만 할 때 사용한다.
'w' - 쓰기모드:파일에 내용을 쓸 때 사용한다.
'a' - 추가모드:파일의 마지막에 새로운 내용을 추가할 때 사용한다.
'''

# 파일을 쓰기 모드로 열어 내용 쓰기
# f = open('새파일.txt', 'a')
# for i in range(1, 11):
#     data = '%d번째 줄입니다.\n' % i
#     f.write(data)
# f.close()

# # 파일을 읽는 여러가지 방법
# # 1. readline 함수 이용하기
# f = open('새파일.txt', 'r')
# line = f.readline()
# print(line)
# f.close()

# f = open('새파일.txt', 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# # 2. readlines 함수 사용하기
# f = open('새파일.txt', 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# # read 함수 사용하기
# f = open('새파일.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# f = open('새파일.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# # 파일 객체를 for문과 함께 사용하기
# f = open('새파일.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# 객체(object)란: 객체는 어떠한 속성값과 행동을 가진 데이터

# 파일에 새로운 내용 추가하기
f = open('새파일.txt', 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# with 문과 함께 사용하기
with open('새파일.txt', 'r') as f:
    data = f.read()
    print(data)
