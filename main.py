'''
Animal Crossing New Horizons

Updates:
				- More villagers
				- Figured out inputs for going back
				- Wordart ;)

EVERYTHING BASED ON GAME BY NINTENDO
(you should get it)

'''
import os
import wordart
import random
import time
import sys

# VILLAGERS #

villager1 = random.choice([
				"Plucky", "Lolly", "Ankha", "Rosie", "Lily", "Charlise", "Peanut", "Apple",
				"Freya", "Katt", "Cherry", "Daisy", "Goldie", "Maple", "Hazel", "Marina"
])
villager2 = random.choice([
				"Bam", "Apollo", "Pierce", "Rex", "Axel", "Antonio", "Bud", "Beau",
				"Filbert", "Egbert", "Bill", "Buck", "Bob", "Poncho", "Hopper", "Ribbot",
				"Zucker"
])

# Added villagers so that they show up on the villagers screen.

villager3 = ""

villager4 = ""

villager5 = ""

villager6 = ""

villager7 = ""

villager8 = ""

villager9 = ""

villager10 = ""

# FISH AND STATS

total_fish = 0
horsemackerel = 0		# sells for only 150		C
oceansunfish = 0		# sells for 4000... only!? C
arowana = 0		# sells for 10000 C
seabass = 0		# sells for 400 D:<		C
oarfish = 0		# sells for 9000 C
whaleshark = 0		# sells for 13000 :O C
blackbass = 0		# sells for 400 C
tilapia = 0		# sells for 240 C
sweetfish = 0		# sells for 900 C
dace = 0		# sells for 240 C
seahorse = 0		# 1110 C
bluegill = 0		# 180 C

villagers_on_island = 2
spot1 = villager1
spot2 = villager2
spot3 = ""
spot4 = ""
spot5 = ""
spot6 = ""
spot7 = ""
spot8 = ""
spot9 = ""
spot10 = ""

bells = 400
tickets = 5
C = 0
x = 0
words = " "
word = " "
wardrobe_visited = 0

# ocean and River

ocean_fish = 0
river_fish = 0

# the typing effect


def typing(words):
				words
				for char in words:
								time.sleep(random.choice([0.04, 0.04, 0.05, 0.05, 0.04, 0.038, 0.05]))
								sys.stdout.write(char)
								sys.stdout.flush()

t = 0

def fastt(word):
				word
				for char in word:
								time.sleep(random.choice([0.03, 0.02, 0.04, 0.028]))
								sys.stdout.write(char)
								sys.stdout.flush()


def clear():
				os.system("clear")


y = True
villagervisit = 0

# before loading:
for i in range(1):
				print("loading")
				time.sleep(0.56)
				clear()
				print("loading .")
				time.sleep(0.56)
				clear()
				print("loading . .")
				time.sleep(0.56)
				clear()
				print("loading . . .")
				time.sleep(0.56)
				clear()
				print("loading . .")
				time.sleep(0.56)
				clear()
				print("loading .")
				time.sleep(0.56)
				clear()

name = input("\033[1;39;38mWhat is your name?\n")
name = name.capitalize()
island = input("Island name?\n")
time.sleep(1)
clear()
print("Welcome to " + island + ", " + name + "!")
if name == "Jordy":
	C = 5
if C == 5:
	clear()
	sys.exit("You are banned Reason:\nComputers are stupid.")
while x == 0:
				wordart.intro()
				print(
								"\033[1;36;38mAnimal Crossing, \033[1;93mNew Horizons Version3.0\n----------\033[1;39;38m"
				)
				print(
								"\033[1;36;38m1,\033[1;39;38m Fish.\n\033[1;36;38m2, \033[1;39;38mStats.\n\033[1;36;38m3,\033[1;39;38m Meet Villagers.\n\033[1;36;38m4, \033[1;39;38mWardrobe.\n\033[1;36;38m5, \033[1;39;38mExit game.\n\033[1;36;38m6, \033[1;39;38mStore.\n\033[1;36;38m7, \033[1;39;38mDodo Airlines/Airport.\n"
				)
				where = input("Type the corresponding number: ").lower()
				x = 1
				if where == "computers are stupid":
					clear()
					sys.exit("Well, you are stupid as well.")
					C = 5
				elif where == "1":
								# FISH
								clear()
								where_fish = input(
												"Where do you want to fish? \n\n\033[1;93m1,\033[1;39m Ocean.\n\033[1;36m2, \033[1;39mRiver.\n\033[1;93m3, \033[1;39mBack."
								)
								if where_fish == "1":
												clear()
												while x == 1:
																print(
																				"\nOcean Fishing\n\033[1;36;38m1, \033[1;39;38mFish.\n\033[1;36;38m2, \033[1;39;38mBack."
																)
																fishnot = input("Type the corresponding number: ")
																if fishnot == "1":
																				fish_type = random.randint(0, 100)
																				if fish_type <= 20:
																								fastt(
																												"I caught a \033[1;36;38mSea Bass!\n\033[1;39;38mAt least it's a C+!"
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								seabass += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fish_type <= 40:
																								fastt(
																												"I caught a \033[1;36;38mHorse Mackerel!\n\033[1;39;38mOf course, Mack...er...el."
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								horsemackerel += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fish_type <= 48:
																								fastt(
																												"I caught an \033[1;36;38mOarfish!\n\033[1;39;38mI hope I catch morefish!"
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								ocean_fish += 1
																								oarfish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fish_type <= 60:
																								fastt(
																												"I caught a\033[1;36;38m Sea bass!\n\033[1;39;38mAt least it's a C+!"
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								seabass += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fish_type <= 70:
																								fastt(
																												"I caught a \033[1;36;38mOcean Sunfish!\n\033[1;39;38mGood thing I'm wearing ocean sunscreen!"
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								oceansunfish += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fish_type <= 80:
																								fastt("THAR SHE BLOWS!")
																								time.sleep(0.8)
																								fastt(
																												"\nI caught a \033[1;36;38mWhale Shark!\n\033[1;39;38mI'm tellin' ya, it was thiiiiiiiiiiiiiiis big!"
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								whaleshark += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fish_type <= 90:
																								fastt(
																												"I caught a \033[1;36;38mSeahorse!\n\033[1;39;38mBut...where's it's sea jockey?"
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								seahorse += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				else:
																								fastt(
																												"I caught a \033[1;36;38mHorse Mackerel!\n\033[1;39;38mOf course, Mack...er...el."
																								)
																								time.sleep(0.9)
																								total_fish += 1
																								horsemackerel += 1
																								ocean_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																elif fishnot == "2":
																				x = 0
																				clear()
								elif where_fish == "2":
												clear()
												fastt(
																"You grab your fishing rod and walk over to the river. Look, some shadows!"
												)
												x = 100
												while x == 100:
																typing(
																				"\n\033[1;36;38m1, \033[1;39;38mFish.\n\033[1;36;38m2, \033[1;39;38mBack."
																)
																fishor = input("\nType the corresponding number: ")
																if fishor == "1":
																				fishget = random.randint(0, 100)
																				if fishget <= 20:
																								fastt(
																												"I caught a \033[1;36;38mBlack Bass!\n\033[1;39;38mThe most metal of all fish!"
																								)
																								total_fish += 1
																								river_fish += 1
																								blackbass += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fishget <= 40:
																								fastt(
																												"I caught a \033[1;36;38mDace!\n\033[1;39;38mHope I have some space!"
																								)
																								total_fish += 1
																								river_fish += 1
																								dace += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fishget <= 48:
																								fastt(
																												"I caught a \033[1;36;38mArowana!\n\033[1;39;38mI'd make a joke, but I don't 'wana."
																								)
																								total_fish += 1
																								river_fish += 1
																								arowana += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fishget <= 60:
																								fastt(
																												"I caught a \033[1;36;38mTilapia!\n\033[1;39;38mIt makes me happy-a!"
																								)
																								total_fish += 1
																								river_fish += 1
																								tilapia += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fishget <= 70:
																								fastt(
																												"I caught a \033[1;36;38mSweetfish!\n\033[1;39;38mHope it's not artificially sweet!"
																								)
																								total_fish += 1
																								sweetfish += 1
																								river_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fishget <= 80:
																								fastt(
																												"I caught a \033[1;36;38mBlack Bass!\n\033[1;39;38mThe most metal of all fish!"
																								)
																								total_fish += 1
																								blackbass += 1
																								river_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				elif fishget <= 90:
																								fastt(
																												"I caught a \033[1;36;38mTilapia!\n\033[1;39;38mIt makes me happy-a!"
																								)
																								total_fish += 1
																								tilapia += 1
																								river_fish += 1
																								input("\npress [ENTER]>")
																								clear()
																				else:
																								fastt(
																												"I caught \033[1;36;38mBluegill!\n\033[1;39;38mDo you think it calls me 'pinklung'?"
																								)
																								total_fish += 1
																								river_fish += 1
																								bluegill += 1
																								input("\npress [ENTER]>")
																								clear()
																elif fishor == "2":
																				x = 0
								elif where_fish == "3":
												x = 0
				elif where == "2":
								# STATS
								clear()
								print("Total fish caught:\033[1;36;38m")
								print(total_fish)
								print("\033[1;39;38mTotal River fish caught:\033[1;36;38m")
								print(river_fish)
								print("\033[1;39;38mTotal ocean fish caught:\033[1;36;38m")
								print(ocean_fish)
								time.sleep(0.9)
								print("\033[1;39;38mArowana caught:\033[1;36;38m")
								print(arowana)
								print("\033[1;39;38mBlack bass caught:\033[1;36;38m")
								print(blackbass)
								print("\033[1;39;38mOarfish caught:\033[1;36;38m")
								print(oarfish)
								time.sleep(0.9)
								print("\033[1;39;38mSea bass caught:\033[1;36;38m")
								print(seabass)
								time.sleep(0.9)
								print("\033[1;39;38mHorse Mackerel caught:\033[1;36;38m")
								print(horsemackerel)
								print("\033[1;39;38mOcean Sunfish caught:\033[1;36;38m")
								print(oceansunfish)
								time.sleep(0.9)
								print("\033[1;39;38mDace caught:\033[1;36;38m")
								print(dace)
								print("\033[1;39;38mWhale Shark caught:\033[1;36;38m")
								print(whaleshark)
								time.sleep(0.9)
								print("\033[1;39;38mSeahorse caught:\033[1;36;38m")
								print(seahorse)
								print("\033[1;39;38mSweetfish caught:\033[1;36;38m")
								print(sweetfish)
								print("\033[1;39;38mTilapia caught: \033[1;36;38m")
								print(tilapia)
								time.sleep(0.9)
								print("\033[1;39;38mBluegill caught:\033[1;36;38m")
								print(bluegill)
								print("\033[1;39;38mBells:\033[1;36;38m")
								print(bells)
								print("\033[1;39;38mTickets:\033[1;36;38m")
								print(tickets)
								time.sleep(0.9)
								print("\033[1;39;38mTotal villagers:\033[1;36;38m")
								print(villagers_on_island)
								input("\n>>Press [ENTER] to go back.\033[1;39;38m")
								x = 0
								clear()
				elif where == "3":
								clear()
								wordart.villager()
								if villagervisit == 0:
												# VILLAGERS
												villagervisit += 1
												if villager3 == "":
													print("Your villagers are: ")
												print("Your villagers are: \033[1;36;38m", villager1,
																		",\033[1;36;38m", villager2, "\033[1;39;38m,", villager3, ",\033[1;36;38m", villager4, ",\033[1;36;38m", villager5, ",\033[1;36;38m", villager6, ",\033[1;36;38m", villager7, ",\033[1;36;38m", villager8, ",\033[1;36;38m", villager9, ", and\033[1;36;38m", villager10, ".")
												time.sleep(2)
												clear()
												x = 0
								elif villagervisit >= 1:
												print("Your villagers are: \033[1;36;38m", villager1,
																		",\033[1;36;38m", villager2, "\033[1;39;38m,", villager3, ",\033[1;36;38m", villager4, ",\033[1;36;38m", villager5, ",\033[1;36;38m", villager6, ",\033[1;36;38m", villager7, ",\033[1;36;38m", villager8, ",\033[1;36;38m", villager9, ", and\033[1;36;38m", villager10, ".")
												time.sleep(2)
												clear()
												typing("You greet your villagers. 'Hello!'")
												typing(
																"\nThey greet you too, and say they are excited to be here.")
												input("\n\npress enter to go back >>")
												clear()
												x = 0
				elif where == "4":
								clear()
								wordart.wardrobe()
								if wardrobe_visited == 0:
												wardrobe_visited += 1
												typing("Your 'mom' has left you some clothing!")
												typing("You put on new clothing.")
												typing("......")
												time.sleep(2.45)
												clear()
												wordart.wardrobe()
												print("Oh? you villager\033[1;94m", villager1,
																		"\033[1;39mis here!\033[1;94m\n")
												time.sleep(1)
												print(
																villager1 + "\033[1;39m: Hello", name,
																"\nI found these\033[1;94;38m house slippers\033[1;39;38m in my house the other day. I would like you to have it!\n\nwhat do you want to say?\n1, Thank you!\n2, Hello! Thanks!"
												)
												conversation = input("\033[1;94m")
												if conversation == "1":
																print(name + "\033[1;39m: Thank you!\033[1;94m")
												elif conversation == "2":
																print(name + "\033[1;39m: Hello! Thanks!\033[1;94m")
												print(villager1 +
																		"\033[1;39m: You're welcome! This island is so nice!")
												time.sleep(2)
												input("press Enter to go back")
												clear()
												x = 0
								elif wardrobe_visited >= 0:
												typing("What do you want to put on:\n")
												typing("\033[1;93m1\033[1;39m Marble Dots Tee")
												typing("\n\033[1;36m2\033[1;39m Nook Inc Aloha Shirt")
												typing("\n\033[1;93m3\033[1;39m Patchwork Coat")
												wear = input("")
												typing("Kk :D")
												input("\n\n>>[ENTER] to go back")
												clear()
												x = 0
				elif where == "5":
								clear()
								typing("Bye! Have a good day...\n")
								sys.exit("Thanks for playing!")
				elif where == "6":
								clear()
								typing("WELCOME TO THE STORE!\n")
								typing(
												"Here, you can sell fish and buy tickets for finding villagers.\n\n*nook miles are not yet added*\n"
								)
								input("Press [ENTER]>>")
								clear()
								print("\033[1;94mTommy\033[1;39m: Hello, " + name + "!")
								go = "yes"		#too lazy to fix indentations
								if go == "yes":
												print(
																"\nWhat do you want to do?\n[1] Sell fish\n[2] Buy tickets\n[3] Leave\n(numbers only)"
												)
												
												yesorno = input("")
												if yesorno == "1":
																time.sleep(1)
																clear()
																typing("\033[1;94mTommy\033[1;39m: Here's what you have:		\n")
																print("a. Blackbass", blackbass)
																print("b. Whaleshark", whaleshark)
																print("c. Horsemackerel", horsemackerel)
																print("d. Tilapia", tilapia)
																print("e. Arowana", arowana)
																print("f. Bluegill", bluegill)
																print("g. Ocean sunfish", oceansunfish)
																print("h. Sea bass", seabass)
																print("i. Oarfish", oarfish)
																print("j. Sweetfish", sweetfish)
																print("k. Dace", dace)
																print("l. Seahorse", seahorse)

																sellwhat = input(
																				"\nWhat do you want to sell (type in the letter): ").lower(
																				)
																if sellwhat == "a" and blackbass > 0:
																				continoo = "yes"
																				bells += 400
																				blackbass -= 1
																elif sellwhat == "b" and whaleshark > 0:
																				continoo = "yes"
																				bells += 13000
																				whaleshark -= 1
																elif sellwhat == "c" and horsemackerel > 0:
																				continoo = "yes"
																				bells += 150
																				horsemackerel -= 1
																elif sellwhat == "d" and tilapia > 0:
																				continoo = "yes"
																				bells += 240
																				tilapia -= 1
																elif sellwhat == "e" and arowana > 0:
																				continoo = "yes"
																				bells += 10000
																				arowana -= 1
																elif sellwhat == "f" and bluegill > 0:
																				continoo = "yes"
																				bells += 180
																				bluegill -= 1
																elif sellwhat == "g" and oceansunfish > 0:
																				continoo = "yes"
																				bells += 4000
																				oceansunfish -= 1
																elif sellwhat == "h" and seabass > 0:
																				continoo = "yes"
																				bells += 400
																				seabass -= 1
																elif sellwhat == "i" and oarfish > 0:
																				continoo = "yes"
																				bells += 9000
																				oarfish -= 1
																elif sellwhat == "j" and sweetfish > 0:
																				continoo = "yes"
																				bells += 900
																				sweetfish -= 1
																elif sellwhat == "k" and dace > 0:
																				continoo = "yes"
																				bells += 240
																				dace -= 1
																elif sellwhat == "l" and seahorse > 0:
																				continoo = "yes"
																				bells += 1110
																				seahorse -= 1
																else:
																				continoo = "no"
																				typing(
																								"\n\033[1;94mTommy\033[1;39m: I don't think you have that fish, sry.\n"
																				)
																				input("press enter to go back > ")
																				clear()
																				x = 0
																if continoo == "yes":
																				typing(
																								"\033[1;94mTommy\033[1;39m: Success! Press enter to go back "
																				)
																				input()
																				clear()
																				x = 0
																elif continoo == "no":
																				x = 0
												elif yesorno == "3":
																clear()
																x = 0
												elif yesorno == "2":
																clear()
																typing("\033[1;94mTommy\033[1;39m: Would you like to buy tickets? You have ")
																print(tickets, "tickets.")
																typing("[1] Yes\n[2] No\n(Numbers Only)\n")
																buyticket = input("").lower()
																if buyticket == "1":
																				if bells == 400:
																								print(
																												"\033[1;94mTommy\033[1;39m: Ticket Purchased!\nPress [ENTER] to go back"
																								)
																								tickets += 1
																								bells -= 400
																								input("")
																								clear()
																								x = 0
																				elif bells < 400:
																								typing("\033[1;94mTommy\033[1;39m: Not enough Bells...\nPress [ENTER] to go back.\n")
																								input("")
																								clear()
																								x = 0
																elif buyticket == 2:
																		typing("\033[1;94mTommy\033[1;39m: Maybe next time then...\nPress [ENTER] to go back.\n")
																		input("")
																		clear()
																		x = 0
																else:
																	clear()
																	x = 0
												else:
																clear()
																x = 0
				elif where == "7":
								if villagers_on_island >= 10:
												clear()
												typing("You have the max amount of villagers.")
												time.sleep(2.5)
												clear()
												x = 0
								elif villagers_on_island < 10:
												clear()
												typing("Welcome to the Airport.")
												typing("\nTime to go on a villager hunt!\n")
												typing("")
												if tickets == 0:
																clear()
																typing("Not enough tickets...")
																input("\n([ENTER])")
																clear()
																x = 0
												elif tickets > 0:
																typing(
																				"\nDo you wish to search for a villager?\n\033[1;36m1,\033[1;39m Yes\n\033[1;36m2,\033[1;39m No\n(Numbers only)\n"
																)
																villagerhunt = input("").lower()
																if villagerhunt == "1":
																				time.sleep(0.9)
																				clear()
																				tickets -= 1
																				typing("Dodo Airlines . . . loading . . . ")
																				time.sleep(random.choice([2, 4]))
																				typing("\nboarding plane . . . ")
																				time.sleep(random.choice([1, 2]))
																				typing("\narriving . . . please wait . . . ")
																				time.sleep(0.5)
																				clear()
																				villager_found = random.choice([
																								"Audie", "Beau", "Bianca", "Blair", "Lucky", "Bones",
																								"Bunnie", "Canberra", "Coco", "Cookie", "Deli", "Lily",
																								"Drift", "Filbert", "Kiki", "Murphy", "Raymond"
																				])
																				fs = "no"
																				villagers_on_island += 1
																				if villagers_on_island > 10:
																								print("Error, you have too many villagers...\n")
																								time.sleep(3.5)
																								clear()
																								x = 0
																				elif villagers_on_island <= 10:
																								if spot3 == "":
																												fs = "yes"
																												villager3 = villager_found
																												spot3 = villager3

																								elif spot4 == "":
																												fs = "yes"
																												villager4 = villager_found
																												spot4 = villager4

																								elif spot5 == "":
																												fs = "yes"
																												villager5 = villager_found
																												spot5 = villager5

																								elif spot6 == "":
																												fs = "yes"
																												villager6 = villager_found
																												spot6 = villager6

																								elif spot7 == "":
																												fs = "yes"
																												villager7 = villager7
																												spot7 = villager7

																								elif spot8 == "":
																												fs = "yes"
																												villager8 = villager_found
																												spot8 = villager8

																								elif spot9 == "":
																												fs = "yes"
																												villager9 = villager_found
																												spot9 = villager9

																								elif spot10 == "":
																												fs = "yes"
																												villager10 = villager_found
																												spot10 = villager10
																								print("Success! You invited:")
																								print(villager_found)
																								input("\npresss enter to go back.\n")
																								clear()
																								x = 0
																elif villagerhunt == "2":
																				clear()
																				x = 0
																else:
																	clear()
																	x = 0
				elif where == "650123":
					clear()
					print("Entering dev mode")
					time.sleep(1)
					clear()
					print("Entering dev mode.")
					time.sleep(1)
					clear()
					print("Entering dev mode..")
					time.sleep(1)
					clear()
					print("Entering dev mode...")
					time.sleep(1)
					clear()
					print("Entering dev mode....")
					time.sleep(1)
					clear()
					print("Entering dev mode.....")
					time.sleep(1)
					clear()
					print("Entering dev mode....")
					time.sleep(1)
					clear()
					print("Entering dev mode...")
					time.sleep(1)
					clear()
					print("Entering dev mode..")
					time.sleep(1)
					clear()
					print("Entering dev mode.")
					time.sleep(1)
					clear()
					print("Entering dev mode")
					time.sleep(1)
					clear()
					x = 5
					if name == "Firepup650":
						if island == "Castaways":
							bells = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
							tickets = 10
							clear()
							x=0
						else:
							while x == 5:
								print("\033[0;31mERROR: FEATURE DOES NOT EXIST")
								print(t)
								t += 1
								x = 6
								if t == 100000:
									clear()
									sys.exit("\033[0;31mA fatal error occured")
								else:
									x = 5
					else:
						while x == 5:
								print("\033[0;31mERROR: FEATURE DOES NOT EXIST")
								print(t)
								t += 1
								x = 6
								if t == 100000:
									clear()
									sys.exit("\033[0;31mA fatal error occured")
								else:
									x = 5
				else:
								clear()
								x = 0