#===============================================================================
#CREDITS & LICENSE
#===============================================================================
#Rocket Propelled Games
#Breach: A Warped Perspective
#Chris, Finn, Roman, Liam
#===============================================================================
#IMPORTING LIBRARIES
#===============================================================================
import sys
import math
import random
import time
#===============================================================================
#INITALISING GLOBAL VARIABLES
#===============================================================================
#Player global values should be changed directly by the room functions: No need for passing them into functions
#Will make these an object instead later
playerMaxHP = 100
playerHP = 100
playerDMG = 25
playerAccuracy = 12
playerCrit = 19
playerCritDMG = 1.5
#Enemy global values like player values should be updated by the room functions as needed
#Should also become an object later
MobCurrentHP = 75
mobDMG = 40
mobAccuracy = 10
mobCrit = 19
mobCritDMG = 1.5
MobMaxHP = 75
#Tracks the number of healing kits carried
heal = 1
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
        Load(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation)
        #Runs external function for sending the player to the correct room
        Location = Location(currentLocation)
    elif choice == 3:
        sys.exit("Shutting Down")
#-------------------------------------------------------------------------------
def intro():
    #Displays the game's intro text
    print ("It's been 2 hours since you were seperated from your team.  The cave you stand in is cold and dank and musty refiltered air fills your lungs.")
    print ("")
    input("press enter to continue...")
    print ("You avoided the rockfall unscathed, but were unable to find anyone else who had, and lack the tools to dig through the rubble behind you.")
    print ("If there were any survivors you could not help them and with no where else you could go you headed deeper into the cave.")
    print ("")
    input("press enter to continue...")
    print ("You are aware of how long it has been thanks to your suit’s internal clock,")
    print ("and you have enough rations to survive a week underground, but without an exit plan you will surely die here.")
    print ("")
    input("press enter to continue...")
    print ("The cave you are walking through continues on in a straight line without deviation and with no other visible paths.  It is wide and curved with remarkable smoothness.")
    print ("You are unsure if this used to be an underground river, or was created artificially.")
    print ("")
    input("press enter to continue...")
    print ("This question is answered soon enough as you round the corner by artificial green light and what is quite clearly a very artificial door.")
    print ("")
    input("press enter to continue...")
    print ("As you approach the door, it slides open soundlessly, revealing a dark complex of metal corridors, burnt into your retinas as bright lights burst into life above you.")
    print ("The metal is a glossy dark material and is covered in irregular patterns and you are unsure if they are just a decorative texture or symbols with meaning.")
    print ("")
    input("press enter to continue...")
    print ("You have nowhere else you could go.  You step through the door and it shuts behind you with a soft hissing sound and the green light disappears.")
    print ("This door will not open again.")
    print ("")
    input("press enter to continue...")
    print ("Three more doors to the West, South and East of you activate and begin to cast a viridian glow.")
    print ("")
    input("press enter to continue...")
    print ("What do you do?")
    print ("")
    #Load the first room to begin the game
    room1()
#===============================================================================
#Player Option Functions
#-------------------------------------------------------------------------------
def Load(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation):
    #Loads all revelant global variables from an external file and moves player to the correct room
    with open("BreachSaved.txt", "r") as stats:
        stats = stats.read().split(" ")
        playerHP = stats[0]
        playerMaxHP = stats[1]
        playerDMG = stats[2]
        playerCrit = stats[3]
        playerCritDMG = stats[4]
        playerAccuracy = stats[5]
        heal = stats[6]
        enter1 = stats[7]
        enter2 = stats[8]
        enter3 = stats[9]
        enter4 = stats[10]
        enter5 = stats[11]
        enter6 = stats[12]
        enter7 = stats[13]
        enter8 = stats[14]
        enter9 = stats[15]
        enter10 = stats[16]
        enter11 = stats[17]
        currentLocation = stats[18]
        return playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation
#-------------------------------------------------------------------------------
def Location(currentLocation):
    #Used by the Load function to find the correct room function to run based on the Current Location flag
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
def healthkit():
    #Handles the usage of Health Kits.
    #Health Kits return you to your maximum HP and have one use
    global playerHP, playerMaxHP, heal, gainhealth
    if heal > 0:
        print ("1. Yes")
        print ("2. No")
        print (playerHP)
        gainhealth = 2
        gainhealth = validateNum(gainhealth,1,2)
        print(gainhealth)
        if gainhealth == 1:
            playerHP = playerMaxHP
            print("You have healed yourself")
            print (playerHP)
            heal = heal - 1
        elif gainhealth == 2:
            print("No health kit was used")
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
            healthkit()
        elif Option == 3:
            SaveGame(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation)
            print ("Game Saved")
        elif Option == 4:
            sys.exit("Shutting Down")
#-------------------------------------------------------------------------------
def SaveGame(playerHP,playerMaxHP,playerDMG,playerCrit,playerCritDMG,playerAccuracy,heal,enter1,enter2,enter3,enter4,enter5,enter6,enter7,enter8,enter9,enter10,enter11,currentLocation):
#Handles saving the game to an external file.  Only one save should be supported, saving again will overwrite the last.
    file = open("BreachSaved.txt", "w")
    file.write(str(playerHP))
    file.write(" ")
    file.write(str(playerMaxHP))
    file.write(str(" "))
    file.write(str(playerDMG))
    file.write(str(" "))
    file.write(str(playerCrit))
    file.write(str(" "))
    file.write(str(playerCritDMG))
    file.write(str(" "))
    file.write(str(playerAccuracy))
    file.write(str(" "))
    file.write(str(heal))
    file.write(str(" "))
    file.write(str(enter1))
    file.write(str(" "))
    file.write(str(enter2))
    file.write(str(" "))
    file.write(str(enter3))
    file.write(str(" "))
    file.write(str(enter4))
    file.write(str(" "))
    file.write(str(enter5))
    file.write(str(" "))
    file.write(str(enter6))
    file.write(str(" "))
    file.write(str(enter7))
    file.write(str(" "))
    file.write(str(enter8))
    file.write(str(" "))
    file.write(str(enter9))
    file.write(str(" "))
    file.write(str(enter10))
    file.write(str(" "))
    file.write(str(enter11))
    file.write(str(" "))
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
            value = int(input("Please choose your option"))
        except ValueError:
            print ("Sorry please enter a number")
            continue
        else:
            if value >= min and value <= max:
                return value
            else:
                print ("Please enter a number between",min,"and",max)
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
        print(WeightingList)
        return AttackChoice
    else:
        WeightingList = [1,2,3,Preference1,Preference1,Preference1]
        AttackChoice = random.choice(WeightingList)
        print(WeightingList)
        return AttackChoice
#-------------------------------------------------------------------------------
def PlayerAccuracyCheck(AttackResult):
  #Function for handling the player's accuracy roll and determining the result of their attack
  global playerCrit, playerAccuracy
  Roll = 0
  Roll = random.randint(1,20)
  print ("Player Rolled: ",Roll)

  if Roll >= playerCrit:
      AttackResult = "Crits"
  elif Roll >= playerAccuracy:
      AttackResult = "Hits"
  else:
      AttackResult = "Misses"
  print("The Player",AttackResult+"!")
  return AttackResult
#-------------------------------------------------------------------------------
def MobAccuracyCheck(AttackResult):
  #Function for handling the enemy's accuracy roll and determining the result of their attack
  global mobCrit, mobAccuracy
  Roll = 0
  Roll = random.randint(1,20)
  print ("Monster Rolled: ",Roll)

  if Roll >= mobCrit:
      AttackResult = "Crits"
  elif Roll >= mobAccuracy:
      AttackResult = "Hits"
  else:
      AttackResult = "Misses"
  print("The Monster",AttackResult+"!")
  return AttackResult
#-------------------------------------------------------------------------------
def Combat():
#Main combat function.  Loops until combat ends, and is in charge of calling the other combat functions
    global AttackPreference1, AttackPreference2
    playerAttackResult = ""
    mobAttackResult = ""
    fight = 1

    while playerHP > 0 or MobCurrentHP > 0:
        #Loops until either player or enemy are dead
        if playerHP <= 0:
            print ("You have died, rip in pip")
            break

        elif MobCurrentHP <= 0:
            print ("You have slain the enemy")
            break

        else:
            #Rock/Paper/Scissors combat system with additional roll-to-hit subsystem
            time.sleep(1)
            print ("")
            print (" 1. Make a Defensive Attack")
            print ("2. Make a Offensive Attack")
            print ("3. Make an Opportunistic Attack")
            print ("You have",playerHP,"HP remaining")
            print ("The enemy has",MobCurrentHP,"HP Remaining")
            print ("")
            #Using external validator for all player choices
            fight = validateNum(fight,1,3)
            playerAttackResult = PlayerAccuracyCheck(playerAttackResult)
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
                ComLose(playerAttackResult, mobAttackResult)

            elif fight == 1 and mobAttack == 3:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 1:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 2:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 3:
                ComLose(playerAttackResult, mobAttackResult)

            elif fight ==3 and mobAttack == 1:
                ComLose(playerAttackResult, mobAttackResult)

            elif fight == 3 and mobAttack == 2:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight == 3 and mobAttack == 3:
                ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult =="Crits" and mobAttackResult == "Crits":

            if fight == 1 and mobAttack == 1:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight == 1 and mobAttack == 2:
                ComLose(playerAttackResult, mobAttackResult)

            elif fight == 1 and mobAttack == 3:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 1:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 2:
                ComDraw(playerAttackResult, mobAttackResult)

            elif fight ==2 and mobAttack == 3:
                ComLose(playerAttackResult, mobAttackResult)

            elif fight ==3 and mobAttack == 1:
                ComLose(playerAttackResult, mobAttackResult)

            elif fight == 3 and mobAttack == 2:
                ComWin(playerAttackResult, mobAttackResult)

            elif fight == 3 and mobAttack == 3:
                ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Misses" and mobAttackResult == "Misses":
            print ("Both Miss")
            continue

        elif playerAttackResult == "Hits" and mobAttackResult == "Misses":
            ComWin(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Hits" and mobAttackResult == "Crits":
            ComDraw(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Misses" and mobAttackResult == "Hits":
            ComLose(playerAttackResult, mobAttackResult)

        elif playerAttackResult == "Crits" and mobAttackResult == "Hits":
            ComDraw(playerAttackResult, mobAttackResult)
#-------------------------------------------------------------------------------
def ComWin(playerAttackResult, mobAttackResult):
    #Combat win scenario: Player deals damage, Enemy does not
    global MobCurrentHP, playerDMG, playerCritDMG
    if playerAttackResult == "Crits":
        MobCurrentHP = MobCurrentHP - (round(playerDMG * playerCritDMG))
        print("You Critically Hit!")
    else:
        MobCurrentHP = MobCurrentHP - (playerDMG)
    return MobCurrentHP
#-------------------------------------------------------------------------------
def ComLose(playerAttackResult, mobAttackResult):
    #Combat Lose scenario: Enemy deals damage, Player does not
    global playerHP, mobDMG, mobCritDMG
    if mobAttackResult == "Crits":
        playerHP = playerHP - (round(mobDMG * mobCritDMG))
        print("The mob Critically Hit!")
    else:
        playerHP = playerHP - mobDMG
    return playerHP
#-------------------------------------------------------------------------------
def ComDraw(playerAttackResult, mobAttackResult):
    #Combat Draw scenario: Both parties deal damage
    global MobCurrentHP, mobDMG, playerDMG, playerHP, playerCritDMG, mobCritDMG
    #Resolving player damage
    if playerAttackResult == "Crits":
        MobCurrentHP = MobCurrentHP - (round(playerDMG * playerCritDMG))
        print("You Critically Hit!")
    else:
        MobCurrentHP = MobCurrentHP - (playerDMG)
    #Resolving enemy damage
    if mobAttackResult == "Crits":
        playerHP = playerHP - (round(mobDMG * mobCritDMG))
        print("The mob Critically Hit!")
    else:
        playerHP = playerHP - mobDMG
    return MobCurrentHP, playerHP
#===============================================================================
#Room Functions:
  #Each room handles the display of text for that room, as well as the stats of any enemy you encounter
  #and any items or equipment to be found there
#-------------------------------------------------------------------------------
def room1():
    #Entrance
    global currentLocation
    currentLocation = 1
    print (currentLocation)
    move = ""
    print ("Four large doors of gleaming black metal dominate the four corners of this small chamber.")
    print ("You recognise one of the doors as the entrance to the complex by its lack of green glow.")
    print ("No matter what you attempt this door will not open.")
    print ("If there is an exit to this place it lies beyond these three active doors.")
    print ("")
    input("Press enter to continue...")

    Options()
    print("")

    print ("1. There is a Green door to the West")
    print ("2. There is a Green door to the South")
    print ("3. There is a Green door to the East")
    print ("")
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
    global playerDMG
    global enter2

    if enter2 == 0:
        print("As you walk into the room bright lights burst into life above your head.A deep alien voice booms above your head")
        print("and your suit’s translation program starts up and immediately displays an error.  This language is apparently")
        print("unknown to all of discovered space, the thought of which sends chills down your spine.")
        print(" ")
        input("press enter to continue...")
        print("The voice stops and you flinch as hundreds of compartments fold out of the before featureless wall with a grand")
        print("chorus of thunks.  In the silence that follows, having determined the room wasn’t trying to kill you, you check the")
        print("compartments to find them all empty bar one in the corner which contains what is instantly recognisable as a pistol,")
        print("though it's not a make you recognise.")
        print("")

        if playerDMG < 15:
            print("You take the pistol, the feel of an actual weapon in your hands already making you feel safer.  If you were to")
            print("encounter something now, maybe you could avoid dying an immediate death.")
            print("")
            playerDMG = 15

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
            print ("room1()")
        else:
            print ("room6()")

    else:
        Options()
        print("")

        print ("You have been here")
        print("1. There is a Green door to the West ")
        print("2. There is a Green door to the South ")

        move = 1
        move = validateNum(move,1,2)

        if move == 1:
            print ("room1()")
        else:
            print("room6()")
#-------------------------------------------------------------------------------
def room3():
    #Equipment Bay
    #Contains the Breach Spawn encounter
    global enter3
    global currentLocation
    currentLocation = 3

    if enter3 ==0:
        print("As the door slides open, it reveals a pitch black room.  There is a sound of something whirring and crackling")
        print("seemingly emanating from the back of the room, but you cannot identify the source as what little of the room")
        print("appears to be strewn with debris and machinery and obscures your view.")
        print("")
        input("press enter to continue...")
        print("Then you become of the sound of dripping water, then a grunting sound so soft you almost mistook it for your own")
        print("breath.  The hairs on the back of your neck raise and you feel a sense of incredible dread.")
        print("")
        input("press enter to continue...")
        print("The light at your back reminds you a few step backwards, and the door would slide shut and return you to safety")
        print("However if you are to find a way out of this place, you will have to search every corner of this place.")
        print("")
        input("press enter to continue...")
        print("Should you swallow your fear and advance, or retreat for now? ")
        print("")

        print("1. Advance")
        print("2. Retreat")
        enter3 =1

        Options()
        print("")

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

        print("You resolve not to spend a second longer in this room than you have to as you switch your suit lights back on and ")
        print("consider the two available doors.")
        print("")
        print("1.There is a green door to the South")
        print("2.There is a green door to the East")
        print("")

        Options()
        print("")

        move =0
        move = validateNum(move,1,2)
        if move ==1:
            room5()
        else:
            room1()


    else:
        print("You return to the dark room where you had the encounter with the monster.")
        print("The feeling of unease you had the first time you entered has not left you.")
        print("")
        input("press enter to continue...")
        print("The door slides shut behind you plunging you into a green tinted darkness, startling you.  In the silence that ensures ")
        print("the faint sound of whirring at the back of the room, and of liquid dripping, echos inside your brain.")
        print("")
        input("press enter to continue...")
        print("You resolve not to spend a second longer in this room than you have to as you switch your suit lights back on and ")
        print("consider the two available doors.")
        print("")

        Options()
        print("")

        print("1.There is a green door to the South")
        print("2.There is a green door to the East")
        print("What do you do?")



        move =0
        move = validateNum(move,1,2)
        if move ==1:
            room5()
        else:
            room1()
#-------------------------------------------------------------------------------
def room4():
    #Medbay
    #Contains a First Aid kit
    global enter4
    global currentLocation
    global heal
    currentLocation = 4
    enter4 =0

    if enter4 ==0:
        print("This room is well lit and consists of a smaller chamber separated by a low wall, from the larger chamber which")
        print("appears to be filled with regularly spaced rectangular objects, each of which is surrounded by alien machinery.  More ")
        print("such machinery hangs from the ceiling, all of which appears to be completely inert but glows with a soft green light.")
        print("")
        input("press enter to continue...")
        print("Exploring the main chamber fully reveals a small grey box tucked into one corner.  Upon closer examination the box ")
        print("springs open revealing various needles, sprays and other items that normally belong in a first aid kit.")
        print("")
        input("press enter to continue...")
        print("A band of blue light emits from the box and sweeps over your body and your suit is suddenly receives a transmission ")
        print("from what appears to be the box currently resting in your arms.")
        print("")
        input("press enter to continue...")
        print("The transmission does not require translation and informs you it is indeed a first aid kit.   Upon closing the box again ")
        print("it folds into itself, rapidly reducing in size until it is a thin grey square in the palm of your hand.")
        print("")
        input("press enter to continue...")
        print("Considering the layout of the room, what you realise are beds and the fact the room contained a first aid kit you ")
        print("reason that this room was some sort of medical bay.")
        print("")
        input("press enter to continue...")
        print("Disregarding how an alien machine managed to communicate with your suit without translation you tuck the folded ")
        print("first aid kit into one of your suit’s pockets, hoping you will have no need to use it before escaping this place.")

        heal = heal +1
        enter4 =1

        print("")
        input("press enter to continue...")
        print("You notice one of the doors leading from here casts a blue light different from the green doors you have encountered ")
        print("before.")
        print("1.There is a green door to the North")
        print("2.There is a green door to the East")
        print("3.There is a blue door to the West")
        print("What do you do?")

        Options()
        print("")

        while True:
            move =0
            move = validateNum(move,1,3)
            if move ==1:
                room1()
            elif move ==2:
                room6()
            else:
                if room5 ==1:
                    room7()
                else:
                    print("You approach the door, but it does not respond. Since its a different colour from the other green doors you have")
                    print("encountered so far, you reason there must be some sort of key you will need before you can open this door.")
                    print("Shrugging, you turn to consider your other options.")




#-------------------------------------------------------------------------------
#def room5():
    #Equipment Storage
    #Contains the Shotgun
    #Contains the Blue Key

#-------------------------------------------------------------------------------
#def room6():
    #Checkpoint
    #Contains the Sub-Machinegun
    #Drone Walker

#-------------------------------------------------------------------------------
#def room7():
    #Weapons Control Bay
    #Contains the Drone Processor encounter
    #Contains the Assault Rifle
    #Contains the Red Key

#-------------------------------------------------------------------------------
#def room8():
    #Locker Room
    #Contains the Armoured Suit

#-------------------------------------------------------------------------------
#def room9():
    #Habitat Access
    #Contains the Drone Mother encounter
    #Contains a Health Kit

#-------------------------------------------------------------------------------
#def room10():
    #Engineering Bay
    #Contains the Breach Lord encounter

#-------------------------------------------------------------------------------
#def room11():
    #The Bridge
    #GAME END

#===============================================================================
#MAIN CODE
#===============================================================================
#Start()
#intro()
#healthkit()
#Combat()
#room1()
#room2()
#room3()
room4()

#===============================================================================
#PROGRAM END
