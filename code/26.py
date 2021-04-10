# 문제 26 : 행성 문제 2
# 우리 태양계를 이루는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성이 있다.
# 이 행성들의 영어 이름은 Mercury, Venus, Earth, Jupiter, Saturn, Uranus, Neptune 이다.
# 행성의 한글 이름을 입력하면 영어 이름으로 반환하는 프로그램을 만들어 주세요.

planets = {
    '수성': 'Mercury',
    '금성': 'Venus',
    '지구': 'Earth',
    '화성': 'Mars',
    '목성': 'Jupiter',
    '토성': 'Saturn',
    '천왕성': 'Uranus',
    '해왕성': 'Neptune'
}

name = input()
print(planets[name])
