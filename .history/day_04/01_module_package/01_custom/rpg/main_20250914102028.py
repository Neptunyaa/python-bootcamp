from character.knight import Knight
from character.mage import Mage
from character.warrior import Warrior

knight = Knight()
mage = Mage()
warrior = Warrior()


knight.attack(mage)
warrior.attack(mage)
print(mage)

mage.attack(warrior)
