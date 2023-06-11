import keyboard 
import os



class Screen:
	c = []
	Swall ='|'
	Uwall = '-'
	Space = ' ' 
	def __init__(self,height,width):
		self.width = width
		self.height = height
	def Intiate(self):
		# Creating the cordinates array 
		for i in range(self.height+1):
			self.c.append([])
			for j in range(self.width+1):
				self.c[i].append(self.Space)
		# Creating The Screen Borders  

			# Upper/Lower wall
		for i in range(self.width+1):
			self.c[0][i] = self.Uwall
		for i in range(self.width+1):
			self.c[self.height][i] = self.Uwall


			# Left/Right wall
		for i in range(self.height+1):
			self.c[i][0] = self.Swall
		for i in range(self.height+1):
			self.c[i][self.width] = self.Swall

	def Render(self,update):
		while True : 
			# Rendering
			for i in range(len(self.c)):
				for j in range(self.width+1):
					if j == 0 :
						print('')
					print(self.c[i][j], end='')

			os.system("cls")

			update()

			#Exeting 

			if keyboard.is_pressed("e"):
				if keyboard.is_pressed("a"):
					pass
				elif keyboard.is_pressed("e"):
					break

class GameObject:
	def __init__(self,y,x,cords,shapes,speed,screen):
		self.x = x
		self.y = y
		# The cordinates of the Symbols Relative to the gameObject postition 
		self.cords = cords
		# The Symbols
		self.shapes = shapes
		self.speed = speed
		self.screen = screen
	def Draw(self) : 
		# Looping throught each GameObject Shape and Drawing it in the right Place
		for i in range(len(self.shapes)):
			self.screen.c[self.y][self.x] = self.shapes[i]
			if i!= 0 :
				self.screen.c[self.y+self.cords[i-1][0]][self.x+self.cords[i-1][1]] = self.shapes[0]
	def Erase(self):
		for i in range(len(self.shapes)):
			self.screen.c[self.y][self.x] = self.screen.Space
			if i != 0 :
				self.screen.c[self.y+self.cords[i-1][0]][self.x+self.cords[i-1][1]] = self.screen.Space
	def MoveR(self):
		self.Erase()
		self.x += self.speed 
		self.Draw()
	def MoveU(self):
		self.Erase()
		self.y -= self.speed 
		self.Draw()
	def MoveD(self):
		self.Erase()
		self.y += self.speed
		self.Draw()
	def MoveL(self):
		self.Erase()
		self.x -= self.speed 
		self.Draw()	



