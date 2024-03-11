import discord
from discord.ext import commands
import time
import os
import random
from players import players
from weapon import weapon

def startGame(authorName, opponentName, embedMessage):
    playerAuthor = players(authorName)
    playerOpponent = players(opponentName)
    magnum = weapon("Magnum", 6)
    
    while True:
        if not magnum.get_magazine():
            print("A arma está sendo recarregada!")
            magnum.set_magazine()
            print("A arma foi recarregada!")
        print("Sua vez!")
        print("Escolha sua ação:")
        print("1 - Atirar em si mesmo.")
        print("2 - Atirar no monstro.")
        print(f"Sua vida: {player.get_life()}")
        print(f"Vida de {monster.get_name()}: {monster.get_life()}")
        print("=============================")
        playerAction = int(input("Sua ação: "))
        time.sleep(1.3)
        if playerAction == 1:
            magnum.shoot(player)
            if player.get_life() == 0:
                print("Você morreu!")
                print("=============================")
                break    
        else:
            magnum.shoot(monster)
            if  monster.get_life() == 0:
                print(f"{monster.get_name()} morreu!")
                print("Você venceu! Dessa vez você teve sorte.")
                break
        time.sleep(3)
        os.system('cls')
        print(f"Vez de {monster.get_name()}!")
        print(f"Sua vida: {player.get_life()}")
        print(f"Vida de {monster.get_name()}: {monster.get_life()}")
        print("=============================")
        time.sleep(3)
        monsterAction = random.randint(1,2)
        print(f"{monster.get_name()} escolheu {monsterAction}")
        print("=============================")
        time.sleep(3)
        if monsterAction == 1:
            magnum.shoot(monster)
            if  monster.get_life() == 0:
                print(f"{monster.get_name()} morreu!")
                print("Você venceu! Dessa vez você teve sorte.")
                break
        else:
            magnum.shoot(player)
            if  player.get_life() == 0:
                print(f"{player.get_name()} morreu!")
                print("Você perdeu!")
                break
        time.sleep(3)