# 문제 48 : 대소문자 바꿔서 출력하기
# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성하세요.

a = input()
b = []

for i in a:
    if i.islower():
        b.append(i.upper())
    else:
        b.append(i.lower())

    for i in b:
        print(i, end='')

"""
1. upper : 문자열을 모두 대문자로 바꿔준다.

2. lower : 문자열을 모두 소문자로 바꿔준다.

3. isupper, islower : 문자열의 전체가 소문자인지 대문자인지 Boolean 형태(True, False)로 구분해준다.
"""
