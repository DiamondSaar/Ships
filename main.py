import random

class Game:

    def __init__(self, Fleet):
        self.Fleet = Fleet


class Field:
    fGame = [["O"] * 6 for i in range(6)]

    def printField(self):
        print("     поле игрока",)
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |", )
        print("-" * 27)
        for i in range(6):
            print(i + 1, "|", self.fGame[i][0], "|", self.fGame[i][1], "|", self.fGame[i][2],"|", self.fGame[i][3], "|", self.fGame[i][4], "|", self.fGame[i][5])
        print("-" * 27)
"""
class Board: #передадим в класс две доски и два флота
    boardUser = Field()
    boardAI = Field()

    FleetUser = Fleet()
    FleetAI = Fleet()
"""
class CoordShip:    # первая координата корабля
    x1 = int(random.randint(0, 5))
    y1 = int(random.randint(0, 5))
    v = int(random.randint(0, 1)) #0 => (вправо); 1 v (вниз);

"""
class Ships:    #Класс кораблей
    def __init__(self, CoordShip, health):
        self.CoordShip = CoordShip
        self.health = health

    def status(self):   #Возможно сюда стоит добавить проверку состояния "жив/мертв" у корабля.
        return True if self.health > 0 else False

"""

class BigShips():  #Класс больших кораблей те что больше чем 1 клетка
    health = int(3)
    x1 = CoordShip.x1
    y1 = CoordShip.y1
    v = CoordShip.v


    def SetShip(self):
        if self.v == 0:
            if self.x <= 3:
                self.x2 = self.x + 1
                self.x3 = self.x + 2
                self.y2 = self.y + 1
                self.y3 = self.y + 2

            else:
                self.x2 = self.x - 1
                self.x3 = self.x - 2
                self.y2 = self.y - 1
                self.y3 = self.y - 2

            return x2, x3, y2, y3
"""
    x2 = SetShip(x2)
    y2 = SetShip(y2)
    x3 = SetShip(x3)
    y3 = SetShip(y3)
"""

BigShipUser = BigShips() #првоеряем все ли получилось

print(BigShipUser.health)
print(BigShipUser.v)
print(BigShipUser.x1)
print(BigShipUser.y1)
print(BigShipUser.x2)
print(BigShipUser.y2)
print(BigShipUser.x3)
print(BigShipUser.y3)

class Fleet:    #Содержание кораблей
    BigShip = BigShips
    MediumShip1 = BigShips
    MediumShip2 = BigShips
    SmallShip1 = Ships
    SmallShip2 = Ships
    SmallShip3 = Ships
    SmallShip4 = Ships






