# PythonMonsterAttack
クラスでモンスターへの攻撃

## 処理
playerクラスのattack()メソッドを使って、モンスターへの攻撃を出力する。

## コード
```
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
```

## 出力結果  
```
スライムは勇者を攻撃した
スライムは戦士を攻撃した
スライムは魔法使いを攻撃した
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |
