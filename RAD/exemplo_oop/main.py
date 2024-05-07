# ------------ imports ------------
import os
from personagem import Hero, Enemy
from arma import arco_curto, espada_aco

# ------------ setup ------------
hero = Hero(name="Hero", health=100)
hero.equip(espada_aco)
enemy = Enemy(name="Enemy", health=100, weapon=arco_curto)

# ------------ game loop ------------
while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
