class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

team = []
team.append("勇者")
team.append("戦士")
team.append("魔法使い")

p = Player("スライム")
for person in team:
    p.attack(person)
