# 문제 30 : 문자열 속 문자 찾기
# 문자 pineapple에는 apple이라는 문자가 숨어 있습니다. 원범이는 이렇듯 문자열 속에 숨어 있는 문자를 찾아보려고 한다.
# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면
# 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요.

"""
    입력

    pineapple is yummy
    apple

    출력
    4
"""

data = input()
word = input()

print(data.find(word))

"""
find & index :
    - 문자열에서 원하는 문자나 문자열이 어디 있는지를 알려주는 것

find : 찾는 문자나 문자열이 없을 경우에는 -1을 return 하게 된다.
index : 없을 경우에 오류를 발생 시키게 된다.
"""
