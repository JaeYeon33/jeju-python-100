# 문제 28 : 2-gram
# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법이다.
"""
    Py
    yt
    th
    ho
    on
"""

# 입력으로 문자열이 주어지면 2-gram으로 출력하는 프로그램을 작성해 주세요.

data = input()

for i in range(len(data) - 1):
    print(data[i], data[i + 1], sep='')
