import time
import sys
import random
import threading

#tools = ['WOOD SWORD': 0, 'WOOD PICKAXE': 0, 'WOOD SHOVEL:': 0]
things = {'PLANKS': 64, 'STICKS': 64, 'COBBLESTONE': 64,'WOOD SWORD': 0, 'IRON ORE': 1, 'GOLD ORE': 1, 'WOOD PICKAXE': 0, 'WOOD SHOVEL': 0, "DIAMONDS": 0, "IRON": 0, "COAL": 0,"GOLD": 0, "DIAMOND SWORD": 0, 'DIAMOND PICK': 0, 'DIAMOND AXE': 0, 'DIAMOND SHOVEL': 0, "IRON SWORD": 0, 'IRON PICK': 0, 'IRON AXE': 0, 'IRON SHOVEL': 0, "STONE SWORD": 0, 'STONE PICK': 0, 'STONE AXE': 0, 'STONE SHOVEL': 0,}
#craftingmaterials = ['COBBLESTONE', 'WOOD LOGS', 'STICKS','PLANKS']
biomes = ['GRASSLAND', 'MOUNTAINS', 'DESERT', 'ICE', 'BEACH', 'DARK OAK FOREST']
monsters = {'ZOMBIE': 3, 'SKELETON': 3, 'SPIDER': 3, 'CREEPER': 6}


exp = 0
health = 100
night = False
hunger = 100

"""
def dayTimeThread():
	global night
	while True:
		time.sleep(3)
		night = True
		print("\nIT HAS TURNED NIGHT!")
		ifhealthlessthan50()
		time.sleep(3)
		night = False
		input("\nIT HAS TURNED DAY!\n>")





def hungerSystemThread():
	global hunger
	while True:
		time.sleep(5)
		hunger = hunger - 33
		print("\nYOU HAVE LOST SOME OF YOUR HUNGER\n>")


timeThread = threading.Thread(target = dayTimeThread)
timeThread.daemon = True
timeThread.start()


timeThread = threading.Thread(target = hungerSystemThread)
timeThread.daemon = True
timeThread.start()
"""


print("WELCOME TO TEXTCRAFT")
time.sleep(1)
print("THE UNIVERSAL COMMANDS ARE 'HELP' 'EXIT' ")


def intro():

	opening = input("TYPE PLAY TO START\n> ")

	if opening.lower() == "play":
		print("starting stuff goes here")

	elif opening.lower() == "help":
		print("COMMANDS\n1. THE COMMAND CRAFT ALLOWS YOU TO CRAFT ANY ITEM WITHIN THE RECIPES OF TEXTCRAFT"
			  "\n2. THE COMMAND EXIT WORKS AT ANY TIME TO ALLOW YOU TO EXIT THE GAME \n"
			  "3. THE COMMAND HELP ALLOWS YOU TO ACCESS THIS MENU AT ANY TIME\n"
			  "4. THE MOVE COMMAND CAN BE COMBINED WITH N, E, S, W TO MOVE IN NORTH EAST SOUTH AND WEST.")
		intro()

	elif opening.lower() == "exit":
		sys.exit()

	else:
		intro()
intro()




def ifhealthlessthan50():


	while health >0:






		choice2 = input("WHAT WOULD YOU LIKE TO DO?\n> ")

		if choice2.lower() == 'move n':
			if night == True:
				print(random.choice(biomes),  "IS WHERE YOU END UP")
				print("IT IS CURRENTLY NIGHT TIME YOU ENCOUNTERED A:",random.choice(list(monsters)))
				ifhealthlessthan50()
				fightingchoice = input("WOULD YOU LIKE TO FIGHT OR TRY TO RUN?")
				if fightingchoice.lower() == 'fight':
					fight = input("WOULD YOU LIKE TO ATTACK, EAT, OR TRY TO RUN?")
					if fight.lower() == 'attack':
						print("YOU HIT THE MONSTER FOR")
			elif night == False:
				print(random.choice(biomes),  "IS WHERE YOU END UP")
				ifhealthlessthan50()




		elif choice2.lower() == 'move s':
			print(random.choice(biomes), "IS WHERE YOU END UP")

		elif choice2.lower() == 'move e':
			print(random.choice(biomes), "IS WHERE YOU END UP")

		elif choice2.lower() == 'move w':
			print(random.choice(biomes), "IS WHERE YOU END UP")
		elif choice2.lower() == "help":
			print("COMMANDS\n1. THE COMMAND CRAFT ALLOWS YOU TO CRAFT ANY ITEM WITHIN THE RECIPES OF TEXTCRAFT"
				  "\n2.THE COMMAND EXIT WORKS AT ANY TIME TO ALLOW YOU TO EXIT THE GAME \n"
				  "3. THE COMMAND HELP ALLOWS YOU TO ACCESS THIS MENU AT ANY TIME\n"
				  "4. THE MOVE COMMAND CAN BE COMBINED WITH N, E, S, W TO MOVE IN NORTH EAST SOUTH AND WEST.")
			ifhealthlessthan50()

		elif choice2.lower() == 'exit':
			print("NOW EXITING...")
			sys.exit()

		elif choice2.lower() == 'inventory':
			for k in things:
				print("%s:%d"%(k, things[k]))
			ifhealthlessthan50()
		elif choice2.lower() == 'time':
			if night == True:
				print("NIGHT")
				ifhealthlessthan50()
			else:
				print("DAY")
				ifhealthlessthan50()


		elif choice2.lower() == 'hunger':
				print(hunger)
				ifhealthlessthan50()



		elif choice2.lower() == 'craft':
			craftinginput = input("WHAT WOULD YOU LIKE TO CRAFT?\n> ")

			if craftinginput.lower() == 'wood pickaxe':

				if things['PLANKS'] < 3 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()

				things['PLANKS'] -= 3
				things['STICKS'] -= 2
				things['WOOD PICKAXE'] += 1
				print("WOOD PICKAXE CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'wood sword':

				if things['PLANKS'] < 2 or things['STICKS'] < 1:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()

				things['PLANKS'] -= 2
				things['STICKS'] -= 1
				things['WOOD SWORD'] += 1
				print("WOOD SWORD CRAFTED!")

				ifhealthlessthan50()

			elif craftinginput.lower() == 'wood shovel':
				if things['PLANKS'] < 1 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()

				things['PLANKS'] -= 1
				things['STICKS'] -= 2
				things['WOOD SHOVEL'] += 1
				print("WOOD SHOVEL CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'diamond sword':
				if things['DIAMONDS'] < 2 or things['STICKS'] < 1:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['DIAMONDS'] -= 2
				things['STICKS'] -= 1
				things['DIAMOND SWORD'] += 1
				print("DIAMOND SWORD CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'diamond axe':
				if things['DIAMONDS'] < 3 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['DIAMONDS'] -= 3
				things['STICKS'] -= 2
				things['DIAMOND AXE'] += 1
				print("DIAMOND AXE CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'diamond shovel':
				if things['DIAMONDS'] < 1 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['DIAMONDS'] -= 1
				things['STICKS'] -= 2
				things['DIAMOND SHOVEL'] += 1
				print("DIAMOND SWORD CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'stone sword':
				if things['DIAMONDS'] < 2 or things['STICKS'] < 1:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['COBBLESTONE'] -= 2
				things['STICKS'] -= 1
				things['COBBLESTONE SWORD'] += 1
				print("COBBLESTONE SWORD CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'stone axe':
				if things['COBBLESTONE'] < 3 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['COBBLESTONE'] -= 3
				things['STICKS'] -= 2
				things['COBBLESTONE AXE'] += 1
				print("COBBLESTONE AXE CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'stone shovel':
				if things['COBBLESTONE'] < 1 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['COBBLESTONE'] -= 1
				things['STICKS'] -= 2
				things['COBBLESTONE SHOVEL'] += 1
				print("COBBLESTONE SWORD CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'iron sword':
				if things['IRON'] < 2 or things['STICKS'] < 1:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['IRON'] -= 2
				things['STICKS'] -= 1
				things['IRON SWORD'] += 1
				print("IRON SWORD CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'iron axe':
				if things['IRON'] < 3 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['IRON'] -= 3
				things['STICKS'] -= 2
				things['IRON AXE'] += 1
				print("IRON AXE CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'iron shovel':
				if things['IRON'] < 1 or things['STICKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['IRON'] -= 1
				things['STICKS'] -= 2
				things['IRON SHOVEL'] += 1
				print("IRON SWORD CRAFTED!")
				ifhealthlessthan50()

			elif craftinginput.lower() == 'sticks':
				if things['PLANKS'] < 2:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()
				things['PLANKS'] -= 2
				things['STICKS'] += 4
				print("STICKS CRAFTED")
				ifhealthlessthan50()

		elif choice2.lower() == 'smelt':
			smelting = input("WHAT WOULD YOU LIKE TO SMELT\n> ")
			if smelting.lower() == "iron":
				if things['IRON ORE'] < 1:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()

				things['IRON ORE'] -= 1
				things['IRON'] += 1
				print("IRON SMELTED")
				ifhealthlessthan50()

			if smelting.lower() == "gold":
				if things['GOLD ORE'] < 1:
					print("YOU DON'T HAVE THE RIGHT MATERIALS!")
					ifhealthlessthan50()

				things['GOLD ORE'] -= 1
				things['GOLD'] += 1
				print("GOLD SMELTED")
				ifhealthlessthan50()




		if health <0:
			print("YOU DIED!")
			time.sleep(1)
			print("RESTARTING...")

		else:
			print("THAT DOES NOT WORK")
		ifhealthlessthan50()
ifhealthlessthan50()
