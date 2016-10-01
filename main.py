import random
class Skeleton(object):
	def __init__(self,name):
		#Sets up specific skeleton features.
		self.life = random.randint(5,13)
		self.armor = random.randint(0,3)
		self.attack = random.randint(1,5)
		self.name = name
		self.armorquality = {0 : "no armor",1 : "broken armor",2 : "simple armor",3 : "magical armor"}
		self.sword = {1 : "no sword", 2 : "shattered sword", 3 : "normal sword", 4 : "powerful mace", 5 : "legendary sword"}
		self.alive = True

	def fight(self,damage,plife):
		#Checks if skeleton already dead
		if self.alive == False:
			print("Already dead...")
			return plife,damage
		#Calculates dealt damage
		hit = damage+random.randint(-1,1)-self.armor
		if hit > 0:
			self.life -= hit
		plife -= self.attack
		#Runs death event. Should probably be a function :P
		if self.life <= 0:
			print("%s is dead" % self.name)
			print("You now have %i life points" % plife)
			self.alive = False
			print('%s dropped a "%s"' % (self.name,self.sword[self.attack]))
			print('want to equip it? (y/n)')
			answer = input(">> ")
			if answer == "y":
				damage = self.attack
			return plife,damage
		print("You now have %i life points" % plife)
		print("%s now has %i life points" % (self.name,self.life))

		return plife,damage

	def look_at(self):
		#Checks if skeleton is dead
		if self.alive == False:
			print("Crushed bones...")
			return None
		#Gives player information about player.
		print("You look at %s:" % self.name)
		print("\n")
		print("He has %s and a %s" % (self.armorquality[self.armor],self.sword[self.attack]))
		print("He has %i life points. \n" % self.life)

def act():
	#Asks player for input and converts it to usable format.
	print("What do you want to do?")
	inputed = input(">> ").split(" ")
	for i in range(len(inputed)):
		inputed[i] = inputed[i].lower()
	return inputed

def main():
	print("You will be fighting against three skeletons:")
	print("Bob, Jeff and Carl")
	print("Your options are:")
	print("look at bob/carl/jeff")
	print("attack bob/carl/jeff")
	print('or exit by typing "quit"')
	#Sets up the three skeletons, as well as your life and starting sword.
	damage = 2
	plife = 100
	bob = Skeleton("Bob")
	carl = Skeleton("Carl")
	jeff = Skeleton("Jeff")

	#Main loop of the game. Stops when player is dead or pressed "Quit"
	while plife > 0:
		choice = act()
		if choice[0] == "quit":
			print ("GAME ENDED")
			exit(0)
		elif choice[-1] == "bob":
			if "look" in choice[0]:
				bob.look_at()
			else:
				plife,damage = bob.fight(damage,plife)
		elif choice[-1] == "carl":
			if "look" in choice[0]:
				carl.look_at()
			else:
				plife,damage = carl.fight(damage,plife)
		elif choice[-1] == "jeff":
			if "look" in choice[0]:
				jeff.look_at()
			else:
				plife,damage = jeff.fight(damage,plife)
	print("You lost!")
	print("Restarting...")
	main()

main()



