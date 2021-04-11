# 문제 42 : 2020년 (datetime 모듈 사용)
# 2020년 1월 1일은 수요일입니다. 2020년 a월 b일은 무슨 요일일까요?
# 두 수 a, b를 입력받아 2020년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN, MON, TUE, WED, THU, FRI, SAT 입니다.
# 예를 들어 a = 5, b = 24라면 5월 24일은 일요일이므로 문자열 "SUN"를 반환하세요.

import datetime

m = int(input())
d = int(input())


def find_day(a, b):
    day = ['MON', 'TUE', "WED", 'THU', 'FRI', 'SAT', ' SUn']
    return day[datetime.date(2020, a, b).weekday()]


print(find_day(m, d))
