import ASCIIEngine
import random 
import time
import keyboard 

# Creating The Screen 
screen = ASCIIEngine.Screen(15,63)
screen.Intiate()



# Game Code Here (a simple game test)


# Initial Game Objects
Player = ASCIIEngine.GameObject(5,5,[[1,0],[0,1],[1,1]],["|","|","|","|"],1, screen)
Player.Draw()


Obstical = ASCIIEngine.GameObject(random.randint(2,14),62,[],["¤"],2,screen)

Obstical.Draw()



# Updates 
def Update(): 

	if keyboard.is_pressed("w"):
		Player.MoveU()
	if keyboard.is_pressed("s"):
		Player.MoveD()
	if keyboard.is_pressed("d"):
		Player.MoveR()
	if keyboard.is_pressed("a"):
		Player.MoveL()

	Obstical.MoveL()





# Game Code Here 


# Rendering The Screen 
screen.Render(Update)
