import re, random, logging, os, sys, pickle, time, traceback
from enum import Enum

#version
version = "Beta 0.5.0.0-EXPERIMENTAL"
experimental_version = True

credits = '''
           :dNdhs+\-._              	=============< Mildwind >=============
         :dMMMMMMMMMMNdhs+\._       	Developed by Keyboard Junkie Dev Team
      ./dMMMMMMMMMMMMMMMMMMMMNd-    
    ./dMMMNMMMMMMMNNMMMMNNMMMMMd    	Lead Programmer and Director
  ./dMMMM| mMMMd /dMMMMN |MMMMMM\   	Tyler "Ratchet Miles" Gilbert
.+mMMMMMM| dMMm /yNMMMMN |MMMMMMN`  
hMMMMMMMM| dm' /NMMMMMMN |MMMMMMMs  	Creative, Nagger, Tester, and Reviser
\MMMMMMMM|    +NMMMMMMMN |MMMMMMMM. 	James "Draco_rt" Stocchi
 hMMMMMMM| Mm  \MMNMMMMN |MMMMMMMMd 
 .NMMMMMM| dNm  \MMMMMMN |MMMMMMMMM:	Reviser and Tester
  sMMMMMM|_dMMm__\MMMMMN |MMMMMMMMM:    Chris "Ccosenza" Cosenza
  `mMMMMMNMMMMMMMMMMy.Md +MMMMMMMm+`
   \MMMMMMMMMMMMMMMMM\__+NMMMMMm+`      ASCII fonts provided by patorjk.com
    hMMMMMMMMMMMMMMMNNNNMMMMMd/`    
    -dNMMMMMMMMMMMMMMMMMMMMd/`      
      ``-\oshdNMMMMMMMMMMd:         	Version
               `-\+shmNh:           	''' + version + '''

Mildwind by Keyboard Junkie Dev Team is licensed under a Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.
'''

#logging
logging.basicConfig(filename='log.log', level=logging.DEBUG)
logging.debug("Game version: %s" % (version))
logging.debug("If you are experiencing issues, or feel like some commands should be added, copy and paste this log to http://pastebin.com/ and send the link to Keyboard Junkie Dev Team or Ratchet Miles.")

#todo
'''
-Finish game (duh)
-Decrease lines of code used (If possible)
-increase difficulty and chance of death
-Finish help (again)
-Randomized loot?
-Achievements?
'''

#intro
random_quotes = ["\"Alright, I've been thinking. When life gives you lemons, don't make lemonade! Make life take the lemons back! Get mad! I don't want your damn lemons; what am I supposed to do with these? Demand to see life's manager! Make life rue the day it thought it could give Cave Johnson lemons! Do you know who I am? I'm the man who's gonna burn your house down... with the lemons! I'm gonna get my engineers to invent a combustible lemon that burns your house down!\" -Cave Johnson", "\"Is a man not entitled to the sweat of his brow? \"No,\" says the man in Washington, \"it belongs to the poor.\" \"No,\" says the man in the Vatican, \"it belongs to God.\" \"No,\" says the man in Moscow, \"it belongs to everyone.\" I rejected those answers; instead, I chose something different. I chose the impossible. I chose... Rapture. A city where the artist would not fear the censor; where the scientist would not be bound by petty morality; where the great would not be constrained by the small! And with the sweat of your brow, Rapture can become your city as well.\" -Andrew Ryan", "\"A man chooses; a slave obeys.\" -Andrew Ryan", "\"I never asked for this.\" -Adam Jensen", "\"The right man in the wrong place can make all the difference in the world\" -G-Man", "\"Like is says in the book, we are blessed and cursed.\" -Big Smoke", "\"If today were the last day of your life, would you want to do what you're about to do today?\" -Steve Jobs", "\"Try not to become a man of success, but rather try to become a man of value.\" -Albert Einsein", "\"Whoever is careless with the truth in small matters cannot be trusted with important matters.\" -Albert Einsein", "\"Knowledge is knowing that a tomato is a fruit, wisdom is not putting it in a fruit salad.\" -Miles Kington"]

def show_random_quote():
	print(random.choice(random_quotes))

KJ = '''
           :dNdhs+\-._              
         :dMMMMMMMMMMNdhs+\._       
      ./dMMMMMMMMMMMMMMMMMMMMNd-    
    ./dMMMNMMMMMMMNNMMMMNNMMMMMd    
  ./dMMMM| mMMMd /dMMMMN |MMMMMM\   	 _____ _ _   _       _       _ 
.+mMMMMMM| dMMm /yNMMMMN |MMMMMMN`  	|     |_| |_| |_ _ _|_|___ _| |
hMMMMMMMM| dm' /NMMMMMMN |MMMMMMMs  	| | | | | | . | | | | |   | . |
\MMMMMMMM|    +NMMMMMMMN |MMMMMMMM. 	|_|_|_|_|_|___|_____|_|_|_|___|
 hMMMMMMM| Mm  \MMNMMMMN |MMMMMMMMd 	
 .NMMMMMM| dNm  \MMMMMMN |MMMMMMMMM:		 _       
  sMMMMMM|_dMMm__\MMMMMN |MMMMMMMMM:		| |_ _ _ 
  `mMMMMMNMMMMMMMMMMy.Md +MMMMMMMm+`		| . | | |
   \MMMMMMMMMMMMMMMMM\__+NMMMMMm+`  		|___|_  |
    hMMMMMMMMMMMMMMMNNNNMMMMMd/`    		    |___|
    -dNMMMMMMMMMMMMMMMMMMMMd/`      
      ``-\oshdNMMMMMMMMMMd:         
               `-\+shmNh:           
                 _                         _    __              _    _      
  /\ /\___ _   _| |__   ___   __ _ _ __ __| |   \ \ _   _ _ __ | | _(_) ___ 
 / //_/ _ \ | | | '_ \ / _ \ / _` | '__/ _` |    \ \ | | | '_ \| |/ / |/ _ \\
/ __ \  __/ |_| | |_) | (_) | (_| | | | (_| | /\_/ / |_| | | | |   <| |  __/
\/  \/\___|\__, |_.__/ \___/ \__,_|_|  \__,_| \___/ \__,_|_| |_|_|\_\_|\___|
           |___/                                                            '''

print(KJ)
input("================================ Press Enter ================================")
print("\n")
print("The time is " + time.ctime())
show_random_quote()
print("\nVersion: %s\n" % (version))
if experimental_version:
	print("NOTE: THIS IS AN EXPERIMENTAL BUILD OF MILDWIND -PLEASE- TELL ME IF THERE ARE ANY PROBLEMS YOU COME PAST.\n")

#variables
help = "=< HELP >=\nObjective: The objective of the game is to type commands to beat the game. You simply type a command and read the results.\n\nStats: You can view your stats using the \"stats\" command. Your health is, well, your health. Armor reduces your health damage. Potions are a limited resource that restore 40 health per use. Attack is how much damage you give per hit. Stamina is how much strength you have. This is degraded when you use your shield and regained when the chapter ends. Hints are a limited amount of tips that assist you when you're stuck. These are also known as scrolls.\n\nCommon commands:\n-Help: Brings up this menu.\n-Hint: Gives you a hint as to what to do.\n-Potion: Uses a potion.\n-Attack: Cannot be used all the time, but is used to battle enemies.\n-Shield: Cannot be used all the time, but can give a small amount of damage and regenerate a little health. Uses stamina.\n-Continue, Press forward, Follow, etc: Cannot be used all the time, but is used to progress to the next chapter.\n-Stats: Displays stats such as health.\n-Newname: Gives you the option to change your name.\n-Newgame: Gives you the option to start a new game. \n-Reload: Loads game from last save.\n-Exit, kill, quit, and close: Close the game."

player_stats = "=< STATS >=\nName: %s\nHealth: %s/%s\nItems:\n Weapon: %s \n Armor: %s \n Shield: %s\nArmor: %s\nWeapon Damage: %s\nAttack: %s\nStamina: %s/%s\nInventory:\n %s\nTime Played: %s"

enemy_stats = "=< ENEMY STATS >=\nName: %s\nHealth: %s\nAttack Damage: %s-%s\nArmor: %s"

#classes
class Weapon(Enum):
	fists				= ("Fists",				10)
	steel_sword			= ("Cheap Steel Sword",	40)
	dagger				= ("Old Dagger",		20)
	broadsword			= ("Broadsword",		50)
	machete				= ("Ancient Machete",	45)
	hero_sword			= ("Hero Sword",		75)
	dragon_slayer		= ("Dragon Slayer",		100)

	def name(self):
		return self.value[0]

	def damage(self):
		return self.value[1]

class Armor(Enum):
	prison_clothes		= ("Worn Prison Clothes",	1)
	leather_armor		= ("Cheap Leather Armor",	1.5)
	rusty_armor			= ("Rusty Old Armor",		1.4)
	scorpio_armor		= ("Scorpio Armor",			2)

	def name(self):
		return self.value[0]

	def armor(self):
		return self.value[1]

class Shield(Enum):
	none				= ("None", 0, 0)
	wooden_shield		= ("Wooden Shield", 3, 25)
	shield_of_the_gods	= ("Shield of the Gods", 6, 5)

	def name(self):
		return self.value[0]

	def damage(self):
		return self.value[1]

	def chance(self):
		return self.value[2]

class Potion(Enum):
	small	= ("Small Potion",    25)
	medium	= ("Medium Potion",   40)
	large	= ("Large Potion",   100)
	super	= ("Super Potion", "max")

	def name(self):
		return self.value[0]

	def healing(self):
		return self.value[1]

class Item(Enum):
	scroll				= "Scroll (Hint)"
	torch				= "Torch"
	prison_key			= "Prison Key"
	trans_book			= "Book of the Dragon Language"
	relic				= "Dragon Stone"
	drazmite			= "Drazmite Ore"
	iron				= "Iron Ore"
	herb				= "Herb"
	scorpion_shell		= "Scorpion Shell"
	swamp_map			= "Map to Swamp"
	strange_recipe		= "Strange potion recipe book"

	def name(self):
		return self.value

class InventoryItem():
	def __init__(self, type, amount=1):
		self.type = type
		self.amount = amount

class Inventory():
	def __init__(self):
		self.weapons		= [Weapon.fists]
		self.armors			= [Armor.prison_clothes]
		self.shields		= [Shield.none]
		self.items			= [InventoryItem(Item.scroll, 3)]
		
class Unlocked_areas():
	def __init__(self):
		self.dracordlair		= False
		#[DONE] Visit the first time to discover where the key is. No understanding of words without book.
		#[DONE] Fail to fight Dracord. Revived by Ruffin's ghost at Redwind. Visit Bruce.
		#Fight with new sword, win.
		self.forest				= False
		#[DONE] Gain access by talking to Bruce. Collect materials for potions. Player can theoretically come here as much as he/she wants, but it takes forever.
		#[DONE] Make player wait 30 minutes. Get random amount of herbs.
		self.swamp				= False
		#[DONE] Library gives you map to swamp.
		#Fight Giant Turtle and trolls, boss fight with chief. Get shield. Use special potion.
		self.mountains			= False
		#[DONE] Fight bear. Grab key.
		self.northmine			= False
		#[DONE] Visit to gather materials to make a powerful sword.
		#[DONE] Go to Bruce. 
		self.southmine			= False
		#[DONE] Come here for special ore. Fight scorpion.
		#[DONE] Bruce can turn scorpion shell into armor.
		#[DONE] Scorpion blood can be drank as special potion.
		self.river				= False
		#[DONE] Bruce refers you to Dazzle. Enchant sword. Get directed other mine. Gives special potion.
		#[DONE] Player can come here to brew potions.
		self.library			= False
		#[DONE] Go here for translation book.
		#[DONE] Also get scroll if 0.

'''
class Achievements():
	def __init__(self):
		#ID				= ["achievement", "description"]
		headbanger		= ["Headbanger", "Bash your head into the wall"]
		encounter		= ["The Encounter", "Meet Ruffin"]
		suicide			= ["Suicide", "Kill yourself (the doppleghanger)"]
		farmer			= ["Farmer", "Gather herbs in the forest"]
'''
		
class Player():
	def __init__(self, name):
		self.name			= name
		self.command		= ""
		self.printer		= True
		self.version		= version
		self.inventory		= Inventory()

		self.weapon			= Weapon.fists
		self.armor			= Armor.prison_clothes
		self.shield			= Shield.none

		self.healthbank		= 0
		self.stambank		= 0
		self.armorbank		= 0

		self.maxstamina		= 0
		self.maxhealth		= 100
		self.health			= self.maxhealth

		self.extattack		= 0
		self.stamina		= 0

		self.farmwait		= 30
		self.minewait		= 15
		
		self.sarmor			= False
		self.sshield		= False
		self.smetals		= False
		self.metals			= False
		self.shell			= False
		self.strangeblood	= False
		self.hassarmor		= False
		self.sforged		= False
		self.forged			= False
		self.strangeperm	= False
		self.strangerecipe	= False
		self.hasmap			= False
		self.hasstone		= False
		self.hasitems		= False
		self.stolen			= False
		self.ruffindead		= False
		self.headbanger		= False
		self.runfailed		= False
		self.haswolf		= False
		self.visiteddracord = False

		self.transbook		= False
		self.dracordUnlock	= False
		self.dracordReady	= False
		self.dracordTry		= False
		self.shielduse		= 0
		self.cheated		= False
		self.savepos		= []
		self.randhint		= []
		self.logging		= ""
		self.cmdext			= ""
		
		self.areas			= Unlocked_areas()

	def gethealth(self):
		return int(self.health)

	def sethealth(self, health, damagemsg="", deathmsg="", ending=""):
		self.health = int(health)
		if (self.health > self.maxhealth):
			self.health = self.maxhealth
		if self.health <= 0:
			self.health = 0
			show_end_message(deathmsg, ending, "lose")
		else:
			print(damagemsg.format("", self.gethealth()))

	def heal(self, amount):
		self.sethealth(self.health + amount)

	def fullheal(self):
		self.sethealth(self.maxhealth)

	def hurt(self, amount, armor=False, damagemsg="", deathmsg="", ending=""):
		if (armor):
			amount /= self.armor.armor()
		self.sethealth(self.health - amount, damagemsg, deathmsg, ending)

	def get_attack_damage(self):
		return self.weapon.damage() + self.extattack

	def attack_enemy(self, enemy, giveshielduse=True):
		if enemy.dead:
			print(enemy.deadmsg)
		else:
			enemy.hurt(self.get_attack_damage() / enemy.armor)
			if enemy.dead:
				self.give_items(enemy.rewards)
				talking(enemy.killedmsg.format(self.gethealth()))
			else:
				damage = enemy.random_attack()
				self.hurt(damage, True, enemy.damagemsg.format(enemy.health, "{1}"), enemy.deathmsg, enemy.ending)
				if giveshielduse:
					if (self.shielduse > 0):
						self.shielduse -= 1

	def use_shield(self, enemy):
		if game.player.shield is not Shield.none:
			if enemy.dead:
				talking(enemy.deadmsg, .02)
			else:
				if self.stamina <= 0:
					talking("You don't have enough stamina.", .02)
				else:
					if game.player.shielduse >= 2:
						damage = enemy.random_attack()
						self.hurt(damage, True, enemy.learnedmsg.format("{1}"), enemy.deathmsg)
					else:
						game.player.stamina -= 1
						game.player.shielduse += 1
						if game.random_chance(self.shield.chance()):
							damage = enemy.random_attack() / 2
							self.hurt(damage, True, enemy.reachmsg.format("{1}"), enemy.deathmsg)
						else:
							enemy.hurt(self.shield.damage() / enemy.armor)
							self.heal(10)
							if enemy.dead:
								self.give_items(game.current_enemy.rewards)
								talking(enemy.shieldkilledmsg.format(self.gethealth()), .02)
							else:
								print(enemy.shieldmsg.format(enemy.health, self.gethealth()))
		else:
			talking("You don't have a shield.", .02)

	def run_from_enemy(self, enemy, damage=[0, 5]):
		ran = False
		if not enemy.dead:
			randomdamage = random.choice(damage)
			if (randomdamage > 0):
				self.hurt(randomdamage, False, enemy.rundamagemsg, enemy.rundeathmsg, enemy.runending)
				if self.runfailed:
					if enemy.runfailedmsg is not "":
						print(enemy.runfailedmsg.format(self.name))
				self.runfailed = True
			else:
				print(enemy.runmsg)
				ran = True
		else:
			talking("You continue your journey to defeat Dracord.", .04)
			ran = True
		return ran

	def getitem(self, item):
		for invitem in self.inventory.items:
			if invitem.type == item:
				return invitem

	def get_item_amount(self, item):
		amount = 0
		if self.getitem(item) is not None:
			amount = self.getitem(item).amount
		return amount

	def has_item(self, item):
		return self.getitem(item) is not None

	def give_item(self, item, amount=1):
		if isinstance(item, Weapon):
			type_inv = self.inventory.weapons
			self.weapon = item
		elif isinstance(item, Armor):
			type_inv = self.inventory.armors
			self.armor = item
		elif isinstance(item, Shield):
			type_inv = self.inventory.shields
			self.shield = item
		else:
			if self.has_item(item):
				self.getitem(item).amount += amount
			else:
				self.inventory.items.append(InventoryItem(item, amount))
			return
		type_inv.append(item)

	def give_items(self, items):
		for item in items:
			self.give_item(item[0], item[1])

	def take_item(self, item, amount=1):
		if self.has_item(item):
			invitem = self.getitem(item)
			if invitem.amount >= 1:
				invitem.amount -= amount
			if invitem.amount < 1:
				self.inventory.items.remove(self.getitem(item))

class Enemy():
	def __init__(self, name="Enemy", health=100, attack=(5, 20), armor=1):
		self.name				= name
		self.health				= health
		self.attack				= attack
		self.armor				= armor
		self.dead				= False
		self.rewards    		= []
		self.deadmsg			= "You look at the dead %s." % (self.name.lower())
		self.killedmsg			= "The %s is dead." % (self.name.lower())
		self.damagemsg  		= "You attack the %s." % (self.name.lower())
		self.deathmsg   		= "You were killed."

		self.shieldkilledmsg 	= "You safely deflect the enemy's attacks and kill it."
		self.shieldmsg			= "You deflect the enemy's attack and it hurts itself in the process. You used some of your stamina."
		self.learnedmsg			= "The %s learned your moves and attacked you. Your health is now {0}" % (self.name.lower())
		self.reachmsg			= "The %s was able to reach over your shield and stab you a bit. Your health is now {0}." % (self.name.lower())

		self.rundamagemsg		= "The %s attacked you." % (self.name.lower())
		self.rundeathmsg		= "You were killed by the %s." % (self.name.lower())
		self.runmsg				= "You escaped the %s." % (self.name.lower())
		self.runfailedmsg		= ""
		self.ending				= ""
		self.runending			= ""

	def min_attack(self):
		return self.attack[0]

	def max_attack(self):
		return self.attack[1]

	def random_attack(self):
		return random.randrange(self.min_attack(), self.max_attack())

	def gethealth(self):
		return int(self.health)

	def sethealth(self, health):
		self.health = int(health)
		if self.health <= 0:
			self.kill()

	def hurt(self, amount):
		self.sethealth(self.health - amount)

	def kill(self):
		self.health = 0
		self.dead = True

no_enemy = Enemy("None", 0)
		
class Game():
	def __init__(self):
		self.player = Player("Player")
		self.current_enemy = no_enemy
		self.starttime = ""
		self.set_start_time()

	def set_current_enemy(self, enemy):
		self.current_enemy = enemy

	def set_start_time(self):
		self.starttime = time.time()

	def random_chance(self, percent):
		return random.randrange(100) < percent

game = Game()

#functions

#save/load
#saving
def save():
	fwrite = open("saves/" + game.player.name, "wb")
	pickle.dump(game.player, fwrite)
	fwrite.close()

#restoring
def load():
	f = open("saves/" + game.player.name, "rb")
	game.player = pickle.load(f)
	f.close()
	print(">>>Starting from save...")
	
def choose_name():
	while True:
		game.player.name = input("Identify yourself (Just press enter to use your PC's name)\n>")
		if game.player.name == "":
			print("Nothing entered. Using system name.")
			game.player.name = os.getlogin()
			if re.match(r'^[A-Za-z0-9 _~-]+$', game.player.name):
				break
			else:
				print("Can't use system name. Please type a name.")
		elif re.match(r'^[A-Za-z0-9 _~-]+$', game.player.name):
			break
		else:
			print("Invalid use of characters.")
	
def commands():
	while True:
		game.player.command = input(">").lower()
		logging.info(str(game.player.savepos) + ":" + game.player.command)
		if game.player.command in ["hint", "scroll"]:
			use_hint()
		elif game.player.command in ["potion", "use potion", "drink potion", "potions"]:
			list_potion_types()
		elif game.player.command in ["spot", "smallpot", "smallpotion", "small potion"]:
			use_potion(Potion.small)
		elif game.player.command in ["mpot", "medpot", "mediumpot", "medpotion", "mediumpotion", "medium potion"]:
			use_potion(Potion.medium)
		elif game.player.command in ["lpot", "lrgpot", "largepot", "lrgpotion", "largepotion", "large potion"]:
			use_potion(Potion.large)
		elif game.player.command in ["sppot", "suppot", "superpot", "suppotion", "superpotion", "super potion"]:
			use_potion(Potion.super)
		elif game.player.command == "stats":
			show_player_stats()
		elif game.player.command == "enstats":
			show_enemy_stats()
		#elif game.player.command == "inventory":
			#show_inventory()
		elif game.player.command == "help":
			show_help()
		elif game.player.command == "newname":
			change_name()
		elif game.player.command == "newgame":
			start_new_game()
		elif game.player.command == "reload":
			reload()
		elif game.player.command in ["clear", "cls"]:
			clear_console()
		elif game.player.command in ["exit", "quit", "kill", "close"]:
			quit()
		elif game.player.command == "quote":
			show_random_quote()
		#elif game.player.command == "achievement":
			#show_achievement()
		elif game.player.command == "printing":
			printingtoggle()
		elif game.player.command == "credits":
			show_credits()
		elif game.player.command == "cheats":
			show_cheats()
		elif game.player.command == "cmd":
			cmdmode()
		else:
			game.player.cmdext()

def printingtoggle():
	game.player.printer = not game.player.printer
	if game.player.printer:
		talking("Printing is on.", .04)
	else:
		print("Printing is off.")

def talking(phrasetext, texttime=.03):
	for i in str(phrasetext):
		if game.player.printer:
			time.sleep(texttime)
		sys.stdout.write(i)
		sys.stdout.flush()
		if game.player.printer:
			if i in [".", "!", "?", ":"]:
				time.sleep(texttime*5)
			elif i in [",", ";"]:
				time.sleep(texttime*3)
	time.sleep(.55)
	print()
	
def talking_TEST_DO_NOT_REMOVE(phrasetext, texttime=.03):
	p = [".", "!", "?", ":"]
	p2 = [",", ";"]
	for i, c in enumerate(str(phrasetext)):
		nc = phrasetext[i]
		if game.player.printer:
			time.sleep(texttime)
		sys.stdout.write(c)
		sys.stdout.flush()
		if nc not in ["\""] and nc not in p and nc not in p2:
			if c in p:
				time.sleep(texttime * 10)
			elif c in p2:
				time.sleep(texttime * 3)
	time.sleep(.75)
	print()

def show_credits():
	print(credits)

def get_time_played():
	return str(int(time.time() - game.starttime))

def use_hint():
	if game.player.has_item(Item.scroll):
		game.player.take_item(Item.scroll)
		talking(random.choice(game.player.randhint), .02)
		print("You have %s scroll(s) left." % (game.player.get_item_amount(Item.scroll)))
	else:
		talking("You don't have any scrolls to use.")

def list_potion_types():
	print("Potion Commands:\nSmall Potion:\n spot\n smallpot\n smallpotion\n small potion\nMedium Potions:\n mpot\n medpot\n mediumpot\n medpotion\n mediumpotion\n medium potion\nLarge Potions:\n lpot\n lrgpot\n largepot\n lrgpotion\n largepotion\n large potion\nSuper Potions:\n sppot\n suppot\n superpot\n suppotion\n superpotion\n super potion\n")

def use_potion(type):
	if (not game.player.has_item(type)):
		talking("You don't have any of that type of potion to use.", .01)
		return
	if game.player.gethealth() >= game.player.maxhealth:
		talking("You already have max health.", .01)
	else:
		if type.healing() == "max":
			game.player.fullheal()
		else:
			game.player.heal(type.healing())
		print("Potion used. Your health is now %s." % (game.player.gethealth()))
		game.player.take_item(type, 1)

def show_player_stats():
	def if_not_zero(statname, amount, maxamount):
		if amount == 0 and maxamount == "" or amount == "[N/A]" or maxamount == 0:
			pass
		elif maxamount == "":
			print(statname, amount)
		elif maxamount > 0:
			print(statname, amount, "/", maxamount)
	print()
	print("=< STATS >=")
	print("Name:           ", game.player.name)
	print("Health:         ", game.player.gethealth(), "/", game.player.maxhealth)

	print("Items:")
	print(" Weapon:        ", game.player.weapon.name())
	print(" Armor:         ", game.player.armor.name())
	if game.player.shield is not Shield.none:
		print(" Shield:        ", game.player.shield.name())

	print("Armor:          ", game.player.armor.armor())
	print("Weapon Damage:  ", game.player.weapon.damage())
	print("Total Damage:   ", game.player.get_attack_damage())
	if_not_zero("Stamina:        ", game.player.stamina, game.player.maxstamina)

	print("Inventory:")
	for item in game.player.inventory.items:
		itemstring = " %s" % (item.type.name())
		if item.amount > 1:
			itemstring += " (%s)" % (item.amount)
		print(itemstring)

	print("Time Played:    ", get_time_played() + " seconds")
	if game.player.cheated:
		print("CHEATED")
	else:
		pass

def show_enemy_stats():
	enemy = game.current_enemy
	print(enemy_stats % (enemy.name, enemy.health, enemy.min_attack(), enemy.max_attack(), enemy.armor))
	
def show_help():
	print("What would you like help with?\n\nYou can also press enter for a summary.\n")
	print("Objective\nCommands\nStats\nPotions\nHints\nExit")
	while True:
		helpcmd = input("HELP>").lower()
		if helpcmd == "":
			print(help)
			print("\nOther commands for help:")
			print("Objective\nCommands\nStats\nPotions\nHints\nExit")
		elif helpcmd == "objective":
			print("Objective: The objective of the game is to type commands to beat the game. You simply type a command and read the results.")
		elif helpcmd == "commands":
			print("Common commands:\n-Help: Brings up this menu.\n-Hint: Gives you a hint as to what to do.\n-Potion: Uses a potion.\n-Attack: Cannot be used all the time, but is used to battle enemies.\n-Shield: Cannot be used all the time, but can give a small amount of damage and regenerate a little health. Uses stamina.\n-Continue, Press forward, Follow, etc: Cannot be used all the time, but is used to progress to the next chapter.\n-Stats: Displays stats such as health.\n-Newname: Gives you the option to change your name.\n-Newgame: Gives you the option to start a new game. \n-reload: Loads game from last save.\n-Exit, kill, quit, and close: Close the game.")
		elif helpcmd == "stats":
			print("Stats: You can view your stats using the \"stats\" command. Your health is, well, your health. Armor reduces your health damage. Your strength is how strong you are. Potions are a limited resource that restore 40 health per use. Attack is how much damage you give per hit. Stamina is how much strength you have. This is degraded when you use your shield and regained when the chapter ends. Hints are a limited amount of tips that assist you when you're stuck. These are also known as scrolls.")
		elif helpcmd == "potions":
			print("Potions: Potions heal you. There are many different types of potions though. There are small potions which heal 25 health, medium potions which heal 40 health, large potions which heal 100 health, and super potions which heal to your max health.\n")
			print("Potion Commands:\nSmall Potion:\n spot\n smallpot\n smallpotion\n small potion\nMedium Potions:\n mpot\n medpot\n mediumpot\n medpotion\n mediumpotion\n medium potion\nLarge Potions:\n lpot\n lrgpot\n largepot\n lrgpotion\n largepotion\n large potion\nSuper Potions:\n sppot\n suppot\n superpot\n suppotion\n superpotion\n super potion\n")
		elif helpcmd == "hints":
			print("Hints: Also known as scrolls, hints can be used to help you when you are lost or stuck in an area. Hints are limited but can be found by fighting enemies or talking to people.")
		elif helpcmd in ["exit", "quit", "kill", "close"]:
			print("Resuming game...")
			break
		else:
			print("Invalid command")
			print("Objective\nCommands\nStats\nPotions\nHints\nExit")
	
def cmdmode():
	game.player.cheated = True
	print("WARNING! You may ruin your save! Be careful!")
	while True:
		cmd = input("CMD>")
		if cmd == "exit":
			break
		else:
			try:
				exec(cmd)
			except:
				traceback.print_exc()
	
def show_cheats():
	talking("WARNING! Cheats could break your save!\n", 0.02)
	print("Maxstamina\nStamfill\nMaxhealth\nHeal\nPotions\nHints\nEvents\nAreas\nExit")
	game.player.cheated = True
	while True:
		cheatcmd = input("CHEATS>").lower()
		if cheatcmd == "maxstamina":
			value = input("Set maxstamina value.\nCHEATS/maxstamina>")
			try:
				if float(value) > 0:
					print("maxstamina set to %s." % (float(value)))
					game.player.maxstamina = float(value)
				else:
					print("Must be greater than 0.")
			except ValueError:
				print("Not a number.")
		elif cheatcmd == "stamfill":
			print("Stamina filled.")
			game.player.stamina = game.player.maxstamina
		elif cheatcmd == "maxhealth":
			value = input("Set maxhealth value.\nCHEATS/MAXHEALTH>")
			try:
				if float(value) > 0:
					print("Maxhealth set to %s." % (float(value)))
					game.player.maxhealth = float(value)
					game.player.fullheal()
				else:
					print("Must be greater than 0.")
			except ValueError:
				print("Not a number.")
		elif cheatcmd == "heal":
			print("Healed.")
			game.player.fullheal()
		elif cheatcmd == "shieldreset":
			print("Shielduse reset.")
			game.player.shielduse = 0
		elif cheatcmd == "potions":
			print("Small\nMedium\nLarge\nSuper")
			value = input("Choose a potion size\nCHEATS/POTIONS>").lower()
			if value == "small":
				value = input("How many?\nCHEATS/POTIONS/SMALL>")
				try:
					game.player.give_item(Potion.small, int(value))
					print("You have %s potions." % (value))
				except ValueError:
					print("Not a number.")
			elif value == "medium":
				value = input("How many?\nCHEATS/POTIONS/MEDIUM>")
				try:
					game.player.give_item(Potion.medium, int(value))
					print("You have %s potions." % (value))
				except ValueError:
					print("Not a number.")
			elif value == "large":
				value = input("How many?\nCHEATS/POTIONS/LARGE>")
				try:
					game.player.give_item(Potion.large, int(value))
					print("You have %s potions." % (value))
				except ValueError:
					print("Not a number.")
			elif value == "super":
				value = input("How many?\nCHEATS/POTIONS/SUPER>")
				try:
					game.player.give_item(Potion.super, int(value))
					print("You have %s potions." % (value))
				except ValueError:
					print("Not a number.")
			else:
				show_entry_message()
		elif cheatcmd == "hints":
			value = input("How many?\nCHEATS/HINTS>")
			try:
				game.player.give_item(Item.scroll, float(value))
				print("You have %s scrolls." % (value))
			except ValueError:
				print("Not a number.")
		elif cheatcmd == "events":
			print("hasitems = ", game.player.hasitems)
			print("stolen = ", game.player.stolen)
			print("ruffindead = ", game.player.ruffindead)
			print("headbanger = ", game.player.headbanger)
			print("runfailed = ", game.player.runfailed)
			value = input("Choose a value to toggle.\nCHEATS/EVENTS>")
			if value == "hasitems":
				game.player.hasitems = not game.player.hasitems
			if value == "transbook":
				game.player.transbook = not game.player.transbook
			elif value == "stolen":
				game.player.stolen = not game.player.stolen
			elif value == "ruffindead":
				game.player.ruffindead = not game.player.ruffindead
			elif value == "headbanger":
				game.player.headbanger = not game.player.headbanger
			elif value == "runfailed":
				game.player.runfailed = not game.player.runfailed
			else:
				show_entry_message()
		elif cheatcmd == "areas":
			print("Dracord = ", game.player.areas.dracordlair)
			print("Forest = ", game.player.areas.forest)
			print("Swamp = ", game.player.areas.swamp)
			print("Mountains = ", game.player.areas.mountains)
			print("North Mine = ", game.player.areas.northmine)
			print("South Mine = ", game.player.areas.southmine)
			print("River = ", game.player.areas.river)
			print("Library = ", game.player.areas.library)
			value = input("Choose a value to toggle.\nCHEATS/AREAS>").lower()
			if value == "dracord":
				game.player.areas.dracordlair = not game.player.areas.dracordlair
			elif value == "forest":
				game.player.areas.forest = not game.player.areas.forest
			elif value == "swamp":
				game.player.areas.swamp = not game.player.areas.swamp
			elif value == "mountains":
				game.player.areas.mountains = not game.player.areas.mountains
			elif value == "north mine":
				game.player.areas.northmine = not game.player.areas.northmine
			elif value == "south mine":
				game.player.areas.southmine = not game.player.areas.southmine
			elif value == "river":
				game.player.areas.river = not game.player.areas.river
			elif value == "library":
				game.player.areas.library = not game.player.areas.library
			else:
				show_entry_message()
		elif cheatcmd in ["exit", "quit", "kill", "close"]:
			print("Resuming game...")
			break
		else:
			print("Invalid command")

def change_name():
	while True:
		newname = input("Identify yourself\n>")
		if newname == "":
			print("Nothing entered!")
		elif re.match(r'^[A-Za-z0-9 _~-]+$', newname):
			break
		else:
			print("Invalid use of characters.")
		check = input("Are you sure? (y/n)\n>").lower()
		if check == "y":
			game.player.name = newname
			talking("Your name is now %s" % (game.player.name))
			break
		else:
			talking("Name left unchanged.")
			break
			
def quit():
	check = input("Are you sure you want to quit? (y/n)\n>").lower()
	while True:
		if check == "y":
			sys.exit()
		else:
			print("Resuming game.")
			break

def show_survey():
	input("When doing this survey, remember to be very descriptive, and you can't press enter to add a new paragraph. Enter goes to the next question.")
	survey1 = input("On a scale of 1 - 10, what do you think of Mildwind so far?\n>")
	logging.info("Question 1 \"On a scale of 1 - 10, what do you think of Mildwind so far?\": " + survey1)
	survey2 = input("Are there any commands I should add? Where?\n>")
	logging.info("Question 2 \"Are there any commands I should add? Where?\": " + survey2)
	survey3 = input("What problems have you faced?\n>")
	logging.info("Question 3 \"What problems have you faced?\": " + survey3)
	survey4 = input("How could I improve the game?\n>")
	logging.info("Question 4 \"How could I improve the game?\": " + survey4)
	input("Thank you for doing the survey. In order for me to see your answers, you must follow the instructions in the log or readme file.")

def show_end_message(deathmsg, ending, winlose):
	if deathmsg is not "":
		print(deathmsg)
	if ending is not "":
		print("\"%s\" ending" % (ending))
	show_player_stats()
	if winlose == "win":
		win()
	else:
		lose()
	sys.exit()
	
def end_game(winlose):
	while True:
		choice = input(winlose).lower()
		if choice == "newgame":
			start_new_game()
		elif choice == "reload":
			load()
			game.player.savepos()
		elif choice == "quit":
			print("Don't forget to send me your log if you don't mind (More info about that in the readme file)!")
			survey = input("Would you like to take a survey to help me improve my game? The survey answers will be saved in the log file. (y/n)\n>").lower()
			if survey == "y":
				show_survey()
				sys.exit()
			else:
				logging.info("END OF SESSION; NO SURVEY")
				input("Thank you for playing my game!")
				sys.exit()
		else:
			show_entry_message()
	
def win():
	end_game("You win. Would you like to play again, start from a save, or quit (newgame/reload/quit)?\n>")

def lose():
	end_game("You lose. Would you like to play again, start from a save, or quit (newgame/reload/quit)?\n>")
	
def reset_stats():
	file = game.player.name
	os.remove("saves/" + file)
	game.player = Player(file)
			
def clear_console():
	clear = "\n" * 100
	choice = input("Would you like to clear the console? This cannot be undone. (y/n)\n>").lower()
	if choice == "y":
		print(clear)
	else:
		print("Resuming game")
		
def start_new_game():
	choice = input("Would you like to start a new game? (y/n)\n>").lower()
	if choice == "y":
		reset_stats()
		game.set_start_time()
		print("Starting new game...")
		part1()
	else:
		print("Resuming game")
		
def reload():
	choice = input("Would you like to load from the last checkpoint? (y/n)\n>").lower()
	if choice == "y":
		print("\n")
		load()
		game.player.savepos()
	else:
		print("Resuming game")
		
def show_entry_message():
	print("Invalid entry. (Need help? Try 'hint' or 'help'.)")

def log_stats(part):
	logging.info("Part " + part + " Stats:" + "\n" + player_stats % ("game.player", game.player.gethealth(), game.player.maxhealth, game.player.weapon.name(), game.player.armor.name(), game.player.shield.name(), game.player.armor.armor(), game.player.weapon.damage(), game.player.get_attack_damage(), game.player.stamina, game.player.maxstamina, game.player.inventory, get_time_played()) + "\n" + "Cheated: " + str(game.player.cheated))
	
#===========================actual game===========================
	
#tutorial
def tutorial():
	talking("Welcome to Mildwind! In this tutorial, I will guide you on how the basics of the game work.", .04)
	while True:
		tuthint = input("Firstly, let's show you what to do when you're stuck. When you don't know what to do, just type \"hint\". Using the hint command will subtract one hint from your stats. Hints are also known as scrolls. You can find them throughout Mildwind. Use \"hint\" now.\n>").lower()
		if tuthint == "hint":
			talking("Great! You just used a hint. (This hint use will not count against you in the actual game)")
			print("You have 2 hint(s) left.")
			break
		else:
			talking("That's not how you use hints. Try again (Type \"hint\").", .04)
	while True:
		tutpotion = input("You look a little hurt, drink a potion. To drink a potion, just type \"potion\". Potions can be found often and will be critical to your survival later on in Mildwind. Use \"potion\" now.\n>").lower()
		if tutpotion == "potion":
			print("Potion used. Your health is now maxed.")
			break
		else:
			talking("That's not how you use potions. Try again (Type \"potion\").", .04)
	while True:
		tutattack = input("LOOK OUT! There's a wolf coming right at you! To attack enemies, type \"attack\".\n>").lower()
		if tutattack == "attack":
			print("You defeated the wolf.")
			break
		else:
			talking("That's not how you use attacks. Try again (Type \"attack\").", .04)
	while True:
		tutgeneral = input("Sometimes the game won't tell you what to do. For instance: \"There is a door in front of you.\" What do you think you have to do here?\n>").lower()
		if tutgeneral in ["door", "open door", "open the door"]:
			talking("You opened the door and went into the next room.", .05)
			talking("Good! When playing Mildwind, be sure to read carefully. You may need to do certain actions to get things you may need. In some instances, you won't even be able to progress without trying to figure out what to do on your own. If you ever get stuck, remember to use \"hint\", but also know that hints are limited.", .05)
			break
		else:
			print("Try \"open door\".")
	while True:
		tutstats = input("Have you ever wondered how much health you have left? You can easily view your stats using the \"stats\" command.\n>").lower()
		if tutstats == "stats":
			show_player_stats()
			break
		else:
			print("That's not how you use stats. Try again (Type \"stats\").")
	input("Good! You've learned the basics of Mildwind. If you need any help in-game, just type \"help\" at any time. To continue with the main story, press enter.")
	part1()
	
#part1
def en_part1():
	guard = Enemy("Guard", 100, (5, 45))
	guard.rewards = [(Potion.medium, 1), (Potion.small, 1), (Item.torch, 1)]
	guard.deadmsg = "You look at the dead guard."
	guard.killedmsg = "The guard is dead, and you have a health of {0}. You also picked up 2 potions, a small one and a medium one. You continue to escape the dungeon. The halls are dark, so you grab a torch on your way out. As you escape, you are met by a man who stouts \"Follow me %s!\". You followed him." % (game.player.name)
	guard.damagemsg = "You attacked the guard. The guard has a health of {0}, and you have a health of {1}."
	guard.deathmsg = "You were beaten to death."
	guard.ending = "Failed Escape"
	game.set_current_enemy(guard)

def ext_part1():
	if game.player.command in ["look at window", "look out window", "window"]:
		talking("You sigh and gaze out the window.", .04)
	elif game.player.command in ["look at guard", "analyse guard", "guard"]:
		if game.player.stolen:
			talking("You snicker a little as you notice the guard's empty pocket.", .02)
		else:
			talking("You notice the guard has something in his pocket. As he walks, it seems to be within your reach.", .02)
	elif game.player.command in ["bash head into wall", "bang head into wall", "bang head against wall", "bash head against wall"]:
		damage = 5
		damagemsg = "You bashed your head into the wall out of misery. It hurts a little. You lost %s health."
		deathmsg = "You bashed your head to death out of misery."
		ending = "Hopeless and Stupid"
		game.player.headbanger = True
		game.player.hurt(damage, False, damagemsg % (damage), deathmsg, ending)
	elif game.player.command in ["attack", "fight", "a"]:
		talking("You can't attack behind bars.", .02)
	elif game.player.command == "talk to prisoner":
		if game.player.hasitems:
			talking("I have nothing else to say...", .04)
		else:
			game.player.hasitems = True
			game.player.give_item(Potion.small, 2)
			game.player.maxhealth += 5
			talking("\"Greetings %s, today is my last day alive... I must face my death sentence... Take these. They won't be of use to me in my afterlife.\"" % (game.player.name), .05)
			if game.player.stolen:
				talking("\"Heh, I saw what you did back there.\"")
				game.player.maxhealth = game.player.maxhealth + 5
			if game.player.headbanger:
				talking("\"I see that your head is bleeding...take this bandage.\" Your health is now restored to max.")
				game.player.fullheal()
			talking("You were given 2 small potions and a mysterious one. The prisoner recommended that you drink the mysterious one, so you did. Your max health increased a little.", .04)
	elif game.player.command == "wait":
		if game.player.stolen:
			talking("You wait. Nothing happened.", .02)
		else:
			talking("You hear a noise coming from the window, when suddenly, the wall breaks down. A man with a wooden metal-plated battering ram bashes the wall down. \"%s, We need your help, only you are capable of killing the dragon. No time to explain right now. Take these items.\"\nYou have been given a steel sword, cheap armor, and a scroll." % (game.player.name), .04)
			game.player.give_item(Item.scroll)
			game.player.give_item(Weapon.steel_sword)
			game.player.give_item(Armor.leather_armor)
			print("Weapon damage increased to 4, armor increased to 1.5, and a hint added.")
			part2()
	elif game.player.command in ["pickpocket guard", "steal", "pickpocket", "steal from guard", "pick guards pocket", "pick pocket", "take from guard", "reach into guards pocket"]:
		if game.player.stolen:
			damage = 20
			damagemsg = "The guard shouts \"Hey, I saw that!\" and shanks you for stealing. You lost %s health."
			game.player.hurt(damage, True, damagemsg % (damage), "You were shanked to death.\n", "Greedy")
			if game.player.hints > 0:
				game.player.hints = game.player.hints - 1
		else:	
			talking("As the guard passes by, you reach in his pocket and grabbed some items. You found a dagger, scroll, and key.")
			game.player.give_item(Item.scroll)
			game.player.give_item(Weapon.dagger)
			game.player.give_item(Item.prison_key)
			game.player.stolen = True
	elif game.player.command in ["open door", "unlock door"]:
		if game.player.has_item(Item.prison_key):
			game.player.take_item(Item.prison_key)
			part1_1()
		else:
			talking("You don't have a key.")
	else:
		show_entry_message()

def part1():
	game.player.savepos = part1
	save()
	game.player.cmdext = ext_part1
	game.player.randhint = ["Maybe the guard has something of use?", "Wait for something to happen?", "Maybe the prisoner has something to say?", "The door can be unlocked.", "I guess all you can do is bash your head against the wall."]
	talking("\nYou awaken in a dungeon. Behind you is a tiny barred window, and in front of you is a locked, barred door. There is a prisoner in the cell across from you and a guard that marches back and forth in the halls.")
	game.player.ruffindead = False
	commands()

#part1_1
def ext_part1_1():
	if game.player.command == "run":
		talking("As you run, a man comes from behind and kills the guard. The man says \"Follow me, %s!\", and you run to the exit." % (game.player.name))
		part2()
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
		if game.current_enemy.dead:
			part2()
	elif game.player.command in ["walk", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.current_enemy.dead:
			part2()
		else:
			print("You cannot leave until the guard is dead.")
	else:
		show_entry_message()

def part1_1():
	game.player.savepos = part1_1
	save()
	log_stats("1-1")
	game.player.randhint = ["RUN MAN."]
	game.player.cmdext = ext_part1_1
	en_part1()
	talking("You open the door. The guard sees you and begins to run towards you. What do you do?")
	commands()
	
#part2
def en_part2():
	game.set_current_enemy(no_enemy)

def ext_part2():
	if game.player.command in ["yes", "walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		talking("You follow Ruffin to the Dungeon that the dragon resides in.")
		part3()
	elif game.player.command in ["run free", "no"]:
		print("You are a free man now.")
		print("\"Careless\" ending")
		show_player_stats()
		win()
		sys.exit()
	else:
		show_entry_message()

def part2():
	game.player.savepos = part2
	save()
	log_stats("1")
	game.player.randhint = ["This is your chance you run free and be your own man.", "You could follow Ruffin on his quest."]
	game.player.cmdext = ext_part2
	game.player.extattack = 15
	game.player.hasitems = False
	game.player.stolen = False
	talking("\nYou just escaped the dungeon, you meet the man who helped you escape. \"%s, you are the world's only hope of defeating the dragon Dracord. Dracord has risen from the dead thanks to a curse casted upon the world. My name is Ruffin and the prophecy says that you can save humanity, that is why I saved you. Will you please follow me and help me defeat the dragon?\"" % (game.player.name))
	if game.player.headbanger:
		talking("\"Also, what is up with your face? You look like you bashed your head into a wall.\"")
	if game.player.name == "Keyboard-Junkie":
		talking("\"While I was coming for you, I found this.\" Ruffin handed you a black cube with \"KJ\" engraved into it. You feel a breeze through your body. You max health, stamina, and strength increased.")
		game.player.maxhealth += 50
		game.player.fullheal()
		game.player.maxstamina += 5
		game.player.extattack += 25
	commands()
	
#part3
def en_part3():
	wolves = Enemy("Pack of wolves", 200, (1, 5))
	wolves.rewards = [(Potion.small, 2)]

	wolves.deadmsg = "You and Ruffin look at the dead wolf pack."
	wolves.killedmsg = "You and Ruffin attacked the wolves. They are now dead, and you have a health of {0}. You also picked up 2 small potions."
	wolves.damagemsg = "You and Ruffin attacked the wolves. The wolves have a health of {0}, and you have a health of {1}."
	wolves.deathmsg = "You were bitten to death."

	wolves.rundamagemsg = "The wolves bit you in the back. Your health is now {1}. You can't leave until they are dead."
	wolves.runmsg = "You and Ruffin escaped from the pack of wolves safely."
	wolves.runfailedmsg = "\"{0}, stop being a wuss and fight these puppies like a warrior!\" Ruffin yelled."

	wolves.ending = "THIS BITES!"
	wolves.runending = "Manbaby"

	game.set_current_enemy(wolves)

def ext_part3():
	if game.player.command in ["torch", "use torch", "wave torch", "scare"]:
		if game.player.has_item(Item.torch):
			talking("You wave your torch at the wolves to scare them off. You continue your journey.")
			part4()
		else:
			talking("You don't have a torch.")
	elif game.player.command in ["shake", "shake wolf off", "shake off wolf", "shake off"]:
		if game.player.haswolf:
			game.player.haswolf = False
			print("You shook the wolf off your arm.")
		else:
			show_entry_message()
	elif game.player.command in ["attack", "fight", "a"]:
		if game.current_enemy.dead:
			talking("You and Ruffin look at the dead wolf pack.")
		else:
			if game.player.haswolf:
				damagemsg = "The wolf is still stuck to your arm, you cannot attack. You lost some health in the process. Your health is now %s. Shake him off."
				game.player.hurt(25, False, damagemsg % (game.player.gethealth()), "You bled to death.")
			else:
				game.player.attack_enemy(game.current_enemy)
				if not game.current_enemy.dead and game.random_chance(16):
					game.player.hurt(15, False, "A wolf just locked its jaw onto your arm! You must shake it off to continue fighting. You lost 15 more health.")
					game.player.haswolf = True
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 4, 10, 15, 20]):
			part4()
	else:
		show_entry_message()
		
def part3():
	game.player.savepos = part3
	save()
	en_part3()
	log_stats("2")
	game.player.randhint = ["Try to fight your way out.", "Once you've killed em off, maybe you can press forward.", "Wolves hate fire."]
	game.player.cmdext = ext_part3
	talking("\nYou have chosen to follow Ruffin. On your way to the cave that Dracord resides in, you are stopped by a pack of wolves. \"Wolves! If I remember correctly, wolves are afraid of fire!\" Ruffin noted.")
	game.player.haswolf = False
	commands()
		
#part4
def en_part4():
	game.set_current_enemy(no_enemy)

def ext_part4():
	if game.player.command == "ponies!!!":
		game.player.extattack += 15
		talking("You found a purple princess pony. She will now follow you and add 15 damage to your attacks.")
	elif game.player.command in ["skeleton", "examine skeleton", "examine", "check", "check skeleton", "loot", "loot skeleton", "look at skeleton", "scavenge", "scavenge skeleton"]:
		if game.player.hasitems:
			talking("You mourn over the death of the knight.")
		else:
			game.player.maxstamina = 0
			game.player.maxstamina = game.player.maxstamina + 3
			game.player.stamina = game.player.maxstamina
			game.player.hasitems = True
			game.player.give_item(Shield.wooden_shield)
			game.player.give_item(Armor.rusty_armor)
			talking("The skeleton has rusty old armor and wooden shield. Your armor is now increased to 1.4. You can now use \"shield\" to defend yourself from enemies and give a small amount of damage.")
	elif game.player.command == "shield":
		if game.player.shield == Shield.none:
			talking("You don't have a shield.")
		else:
			talking("\"Don't swing that like a madman!\" Ruffin complained.")
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		talking("You and Ruffin continue into the dark cave.")
		part5()
	else:
		show_entry_message()

def part4():
	game.player.savepos = part4
	save()
	log_stats("3")
	game.player.randhint = ["\"I wonder what the skeleton left behind.\" Ruffin thought.", "You can move along if you wish."]
	game.player.cmdext = ext_part4
	talking("\nYou make it to the entrance of the cave. You and Ruffin walk inside. There is a skeleton to the right and the darkness of the cave ahead.")
	game.player.hasshield = False
	commands()
	
#part5
def en_part5():
	game.set_current_enemy(no_enemy)

def ext_part5():
	if game.player.command in ["dodge", "duck"]:
		talking("You dodged the incoming arrows as you ran to the end of the trap, but Ruffin...Ruffin was hit by an arrow in the stomach... He limped towards you, then leaned against the wall. You walk up to Ruffin. \"%s, I won't make it...you'll have to defeat Dracord without me... Here, take this...it will greatly assist you in your journey.\" He weakly handed you his broadsword...immediately after, his body collapsed.\nYou get up from your knees. You slowly progress further into the cave." % (game.player.name), 0.1)
		talking("Before you left Ruffin's lifeless body, you grabbed 2 medium potions from him. You also found a mysterious potion and drank it. Your max health increased.")
		game.player.ruffindead = True
		game.player.extattack -= 15
		game.player.give_item(Potion.medium, 2)
		game.player.give_item(Weapon.broadsword)
		game.player.maxhealth += 10
		part6()
	elif game.player.command in ["shield", "use shield"]:
		if game.player.shield == Shield.none:
			print("You don't have a shield.")
		else:
			talking("You and Ruffin walk right through the arrows without getting hit and make it to the end. \"%s, thank you for helping me get through with the shield. Here, I want to give you these.\"" % (game.player.name))
			talking("Ruffin handed you a machete that he says was passed down to him through family generations. He also handed you 2 medium potions and anther mysterious potion. You drink the mysterious potion. Your max health increased a little.")
			talking("You and Ruffin continue on after a short break of relief.")
			game.player.give_item(Potion.medium, 2)
			game.player.give_item(Weapon.machete)
			game.player.maxhealth += 5
			part6()
	else:
		print("You were killed by the arrows (wrong command).")
		show_player_stats()
		lose()
		sys.exit()
	
def part5():
	game.player.savepos = part5
	save()
	log_stats("4")
	game.player.randhint = ["Ruffin CAN'T die."]
	game.player.cmdext = ext_part5
	talking("\n\"%s, watch out!\" Ruffin tried to warn you about the pressure plate, but it was too late. Arrows are headed in your direction. What do you do?" % (game.player.name))
	commands()

#part6
def en_part6():
	warrior = Enemy("Undead Warrior", 200, (15, 45), 1.6)
	warrior.rewards = [(Potion.small, 2), (Item.scroll, 1)]
	warrior.deadmsg = "You gaze at the once-again dead soldier."
	warrior.killedmsg = "You attacked the undead soldier. He is now in his previous state, and you have a health of {0}. You also picked up 2 small potions and a scroll."
	warrior.damagemsg = "You attacked the undead soldier. The soldier has a health of {0}, and you have a health of {1}."
	warrior.deathmsg = "You were killed."

	warrior.shieldkilledmsg = "You safely deflected the soldier's attacks and killed him. Your health is now {0} and you obtained 2 small potions and a scroll."
	warrior.shieldmsg = "You deflected the undead soldier's attack and he hurt himself in the process. You used some of your stamina in the process. His health is {0} and yours is {1}."

	warrior.rundamagemsg = "The soldier backstabbed you. Your health is now {1}. You can't leave until he's dead."

	game.set_current_enemy(warrior)

def ext_part6():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 15, 20, 45, 50, 60]):
			part7()
	else:
		show_entry_message()
		
def part6():
	game.player.savepos = part6
	save()
	en_part6()
	log_stats("5")
	game.player.randhint = ["Try to fight your way out.", "Once you've killed it off, maybe you can press forward.", "Do you have a shield?"]
	game.player.cmdext = ext_part6
	talking("\nYou walked past a series of already-looted skeletons of soldiers just like you. You feel a breeze pass you, when suddenly one of the soldiers seemingly awakens from the dead and begins to run towards you alarmingly fast.")
	commands()

#part7
def en_part7():
	spectre = Enemy("Spectre", 666, ("YOU", "ARE"), "DEAD")
	spectre.deathmsg = "DIE!!!"
	spectre.ending = "..."

	game.set_current_enemy(spectre)

def ext_part7():
	if game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		talking("You finish relaxing and continue deeper into the cave.")
		part8()
	elif game.player.command == "place torch":
		if game.player.has_item(Item.torch):
			talking("You placed the torch onto the holder. It opened a secret path. You walk through it.")
			talking("You skipped two fights.")
			game.player.healthbank = game.player.maxhealth
			part10()
		else:
			talking("You do not have a torch.")
	elif game.player.command in ["chest", "open chest"]:
		if game.player.hasitems:
			talking("You look at the empty chest.")
		else:
			talking("You open the chest. Inside, you find a large stamina potion. You drink it. Your max stamina increased.")
			game.player.maxstamina += 2
			game.player.stamina = game.player.maxstamina
			game.player.hasitems = True
	elif game.player.command == "wait":
		game.player.sethealth(-666, "You decided to sit for a bit.\n \n \n \nDIE!!!", "...", "...")
	else:
		show_entry_message()
	
def part7():
	game.player.savepos = part7
	save()
	en_part7()
	log_stats("6")
	game.player.randhint = ["Do you have a torch to place on the holder?", "Take a look inside the chest.", "DON'T SLEEP."]
	game.player.hasitems = False
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_part7
	print("\nYou stop to take a break. You see a chest on the ground against the wall and a holder for a torch.")
	commands()

#part8
def en_part8():
	doppelganger = Enemy(game.player.name, 50, (25, 26), 5)
	doppelganger.rewards = [(Potion.medium, 2), (Item.scroll, 1)]

	doppelganger.deadmsg = "You stare at a dead, faceless version of yourself."
	doppelganger.killedmsg = "You attacked the doppelganger. He is now dead, and you have a health of {0}. You also picked up 2 medium potions and a scroll."
	doppelganger.damagemsg = "You attacked the doppelganger. He has a health of {0}, and you have a health of {1}."
	doppelganger.deathmsg = "You were killed."

	doppelganger.shieldkilledmsg = "You safely deflected the doppelganger's attacks and killed him. Your health is now {0} and you obtained 2 medium potions and a scroll."
	doppelganger.shieldmsg = "You deflected the doppelganger's attack and he hurt himself in the process. You used some of your stamina. His health is {0} and yours is {1}."
	doppelganger.learnedmsg	= "The doppelganger learned your moves and attacked you. Your health is now {0}."
	doppelganger.reachmsg = "The doppelganger was able to reach over your shield and stab you a bit. Your health is now {0}."

	doppelganger.rundamagemsg = "The doppelganger backstabbed you. Your health is now {1}. You can't leave until it's dead."
	doppelganger.rundeathmsg = "You killed yourself."
	doppelganger.runmsg = "You escaped yourself."

	game.set_current_enemy(doppelganger)
	
def ext_part8():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy, False)
		if game.current_enemy.dead:
			game.player.armor = game.player.armorbank
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 15, 20, 45, 50, 60]):
			part9()
	else:
		show_entry_message()

def part8():
	game.player.savepos = part8
	save()
	en_part8()
	log_stats("7")
	game.player.randhint = ["ATTACK!"]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_part8
	game.player.armorbank = game.player.armor
	game.player.armor = Armor.prison_clothes
	talking("\nYou hear crying down the hall. When you turn down the corner, you spot a crying child. When you walk up to him and touch his shoulder, suddenly he grows to your size. When he turns around, he's faceless.\n\"I WANT YOUR FACE!\"\nA curse was casted on you. You cannot use your armor.\nYou jump back. What now?")
	game.player.shielduse = 1
	commands()
	

#part9
def en_part9():
	spider = Enemy("Fanged Giant Spider", 500, (10, 30))
	spider.rewards = [(Potion.super, 1)]

	spider.deadmsg = "You stare at the dead spider and watch it twitch."
	spider.killedmsg = "You attacked the spider. She has been squashed, and you have a health of {0}. You also picked up a super potion."
	spider.damagemsg = "You attacked the spider, but she poisoned you a bit. She has a health of {0}, and you have a health of {1}."
	spider.deathmsg = "You were killed."

	spider.shieldkilledmsg = "You safely deflected the spider's attacks and killed her. Your health is now {0} and you obtained a super potion."
	spider.shieldmsg = "You deflected the spider's attack and she hurt herself in the process. You used some of your stamina in the process. Her health is {0} and yours is {1}."

	spider.rundamagemsg = "The spider clawed you. Your health is now {1}. You can't leave until she's dead."

	game.set_current_enemy(spider)
	
def ext_part9():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
		if game.current_enemy.dead:
			game.player.armor = game.player.armorbank
		else:
			game.player.maxhealth -= 5
			print("Your max health is now %s." % (game.player.maxhealth))
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 15, 20, 45, 50, 60]):
			part10()
	else:
		show_entry_message()

def part9():
	game.player.savepos = part9
	save()
	en_part9()
	log_stats("8")
	game.player.randhint = ["Squash that spider like a bug! (attack)"]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.healthbank = game.player.maxhealth
	game.player.cmdext = ext_part9
	talking("\nYou continue down the path in fear and confusion. You hear a hissing sound. Suddenly a spider falls in front of you and spits her fangs in your face.")
	commands()

#part10
def en_part10():
	game.set_current_enemy(no_enemy)
	
def ext_part10():
	if game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		talking("You bravely walk into Dracord's lair.")
		part11()
	elif game.player.command in ["vase", "look in vase", "look in the vase", "loot", "loot vase"]:
		if game.player.hasitems:
			talking("You look at the empty vase.")
		else:
			talking("You look inside the vase. You found a few small potions.")
			game.player.give_item(Potion.small, 2)
			game.player.hasitems = True
	else:
		show_entry_message()
	
def part10():
	game.player.savepos = part10
	save()
	en_part10()
	log_stats("9")
	game.player.randhint = ["What's in the vase?"]
	game.player.maxhealth = game.player.healthbank
	game.player.hasitems = False
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_part10
	talking("\nYou stop to rest. After a while, you feel reinvigorated. You hear snoring in the distance, it must be Dracord sleeping. As you stand up, you see a large vase.")
	commands()

#part11	
def en_part11():
	dracord = Enemy("Dracord", 5000, (35, 45), 10)
	game.set_current_enemy(dracord)

def ext_part11():
	dracord_hint = "HINT: It looks like this battle can't be fought alone..."
	if game.player.command == "shield":
		if game.player.ruffindead:
			game.player.sethealth(0, "You begin to hold up your shield. As soon as you raise it, Dracord whips it out of your hands with his tail and claws you to death.")
			talking(dracord_hint)
		else:
			talking("\"Stay here, I'll try to attack him, you stay here and wait for my cue.\" Ruffin runs straight into Dracord without fear. He runs behind Dracord and attempts to climb up his tail. Dracord feels him climbing up him like a flea and smacks his tail into the ground to shake Ruffin off. Ruffin hits the ground hard.")
			talking("")
			talking("You run towards Ruffin and drag him into a crack in the walls. \"%s, Dracord can't be defeated with his current power compared to yours... Take this, it will lead you to a village; Redwind... Bruce will help you... I'm not going to make it... Here's my dagger...put me to rest...\"" % (game.player.name))
			talking("Ruffin handed you his letter regarding Redwind, and his dagger. You take Ruffin's dagger and go for the heart. \"AHH!\" *silence*")
			talking("You get up and leave the cracks to finish what you and Ruffin started. You raise your weapon and run towards the violent dragon. Before you can attack, he flies up and breaks through the ceiling. Rubble begins to fall and causes the ground to collapse. You fall through and everything goes black...")
			game.player.ruffindead = True
			input("Wake up (Press enter).")
			part12()
	elif game.player.command in ["attack", "fight", "a"]:
		if game.player.ruffindead:
			game.player.sethealth(0, "With no other option, you begin to charge towards Dracord without regret. Dracord slams you into the rocky walls and kills you.")
			talking(dracord_hint)
		else:
			talking("\"Stay here, I'll try to attack him, you stay here and wait for my cue.\" Ruffin runs straight into Dracord without fear. He runs behind Dracord and attempts to climp up his tail. Dracord felt him climbing up him like a flea and smacked his tail into the ground to shake Ruffin off. Ruffin hit the ground hard.")
			talking("")
			talking("You run towards Ruffin and drag him into a crack in the walls. \"%s, Dracord can't be defeated with his current power compared to yours... Take this, it will lead you to a village; Redwind... Bruce will help you... I'm not going to make it... Here's my dagger...put me to rest...\"" % (game.player.name))
			talking("Ruffin handed you his letter regarding Redwind, and his dagger. You take Ruffin's dagger and go for the heart. \"AHH!\" *silence*")
			talking("You get up and leave the cracks to finish what you and Ruffin started. You raise your weapon and run towards the violent dragon. Before you could attack, he flew up and broke through the ceiling. Rubble began to fall and caused the ground to collapse. You fall through and everything goes black...")
			game.player.ruffindead = True
			input("Wake up (Press enter).")
			part12()
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		game.player.sethealth(0, "You attempt to run away from Dracord. He blows fire at you and you burn to death.")
	else:
		show_entry_message()

def part11():
	game.player.savepos = part11
	save()
	en_part11()
	log_stats("10")
	game.player.randhint = ["You're screwed kid."]
	game.player.hasitems = False
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_part11
	talking("\nYou walk down the hallway towards the snoring. It gets louder as you approach it. You stop in front of a pair of stone doors and pull the chain to open it. The loud noise created from the grinding awakens Dracord. The 50-foot-tall beast spots you and begins to ready for attack.")
	commands()
	
#part12
def en_part12():
	game.set_current_enemy(no_enemy)
	
def ext_part12():
	if game.player.command in ["open door", "pick lock", "pick"]:
		talking("To pick a lock, you must guess the right number.")
		combo = random.triangular(000, 999)
		number = "%03d" % int(combo)
		while True:
			answer = input("What's the number?\n>")
			if answer == number:
				talking("Door unlocked.")
				part13()
			elif len(answer) != 3:
				print("Number must be 3 digits (000 - 999).")
			elif answer > number:
				talking("Lower...", 0.02)
			elif answer < number:
				talking("Higher...", 0.02)
			elif answer == "exit":
				return
			else:
				talking("NOT A NUMBER.")
	else:
		show_entry_message()

def part12():
	game.player.savepos = part12
	save()
	en_part12()
	log_stats("11")
	game.player.randhint = ["Pick the door with your lockpick."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_part12
	talking("\nYou awaken in a room with a large hole in the ceiling above you. You are surrounded by rubble, but there's a locked door in front of you.\n*TING*\nA lock pick fell from the ceiling.")
	commands()

#part13
def en_part13():
	game.set_current_enemy(no_enemy)

def ext_part13():
	if game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow stream", "follow", "yes"]:
		part14()
	else:
		show_entry_message()

def part13():
	game.player.savepos = part13
	save()
	en_part13()
	log_stats("12")
	game.player.randhint = ["Follow the stream."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_part13
	talking("\nYou walk out the door into a cave that exits to a stream. Should you follow it?")
	commands()

#part14
def en_part14():
	game.set_current_enemy(no_enemy)

def ext_part14():
	show_entry_message()

def part14():
	game.player.savepos = part14
	save()
	en_part14()
	log_stats("13")
	game.player.cmdext = ext_part14
	talking("\nAfter a while of following the stream, you pass some bushes. You hear rustling from them when suddenly a pack of wolves jump out.")
	time.sleep(10)
	talking("\nYou begin to run. As you are running, you start to see a small village in the distance, but you also hear growling and barking from behind.")
	time.sleep(10)
	talking("\nYou hear a yelp from behind you but don't want to look back. You still hear angry wolves chasing you.")
	time.sleep(10)
	talking("\nYou hear another cry from a wolf. It gets a bit quiet, but you still hear a wolf chasing you.")
	time.sleep(10)
	talking("\nYou hear one last thud of a wolf hitting the ground. It begins to feel calm. You slow down and look behind you. The wolves have been shot by arrows.")
	time.sleep(10)
	talking("\nYou walk toward the village and meet a man holding a bow.")
	talking("\n\"You alright? You were nearly mauled by those wolves back there. Good thing I was about to go hunting. Stay for a while as you take a break. If you need info, come to my house. By the way, I'm Bruce.\"")
	talking("You are now in Redwind Village")
	redwind()
	
#redwind
def en_redwind():
	game.set_current_enemy(no_enemy)
	
def ext_redwind():
	def area_check(area, area_func):
		if area:
			area_func()
		else:
			show_entry_message()
	if game.player.command == "bruce":
		bruce()
	elif game.player.command == "dracord":
		area_check(game.player.areas.dracordlair, dracord)
	elif game.player.command == "forest":
		area_check(game.player.areas.forest, forest)
	elif game.player.command == "swamp":
		area_check(game.player.areas.swamp, swamp)
	elif game.player.command == "mountains":
		area_check(game.player.areas.mountains, mountains)
	elif game.player.command == "north mine":
		area_check(game.player.areas.northmine, northmine)
	elif game.player.command == "south mine":
		area_check(game.player.areas.southmine, southmine)
	elif game.player.command == "river":
		area_check(game.player.areas.river, river)
	elif game.player.command == "library":
		area_check(game.player.areas.library, library)
	else:
		show_entry_message()

def redwind():
	def available_areas(area, areaname):
		if area:
			print(areaname)
		else:
			pass
	game.player.savepos = redwind
	save()
	en_redwind()
	log_stats("14")
	game.player.randhint = ["Be sure to talk to Bruce if you need something."]
	game.player.cmdext = ext_redwind
	print("===Redwind Village===")
	print("-Bruce's House (Bruce)")
	available_areas(game.player.areas.dracordlair, "-Dracord's Lair (Dracord)")
	available_areas(game.player.areas.forest, "-Forest")
	available_areas(game.player.areas.swamp, "-Swamp")
	available_areas(game.player.areas.mountains, "-Mountains")
	available_areas(game.player.areas.northmine, "-North Mine")
	available_areas(game.player.areas.southmine, "-South Mine")
	available_areas(game.player.areas.river, "-River")
	available_areas(game.player.areas.library, "-Library")
	commands()
	#list of places to go to. I plan to have areas that unlock as you progress.

#bruce	
def en_bruce():
	game.set_current_enemy(no_enemy)
	
def ext_bruce():
	if game.player.command in ["back", "return", "redwind"]:
		redwind()
	else:
		show_entry_message()
	
def bruce():
	game.player.savepos = bruce
	save()
	en_bruce()
	log_stats("redwind")
	game.player.randhint = ["What do you want? Talk to Bruce..."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_bruce
	#print("(To leave, type "return")")
	if game.player.areas.dracordlair == False:
		talking("\"So, you want to fight a dragon? Who sent you?\"")
		time.sleep(2)
		talking("\"Ruffin? I know him! You must be the chosen one! Where is he anyway?\"")
		time.sleep(5)
		talking("...", 0.6)
		time.sleep(3)
		talking("\"Oh... How sad... He was a great friend and ally...\"")
		time.sleep(4)
		talking("\"Well... He probably wants you to have this... It's directions to Dracord's lair.\"")
		time.sleep(5)
		talking("\"Oh, I forgot to mention, if you need any help, check the library.\"")
		time.sleep(3)
		talking("Here, take these small potions for your journey.")
		game.player.give_item(Potion.small, 5)
		time.sleep(2)
		talking("\"Farewell and good luck %s.\"" % (game.player.name))
		time.sleep(4)
		game.player.areas.dracordlair = True
		game.player.areas.library = True
		redwind()
	elif game.player.areas.forest == False and game.player.dracordTry:
		talking("\"Hm... You tried to beat Dracord and failed? How are you alive?\"")
		time.sleep(3)
		talking("\"Ruffin's ghost? Wow.\"", 0.04)
		time.sleep(3)
		talking("\"Listen, I know an enchantress who can make potions. Bring her herbs, and she'll help you out. Follow the river, and you'll find her hut. You can find herbs in the forest over to the west.\"")
		time.sleep(4)
		talking("\"There's also a mine close by. Go there to gather the materials for a sword, and I'll forge them for you. Just head north.\"")
		game.player.areas.forest = True
		game.player.areas.river = True
		game.player.areas.northmine = True
		redwind()
	elif game.player.metals and game.player.forged == False:
		talking("\"Great! You found all the iron we need!\"")
		game.player.take_item(Item.iron, 5)
		time.sleep(2)
		talking("A few hours later...")
		time.sleep(3)
		talking("\"Here you go! It's ready for battle.\"")
		print("You were given the Hero Sword.")
		game.player.give_item(Weapon.hero_sword)
		game.player.forged = True
		redwind()
	elif game.player.smetals and game.player.forged and game.player.sforged == False:
		talking("What's this?")
		time.sleep(2)
		talking("Ah. Drazmite! This mineral will greatly improve your sword. Let me forge this into it for you.")
		game.player.take_item(Item.drazmite, 3)
		time.sleep(5)
		talking("Here you go! Better than ever.")
		game.player.give_item(Weapon.dragon_slayer)
		game.player.sforged = True
		if game.player.shell:
			talking("Ah, you also brought back some scorpion shell! Let me make that into armor for you.")
			time.sleep(5)
			print("You now have Scorpio Armor!")
			game.player.sarmor = True
			game.player.give_item(Armor.scorpio_armor)
		redwind()
	else:
		print("Bruce doesn't have anything to tell you.")
		redwind()

#dracord		
def en_dracord():
	game.set_current_enemy(no_enemy)
	
def ext_dracord():
	if game.player.command in ["back", "return", "redwind"]:
		redwind()
	else:
		show_entry_message()
	
def dracord():
	game.player.savepos = dracord
	save()
	en_dracord()
	log_stats("redwind")
	game.player.randhint = ["Did you check the library?"]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_dracord
	time.sleep(2)
	talking("You begin walking to Dracord's lair.")
	time.sleep(4)
	print("(To leave, type \"return\")")
	if game.player.dracordUnlock:
		while True:
			choice = input("Are you ready to fight Dracord (y/n)?\n>").lower()
			if choice == "y":
				final_battle()
			elif choice == "n":
				redwind()
			else:
				print("Not \"y\" or \"n\"")
	elif game.player.dracordUnlock == False:
		talking("There is a large door with hieroglyphs on it.")
		time.sleep(4)
		if game.player.hasstone:
			talking("You place the Dragon Stone on the pedestal. The door starts to slowly open. As you watch the beastly Dracord sleep, you feel a negative energy.")
			game.player.dracordUnlock = True
			time.sleep(5)
			dracord()
		elif game.player.transbook:
			talking("According to the translations in the book, the hieroglyphs on the door say\n\"If entry is what you seek, you must place the Dragon Stone on the Pedestal of Darkness. The Dragon Stone is stowed away and guarded at the highest point in Redwind.\"")
			if game.player.areas.mountains:
				pass
			else:
				print("\nYou can now go to the Mountains.")
				game.player.areas.mountains = True
			time.sleep(20)
			talking("You decide to return back to the village.")
			time.sleep(4)
			redwind()
		else:
			talking("You don't understand any of the hieroglyph on the door. You return to the village.")
			time.sleep(4)
			redwind()
	else:
		talking("You're not ready to fight Dracord.")
		redwind()

#swamp
def en_swamp():
	turtle = Enemy("Giant Turtle", 50, (5, 30), 5)
	turtle.rewards = [(Potion.medium, 1)]

	turtle.deadmsg = "I like turtles."
	turtle.killedmsg = "You attacked the giant turtle. It was hard. You have a health of {0}. You also picked up a medium potion."
	turtle.damagemsg = "You attacked the giant turtle, but he clawed you back. He has a health of {0}, and you have a health of {1}."
	turtle.deathmsg = "You were mauled to death."

	turtle.shieldkilledmsg = "You safely deflected the turtle's attacks and killed him. Your health is now {0} and you obtained a medium potion."
	turtle.shieldmsg = "You deflected the giant turtle's attack and he hurt himself in the process. You used some of your stamina in the process. His health is {0} and yours is {1}."

	turtle.rundamagemsg = "The giant turtle clawed you. Your health is now {1}. You can't leave until he's dead."

	game.set_current_enemy(turtle)
	
def ext_swamp():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 75]):
			swamp_1()
	else:
		show_entry_message()
	
def swamp():
	en_swamp()
	log_stats("redwind")
	game.player.randhint = ["You like turtles, don't you?"]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_swamp
	if game.player.sshield:
		talking("As you walk towards the swamp, you hear someone yell \"STAY OUT OF MY SWAMP\" in the distance. You turn around and return to the village.")
		time.sleep(3)
		redwind()
	else:
		talking("You begin to follow the map to see where it takes you.")
		time.sleep(4)
		talking("On your way down the path, there is giant turtle in the way. You try to move him.")
		time.sleep(3)
		talking("It got angry and turned to you and begins to fight.")
		commands()

#swamp_1
def en_swamp_1():
	trolls = Enemy("Tribe of Trolls", 500, (1, 75), 1)
	trolls.rewards = [(Potion.small, 4)]

	trolls.deadmsg = "You look at the dead trolls."
	trolls.killedmsg = "You killed the trolls. You have a health of {0}. You also picked up 4 small potions."
	trolls.damagemsg = "You attacked the trolls, but they stabbed you back. they have a collective health of {0}, and you have a health of {1}."
	trolls.deathmsg = "You were stabbed to death."

	trolls.shieldkilledmsg = "You safely deflected the trolls' attacks and killed them. Your health is now {0} and you obtained small potions."
	trolls.shieldmsg = "You deflected the trolls' attacks and they hurt themselves in the process. You used some of your stamina in the process. Their collective health is {0} and yours is {1}."

	trolls.rundamagemsg = "The trolls stabbed you. Your health is now {1}. You can't leave until they're dead."

	game.set_current_enemy(trolls)
	
def ext_swamp_1():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 25, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 75, 75, 75, 75, 75, 85, 85, 85, 85, 85, 85, 85, 85, 85, 100]):
			swamp_2()
	else:
		show_entry_message()
	
def swamp_1():
	en_swamp_1()
	log_stats("swamp")
	game.player.randhint = ["Get rekt m8."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_swamp_1
	time.sleep(5)
	talking("You continue on your path to this mysterious destination.")
	time.sleep(3)
	talking("A tribe of angry trolls jump ouf of the bushes and from the trees. They don't like your presence. They begin to run towards you.")
	commands()


#swamp_2
def en_swamp_2():
	chief = Enemy("Troll Chief", 300, (45, 75), 1.5)
	chief.rewards = [(Potion.large, 2)]

	chief.deadmsg = "It's all ogre now."
	chief.killedmsg = "You killed the troll chief. You have a health of {0}. You also picked up a large potion or two (\"continue\")."
	chief.damagemsg = "You attacked the chief, but he hit you back. He has a health of {0}, and you have a health of {1}."
	chief.deathmsg = "You were beaten to death."

	chief.shieldkilledmsg = "You safely deflected the chief's attacks and killed him. Your health is now {0} and you obtained two large potions (\"continue\")."
	chief.shieldmsg = "You dodged the chief's club and he hurt himself in the process. You used some of your stamina in the process. His health is {0} and yours is {1}."

	chief.rundamagemsg = "The chief punched you. Your health is now {1}. You can't leave until he's dead."

	game.set_current_enemy(chief)
	
def ext_swamp_2():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 25, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 75, 75, 75, 75, 75, 75, 75, 75, 100]):
			mountains_2()
	else:
		show_entry_message()
	
def swamp_2():
	en_swamp_2()
	log_stats("swamp_1")
	game.player.randhint = ["Why do you need hints?"]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_swamp_2
	time.sleep(5)
	talking("Just ahead is a shrine with the sunrays peeking through the ceiling shining on a shield.")
	time.sleep(3)
	talking("You are stopped by the troll chief. \"YOU KILLED MY PEOPLE! NOW I WILL KILL YOU!\".")
	commands()

#swamp_3
def swamp_3():
	game.set_current_enemy(no_enemy)
		
def ext_swamp_3():
	show_entry_message()
		
def swamp_3():
	game.player.savepos = swamp_3
	save()
	en_swamp_3()
	log_stats("swamp_2")
	game.player.randhint = ["Hints are useless."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.hasitems = False
	game.player.cmdext = ext_swamp_3
	time.sleep(2)
	talking("You slowly walk towards the shield.")
	time.sleep(7)
	talking("Under the pedestal reads \"Shield of the Gods\". You pick it up and feel its power.")
	game.player.give_item(Shield.shield_of_the_gods)
	game.player.sshield = True
	talking("You return to the village.")
	time.sleep(6)
	redwind()
		
#mountains
def en_mountains():
	game.set_current_enemy(no_enemy)
		
def ext_mountains():
	if game.player.command in ["back", "return", "redwind"]:
		redwind()
	elif game.player.command in ["skeleton", "examine skeleton", "examine", "check", "check skeleton", "loot", "loot skeleton", "look at skeleton", "scavenge", "scavenge skeleton"]:
		if game.player.hasitems:
			talking("You hope to not be in the same position as this person.")
		else:	
			talking("You picked up some potions. One of which increased your health and made you stronger.")
			game.player.maxhealth += 20
			game.player.fullheal()
			game.player.maxstamina += 2
			game.player.extattack += 20
			game.player.hasitems = True
	elif game.player.command == "climb":
		talking("You continue up Mount Amberdrift.")
		mountains_1()
	else:
		show_entry_message()
		
def mountains():
	game.player.savepos = mountains
	save()
	en_mountains()
	log_stats("redwind")
	game.player.randhint = ["Hints tend to be useless."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_mountains
	if game.player.hasstone:
		talking("There is no need to go back to the mountains.")
		redwind()
	else:	
		talking("You begin to walk to Mount Amberdrift.")
		time.sleep(3)
		print("(To leave, type \"return\")")
		time.sleep(1)
		talking("You look up a the tall mountain. Everything begins to feel big around you. You start climbing.")
		time.sleep(20)
		talking("After some time, you made it to a spot to rest. You find the skeleton of a person that looks to be wearing similar gear to yours. He looks to have fallen from above (to continue, type \"climb\").")
		commands()

#mountains_1
def en_mountains_1():
	bear = Enemy("Guardian Bear", 150, (45, 65), 3)
	bear.rewards = [(Potion.large, 2)]

	bear.deadmsg = "You take the fur to use as a coat."
	bear.killedmsg = "You attacked the bear. It was unbearable. You have a health of {0}. You also picked up a large potion or two (\"continue\")."
	bear.damagemsg = "You attacked the bear, but he clawed you back. He has a health of {0}, and you have a health of {1}."
	bear.deathmsg = "You were mauled to death."

	bear.shieldkilledmsg = "You safely deflected the bear's attacks and killed him. Your health is now {0} and you obtained two large potions (\"continue\")."
	bear.shieldmsg = "You deflected the bear's attack and he hurt himself in the process. You used some of your stamina in the process. His health is {0} and yours is {1}."

	bear.rundamagemsg = "The bear clawed you. Your health is now {1}. You can't leave until he's dead."

	game.set_current_enemy(bear)
	
def ext_mountains_1():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [0, 25, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 75, 75, 75, 75, 75, 75, 75, 75, 100]):
			mountains_2()
	else:
		show_entry_message()
	
def mountains_1():
	game.player.savepos = mountains_1
	save()
	en_mountains_1()
	log_stats("mountains")
	game.player.randhint = ["Hints tend to be useless."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_mountains_1
	time.sleep(5)
	talking("You make it to the top of the mountain. The cave is just ahead. You begin to approach it.")
	time.sleep(3)
	talking("You got to the entrance of the cave. Suddenly an armored bear; the Guardian Bear, jumps in front of you.")
	commands()

#mountains_2
def en_mountains_2():
	game.set_current_enemy(no_enemy)
		
def ext_mountains_2():
	show_entry_message()
		
def mountains_2():
	game.player.savepos = mountains_2
	save()
	en_mountains_2()
	log_stats("mountains_1")
	game.player.randhint = ["Hints tend to be useless."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.hasitems = False
	game.player.cmdext = ext_mountains_2
	time.sleep(2)
	talking("You look up to see the Dragon Stone. You gaze upon it and embrace its beauty.")
	time.sleep(7)
	talking("After a few moments, you regain your focus and grab the Dragon Stone. You begin to walk back to Redwind.")
	game.player.give_item(Item.relic)
	game.player.hasstone = True
	time.sleep(6)
	redwind()
	
#library
def en_library():
	game.set_current_enemy(no_enemy)
		
def ext_library():
	if game.player.command in ["back", "return", "redwind"]:
		redwind()
	elif game.player.command == "ask for scrolls":
		if (not game.player.has_item(Item.scroll)):
			talking("\"Here are some scrolls I have lying around.\"")
			game.player.give_item(Item.scroll, 3)
		else:
			talking("\"You seem to have scrolls. Sorry, but I'm saving these for people who need them.\"")
	else:
		show_entry_message()
		
def library():
	game.player.savepos = library
	save()
	en_library()
	log_stats("redwind")
	game.player.randhint = ["Hints tend to be useless."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_library
	time.sleep(3)
	print("(To leave, type \"return\")")
	time.sleep(1)
	talking("\"Welcome to the Redwind Library. I'm Adam.\nIf you need any scrolls, I've got plenty, just ask.\"")
	if game.player.transbook == False:
		time.sleep(3)
		talking("\"I heard you need to go to Dracord's Lair. You might need this translation book for the Dragon Language. Here, take it.\"")
		game.player.transbook = True
		game.player.give_item(Item.trans_book)
	elif game.player.dracordTry and game.player.hasmap == False:
		talking("\"I saw you going to the mountain earlier. You seem like an adventurer. Here. Have this map I found.\"")
		game.player.hasmap = True
		game.player.give_item(Item.swamp_map)
		game.player.areas.swamp = True
	elif game.player.strangeperm == True and game.player.strangerecipe == False:
		talking("Hey! I found this recipe when I was cleaning out an old chest. You might need it.")
		print("You were given a recipe for strange potions.")
		game.player.strangerecipe = True
		game.player.give_item(Item.strange_recipe)
	else:
		pass
	commands()

#forest	
def forest():
	talking("You walk to the forest.")
	time.sleep(2)
	confirm = input("Would you like to search the forest for herbs (y/n)?\n>")
	if confirm == "y":
		talking("Hunting for herbs...")
		toolbar_width = 60
		sys.stdout.write("[%s]" % (" " * toolbar_width))
		sys.stdout.flush()
		sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

		for i in range(toolbar_width):
			time.sleep(game.player.farmwait)
			sys.stdout.write("*")
			sys.stdout.flush()
		talking("] DONE!")
		herbs = random.choice([8, 9, 10, 11, 12, 13, 14, 15, 16])
		print("You found ", herbs, " herbs.")
		game.player.give_item(Item.herb, herbs)
		time.sleep(3)
		redwind()
	else:
		redwind()

#northmine
def northmine():
	if not game.player.metals:
		talking("You walk to the mine.")
		time.sleep(2)
		confirm = input("Would you like to mine for iron (y/n)?\n>")
		if confirm == "y":
			talking("Mining...")
			toolbar_width = 60
			sys.stdout.write("[%s]" % (" " * toolbar_width))
			sys.stdout.flush()
			sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

			for i in range(toolbar_width):
				time.sleep(game.player.minewait)
				sys.stdout.write("*")
				sys.stdout.flush()
			talking("] DONE!")
			game.player.metals = True
			game.player.give_item(Item.iron, 5)
			time.sleep(3)
			redwind()
		else:
			redwind()
	else:
		talking("You already have materials from this mine.")
		redwind()

#southmine
def en_southmine():
	scorpion = Enemy("Scorpion", 750, (20, 40), 2)
	scorpion.rewards = [(Potion.super, 2)]

	scorpion.deadmsg = "You stare at the dead scorpion and watch it twitch."
	scorpion.killedmsg = "You attacked the scorpion. He has been killed, and you have a health of {0}. You also picked up a few super potions.\nYou notice that the scorpion shell looks kinda sturdy. The blood looks -strange-."
	scorpion.damagemsg = "You attacked the scorpion, but he poisoned you a bit. She has a health of {0}, and you have a health of {1}."
	scorpion.deathmsg = "You were killed."

	scorpion.shieldkilledmsg = "You safely deflected the scorpion's attacks and killed him. Your health is now {0} and you obtained 2 super potions.\nYou notice that the scorpion shell looks kinda sturdy. The blood looks -strange-."
	scorpion.shieldmsg = "You deflected the scorpion's attack and he hurt himself in the process. You used some of your stamina in the process. Her health is {0} and yours is {1}."

	scorpion.rundamagemsg = "The scorpion clawed you. Your health is now {1}. You can't leave until he's dead."

	game.set_current_enemy(scorpion)
	
def ext_southmine():
	if game.player.command == "shield":
		game.player.use_shield(game.current_enemy)
	elif game.player.command in ["attack", "fight", "a"]:
		game.player.attack_enemy(game.current_enemy)
		if game.current_enemy.dead:
			game.player.armor = game.player.armorbank
		else:
			game.player.maxhealth -= 2
			print("Your max health is now %s." % (game.player.maxhealth))
	elif game.player.command in ["walk", "run", "continue", "press forward", "move along", "follow ruffin", "follow"]:
		if game.player.run_from_enemy(game.current_enemy, [40]):
			southmine_1()
	elif game.player.command == "scorpion shell":
		if game.current_enemy.dead:
			print("You pick up the scorpion shell. Maybe Bruce can turn it into armor.")
			game.player.shell = True
			game.player.give_item(Item.scorpion_shell)
		else:
			show_entry_message()
	elif game.player.command in ["drink blood", "scorpion blood", "blood", "drink scorpion blood"]:
		if game.player.strangeblood:
			show_entry_message
		else:	
			if game.current_enemy.dead:
				print("You drink the strange blood. You feel stronger.")
				game.player.strangeblood = True
				game.player.maxhealth += 15
				game.player.maxstamina += 1
				game.player.fullheal()
			else:
				show_entry_message()
	else:
		show_entry_message()

def southmine():
	en_southmine()
	log_stats("redwind")
	game.player.randhint = ["Squash that scorpion! (attack)"]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.healthbank = game.player.maxhealth
	game.player.cmdext = ext_southmine
	if game.player.smetals:
		talking("There is no need to return here.")
		redwind()
	else:
		talking("You walk into the cave mine and see the drazmite ores. You approach them, but are interupted by a scorpion.")
		commands()
		
#southmine_1
def en_southmine_1():
	game.set_current_enemy(no_enemy)
	
def ext_southmine_1():
	show_entry_message
	
def southmine_1():
	game.player.savepos = southmine_1
	save()
	en_southmine_1()
	log_stats("southmine")
	game.player.randhint = ["Beep"]
	game.player.maxhealth = game.player.healthbank
	game.player.hasitems = False
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_southmine_1
	talking("\nYou excitedly run to the drazmite ores. They seem to be loose enough to not have to mine at. You pick some up and return to the village.")
	time.sleep(4)
	game.player.give_item(Item.drazmite, 3)
	game.player.smetals = True
	redwind()
	
def en_river():
	game.set_current_enemy(no_enemy)

def ext_river():
	def brewing():
		def herbamnt():
			for item in game.player.inventory.items:
				if item.type.name() == "Herb":
					return item.amount
		while True:
			print("~-< BREWING >-~")
			print("Herbs = ", herbamnt())
			print("Small		= 3")
			print("Medium		= 5")
			print("Large		= 7")
			print("Super		= 9")
			if not game.player.strangerecipe:
				print("Strange		= ?")
			else:
				print("Strange		= 45")
			print("To exit, type \"return\"")
			brewcmd = input("BREWING>").lower()
			if brewcmd == "return":
				break
			elif brewcmd == "small":
				try:
					if herbamnt() >= 3:
						game.player.take_item(Item.herb, 3)
						game.player.give_item(Potion.small, 1)
						talking("Small potion brewed.")
					else:
						print("Not enough herbs.")
				except TypeError:
					print("No herbs.")
			elif brewcmd == "medium":
				try:
					if herbamnt() >= 5:
						game.player.take_item(Item.herb, 5)
						game.player.give_item(Potion.medium, 1)
						talking("Medium potion brewed.")
					else:
						print("Not enough herbs.")
				except TypeError:
					print("No herbs.")
			elif brewcmd == "large":
				try:
					if herbamnt() >= 7:
						game.player.take_item(Item.herb, 7)
						game.player.give_item(Potion.large, 1)
						talking("Large potion brewed.")
					else:
						print("Not enough herbs.")
				except TypeError:
					print("No herbs.")
			elif brewcmd == "super":
				try:
					if herbamnt() >= 9:
						game.player.take_item(Item.herb, 9)
						game.player.give_item(Potion.super, 1)
						talking("Super potion brewed.")
					else:
						print("Not enough herbs.")
				except TypeError:
					print("No herbs.")
			elif brewcmd == "strange":
				if game.player.strangerecipe:
					try:	
						if herbamnt() >= 45:
							game.player.take_item(Item.herb, 45)
							game.player.maxhealth += 35
							game.player.maxstamina += 2
							game.player.fullheal()
							talking("Your stamina and health increased.")
						else:
							print("Not enough herbs.")
					except TypeError:
						print("No herbs.")
				elif game.player.strangeperm:
					talking("You don't know that recipe.")
				else:
					talking("\"I don't know the recipe for that yet. Maybe you can find it somewhere though.\"")
					game.player.strangeperm = True
			else:
				print("Not a potion.")
	if game.player.command in ["back", "return", "redwind"]:
		redwind()
	elif game.player.command == "brew":
		if (not game.player.has_item(Item.herb)):
			talking("\"You don't have any herbs. Find some in the forest.\"")
		else:
			brewing()
	else:
		show_entry_message()
	
def river():
	game.player.savepos = river
	save()
	en_river()
	log_stats("redwind")
	game.player.randhint = ["Hints? Stop wasting them."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_river
	time.sleep(3)
	print("(To leave, type \"return\")")
	time.sleep(1)
	talking("\"Welcome. Feel free to use my brewing stand to make potions (brew).\"")
	if game.player.areas.southmine == False:
		time.sleep(3)
		talking("\"What brings you here adventurer?\"")
		time.sleep(3)
		talking("\"Ruffin sent you? You have to make a sword?\"")
		time.sleep(4)
		talking("\"You should probably check the south mine for some Drazmite. It will give your sword great power when forged with it.\"")
		game.player.areas.southmine = True
	else:
		pass
	commands()
		
def en_final_battle():
	game.set_current_enemy(no_enemy)
	
def ext_final_battle():
	show_entry_message()
	
def final_battle():
	game.player.savepos = final_battle
	save()
	en_final_battle()
	log_stats("dracord")
	game.player.randhint = ["Hints tend to be useless."]
	game.player.stamina = game.player.maxstamina
	game.player.shielduse = 0
	game.player.cmdext = ext_final_battle
	if game.player.dracordReady:
		time.sleep(3)
		talking("You bravely walk into Dracord's lair. You drag your sword across the floor to announce your precense. Dracord growls. It is time to battle.")
	else:
		if game.player.dracordTry:
			talking("You already attempted to fight him before... You need to prepare. You return to Redwind.")
			redwind()
		else:
			time.sleep(3)
			talking("You approach Dracord. He notices you walk in and angrily breathes smoke.")
			time.sleep(4)
			talking("You charge at him with your sword.")
			time.sleep(3)
			print("*DING*")
			time.sleep(1)
			talking("Your sword is useless. Dracord smirks and whips you out the door with his tail. You pass out.")
			time.sleep(20)
			talking("%s!" % (game.player.name))
			time.sleep(3)
			talking("%s! Wake up!" % (game.player.name))
			time.sleep(5)
			talking("You slowly open your eyes. You see a glowing orb.")
			talking("%s, it's me, Ruffin...at least the spirit of me anyway. You're not ready to fight Dracord. You need a better weapon. Talk to Bruce. He can help you." % (game.player.name))
			game.player.dracordTry = True
			redwind()
	
#end
def end():
	#print("")
	talking("To be continued...")
	time.sleep(2)
	log_stats("End")
	show_player_stats()
	talking("The game isn't done. Don't forget to send me your log if you don't mind (More info about that in the readme file)!")
	survey = input("Would you like to take a survey to help me improve my game? The survey answers will be saved in the log file. (y/n)\n>").lower()
	if survey == "y":
		show_survey()
		sys.exit()
	else:
		logging.info("END OF SESSION; NO SURVEY")
		input("Thank you for playing my game!")
		sys.exit()

#************************************************************start************************************************************
		
def Save_Manager():
	def printsaves():
		print("AVAILABLE SAVES")
		print(", ".join(map(str, os.listdir("saves"))))
		print("\n")

	talking("MILDWIND SAVE MANAGER (EXPERIMENTAL)", 0.02)

	try:
		os.listdir("saves")
		print("\n")
		print("With the save manager, you can type the following commands:\nDelete\nRefresh\nClear\nBack\nExit")

		while True:
			print("\n")
			printsaves()
			command = input(">").lower()
			if command == "delete":
				file = input("Type the name of the save file you want to delete.\n>")
				confirm = input("Are you sure you want to delete " + file + " (y/n)?\n>").lower()
				if confirm == "y":
					try:
						os.remove("saves/" + file)
					except FileNotFoundError:
						print("File not found.")
				else:
					print("Back to main menu.")
			elif command == "exit":
				confirm = input("Are you sure you want to exit (y/n)?\n>").lower()
				if confirm == "y":
					sys.exit()
				else:
					print("Back to main menu.")
			elif command == "back":
				select()
			elif command in ["clear", "cls"]:
				clear = "\n" *100
				print(clear)
			else:
				print("Invalid command entered.")
	except FileNotFoundError:
		input("\nNo \"saves\" folder found. Run the game first.")
		
if not os.path.exists("saves"):
	os.makedirs("saves")

print("~ Saves ~")
print(", ".join(map(str, os.listdir("saves"))))
print("\n")


def select():
	while True:
		choice = input("Type \"start\" or press enter to start, or \"save manager\" to mangage saves.\n>")
		if choice in ["", "start"]:
			start()
		elif choice == "save manager":
			Save_Manager()
		else:
			print("Invalid entry.")


def tutorial_input():
	choice = input("Would you like to play the tutorial first? (y/n)\n>").lower()
	if choice == "y":
		tutorial()
	else:
		part1()

#possibly subject to being a function
def start():
	choose_name()
	try:
		load()
		print("Save version: " + game.player.version)
		if game.player.version != version:
			print("WARNING: SAVE NOT SAME AS GAME VERSION! CRASHES MAY RESULT!")
		while True:
			choice = input("Would you like to load from a save? (y/n) (Enter automatically selects yes)\n>").lower()
			if choice in ["y", ""]:
				game.player.savepos()
			elif choice == "n":
				reset_stats()
				tutorial_input()
			else:
				print("Nothing entered.")
	except FileNotFoundError:
		tutorial_input()
		
select()

