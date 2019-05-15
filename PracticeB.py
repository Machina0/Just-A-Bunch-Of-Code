import monsterA as m1
import monsterB as m2
try:
  alive = True
  GameOver = False
  stats = {health : 100, defense : 5}
  bomb = {quantity : 2, damage : 25}
  BadSword = {damage : 10}
  def fightFunction():
    choice = int(input("""Two Monsters approach you threateningly!
    What will you do?
    1. Bomb
    2. Sword
    3. Block and Counter
		
		(Type the number of your choice, not the word!)"""))
    if choice == 1:
			if bomb[0] == 0:
				print("No bombs left!")
			else:
				stats[0] -= bomb[2] - stats[1]
				bomb[0] -= 1
				print bomb[0:]
except ValueError:
	print("Not a number")
	fightFunction()
