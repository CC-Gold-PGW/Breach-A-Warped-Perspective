#===============================================================================
#CREDITS & LICENSE
#===============================================================================
#Rocket Propelled Games
#Breach: A Warped Perspective
#Chris, Finn, Roman, Liam
#===============================================================================
#IMPORTING LIBRARIES
#===============================================================================
import math
import random
import time
import sys
import csv
import os
#===============================================================================
#INITALISING GLOBAL VARIABLES
#===============================================================================
#Player global values should be changed directly by the room functions: No need for passing them into functions
#Will make these an object instead later
playerMaxHP = 100
playerHP = 100
playerDMG = 10
playerAccuracy = 1
playerCrit = 21
playerCritDMG = 1.5
#Enemy global values like player values should be updated by the room functions as needed
#Should also become an object later
MobCurrentHP = 1000
mobDMG = 1
mobAccuracy = 1
mobCrit = 21
mobCritDMG = 1.5
MobMaxHP = 1000
#Tracks the number of healing kits carried
heal = 100
#Tracks if a healthkit was actually used in combat to see if a turn needs to be skipped
HealthKitUsed = False
#Holds the monsters 2 attack preferences
#3 types of attacks.  Defensive beats Opportunistic, Opportunistic beats Offensive, Offensive beats Defensive
AttackPreference1 = "Offensive"
AttackPreference2 = "Offensive"
#Tracks the players current location
currentLocation = 0
#------------------------------------------------------------------------------
 #Flags tracking which rooms have been entered
enter1 = 0
enter2 = 0
enter3 = 0
enter4 = 0
enter5 = 0
enter6 = 0
enter7 = 0
enter8 = 0
enter9 = 0
enter10 = 0
enter11 = 0
#===============================================================================
#DEFINING FUNCTIONS
#===============================================================================
#Game Start Functions
#-------------------------------------------------------------------------------
def Start():
    #Shows title screen and provides options for starting a new game or loading an existing one.
    global playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation
    print ("")
    print ("1. New Game")
    print ("2. Continue")
    print ("3. Exit Game")
    print ("")
    choice = 0
    #Using external validator function for all choices
    choice = validateNum(choice,1,3)
    if choice == 1:
        intro()
    elif choice == 2:
        Load()
        #Runs external function for sending the player to the correct room
        Location(currentLocation)
    elif choice == 3:
        sys.exit("Shutting Down")
#-------------------------------------------------------------------------------
def intro():
    #Displays the game's intro text
    print ("It's been 2 hours since you were seperated from your team.  The cave you stand in is cold and dank, musty air fills your lungs.")
    print ("")
    os.system("pause")
    print ("You avoided the rockfall unscathed, but were unable to find anyone else who had, and lack the tools to dig through the rubble behind you.")
    print ("If there were any survivors you could not help them and with no where else you could go you headed deeper into the cave.")
    print ("")
    os.system("pause")
    print ("You are aware of how long it has been thanks to your suit’s internal clock,")
    print ("and you have enough rations to survive a week underground, but without an exit plan you will surely die here.")
    print ("")
    os.system("pause")
    print ("The cave you are walking through continues on in a straight line without deviation and with no other visible paths.  It is wide and curved with remarkable smoothness.")
    print ("You are unsure if this used to be an underground river, or was created artificially.")
    print ("")
    os.system("pause")
    print ("This question is answered soon enough as you round the corner by artificial green light and what is quite clearly a very artificial door.")
    print ("")
    os.system("pause")
    print ("As you approach the door, it slides open soundlessly, revealing a dark complex of metal corridors, burnt into your retinas as bright lights burst into life above you.")
    print ("The metal is a glossy dark material and is covered in irregular patterns and you are unsure if they are just a decorative texture or symbols with meaning.")
    print ("")
    os.system("pause")
    print ("You have nowhere else you could go.  You step through the door and it shuts behind you with a soft hissing sound and the green light disappears.")
    print ("This door will not open again.")
    print ("")
    os.system("pause")
    print ("Three more doors to the West, South and East of you activate and begin to cast a viridian glow.")
    print ("")
    os.system("pause")
    print ("What do you do?")
    print ("")
    #Load the first room to begin the game
    room1()
#===============================================================================
#Player Option Functions
#-------------------------------------------------------------------------------
def Load():
    global playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation
    #Loads all revelant global variables from an external file and moves player to the correct room
    stats = ""
    with open("BreachSaved.csv", "r") as loadFile:

        stats = loadFile.read()
        stats = stats.split(",")
        playerHP = int(stats[0])
        playerMaxHP = int(stats[1])
        playerDMG = int(stats[2])
        playerCrit = int(stats[3])
        playerCritDMG = float(stats[4])
        playerAccuracy = int(stats[5])
        heal = int(stats[6])
        enter1 = int(stats[7])
        enter2 = int(stats[8])
        enter3 = int(stats[9])
        enter4 = int(stats[10])
        enter5 = int(stats[11])
        enter6 = int(stats[12])
        enter7 = int(stats[13])
        enter8 = int(stats[14])
        enter9 = int(stats[15])
        enter10 = int(stats[16])
        enter11 = int(stats[17])
        currentLocation = int(stats[18])
        print (currentLocation)
        return
#-------------------------------------------------------------------------------
def Location(currentLocation):
    #Used by the Load function to find the correct room function to run based on the Current Location flag
    print (currentLocation)
    if currentLocation == 1:
        room1()
    elif currentLocation == 2:
        room2()
    elif currentLocation == 3:
        room3()
    elif currentLocation == 4:
        room4()
    elif currentLocation == 5:
        room5()
    elif currentLocation == 6:
        room6()
    elif currentLocation == 7:
        room7()
    elif currentLocation == 8:
        room8
    elif currentLocation == 9:
        room9()
    elif currentLocation == 10:
        room10()
    elif currentLocation == 11:
        room11()
#-------------------------------------------------------------------------------
def healthkit(HealthKitUsed):
    #Handles the usage of Health Kits.
    #Health Kits return you to your maximum HP and have one use
    global playerHP, playerMaxHP, heal
    gainhealth = 0
    if heal > 0:
        print ("Are you sure you want to use a health kit?")
        print ("Health Kits Remaining:",heal)
        print ("Current HP:",playerHP,"/",playerMaxHP)
        print ("1. Yes")
        print ("2. No")
        gainhealth = validateNum(gainhealth,1,2)
        print(gainhealth)
        if gainhealth == 1:
            playerHP = playerMaxHP
            print("You use the Health Kit.  Your HP maxes out at",playerHP)
            heal = heal - 1
            print("Healthkits remaining:",heal)
            return True
        elif gainhealth == 2:
            print("You decide not to use a healthkit")
            return False
    else:
        print("You do not have any Health Kits to use")
        return False
#-------------------------------------------------------------------------------
def Options():
    #Gives the player the option to use a Health Kit, Save the game or continue
    #Should be run at the end of each room before they choose which door to go through
    while True:
        print ("What do you want to do?")
        print ("")
        print ("1. Move")
        print ("2. Heal")
        print ("3. Save Game")
        print ("4. Exit Game")
        print ("")
        Option = 0
        Option = validateNum(Option,1,4)
        if Option == 1:
            return
        elif Option == 2:
            healthkit(HealthKitUsed)
        elif Option == 3:
            SaveGame(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation)
            print ("Game Saved")
        elif Option == 4:
            sys.exit("Shutting Down")
#-------------------------------------------------------------------------------
def SaveGame(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation):
#Handles saving the game to an external file.  Only one save should be supported, saving again will overwrite the last.
    file = open("BreachSaved.csv", "w")
    file.write(str(playerHP))
    file.write(",")
    file.write(str(playerMaxHP))
    file.write(str(","))
    file.write(str(playerDMG))
    file.write(str(","))
    file.write(str(playerCrit))
    file.write(str(","))
    file.write(str(playerCritDMG))
    file.write(str(","))
    file.write(str(playerAccuracy))
    file.write(str(","))
    file.write(str(heal))
    file.write(str(","))
    file.write(str(enter1))
    file.write(str(","))
    file.write(str(enter2))
    file.write(str(","))
    file.write(str(enter3))
    file.write(str(","))
    file.write(str(enter4))
    file.write(str(","))
    file.write(str(enter5))
    file.write(str(","))
    file.write(str(enter6))
    file.write(str(","))
    file.write(str(enter7))
    file.write(str(","))
    file.write(str(enter8))
    file.write(str(","))
    file.write(str(enter9))
    file.write(str(","))
    file.write(str(enter10))
    file.write(str(","))
    file.write(str(enter11))
    file.write(str(","))
    file.write(str(currentLocation))
    file.write("\n")
    file.close()
#===============================================================================
#Validators & Error Catching
#-------------------------------------------------------------------------------
def validateNum(value, min, max):
#Input validator: Takes the inputted number and the range of valid choices and checks for value validity
    while True:
        try:
            value = int(input("Please choose your option\n"))
        except ValueError:
            print ("Sorry please enter a number\n")
            continue
        else:
            if value >= min and value <= max:
                return value
            else:
                print ("Please enter a number between",min,"and",max,"\n")
                continue

#===============================================================================
#Combat System Functions
#Player and enemy make opposed choices in a Rock/Paper/Scissors format and roll 1d20 to determine accuracy
#-------------------------------------------------------------------------------
def EnemyAttackWeighting(Preference1,Preference2):
#This function determines the enemy's choices, selected randomly weighted toward their preference
#Some enemies switch their attack preference when reduced below 1/2 HP
    global MobCurrentHP
    global MobMaxHP
    if MobCurrentHP <= (MobMaxHP/2):
        WeightingList = [1,2,3,Preference2,Preference2,Preference2]
        AttackChoice = random.choice(WeightingList)
        print(AttackChoice)
        return AttackChoice
    else:
        WeightingList = [1,2,3,Preference1,Preference1,Preference1]
        AttackChoice = random.choice(WeightingList)
        print(AttackChoice)
        return AttackChoice
#-------------------------------------------------------------------------------
def PlayerAccuracyCheck(AttackResult):
  #Function for handling the player's accuracy roll and determining the result of their attack
  global playerCrit, playerAccuracy
  Roll = 0
  Roll = random.randint(1,20)
  print ("You attack!  You rolled a",Roll)

  if Roll >= playerCrit:
      AttackResult = "Crits"
  elif Roll >= playerAccuracy:
      AttackResult = "Hits"
  else:
      AttackResult = "Misses"
  time.sleep(0.5)
  print(AttackResult)
  return AttackResult
#-------------------------------------------------------------------------------
def MobAccuracyCheck(AttackResult):
  #Function for handling the enemy's accuracy roll and determining the result of their attack
  global mobCrit, mobAccuracy
  Roll = 0
  Roll = random.randint(1,20)
  print ("The enemy attacks!  They rolled a",Roll)

  if Roll >= mobCrit:
      AttackResult = "Crits"
  elif Roll >= mobAccuracy:
      AttackResult = "Hits"
  else:
      AttackResult = "Misses"
  time.sleep(0.5)
  print(AttackResult
  return AttackResult
#-------------------------------------------------------------------------------
def Combat():
#Main combat function.  Loops until combat ends, and is in charge of calling the other combat functions
    global AttackPreference1, AttackPreference2
    playerAttackResult = ""
    mobAttackResult = ""
    HealthKitUsed = False
    fight = 1

    while playerHP > 0 or MobCurrentHP > 0:
        #Loops until either player or enemy are dead
        if playerHP <= 0:
            print ("...and you were never heard from again")
            print ("GAME OVER")
            print("")
            os.system("pause")
            Start()

        elif MobCurrentHP <= 0:
            print("WIN")
            return

        else:
            #Rock/Paper/Scissors combat system with additional roll-to-hit subsystem
            time.sleep(1)
            while True:
                print ("")
                print ("Current HP:",playerHP,"/",playerMaxHP)
                print ("Health Kits held:",heal)
                print ("1. Make a Defensive Attack")
                print ("2. Make a Offensive Attack")
                print ("3. Make an Opportunistic Attack")
                print ("4. Use a Health Kit")
                print ("Mob HP:",MobCurrentHP,"/",MobMaxHP)
                print ("")
                #Using validator function for all player choices
                fight = validateNum(fight,1,4)
                if fight == 4:
                    HealthKitUsed = healthkit(HealthKitUsed)
                    if HealthKitUsed == True:
                        break
                    else:
                        continue
                else:
                    HealthKitUsed = False
                    break

            #Player loses their opportunity to attack if a Health Kit was used
            if HealthKitUsed == False:
                playerAttackResult = PlayerAccuracyCheck(playerAttackResult)
            else:
                playerAttackResult = "Misses"

            mobAttack = EnemyAttackWeighting(AttackPreference1, AttackPreference2)
            mobAttackResult = MobAccuracyCheck(mobAttackResult)

        #Iterate through all possible scenarios:
        #If both parties Hit combat is resolved by their attack choice
        #If one hits and the other misses the one that hits wins that combat and deals damage
        #Critical Hits are handled the same way as Hits but grant a bonus multiplier to damage dealt
        if playerAttackResult == "Hits" and mobAttackResult == "Hits":
            if fight == 1 and mobAttack == 1:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight == 1 and mobAttack == 2:
                ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

            elif fight == 1 and mobAttack == 3:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 1:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 2:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 3:
                ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

            elif fight ==3 and mobAttack == 1:
                ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

            elif fight == 3 and mobAttack == 2:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight == 3 and mobAttack == 3:
                ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Crits" and mobAttackResult == "Crits":

            if fight == 1 and mobAttack == 1:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight == 1 and mobAttack == 2:
                ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

            elif fight == 1 and mobAttack == 3:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 1:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 2:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 3:
                ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

            elif fight ==3 and mobAttack == 1:
                ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

            elif fight == 3 and mobAttack == 2:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight == 3 and mobAttack == 3:
                ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Misses" and mobAttackResult == "Misses":
            if HealthKitUsed == True:
                print("You are too busy using the Health Kit to fight back!")
                print("...Fortunantly the enemy missed their attack!")
            else:
                print ("Your attack misses the target!")
                print ("...The enemy also misses their counter attack!")
            continue

        elif playerAttackResult == "Hits" and mobAttackResult == "Misses":
            ComWin(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Hits" and mobAttackResult == "Crits":
            ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Misses" and mobAttackResult == "Hits":
            ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

        elif playerAttackResult == "Misses" and mobAttackResult == "Crits":
            ComLose(playerAttackResult, mobAttackResult, HealthKitUsed)

        elif playerAttackResult =="Crits" and mobAttackResult == "Misses":
            ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Crits" and mobAttackResult == "Hits":
            ComDraw(playerAttackResult, mobAttackResult)
#-------------------------------------------------------------------------------
def ComWin(playerAttackResult, mobAttackResult):
    #Combat win scenario: Player deals damage, Enemy does not
    global MobCurrentHP, playerDMG, playerCritDMG
    if playerAttackResult == "Crits":
        MobCurrentHP = MobCurrentHP - (round(playerDMG * playerCritDMG))
        print("You land a Critical Hit and prevent their counter attack!")
    else:
        MobCurrentHP = MobCurrentHP - (playerDMG)
        print ("You score a hit and evade their counter attack!")
    return MobCurrentHP
#-------------------------------------------------------------------------------
def ComLose(playerAttackResult, mobAttackResult, HealthKitUsed):
    #Combat Lose scenario: Enemy deals damage, Player does not
    global playerHP, mobDMG, mobCritDMG
    if mobAttackResult == "Crits":
        playerHP = playerHP - (round(mobDMG * mobCritDMG))
        if HealthKitUsed == True:
            print("You are too busy using the Health Kit to fight back!")
            print("...And the enemy lands a Critical hit on you as a result!")
        else:
            print("The enemy lands a Critical Hit and prevents you from fighting back!")
    else:
        playerHP = playerHP - mobDMG
        if HealthKitUsed == True:
            print("You are too busy using the Health Kit to fight back!")
            print("...And the enemy hits you as a result!")
        else:
            print("The enemy evades your attack and scores a hit on you!")
    return playerHP
#-------------------------------------------------------------------------------
def ComDraw(playerAttackResult, mobAttackResult):
    #Combat Draw scenario: Both parties deal damage
    global MobCurrentHP, mobDMG, playerDMG, playerHP, playerCritDMG, mobCritDMG
    #Resolving player damage
    if playerAttackResult == "Crits":
        MobCurrentHP = MobCurrentHP - (round(playerDMG * playerCritDMG))
        print("You land a Critical hit!")
    else:
        MobCurrentHP = MobCurrentHP - (playerDMG)
        print ("You land a hit!")
    #Resolving enemy damage
    if mobAttackResult == "Crits":
        playerHP = playerHP - (round(mobDMG * mobCritDMG))
        print("...However the enemy lands a Critical counter attack!")
    else:
        playerHP = playerHP - mobDMG
        print ("...However the enemy hits their counter attack!")
    return MobCurrentHP, playerHP

#===============================================================================
#Room Functions:
  #Each room handles the display of text for that room, as well as the stats of any enemy you encounter
  #and any items or equipment to be found there
#-------------------------------------------------------------------------------
def room1():
    #Entrance
    global currentLocation
    global enter1
    currentLocation = 1
    print (currentLocation)

    if enter1 == 0:
        print ("Four large doors of gleaming black metal dominate the four corners of this small chamber.")
        print ("You recognise one of the doors as the entrance to the complex by its lack of green glow.")
        print ("No matter what you attempt this door will not open.")
        print ("If there is an exit to this place it lies beyond these three active doors.")
        print ("")
        os.system("pause")
        print("")

        Options()
        print ("1. There is a Green Door to the West")
        print ("2. There is a Green Door to the South")
        print ("3. There is a Green Door to the East")
        print ("")

        move = 0
        move = validateNum(move,1,3)
        if move == 1:
            room3()
        elif move == 2:
            room4()
        elif move == 3:
            room2()

    else:
        os.system("cls")
        print ("Return Text")
        Options()
        print ("1. There is a Green Door to the West")
        print ("2. There is a Green Door to the South")
        print ("3. There is a Green Door to the East")
        move = 0
        move = validateNum(move,1,3)
        if move == 1:
            room3()
        elif move == 2:
            room4()
        elif move == 3:
            room2()
#-------------------------------------------------------------------------------
def room2():
    #Armoury
    #Contains the Pistol
    global currentLocation
    currentLocation = 2
    print (currentLocation)
    global playerDMG, playerAccuracy, playerCrit
    global enter2

    os.system("cls")

    if enter2 == 0:
        print("As you walk into the room bright lights burst into life above your head.A deep alien voice booms above your head")
        print("and your suit’s translation program starts up and immediately displays an error.  This language is apparently")
        print("unknown to all of discovered space, the thought of which sends chills down your spine.")
        print(" ")
        os.system("pause")
        print("")
        print("The voice stops and you flinch as hundreds of compartments fold out of the before featureless wall with a grand")
        print("chorus of thunks.  In the silence that follows, having determined the room wasn’t trying to kill you, you check the")
        print("compartments to find them all empty bar one in the corner which contains what is instantly recognisable as a pistol,")
        print("though it's not a make you recognise.")
        print("")

        if playerDMG < 15:
            print("You take the pistol, the feel of an actual weapon in your hands already making you feel safer.  If you were to")
            print("encounter something now, maybe you could avoid dying an immediate death.")
            print("")
            playerDMG = 25
            playerAccuracy = 8
            playerCrit = 19


        elif playerDMG >=15:
            print("You decide that your current weapon is better than this sorry abandoned pistol.  You leave it in its compartment and")
            print("continue on.")
            print("")

        Options()
        print("")


        print("1. There is a Green door to the West ")
        print("2. There is a Green door to the South ")
        print ("Where do you wish to go?")

        enter2 = 1
        print (enter2)
        move = 0
        move = validateNum(move,1,2)
        if move == 1:
            room1()
        else:
            room6()

    else:
        print ("You have been here")
        print("1. There is a Green door to the West ")
        print("2. There is a Green door to the South ")

        move = 1
        move = validateNum(move,1,2)

        if move == 1:
            room1()
        else:
            room6
#-------------------------------------------------------------------------------
def room3():
    #Equipment Bay
    #Contains the Breach Spawn encounter
    global currentLocation, MobCurrentHP, MobMaxHP, mobAccuracy, mobCrit, mobDMG, AttackPreference1, AttackPreference2
    currentLocation = 3

    os.system("cls")

    print("As the door slides open, it reveals a pitch black room.  There is a sound of something whirring and crackling")
    print("seemingly emanating from the back of the room, but you cannot identify the source as what little of the room")
    print("appears to be strewn with debris and machinery and obscures your view.")
    print("")
    os.system("pause")
    print("")
    print("Then you become of the sound of dripping water, then a grunting sound so soft you almost mistook it for your own")
    print("breath.  The hairs on the back of your neck raise and you feel a sense of incredible dread.")
    print("")
    os.system("pause")
    print("")
    print("The light at your back reminds you a few step backwards, and the door would slide shut and return you to safety")
    print("However if you are to find a way out of this place, you will have to search every corner of this place.")
    print("")
    os.system("pause")
    print("")
    print("Should you swallow your fear and advance, or retreat for now? ")
    print("")

    print("1. Advance")
    print("2. Retreat")

    MobCurrentHP = 75
    MobMaxHP = 75
    mobAccuracy = 10
    mobCrit = 19
    mobDMG = 40
    AttackPreference1 = 2
    AttackPreference2 = 2


    choice = 0
    choice = validateNum(choice,1,2)

    if choice == 1:
        if playerDMG > 10:
            Combat()
        else:
            print("GAME OVER")
            print("")
    elif choice == 2:
        print("You retreat...")
        print("")
        room1()
#-------------------------------------------------------------------------------
def room4():
    #Medbay
    #Contains a First Aid kit
    global enter4
    global currentLocation
    global heal
    currentLocation = 4

    os.system("cls")

    if enter4 ==0:
        print("This room is well lit and consists of a smaller chamber separated by a low wall, from the larger chamber which")
        print("appears to be filled with regularly spaced rectangular objects, each of which is surrounded by alien machinery.  More ")
        print("such machinery hangs from the ceiling, all of which appears to be completely inert but glows with a soft green light.")
        print("")
        os.system("pause")
        print("")
        print("Exploring the main chamber fully reveals a small grey box tucked into one corner.  Upon closer examination the box ")
        print("springs open revealing various needles, sprays and other items that normally belong in a first aid kit.")
        print("")
        os.system("pause")
        print("")
        print("A band of blue light emits from the box and sweeps over your body and your suit is suddenly receives a transmission ")
        print("from what appears to be the box currently resting in your arms.")
        print("")
        os.system("pause")
        print("")
        print("The transmission does not require translation and informs you it is indeed a first aid kit.   Upon closing the box again ")
        print("it folds into itself, rapidly reducing in size until it is a thin grey square in the palm of your hand.")
        print("")
        os.system("pause")
        print("")
        print("Considering the layout of the room, what you realise are beds and the fact the room contained a first aid kit you ")
        print("reason that this room was some sort of medical bay.")
        print("")
        os.system("pause")
        print("")
        print("Disregarding how an alien machine managed to communicate with your suit without translation you tuck the folded ")
        print("first aid kit into one of your suit’s pockets, hoping you will have no need to use it before escaping this place.")

        heal = heal +1
        enter4 =1

        Options()
        print("")

        print("")
        os.system("pause")
        print("")
        print("You notice one of the doors leading from here casts a blue light different from the green doors you have encountered ")
        print("before.")



        while True:
            print("1.There is a green door to the North")
            print("2.There is a green door to the East")
            print("3.There is a blue door to the West")
            print("What do you do?")

            move =0
            move = validateNum(move,1,3)
            if move ==1:
                room1()
            elif move ==2:
                room6()
            else:
                if enter5 ==1:
                    room7()
                else:
                    print("You approach the door, but it does not respond. Since its a different colour from the other green doors you have")
                    print("encountered so far, you reason there must be some sort of key you will need before you can open this door.")
                    print("Shrugging, you turn to consider your other options.")
#-------------------------------------------------------------------------------
def room5():
    global playerDMG, playerAccuracy, playerCrit
    global enter5
    global currentLocation
    currentLocation = 5

    os.system("cls")

    if enter5 == 0:
        print ("")
        print ("Opening the door to this room you are briefly blinded by the bright light thrown from the powerful emitters in the ceiling.")
        print ("After your eyes adjust you discover what appears to be a fairly small storage room filled with tall shelves that reach the ceiling.")
        print ("Locked metal boxes that emit a soft red right mostly lost in the bright light from above litter the ground level of the room.")
        print ("")
        os.system("pause")
        print ("")
        print ("Considering the various dents on the floor and on the boxes that cover it,")
        print ("as well as a complete lack of boxes on the upper shelves,")
        print ("it appears that something had at some point knocked them to the ground.")
        print ("Whether it was the monster you encountered in the room previous or something else you are unsure.")
        print ("")
        os.system("pause")
        print ("")
        print ("However upon searching the room further you discover one of the boxes was so damaged")
        print ("its lid had sprung open and spilled its contents onto the floor which appeared to")
        print ("contain what was recognisably a shotgun and an important looking card shaped object which glows with a blue light")
        print ("intense enough to show clearly in the ambient light.")
        print ("")
        os.system("pause")
        print ("")
        print ("You immediately pocket the blue card, it looked important after all,")
        print ("before turning your attention to the rest of the unfortunate box’s contents.")
        print ("")
        os.system("pause")
        print ("")

        if playerDMG < 70:
            print ("You lift up the shotgun and it briefly glows in your hands,")
            print ("before automatically adjusting the length of the stock and position of the sight before beeping once more.")
            print ("It sits comfortably in your arms as if it had been designed for you,")
            print ("and it's reliable weight inspires a growing hope you might actually be able to make it out of this place alive.")
            print ("")

            playerDMG = 70
            playerAccuracy = 6
            playerCrit = 18

        else:
            print ("You decide to leave the shotgun where it is,")
            print ("judging your current weapon to be a better bet for escaping this place alive.")
            print ("")
            print ("There is a Green Door to the North")
            print ("")
            print ("What do you do?")
            print ("")

            Options()
            print ("1. There is a Green Door to the North")
            move = 0
            move = validateNum(move,1,1)
            if move == 1:
                room3()

    else:
        print ("You are once again blinded by the bright lights of the small store room.")
        print ("All you can find here is the fallen boxes and the bare shelves that once held them.")
        print ("The only door leading from this room is the one through which you entered.")
        print ("Wondering why you bothered to return here, you consider your single available option.")
        print ("")
        print ("There is a Green Door to the North")
        print ("")
        print ("What do you do?")
        print ("")

        Options()

        print ("There is a Green Door to the North")
        move = 0
        move = validateNum(move,1,1)

        if move == 1:
            room3()





#-------------------------------------------------------------------------------
def room6():
    #Checkpoint
    #Contains the Sub-Machinegun
    #Drone Walker
    global enter6, playerDMG, playerAccuracy, playerCrit, mobDMG, MobCurrentHP, MobMaxHP, mobCritDMG, mobCrit,mobAccuracy, AttackPreference1, AttackPreference2
    global currentLocation
    currentLocation = 6

    os.system("cls")

    MobCurrentHP = 25
    mobDMG = 36
    mobAccuracy = 9
    mobCritDMG = 1.45
    mobCrit = 20
    AttackPreference1 = 1
    AttackPreference2 = 1

    if enter6 == 0:
        print ("The door slides open smoothly and you are immediately greeted with a hail of weapon’s fire.")
        print ("A clearly robotic humanoid figure holding a submachine gun has it trained on you and is firing a steady stream of bullets you only ")
        print ("")
        os.system("pause")
        print("")
        print ("Glancing back into the room you can see the robot has good cover behind a pile of metal boxes, which it leans over to release another burst of shots at you that you feel hiss through the air near your face.")
        print ("You immediately lean back into cover, and assess your options")
        print("")
        os.system("pause")
        print ("")


        if playerDMG < 25:
            print ("Without a ranged weapon of your own there is no way to get close without being shot.")
            print ("If you want to explore this room you are going to need to find a gun of your own and deal with that robot somehow.")
            print("")
            room6()
        else:
            print ("You decide it’s time for a firefight.  You draw your weapon and lean round the door frame, ready to fire.")
            print ("")
            Combat()

        print ("Finally, you land a clean hit on the robot’s head and its return fire ends abruptly.")
        print ("Shortly after you hear the sound of metal crashing into metal as the robot disappears from view.")
        print ("Carefully you advance into the room, and lean over the boxes the robot was using as cover.")
        print ("")
        os.system("pause")
        print("")
        print ("You confirm the robot is indeed “dead,” but sink a few more rounds into it just to be sure, and only then do you relax enough to examine the rest of the room.")
        print ("")

        if playerDMG < 45:
            print ("But not before you grab the robot’s gun, discovering it to be a Submachine Gun of a curious shape.")
            print ("It beeps and automatically folds out into a more conventional form which sits snugly between your arms and shoulder when you aim it.")
            print ("")
            os.system("pause")
            print("")
            print ("A holographic sight pops out as you do, bathing the world through its lens in a high contrast yellow.")
            print ("Satisfied you lower your new gun and resume examining the room.")
            print ("")
            os.system("pause")
            print("")
        playerDMG = 45
        playerAccuracy = 7
        playerCrit = 19

        print (playerDMG)

        print ("This room appears to be some sort of reception area or checkpoint.")
        print ("A pile of what you had assumed to be boxes but now appear to be some sort of deployable cover")
        print ("form a defensive position in the centre of the room which it’s only inhabitant was using only moments before.")
        print ("")
        os.system("pause")
        print("")
        print ("Behind another more permanent looking position at the back of the room lies a large door")
        print ("which glows a deep blue at odds with the other green doors you have encountered so far.")
        print ("")
        os.system("pause")
        print("")
        print ("The rest of the room is starkly empty, but telltale marks and trails on the floor")
        print ("suggest whatever had been in this room has since been moved elsewhere, or taken.")
        print ("")
        os.system("pause")
        print("")

        Options()
        print("")

        print ("1. There is a Green door to the West")
        print ("2. There is a Green door to the East")
        print ("3. There is a Blue door to the South")
        print ("")
        print ("What do you do?")

        enter6 = 1

        move = 0
        move = validateNum(move,1,3)

        if move == 1:
            room4()
        elif move == 2:
            room2()
        elif move == 3:
            room8()


    else:
        print ("You return to the empty checkpoint.  The large room is eerily silent, broken only by the tapping of your boots on the metal floor.")
        print ("It also remains as empty as the last time you visited it.")
        print("With a vague sense of unease you turn to consider the three doors leading from the room.")
        print("")
        os.system("pause")
        print("")

    Options()
    print("")

    print ("1. There is a Green door to the West")
    print ("2. There is a Green door to the East")
    print ("3. There is a Blue door to the South")
    print ("")
    print ("What do you do?")

    enter6 = 1

    move = 0
    move = validateNum(move,1,3)

    if move == 1:
        room4()
    elif move == 2:
        room2()
    elif move == 3:
        room8()

#-------------------------------------------------------------------------------
def room7():
    global playerDMG, playerAccuracy, playerCrit
    global MobCurrentHP, MobMaxHP, mobAccuracy, mobCrit, mobDMG
    global enter7
    global currentLocation
    currentLocation = 7

    os.system("cls")

    if enter7 == 0:
        print ("The blue door slides open smoothly as you approach, revealing a dimly lit room containing a constellation of lights.")
        print ("As your eyes adjust the room is clearly filled with computers of some sort.")
        print ("Lights blink on and off, change colours and a soft humming sound permeates the air while screens display information in a format or language you do not recognise.")
        print ("")
        os.system("pause")
        print ("")
        print ("Advancing further into the room, weaving through the rows and banks of computers and equipment,")
        print ("you notice what appears to be a outside view camera on one of the monitors displaying the surface of the planet you are on.")
        print ("A cloud of dust blows past the camera and the sparse vegetation bends in the wind.")
        print ("")
        os.system("pause")
        print ("")
        print ("Below the monitor seems to be some sort of orb affixed to the wall,")
        print ("its shape and proximity leading you to believe it might be some sort of device for manipulating the camera.")
        print ("You reach for it, and the moment your fingers touch it a deafening sound makes you snatch your hand back.")
        print ("The sound continues and is unmistakably an alarm.")
        print ("")
        os.system("pause")
        print ("")
        print ("All the lights in the room change to an ominous red,")
        print ("the monitors now displaying a warning clear enough you do not need to know the language to understand.")
        print ("")
        os.system("pause")
        print ("")
        print ("A violent hissing behind you makes you spin round just to see a hidden compartment in the wall slam open,")
        print ("revealing a huge humanoid figure.  Nearly 2 meters tall and clearly robotic,")
        print ("it hefts a dangerous looking rifle and trains it on you.")
        print ("")
        os.system("pause")
        print ("")
        print ("You dive for cover the moment it opens fire only barely reaching safety in time.")
        print ("Breathing heavily, panic spurred on by the still wailing alarm filling your mind,")
        print ("you draw your weapon and prepare for a fight.")
        print ("")
        os.system("pause")
        print ("")

        MobCurrentHP = 150
        MobMaxHP = 150
        mobAccuracy = 8
        mobCrit = 19
        mobDMG = 44
        AttackPreference1 = 3
        AttackPreference2 = 1

        Combat()

        print ("")
        print ("Your shot hits the robot’s shoulder and its arm is thrown back only barely still attacked.")
        print ("The rifle it held spins out of its grasp and clatters to floor, sliding several metres away.")
        print ("The robot lurches towards cover but you fire again this time scoring a hit on its neck causing its head to separate from its shoulders.")
        print ("The alarm abruptly ends.")
        print ("")
        os.system("pause")
        print ("")
        print ("The lurch becomes a fall and the robot crashes to the ground, the damaged arm finally separating and skidding a few additional few meters.")
        print ("Shortly after the monitors and lights in the room return to normal, and only then do you let out a heavy sigh of relief.")
        print ("")
        os.system("pause")
        print ("")
        print ("Once you catch your breath, you decide to investigate the fallen robot.")
        print ("")
        os.system("pause")
        print ("")

        print ("Retrieving the robot’s gun from the computer bank it had slid under, you heft its great weight onto your shoulder.")
        print ("You almost discard the weapon right then because it is nearly impossible to aim, but it begins humming and somehow grows lighter.")
        print ("It also subtly changes shape, almost like it had briefly became liquid and reformed to perfectly fit your grasp.")
        print ("")
        os.system("pause")
        print ("")
        print ("With a final beep the rifle stops changing, and you are left with a weapon light as a feather that feels like it was made for you.")
        print ("When you try aiming the weapon it pulls towards whatever you aim at and remains dead steady, but freely allows you to switch targets.")
        print ("It gives you an uncanny feeling, like this gun can read your mind.")
        print ("")
        os.system("pause")
        print ("")
        print ("Regardless, this is definitely the most advanced weapon you have encountered so far")
        print ("and probably your best bet of surviving whatever is left in this place.")
        print ("")
        os.system("pause")
        print ("")

        playerDMG = 100
        playerAccuracy = 5
        playerCrit = 17

        print ("Another search of the downed robot reveals a red keycard similar to the blue card you found earlier.")
        print ("You pocket it and return to searching the room.")
        print ("")
        os.system("pause")
        print ("")
        print ("Returning to the console you touched to trigger the alarm you find it once again displaying a feed of the outside world.")
        print ("Gingerly you touch the control again, and the camera swings to one side. ")
        print ("")
        os.system("pause")
        print ("")
        print ("Manipulating it further you get a good view of the barren waste above you and the upper parts of the ruins you came here to investigate,")
        print ("which you realise now must be the upper levels of the installation you are standing in.")
        print ("")
        os.system("pause")
        print ("")
        print ("In the distance, you can barely see the ship you arrived in, its guidance lights still blinking in the billowing dust.")
        print ("You feel an intense relief, followed by a sharp pang of guilt.")
        print ("Your escape from this twisted place is in view, but the fact it remains confirms your worst fears about the rest of your team.")
        print ("")
        os.system("pause")
        print ("")
        print ("You are the sole survivor.  With this fact weighing heavily on your mind, you turn to leave.")
        print ("")
        os.system("pause")
        print ("")
        print ("There is a Blue Door to the East")
        print ("")
        print ("What do you do?")
        print ("")

        enter7 = 1

        Options()
        print ("1. There is a Blue Door to the West")
        move = 0
        move = validateNum(move,1,1)
        if move ==1:
            room4()

    else:
        print ("Return Text")

    Options()

    print ("1. There is a Blue Door to the West")
    move = 0
    move = validateNum(move,1,1)

    if move == 1:
        room4()


#-------------------------------------------------------------------------------
def room8():
    global playerHP, playerMaxHP
    global enter8
    global currentLocation
    currentLocation = 8
    if enter8 == 0:
        print ("")
        print ("As the door hums open you are confronted with a wall of dark gleaming metal.")
        print ("Confused you take a step back and realise the wall does not cover the entirety of the doorway.")
        print ("Closer inspection reveals its not a wall at all, but some sort of metal object knocked against the doorframe.")
        print ("")
        os.system("pause")
        print("")
        print ("You heave against it and succeed in toppling the object, creating an opening into the room.")
        print (" Inside the room many more tall roughly rectangular objects stand,")
        print ("doing their best impression of a forest formed from dark gleaming metal.")
        print ("The face of each rectangle bears a glowing red symbol which provides the only light in the room,")
        print ("casting ominous murky red shadows all about the room.")
        print ("")
        os.system("pause")
        print("")
        print ("Stepping inside the room, you find a clearing of sorts in the forest of objects,")
        print ("and what appears to be a pile of rubble at the edge of the room.")
        print ("Investigating the rubble you discover that it is more of the same rectangular objects, which somehow must have been flung against the wall.")
        print ("What possibly could exert this amount of force, and the fact it may be somewhere close by fills you with dread.")
        print ("")
        os.system("pause")
        print("")
        print ("Just as you were about to turn away, a glint catches the corner of your eye and you spin back around.")
        print ("All is still, but you catch sight of the light again, somewhere in the pile of collapsed objects.")
        print ("You dig around through the pile, heaving away some of the debris, and discover a silver orb embossed with green light emitting material.")
        print ("")
        os.system("pause")
        print("")
        print ("You gingerly pick it up and thankfully nothing happens.")
        print ("You turn it in your hands and find the green detailing converges around a circular protrusion you can only assume is a button. ")
        print ("")
        os.system("pause")
        print("")
        print ("Suddenly your suit receives a communication, the source of which appears to be the orb you are holding.")
        print ("You accept the communication and an alien voice immediately rings through your suit’s sound system,")
        print ("prompting you to quickly struggle to lower the volume to a less deafening level.")
        print ("")
        os.system("pause")
        print("")
        print ("You listen to voice intently but none of the words match your memory, or that of your suit’s translation program,")
        print ("however the message also comes with attached images which you browse through.")
        print ("")
        os.system("pause")
        print("")
        print ("From the images you conclude the device is some sort of personal protective equipment.")
        print ("While the device was clearly not designed for someone of your species,")
        print ("it does appear to be flexible enough to use judging from the variety of things the image shows the item being used on,")
        print ("which include a variety of inanimate objects you cannot identify and what appears to be a vehicle of some sort.")
        print ("")
        os.system("pause")
        print("")
        print ("There is also an image of a roughly humanoid form, despite the additional two legs and arms, using the device.")
        print ("The image directs the alien user to hold the button down and release it pointed at what you assume is it’s head.")
        print ("")
        os.system("pause")
        print("")
        print ("Figuring there is little to lose in trying the device, you end the clearly pre-recorded transmission cutting the alien voice off,")
        print ("and press down the button on the orb.  Lifting it to eye level you point the face of the orb at yourself and release the button.")
        print ("")
        os.system("pause")
        print("")
        print ("Immediately it springs from your grasp and floats in the air in front of you,")
        print ("and rapidly disintegrates into a cloud of silver particles which move towards your head.")
        print (" You resist the urge to take a step back and instead close your eyes.")
        print ("For a few moments you feel your body being tugged starting from your helmet, working its way down your body until it reaches your boots.")
        print ("")
        os.system("pause")
        print("")
        print ("You open your eyes and look at your suit.  It is recognisably your suit, but it looks as if armoured plates had been installed in various places.")
        print ("Feeling around these reinforcements seem to cover vital areas, key arteries in your legs, vital organs and the like.")
        print ("")
        os.system("pause")
        print("")
        print ("Attempting to touch one of these plates, your hand encounters resistance in the air around them as if some invisible force was pushing against you,")
        print ("but eventually eases up and allows your hand to progress forward.")
        print ("You give it an experimental whack and your hand hits a wall of force and a wave of shimmering energy flows over the point you hit.")
        print ("")
        os.system("pause")
        print("")
        print ("Your suit now seems to be equipped with some sort of defensive force field as well.")
        print ("Real hope blooms in your chest, with this new suit you stand a very real chance of surviving this place.")
        print ("")
        os.system("pause")
        print("")
        print ("You quickly search the area again, but finding nothing you decide to move quickly on as you do not know how long your new suit’s power might last.")
        print ("If you are to escape, it will need to be as soon as possible.  You turn to consider the available doors.")
        print ("")
        print ("What do you do?")
        print ("")

        playerHP = 150
        playerMaxHP = 150
        enter8 = 1

        Options()
        print ("1. There is a Blue Door to the North")
        print ("2. There is a Green Door to the West")

        move = 0
        move = validateNum(move,1,2)
        if move == 1:
            room6()
        elif move == 2:
            room9()

    else:
        print ("You return to the room with the forest of dark rectangular objects, finding it much as you had left it.")
        print ("The dim red lightning still gives you an ominous feeling, but the room is otherwise silent.")
        print ("")
        os.system("pause")
        print("")
        print ("You have another look around the room, and try to dig through the pile of rubble to see if you can find anything of interest but return nothing of interest.")
        print ("While the rectangular objects are clearly containers of some sort you cannot discern how to open them.")
        print ("")
        os.system("pause")
        print("")
        print ("Giving up you decide to stop wasting your time and move on.")
        print ("")
        print ("What do you do?")
        print ("")

        Options()
        print ("1. There is a Blue Door to the North")
        print ("2. There is a Green Door to the West")

        move = 0
        move = validateNum(move,1,2)
        if move == 1:
            room6()
        elif move == 2:
            room9()


#-------------------------------------------------------------------------------
def room9():
    global enter9, currentLocation
    global heal
    global mobAccuracy, mobCrit, mobDMG, MobCurrentHP, MobMaxHP,MobCurrentHP, AttackPreference1, AttackPreference2
    currentLocation = 9
    if enter9 == 0:
        print ("With a hiss the door starts opening slowly, then catches before slamming open with a loud crash.")
        print ("With no idea what the racket you just made might have attracted,")
        print ("you move into the cover of the door frame and peer round into the now revealed room.")
        print ("")
        os.system("pause")
        print("")
        print ("You are presented with a huge corridor with many adjoining doors set at regular intervals, each of which cast a faint red glow.")
        print ("Sets of stairs and connecting walkways lead to three more levels of doors.")
        print ("However at the very end of the corridor on the opposite wall a telltale blue light suggests there is a blue door there,")
        print ("however you cannot see it from your current angle.")
        print ("")
        os.system("pause")
        print("")
        print ("You glance at the other side of the doorframe and consider shifting your position to get a better angle")
        print ("but you freeze as you look back into the corridor and see a huge humanoid figure standing at the opposite end.")
        print ("Your blood turns to ice, you heard nothing and had only glanced away yet there it stands, clearly facing you.")
        print ("")
        os.system("pause")
        print("")
        print ("Your mind screams at you to draw your weapon, but your body remains frozen with fear and shock at the impossibility of the creature’s presence.")
        print ("It stands at a height at least three times your size and a pair of huge wings sprout from its waist reaching high above its head")
        print ("with the tips touching the floor.  In its arms it carries a huge object that casts a green light.")
        print ("")
        os.system("pause")
        print("")
        print ("It takes a step towards you and your trance is broken by the sudden sound of an alarm and a deafening clattering")
        print ("as an opening you had noticed in the roof slides open.  A huge bulk of gleaming metal falls suddenly from the opening and races towards the floor.")
        print ("")
        os.system("pause")
        print("")
        print ("An explosion of sound and fire erupts from the room as thrusters ignite and slow the metal object’s decent")
        print ("just before it collides with the floor, bringing it to a gentle stop before it rapidly expands,")
        print ("taking the form of a huge quadrupedal robot.  Green lights blaze along its body, pulsing with energy.")
        print ("An alien voice bellows from the robot as weaponry explode from concealed hardpoints all over its body,")
        print ("the green lights flaring red as it immediately opens fire on the humanoid shape.")
        print ("")
        os.system("pause")
        print("")
        print ("Moving with incredible swiftness the humanoid shape explodes into action in response,")
        print ("dodging the first volley of fire by leaping into the air with a powerful flex of its wings,")
        print ("and returning its own barrage from what you realise is a huge gun of some sort.")
        print ("The streaks of green light it fires roar through the air and vaporise all but one of the robot’s legs.")
        print ("")
        os.system("pause")
        print("")
        print ("However a storm of seeking missiles from above takes the humanoid shape by surprise,")
        print ("and black blood splatters through the room as the resulting explosions mutilate one of the creature’s wings.")
        print ("With a roar of pain it falls to ground, still returning fire.  The robot is left with one half of its body pulverised,")
        print ("but the other half continues firing.")
        print ("")
        os.system("pause")
        print("")
        print ("Growling the creature raises an arm a shield of green energy springs forth,")
        print ("deflecting the barrage of attacks as it backs away towards the blue door.  It slides open behind it and it retreats inside.")
        print ("")
        os.system("pause")
        print("")
        print ("The robot whines, and struggles to move forwards with its one remaining leg but is unsuccessful.")
        print ("One of its remaining thrusters engages and lifts one side of the robot slightly,")
        print ("but it collapses as the thruster coughs and cuts out.")
        print ("")
        os.system("pause")
        print("")
        print ("The robot beeps a few times, and the red light fades back to green.")
        print ("A hatch opens on its back and a few smaller robots emerge, and begin tending to the larger robot,")
        print ("sparks flying as parts are welded, removed and repaired.")
        print ("")
        os.system("pause")
        print("")
        print ("You exhale, realising you had been holding your breath and cowering by the door frame,")
        print ("and carefully stand up making sure to avoid making any noise.")
        print ("Judging by the robots you have encountered previously in this place you highly doubt this one will be any friendlier.")
        print ("And while damaged currently, the smaller robots are repairing the thing with incredible speed.")
        print ("")
        os.system("pause")
        print("")
        print ("If you want to have any chance of exploring further,")
        print ("you are going to need to take it out now while it has been weakened.")
        print ("Gathering your resolve you draw your weapon and prepare to open fire.")
        print ("")

        mobAccuracy = 6
        mobCrit = 18
        mobDMG = 66
        MobCurrentHP = 250
        MobMaxHP = 250
        AttackPreference1 = 1
        AttackPreference2 = 3

        Combat()

    else:
        print ("Return Text")




    #Habitat Access
    #Contains the Drone Mother encounter
    #Contains a Health Kit

#-------------------------------------------------------------------------------
def room10():
    global enter10, currentLocation
    global mobAccuracy, mobCrit, mobDMG, MobCurrentHP, MobMaxHP, AttackPreference1, AttackPreference2

    os.system("cls")

    print ("With a great deal of trepidation you stand before the Red door the demonic figure had retreated through.")
    print ("You recall the speed with which the creature had moved, and the amount of damage it had done to the huge drone from before with only two bursts.")
    print ("Even though the demon might be injured, an confrontation with him would easily be the most dangerous encounter you have had in this place yet.")
    print ("")
    os.system("pause")
    print ("")
    print ("You hesitate at the thought.")
    print ("Perhaps it would be best to retreat for now, explore what you can fully, before taking this creature on.")
    print ("You will need every advantage you can get.")
    print ("")

    print ("1. Advance")
    print ("2. Retreat")
    choice = 0
    choice = validateNum(choice,1,2)
    if choice == 1:
        print ("")
        print ("You calm your nerves with a deep breath.")
        print ("The only way out of this place is to keep moving forward no matter the odds.")
        print ("The door sweeps open as you approach.")
        print ("")
        os.system("pause")
        print ("")
        print ("You step inside a colossal room easily 400 metres long, 200 metres wide and as many tall and filled with the racket of machines in operation.")
        print ("The door you entered from is several metres above the actual floor of the room, as you are standing on an elevated walkway affixed to the wall.")
        print ("")
        os.system("pause")
        print ("")
        print ("You view from above gives you a good view of the state of the room.")
        print ("You realise that it is so densely filled with boxes, parts, pipes, vehicles and all sorts of equipment")
        print ("that navigating the room presents a substantial challenge, with the arrangements of these objects resulting in a maze of sorts filled with dead ends.")
        print ("")
        os.system("pause")
        print ("")
        print ("You remember the demonic form from before.  This room might also be a death trap.")
        print ("")
        os.system("pause")
        print ("")
        print ("However you have no other choice.")
        print ("You gather your resolve and make your way down the walkways adjoining stairs to the floor of the room proper")
        print ("But just as you were about to set foot there, you catch a glint of violet light in the corner of your eye.")
        print ("")
        os.system("pause")
        print ("")
        print ("Without a second thought you dive forwards in a clumsy evasive roll.")
        print ("A roaring sound followed by a wave of intense heat and blinding violet light passes through the space you had just occupied.")
        print ("You scramble off the floor and sprint into the nearby cover a huge container.")
        print ("")
        os.system("pause")
        print ("")
        print ("You spy the culprit, the same demonic form now cast in dim violet light")
        print ("standing in the cover of another huge container not dissimilar from the one you now hide behind.")
        print ("It would have been impossible to see him from where you had entered the room, and the deafening racket")
        print ("of the room made only worse by your proximity to the machines generating it prevented you from hearing him fire that shot.")
        print ("")
        os.system("pause")
        print ("")
        print ("A cold sweat runs down your back, as you realise just how close you were to death.")
        print ("And then the demonic figure moves, stepping easily out of the shade and into the dim light of the room.")
        print ("A twisted grin on his face, he raises his gun and fires another burst at you.")
        print ("")
        os.system("pause")
        print ("")
        print ("You dive away from your cover further into the room, just as the box you had been hiding behind explodes into a rain of shrapnel.")
        print ("If you want to stay alive, you have to keep on the move.")
        print ("With the feeling that you have just become a hunted animal, you draw your weapon and get ready for the hardest fight you have had yet.")
        print ("")
        os.system("pause")
        print ("")

        MobCurrentHP = 375
        MobMaxHP = 375
        mobDMG = 70
        mobAccuracy = 5
        mobCrit = 17
        AttackPreference1 = 3
        AttackPreference2 = 2

        Combat()

        print ("")
        print ("Your latest volley of fire is met by another of the demonic figures.")
        print ("You try to move quickly from your current cover, but you are already gasping for breath.")
        print ("You are just a second too slow, and the explosion catches you.")
        print ("Shrapnel rains over your body and, while your suit prevents most of the damage, pain thunders through your mind as you crash into the ground hard.")
        print ("")
        os.system("pause")
        print ("")
        print ("You struggle to raise yourself and turn around, only to see the demonic figure standing right in front of you.")
        print ("He grabs you around the neck with his free hand and lifts you off the ground easily.  Then he laughs, and throws you forwards.")
        print ("")
        os.system("pause")
        print ("")
        print ("You slam into a huge cylinder and the pain almost makes you black out.")
        print ("Through your dimmed vision you can see the demonic figure approaching you, gun raised.")
        print ("Deciding absent mindedly you don’t want to see death approaching you turn your head to one side.")
        print ("")
        os.system("pause")
        print ("")
        print ("You note, with disembodied interest, that you seem to have landed against some sort of lifting vehicle,")
        print ("the cylinder you currently lying on being its current cargo.  The cockpit of the machine seems to glow with a green light.")
        print ("Green means… active?  And that looks suspiciously like a lever...")
        print ("")
        os.system("pause")
        print ("")
        print ("Your brain snaps back into reality, a plan formulating as adrenaline leaps you off the cylinder and you dive into the machine’s cockpit.")
        print ("The demonic figure fires at you as you do so, its shots aimed at where you had been before entering the vehicle.")
        print ("You can almost hear his growl of annoyance over the din of machines.")
        print ("")
        os.system("pause")
        print ("")
        print ("In the cockpit you slam down the lever you had spied before and leap back out of the machine.")
        print ("Its engine roars, and it smoothly accelerates to an incredible speed, straight towards the demonic figure.")
        print ("From the distance you see it raise its gun and fire at the approaching vehicle.")
        print ("Then everything turned white, as you are slammed backwards by a huge explosion.")
        print ("You collide with something and everything turns black.")
        print ("")
        os.system("pause")
        print ("")
        print ("You regain consciousness.  You don’t know how long it has been, but judging from the fact you are still alive the demon must have been less lucky.")
        print ("You struggle to your feet, every muscle of your body protesting, and survey the room.")
        print ("")
        os.system("pause")
        print ("")
        print ("The explosion wreaked even more havok than you had previously thought.")
        print ("It had thrown a large container in between you and the explosion center which probably explains why you are still alive,")
        print ("however most everything else in the room has been destroyed, including the walkway leading to the door you had entered from.")
        print ("")
        os.system("pause")
        print ("")
        print ("The room is also deathly silent, the once working machines nothing more than melted metal twisted into freakish shapes.")
        print ("")
        os.system("pause")
        print ("")
        print ("However from where you stand, a single red door at ground level is visible,")
        print ("half covered by a broken vehicle which had provided it shelter from the explosion.")
        print ("")
        os.system("pause")
        print ("")
        print ("With nowhere else to go, you approach it and it hums open.  You step through.")

        room11()
    #Engineering Bay
    #Contains the Breach Lord encounter

#-------------------------------------------------------------------------------
def room11():
    print ("")
    print ("The room is small, no more than 3 meters wide and a couple tall, and the door closes behind you.")
    print ("A panel of coloured circles lights up, with all but one of the circles turning red.")
    print ("One green circle at the very top of the panel remains green.")
    print ("")
    os.system("pause")
    print ("")
    print ("You approach it, and realise the circles are buttons.")
    print ("Considering the shape of the room and layout of the buttons, you absentmindedly wonder if the room is an elevator of sorts.")
    print ("")
    os.system("pause")
    print ("")
    print ("With nothing else you could do, you press the only green button and a feeling of inertia grabs you")
    print ("and pulls you to the floor as the room begins to accelerate upwards, you gladly accept the invitation to sit down.")
    print ("")
    os.system("pause")
    print ("")
    print ("The elevator ride continues for a few minutes, giving you time to collect yourself.")
    print ("You suppose you should feel something about having avoided death so many times in this place, but all you feel is a numbness.")
    print ("")
    os.system("pause")
    print ("")
    print ("You are alone.  Your team is dead and all your friends with it.")
    print ("You have spent all this time trying to escape, but for what?  TO what?")
    print ("What is there for you to return to?")
    print ("")
    os.system("pause")
    print ("")
    print ("The elevator stops, and the doors slide open.  You stand up and walk onwards.")
    print ("")
    os.system("pause")
    print ("")
    print ("The room you have been taken to is wide, about 50 metres or so, and the ceiling lies only an outstretched arm’s length above your head.")
    print ("Various banks of computers draw concentric semi-circles around a single elevated desk with a very alien looking chair at the centre of the room.")
    print ("Similar chairs sit in front of terminals set at regular intervals in each semi-circle.")
    print ("")
    os.system("pause")
    print ("")
    print ("The setup would look like an amphitheater if it weren’t for the collosal window each chair was facing.")
    print ("")
    os.system("pause")
    print ("")
    print ("You step forward next to the window, and look up.")
    print ("The sky stretches out above you and the planet surface extends endlessly in front of you.")
    print ("Outside.")
    print ("You have been in this place for so long the feeling of being outside feels almost alien to you.")
    print ("")
    os.system("pause")
    print ("")
    print ("But when you came here there was no such vault of glass or plasticlear.")
    print ("Only dark metal ruins.  So even this view of the outside world is likely a mirage of screens and camera projections.")
    print ("You turn away from the view.")
    print ("")
    os.system("pause")
    print ("")
    print ("You inspect the central chair and its terminal, and what you learn here shapes the future of the universe in ways you could not possibly predict.")
    print ("")
    os.system("pause")
    print ("")
    print ("By linking your suit to the machine, it teaches your suit’s computer the alien language and translates the computer’s contents for you.")
    print ("")
    os.system("pause")
    print ("")
    print ("You stand not in a ruin, but in the first Warp capable ship in the universe.")
    print ("You are currently on the bridge of the ship,")
    print ("looking out on the results of the ship’s catastrophic encounter with an unknown alien force that attacked the ship at some point in space.")
    print ("")
    os.system("pause")
    print ("")
    print ("The records on the ships computer don’t tell the whole story however.")
    print ("Two successful warp attempts are recorded with only one failure that resulted in the ship being embedded inside the planet you are currently on.")
    print ("The resulting force of its arrival decimated the surface of the planet.")
    print ("")
    os.system("pause")
    print ("")
    print ("However there is a gap in the records of the ship’s crew.")
    print ("Somewhere between the second and third warp attempt they appear to have disappeared,")
    print ("replaced instead with the monsters you have encountered on your way here and causing the ship to enter a partial lockdown.")
    print ("")
    os.system("pause")
    print ("")
    print ("Also, the warp drive remains active, and can be used at any time…")
    print ("")
    os.system("pause")
    print ("")
    print ("The events from the this point on are now common knowledge.")
    print ("")
    os.system("pause")
    print ("")
    print ("You, Arthur Cauda, used the warp drive to escape the planet, and catapult yourself into fame and fortune in civilised space.")
    print ("You were heralded as a legendary explorer, the Warp technology you discovered advanced space flight technology by several hundred years")
    print ("and earned you the adoration of adventurous souls for generations afterwards.")
    print ("")
    os.system("pause")
    print ("")
    print ("However no one ever believed you about the monsters in the dark ship.")
    print ("Either you had somehow killed them all, or the had disappeared when you used the Warp drive,")
    print ("but no evidence of their existence remained.  Nor was the mystery of the missing crew ever solved.")
    print ("")
    os.system("pause")
    print ("")
    print ("You were never happy with your wealth, and the fame chafed at your neck like a dog’s collar.")
    print ("A feeling of inescapable dread never left you and your dreams were haunted by dark demonic figures.")
    print ("")
    os.system("pause")
    print ("")
    print ("So you disappeared one day, taking your personal Warp-equipped ship with you.")
    print ("Was it to escape the visions that haunted you?")
    print ("Or was it a journey to discover what really happened aboard the Warp Ship.")
    print ("Or did you simply want to escape the attention the universe now showered upon you.")
    print ("Only you could know.")
    print ("")
    os.system("pause")
    print ("")
    print ("Soon the whole universe would know the truth, either way.")
    print ("But that is a story for another time.")
    print ("")
    os.system("pause")
    print ("")
    print ("""████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝""")

    os.system("pause")
    #The Bridge
    #GAME END

#===============================================================================
#MAIN CODE
#===============================================================================
#Start()
#intro()
#healthkit()
Combat()
#room1()
#room2()
#room3()
#room6()
#room11()
#SaveGame(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation)
#print (playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation)
#Load()
#===============================================================================
#PROGRAM END
