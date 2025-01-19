from random import choice

class Nim:
    def __init__(self, number_of_sticks):
        self.sticks = number_of_sticks
    

    # schrijf hier de functie player_takes()
    def player_takes(self, player_turn):
    
        self.sticks -= player_turn
       
    def AI_turn(self):
      
        if self.sticks <= 3:
            return self.sticks
      
        if self.sticks % 4 == 0:
         return choice(1, 2, 3)
      
        else:
            return self.sticks % 4

    def game_over(self):
      
        return self.sticks <= 0

game = Nim(16)

while True:
    print("Aantal stokjes op tafel: ", game.sticks)

    player_turn = int(input("Hoeveel stokjes pak je? "))

    if player_turn not in [1, 2, 3]:
        print("Aantal niet toegestaan ...")
        continue

    # de beurt van de speler
    game.player_takes(player_turn)

    if game.game_over():
        print("Jij wint")
        break

    # de beurt van de computer
    ai_takes = game.AI_turn()
    game.player_takes(ai_takes)
    print(f"Computer pakt {ai_takes} stokje(s)")

    if game.game_over():
       print ("Computer wint")
       break
       