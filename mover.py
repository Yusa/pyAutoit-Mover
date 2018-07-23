
import autoit
import random
import time
import screeninfo


def mover():
	monitor = screeninfo.get_monitors()

	afk = True

	_X_MAX = monitor[0].width
	_Y_MAX = monitor[0].height

	while(afk):
		try:
			x = random.randrange(0,_X_MAX)
			y = random.randrange(0,_Y_MAX)
			autoit.mouse_move(x,y)
			
			targetPos = (x,y)
			time.sleep(1)
			currentPos = autoit.mouse_get_pos() 
	#		print(currentPos)
			if targetPos != currentPos:
				afk = False
	#			print("I'm Out")
		except:
			pass


def main():
	currentPos = autoit.mouse_get_pos()
	while True:
		try:
			time.sleep(2)
			newPos = autoit.mouse_get_pos()
			if currentPos == newPos:
				mover()
			currentPos = newPos
		
		except KeyboardInterrupt:
			exit()
		
		except:
			pass

if __name__ == "__main__":
	main()