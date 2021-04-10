# 문제 27 : 딕셔너리 만들기
# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고, 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어진다.
# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.

"""
    Yujin Hyewon
    70 100
"""

"""
    {'Yujin' : 70, 'Hyewon' : 100}
"""

keys = input().split()
values = map(int, input().split())

result = dict(zip(keys, values))
print(result)


"""
split() : split() 처럼 괄호안에 아무값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.

zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어 주늖역할을 하는 함수이다.
    - *iterable : 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있는 의미이다.

>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
"""
