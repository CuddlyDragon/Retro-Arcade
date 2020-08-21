5

print ("======Welcome to Retro Arcade!======\n       Choose your game here!")
print("         vvv Pick A Game vvv\n")
print("         1.Pong\n")
print("         2.Space Invaders\n")
print("         3.Tetris\n")
print("         4.Pac-Man\n")
print("         5.Connect 4\n")
print("         6.Classic Snake\n")
print("         7.Infinite Snake\n")
choice = input("Enter Choice, 1/2/3/4/5/6/7:  ")
if choice == '1':
  print("You picked Pong")
  import Pong
elif choice == '2':
  print("You picked Space Invaders")
  import SpaceInvaders
elif choice == '3':
  print("You picked Tetris")
  import Tetris
elif choice == "4": 
  print("You picked PacMan")
  import PacMan
elif choice == "5":
  print("You picked Connect 4")
  import Connect4
elif choice == "6":
  print("You picked Classic Snake")
  import Snake
elif choice == "7":
  print("You picked Infinte Snake")
  import Snake_2
else:
  print("Pick a Number between 1-7")

