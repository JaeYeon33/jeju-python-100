# 문제 12 : 게임 캐릭터 클래스 만들기
# 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게 만드시오.

"""
    <여기서 class를 작성하세요.>

    x = Wizard(health = 545, mana = 210, armor = 10)
    print(x.health, x.mana, x.armor)
    x.attack()    
"""


class Wizard:
    def stats(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def attack(self):
        print('파이어볼')


x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()


"""
x = Wizard(health=545, mana=210, armor=10) 와 같이 클래스에 값을 넣어서 인스턴스를 생성하고,
print(x.health, x.mana, x.armor) 와 같이 인스턴스 속성을 출력하고 있다. 따라서 class로 Wizard 클래스를 만들고
__init__ 메서드에 매개변수로 self, health, mana, armor 를 지정한다. 이 때 반드시 첫 번째 매개변수는 self라고 해야 한다.
함수 안에서는 self.health = health 처럼 모든 매개변수를 그대로 속성으로 만들어준다. 그 다음
x.attack() 와 같이 인스턴스로 메서드를 호출하고 있으므로 Wizard 클래스 안에 attack 메서드를 만들고 print로
'파이어볼'을 출력하도록 만들면 된다.
"""
