#Rocket Propelled Games
#Breach: A Warped Perspective
#Chris, Finn, Roman, Liam
#------------------------------------------------------------------------------
import math
import random
import time

 #Introduction
def intro():
    print ("It's been 2 hours since you were seperated from your team.  The cave you stand in is cold and dank, musty air fills your lungs.")
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

#-------------------------------------------------------------------------------
 #Global Variables
playerMax = 100
playerHP = 80
playerDMG = 5
luck = [0,0,1,1,1,1,1,1.3,1.3]
fight = ""
mobHP = 100
mobDMG = 5
heal = 1
East = False
West = False
North = False
South = False
#=------------------------------------------------------------------------------
 #Room entered
enter1 = 0
enter2 = 1
enter3 = 0
enter4 = 0
enter5 = 0
enter6 = 0
enter7 = 0
enter8 = 0
enter9 = 0
enter10 = 0
enter11 = 0

#-------------------------------------------------------------------------------

#Validator
def validateNum(value, min, max):
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
                print ("ree")
                continue




#Combat System
def Combat():

    while playerHP > 0 or mobHP > 0:
        if playerHP <= 0:
            print ("You have died, rip in pip")
            break

        elif mobHP <= 0:
            print ("You have slain the enemy")
            break

        else:
            time.sleep(1)
            print ("")
            print (" 1. Light Attack")
            print ("2. Medium Attack")
            print ("3. Heavy Attack")
            print ("")
            fight = 1
            fight = validateNum(fight,1,3)
            mobAttack = random.randint(1,3)

            if fight == 1 and mobAttack == 1:
                ComDraw()

            elif fight == 1 and mobAttack == 2:
                ComLose()

            elif fight == 1 and mobAttack == 3:
                ComWin()

            elif fight ==2 and mobAttack == 1:
                ComWin()

            elif fight ==2 and mobAttack == 2:
                ComDraw()

            elif fight ==2 and mobAttack == 3:
                ComLose()

            elif fight ==3 and mobAttack == 1:
                ComLose()

            elif fight == 3 and mobAttack == 2:
                ComWin()

            elif fight == 3 and mobAttack == 3:
                ComDraw()





def ComWin():
    global mobHP, playerDMG
    hit_chance = random.choice(luck)
    mobHP = mobHP - (round(playerDMG * hit_chance))
    print (hit_chance)
    print (mobHP)
    if hit_chance < 1:
        print ("You missed!")
    else:
        print ("You smash")
    return mobHP

def ComLose():
    global playerHP, mobDMG
    hit_chance = random.choice(luck)
    playerHP = playerHP - (round(mobDMG * hit_chance))
    print (hit_chance)
    print (playerHP)
    if hit_chance < 1:
        print ("The monster has missed! You take no damage.")
    else:
        print ("You've taken damage, your HP is ",playerHP)
    return playerHP

def ComDraw():
    global mobHP, mobDMG, playerDMG, playerHP
    hit_chance = random.choice(luck)
    mobHP = mobHP - (round(playerDMG * hit_chance))
    print (hit_chance)
    print (mobHP)
    if hit_chance < 1:
        print ("You have missed!")
    else:
        print ("You smash!")
    hit_chance = random.choice(luck)
    print (hit_chance)
    print (playerHP)
    playerHP = playerHP - (round(mobDMG * hit_chance))
    if hit_chance < 1:
        print ("The monster has missed! You take no damage.")
    else:
        print ("You've taken damage, your HP is ",playerHP)
    return mobHP, playerHP

#-------------------------------------------------------------------------------
  #Rooms
def room1():
    global North, East, South, West
    East = True
    West = True
    South = True
    move = ""
    print ("Four large doors of gleaming black metal dominate the four corners of this small chamber.")
    print ("You recognise one of the doors as the entrance to the complex by its lack of green glow.")
    print ("No matter what you attempt this door will not open.")
    print ("If there is an exit to this place it lies beyond these three active doors.")
    print ("")
    input("Press enter to continue...")
    print ("1. There is a Green door to the West")
    print ("2. There is a Green door to the South")
    print ("3. There is a Green door to the East")
    move = input("Select a door to choose your path...")
    move = validateWord(North,East,West,South,move)


def room2():
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

        if playerDMG < 15:
            print("You take the pistol, the feel of an actual weapon in your hands already making you feel safer.  If you were to")
            print("encounter something now, maybe you could avoid dying an immediate death.")
            playerDMG = 15

        elif playerDMG >=15:
            print("You decide that your current weapon is better than this sorry abandoned pistol.  You leave it in its compartment and")
            print("continue on.")


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
        print ("You have been here")
        print("1. There is a Green door to the West ")
        print("2. There is a Green door to the South ")

        move = 1
        move = validateNum(move,1,2)

        if move == 1:
            print("room1()")
        else:
            print("room6()")



def room3():
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

    choice = input("Advance or Retreat").lower()

    if choice == "advance":
        Combat()
    elif choice == "retreat":
        print("Scared RUN")
        room1()
    else:
        print("WRONG Input")

#def room4():

#def room5():

#def room6():

#def room7():

#def room8():

#def room9():

#def room10():

#def room11():

def healthkit():
    global playerHP, playerMax, heal, gainhealth
    if heal > 0:
        print ("1. Yes")
        print ("2. No")
        print (playerHP)
        gainhealth = 2
        gainhealth = validateNum(gainhealth,1,2)
        print(gainhealth)
        if gainhealth == 1:
            playerHP = playerMax
            print("You have healed yourself")
            print (playerHP)
            heal = heal - 1
        elif gainhealth == 2:
            print("No health kit was used")






#intro()
#healthkit()
#Combat()
#room1()
room2()
#room3()
