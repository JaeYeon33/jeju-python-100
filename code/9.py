# 문제 9 : sep과 end를 활용한 출력방법
# 다음 소스 코드를 완성하여 날짜와 시간을 출력하시오.
"""
    year = '2019'
    month = '04'
    day = '26'
    hour = '11'
    minute = '34'
    second = '27'

    print(year, month, day, )
    print(hour, minute, second, )
"""

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')


"""
1. sep (separation)
    - 영단어 그래도, 분리하여 출력한다. (갈라놓을 문자를 지정할 수 있다) 이것을 구분자라고 한다.

2. end
    - 그 뒤의 출력값과 이어서 출력한다. (즉, 줄바꿈을 하지 않게 된다.)
    - end=' ' 사이에 무언가를 입력하게 되면, sep와 비슷한 기능을 한다.

3. format
    - 포매팅을 통해 특정 서식에 따라 문자를 출력할 수 있다. 부분적으로 문자열을 바꾸어 반복적으로 출력할때 유용하다.
"""
