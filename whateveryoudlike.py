#########################################
#                                       #
# Kash's Choose Your Own Adventure Game #
#                                       #
#                                       #
#########################################

from asciimatics.screen import Screen
from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from time import sleep

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("Choose your own", font='big', width=screen.width+200),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("ADVENTURE!!!", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 100)], repeat=False)

Screen.wrapper(demo)

import os
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

#coding=utf-8

def death():
  if health == 0:
    print("\nYou're literally free, Boxed you, Dog water, 0 Pr,\nYou have no earnings, No wager earnings,\nYou're free, Literally so free, Freer than a free sample at Costco,\nYou're dog water, literally so dog\n")


print ("You are now about to witness the strength of the government's full power...\nYou will need to take down the government entirely on your own...\nGood luck soldier and remember... the people of the world are counting on you to take down the communists\nChoose Your Name Here: ")
player_name = input()
print ("\nWelcome to the party " + player_name + " \nChoose your specialist type:\n\nLone Wolf: Gets two extra rounds of ammo per gun\n\nAssassin: Gets a knife to silent kill\n\nComputer Hacker: Gets infinite tries on hacking instead of one\n\nMedic: Gets three stim canisters instead of one\n\nLieutenant: Gets extra starting health\n")
while True:
  specialist_class = input().lower().strip()
  if specialist_class == 'lone wolf' or specialist_class == 'assassin' or specialist_class == 'computer hacker' or specialist_class == 'medic' or specialist_class == 'lieutenant':
    break
  else:
    print ("BRO I GAVE YOU FIVE OPTIONS! YOU JUST HAD TO PICK 1 2 3 4 or 5 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")

health = 100

ammo = 50

stims = 1

weapons = []

knife = 0

    
if specialist_class == "lone wolf":
  ammo += 50
elif specialist_class == "assassin" :
  knife += 1
elif specialist_class == "medic":
  stims += 2
elif specialist_class == "lieutenant":
  health += 50

def help_():

  print("health: " + str(health))
  print("ammo: " + str(ammo))
  print("stims: " + str(stims))
  print("weapons: " + str(weapons))
  print("knife: " + str(knife))

print ("\nYou have chosen " + specialist_class)
print ("\nNow for one final question... what weapons do you want?\nMac 11: Rapid fire smg with a small mag size\nAk47: Standard issue assault rifle with a 25 round mag\nSKS: Semi-Automatic marksman rifle with a 20 round clip\nM16: Burst marksman rifle with a 30 round clip\nPKM: An lmg with a 100 round clip but insanely susceptible to recoil")


while True:
  weapon = input().lower().strip()
  if weapon == 'mac 11' or weapon == 'ak47' or weapon == 'sks' or weapon == 'm16' or weapon == 'pkm':
    break
  else:

    print ("BRO I GAVE YOU FIVE OPTIONS! YOU JUST HAD TO PICK 1 2 3 4 or 5 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")



if specialist_class == "assasin":
  weapons = ['knife',weapon]
else:
  weapons = [weapon]

if weapon == "mac 11":
  print ("The Ingram MAC-11 (Military Armament Corporation Model 11) \nis a subcompact machine pistol/submachine gun \ndeveloped by American gun designer Gordon Ingram\n at the Military Armament Corporation (MAC) during\n the 1970s in Powder Springs, Georgia.[5][6] The weapon\n is a sub-compact version of the Model 10 (MAC-10),\n and is chambered to fire the smaller .380 ACP round -Wikipedia")
elif weapon == "ak47":
  print("The AK-47, officially known as the Avtomat Kalashnikova\n (Russian: Автома́т Кала́шникова, lit. 'Kalashnikov's assault\n rifle'; also known as the Kalashnikov or just AK),\n is a gas-operated, 7.62×39mm assault rifle\n developed in the Soviet Union by Mikhail Kalashnikov\n circa WWII. It is the originating firearm of\n the Kalashnikov rifle (or 'AK') family. The number\n 47 refers to the year it was finished. -Wikipedia")
elif weapon == "sks":
  print ("The SKS is a Soviet semi-automatic carbine chambered for\n the 7.62×39mm round, designed in 1943 by Sergei Gavrilovich Simonov.\n Its complete designation, SKS-45, is an\n initialism for Samozaryadny Karabin sistemy Simonova,\n 1945 (Russian: Самозарядный карабин системы Симонова, 1945;\n Self-loading Carbine of (the) Simonov system, 1945).\n The SKS is an extremely reliable, simply\n constructed weapon with two unique distinguishing\n characteristics: a permanently attached folding bayonet,\n and a hinged non-detachable magazine. However, it is\n incapable of fully automatic fire and limited by its twenty\n round magazine capacity, and was rendered obsolete\n by the introduction of the AK-47 in the 1950s. -Wikipedia")
elif weapon == "m16":
  print ("The M16 rifle, officially designated Rifle, Caliber 5.56 mm, M16,\n is a family of military rifles adapted from the ArmaLite\n AR-15 rifle for the United States military. The\n original M16 rifle was a 5.56mm automatic rifle with a\n 20-round magazine. In 1964, the M16 entered US military\n service and the following year was deployed\n for jungle warfare operations during the\n Vietnam War.[1] In 1969, the M16A1 replaced the M14\n rifle to become the US military's standard service\n rifle.[9][10] The M16A1 improvements include a\n bolt-assist, chrome-plated bore and a 30-round magazine. -Wikipedia")
elif weapon == "pkm":
  print ("The PK (Russian: Пулемёт Калашникова, transliterated as\n Pulemyot Kalashnikova, or Kalashnikovs machine\n gun),[7] is a 7.62×54mmR general-purpose machine\n gun designed in the Soviet Union and currently in\n production in Russia.[8] The original PK machine gun\n was introduced in 1961 and then the improved PKM in\n 1969 to replace the SGM and RP-46 machine guns in\n Soviet service. It remains in use as a front-line infantry\n and vehicle-mounted weapon with Russias armed\n forces. The PK has been exported extensively and\n produced in several other countries under license. -Wikipedia")

def ending_1():
  global health
  print ("You see the panel in the next room, the final step to success.\nThe button is right there in front of you and it looks like everything has been controlled by this.\nBut... there is always a second option.\nChoose wisely " + player_name + " remember, the world is counting on you.\n1: Shut the operation down.\n2: Take control of the machine")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2':
      break
    else:
      print ("PUT IN 1 OR 2 IT'S NOT THAT HARD")

  if choice == '1':
    print ("\n\nYou hear a loud whir of machinery and the machine shuts down.\nYou beat the simulation, you won!\nBut, what would've happened if you tried to take control...\nI guess we will never know.\nYou are a hero to the people " + player_name +".\nWhat would the world have done without you.\n\nThank you for playing.")

  elif choice == '2':
    print (("\n\nOh no no no no.\nDid you really think that you could take control.\nYou got all the way to the end and this is what you decide to do?!\nListen {}, I thought that we were friends.\nBut I guess that you wanted to take control...\nSo you reign for about a year before another person overthrows you and suffers the same fate.\nBut anyways...\n\nThank you for playing.").format(player_name))


def ending_2():
  global health
  print("\n\nAs you walk past the juggernaut you see two PCs and the juggernaut says,\nyou wanna run some duos in warzone?\n1: Say yes\n2: Say no")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2':
      break
    else:
      print ("PUT IN 1 OR 2 IT'S NOT THAT HARD")

  if choice == "1":
    print("You forget about your entire mission and say hell yeah!\nYou guys win three games in a row and become lifelong friends to the end. Thank you for playing.")
  if choice == "2":
    print("The juggernaut pulls out his sniper and 360 no-scopes you\nand as you die you watch him win three games in a row by himself and your last words were, niceeeee")



def final_Boss_Part_2():
  global health
  global weapons
  global ammo
  print("Behind the desk you have four choices...\n1: Throw a grenade at him\n2: Jump up and start spraying bullets everywhere\n3: Buy everything in the warzone item shop\n4: Use the desk as a tactical advantage and start advancing at him with the desk")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      break
    else:
      print ("PUT IN 1, 2, 3, OR 4 IT'S NOT THAT HARD")

  if choice == "1":
    print("The grenade bounces off his thick armor and hits you in the head and you explode")
    health = 0

  elif choice == "2":
    print ("Did you really think that spraying bullets at a juggernaut would work?!\nHe kills you, simple as that.")
    health = 0

  elif choice == "3":
    print ("You buy all the packs in the warzone item shop\nand give it to the juggernaut and he lets you past.")
    ending_2()

  elif choice == "4":
    print ("As you start pushing the desk towards him he easily realizes\nwhere you are and pulls out his sniper and 360 no scopes you.")
    health = 0


def final_Boss_Part_1():
  global health
  global weapons
  global ammo
  juggernaut()
  print ("\n\nAs you finish off the guys in the last room and bust through the next door you see a horrific sight...\nA juggernaut is staring right at you from across the room,\nChoose your next move wisely.\n1: Drop-shot him\n2: Talk about your feelings with him\n3: Start spraying bullets everywhere\n4: Run for cover\n5: Surrender\n6: Slide cancel and try to run around him and melee him over and over again\n7: Ask if he drops superstore\n8: Fortnite dance at him\n")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8':
      break
    else:
      print ("PUT IN 1, 2, 3, 4, 5, 6, 7, OR 8 IT'S NOT THAT HARD")

  if choice == "1":
    print ("\n\nAs I said before drop-shotting is even good against juggernauts so you end up killing him")
    ammo -= 10
    ending_1()
  elif choice == "2":
    print ("\n\nYou have a very heartfelt talk with the Juggernaut and he lets you pass")
    ending_1()

  elif choice == "3":
    print ("\n\nAs you spray bullets all over the room the juggernaut starts spraying\nso you take cover behind a desk...")
    final_Boss_Part_2()

  elif choice == "4":
    print ("\n\nYou take cover behind a desk...")
    final_Boss_Part_2()

  elif choice == "5":
    print ("\n\nAs you surrender he pulls out a sniper a 360 no scopes you")
    health = 0

  elif choice == "6" and specialist_class == 'assasin':
    print ("\n\nYou stab him over and over again and he dies")
    ending_1()

  elif choice == "6":
    print ("\n\nYou try to punch him and he kills you, it's that simple")
    health = 0

  elif choice == "7":
    print ("\n\nHe says he usually drops hospital but sometimes superstore and lets you past")
    ending_1()


  elif choice == "8":
    print ("\n\n$19 fortnite card, who wants it? *Donk* Noooo mooore fortnite")
    health = 0


def paths_Meet():
  global health
  global weapons
  global ammo
  print ("\n\nAs you walk down the hallway of which you came you see two guards in the hallway\nYou have four options:\n1: Try to sneak past them\n2: Shoot one of them and try to melee the other one\n3: Pull out your fists, tactical sprint,and stim all the way past them\n4: 360 no-scope collateral them")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      break
    else:
      print ("PUT IN 1 2 3 OR 4 IT'S NOT THAT HARD")

  if choice == "1":
    print ("\n\nYou successfully sneak past them")
    final_Boss_Part_1()
  elif choice == "2" and specialist_class == "assasin":
    print ("\n\nJust like last time, you kill the first one with your gun\nand since you had a knife you kill the second one")
    ammo -= 15
    final_Boss_Part_1()
  elif choice == "2":
    print ("\n\nYou kill the first one but as you go to knock the second guy out he stabs you")
    health = 0
  elif choice == "3" and specialist_class == "medic":
    print ("\n\nYou are just too fast for them and speed past them into the next room\nAlso you end up finding some more stims in the next room so you don't have to lose anything\n\n")
    final_Boss_Part_1()
  elif choice == "3":
    print ("\n\nYou run out of stims very quickly and stop right in front of them and they kill you")
    health = 0
  elif choice == "4" and 'sks' in weapons:
    print ("\n\nAs you reach to pull the trigger of your sks they line up perfectly and you 360 no scope collateral them")
    ammo -= 10
    final_Boss_Part_1()
  elif choice == "4":
    print ("\n\nAs your reach for your sniper rifle you realise you don't have one... get good")
    final_Boss_Part_1()

def dungeon_Question_Three():
  global health
  print ("Final question...\n\nWhat can you hold in your right hand, but never in your left hand?")

  while True:
    choice = input().lower().strip()
    if choice == "your left hand":
      print("Fine... You win... Just get out of the dungeon")
      paths_Meet()
      break
    elif specialist_class == "computer hacker":
      print("\n\nTry again\n\n")
    else:
      print("\n\nNo\n\n")
      health = 0
      break

def dungeon_Question_Two():
  global health
  print ("Next question...\n\nFirst you eat me, then you get eaten. What am I?\n")

  while True:
    choice = input().lower().strip()
    if choice == "a fishhook":
      dungeon_Question_Three()
      break
    elif specialist_class == "computer hacker":
      print("\n\nTry again\n\n")
    else:
      print("\n\nNo\n\n")
      health = 0
      break

def dungeon_Question_One():
  global health
  print ("\n\nSince you obviously don't know what S.R. is\nyou get thrown in a dungeon with other fake fortnite kids like you...")
  print ("\n\nYou see a small panel at the corner of the room with a keypad on it...\n\n\nIt asks you this... With pointed fangs I sit and wait;\nwith piercing force I crunch out fate; grabbing victims, proclaiming might;\nphysically joining with a single bite. What am I?")

  while True:
    choice = input().lower().strip()
    if choice == "a stapler":
      dungeon_Question_Two()
      break
    elif specialist_class == "computer hacker":
      print("\n\nTry again\n\n")
    else:
      print("\n\nNo\n\n")
      health = 0
      break

def executive_lounge():
  global health
  print ("\n\nSince you know what SR is you can just relax in the executive lounge... you can choose your next move.\n1: Go over to the couch.\n2: Go and walk down the hallway out of the lounge.\n3: Go eat a sandwich.")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3':
      break
    else:
      print ("PUT IN 1 2 OR 3 IT'S NOT THAT HARD")

  if choice == '1':
    print("You go over to the couch...\nit feels good and you feel jealous that you don't have this couch.\nBut the couch suddenly sucks you into the cushions and you suffocate.")
    health = 0
  elif choice == '2':
    paths_Meet()
  elif choice == '3':
    print("As you eat the sandwich you realize that it is poisoned and you die lol")
    health = 0

def elevator():
  global health
  print ("\n\nAs you step into the elevator you see 2999 buttons and\nthere is a message written in brail on the button pad\ntoo bad you can't read brail\nbut there is also a message on the ceiling that says the button you choose is your sr...\nyou have 2999 choices... GO!")

  while True:
    choice = input().lower().strip()
    choice = int(choice)
    if choice in range(1, 3000):
      break
    else:
      print("\nBro there is 2999 choices and you chose something else?!\nJust pick already")


  if choice in range(2, 2999):
    print("\n\nThe elevator crashes and you die... L")
    health = 0
  elif choice == 1:
    print("\n\n...\n\nYou obviously don't know anything about sr...\n\nYou need to do extra work")
    dungeon_Question_One()
  elif choice == 2999:
    print("\n\n...\n\nYay! You know what S.R. is!\nyou can move on to the next stage...")
    executive_lounge()

def ufo_first_choice():
  global health
  print ("\n\nAfter crashing into the ufo you see that you are surrounded by aliens (former hostages from area 51) and they seem angry.\n1: Use the powers of over 9000 to destroy the ship along with the aliens\n2: Do a spin move and shoot all of the aliens heads off\n3: Use a detonater and detonate the bomb that you planted inside this ship 5 years ago\n4: Punch all the aliens really hard and make them into alien soup.")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      break
    else:

      print ("BRO I GAVE YOU FOUR OPTIONS! YOU JUST HAD TO PICK 1 2 3 or 4 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")

  if choice == "1":
    print ("As you are turning into the true form of Goku one of the aliens 360 no-scopes you")
    health = 0

  if choice == "2":
    print ("As you are spining around weirdly one of the aliens 360 no-scopes you")
    health = 0

  if choice == "3":
    print ("As you detonate the bomb you placed 5 years ago you jump off the ufo\nand walk away from the explosion of the white house and the ufo with sunglasses. Thank you for playing")

  if choice == "4":
    print ("As you try to make all the aliens into alien soup trump comes out of the\nwhite house and 360 no-scopes you")
    health = 0

def tbh_Idk_What_Choice():
  global health
  print ("\n\nYou see a pit of molten lava. What do you do?\n1: You just jump across LMAO\n2: Pile up the guards dead bodies and use it as a bridge\n3: Use your flamethrower to flamethrower across\n4: All of the above")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      break
    else:
      print ("BRO I GAVE YOU FOUR OPTIONS! YOU JUST HAD TO PICK 1 2 3 or 4 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")

  if choice == "1":
    print("\nAh you thought this would be easy? NO IT WILL NOT BE EASY.\nYOU TRIP IN THE LAVA AND BOUNCE AROUND AS YOU TURN TO HUMAN ASH. (Humans float on lava)")
    health = 0

  elif choice == "2":
    print("\nAs you start stacking the guards dead bodies you get 360 no-scoped by Abraham Lincoln")
    health = 0

  elif choice == "3":
    print ("\nBro... YOU FLAMETHROWER ACROSS THE BRIDGE!!! LEZ GOOOOOOOOOOOOO")

  elif choice == "4":
    print ("\nWhy would you pick that?? You know on all tests it isn't right :|.")
    health = 0

def second_choice():
  global health
  print ("\n\nNow just four choices...\n1: Go back down the hallway and go to the left\n2: Keep going straight down this hallway\n3: Break the wall to the left of you\n4: Break the wall to the right of you")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
      break
    else:

      print ("BRO I GAVE YOU FOUR OPTIONS! YOU JUST HAD TO PICK 1 2 3 or 4 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")



  if choice == "1":
    print ("\nWelp that was an unfortunate decision because you end up in a pit of lava...\nBUT!!! Click this link to get a second chance:\nhttps://www.youtube.com/watch?v=cGw-8FrRT1E")
    sleep(15)
    health = 0

  elif choice == "2":
    print ("\nThree guards down the hallway were camping and kill you as soon as you come close...\nBUT!!! Click this link to get a second chance:\nhttps://www.youtube.com/watch?v=cGw-8FrRT1E")


    sleep(15)
    health = 0

  elif choice == "3":
    print ("\nYou break into a secret bunker elevator... good job")
    elevator()
  elif choice == "4":
    print ("As you break through the wall to your\nright you fall out of the white house onto a trampoline and bounce into a ufo.")
    ufo_first_choice()


def first_fight():
  global health
  global weapons
  global ammo
  print("You see a middle aged man dressed in black overalls and a suit with an ak47.\n\nYou have 6 choices.\n\n1: 360 no-scope him.\n\n2: Throw down your weapon and surrender.\n\n3: Just drop your weapon and go at him with your fists.\n\n4: Shoot the living hell out of him.\n\n5: Drop shot him like you are playing COD.\n\n6: Crank 90s on him and 220 pump him in the head.")


  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
      break
    else:
      print ("BRO I GAVE YOU SIX OPTIONS! YOU JUST HAD TO PICK 1 2 3 4 5 or 6 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")

  if choice == "1" and 'sks' in weapons:
    print("\nAs you reach for your sks you pull the trigger accidentally and it kills him...\npure skill")
    ammo -= 10
    second_choice()
  elif choice == "1":
    print("\nYou reach for your sniper rifle but you realize you don't have one...\nget good kid")
    health = 0
  elif choice == "2":
    print("\nAs you surrender he 360 no-scopes you")
    health = 0
  elif choice == "3" and specialist_class == "assassin":
    print("\nYou clash your knife with his and make it out victorious")
    second_choice()
  elif choice == "3":
    print("\nYour fists are no match for his knife\nand you fall to the ground dead")
    health = 0
  elif choice == "4" and 'pkm' in weapons:
    print("\nYou end up shooting the living\nhell out of him because of your pkm")
    ammo -= 20
    second_choice()
  elif choice == "4":
    print("\nYour weapon runs out of bullets in 2 seconds\nand he lands a 360 no scope headshot")
    health = 0
  elif choice == "5":
    print("\nHonestly drop-shotting is even good against juggernauts so you destroy him")
    ammo -= 15
    second_choice()
  elif choice == "6":
    print("\nYou reach for your pump and realize you don't have one...\nget good kid")
    health = 0

def tbh_Idk_What_Fight():
  global health
  global weapons
  global health
  print ("\nThere are a couple guards camping a corner to a different hallway.\nWhat do you do?\n1: 360 no scope collateral them all\n2: Run up to them and SLICE ALL OF THEIR NECKS AND\nSPILL THE BLOOD ALL OVER THE HARDWOOD FLOOR\n3: Hack into the mainframe and mind control them\n4: Pull out your flamethrower and flamethrower them\n5: Rick roll them\n6: Stop time with your time watch and make one of them wedgie the other one and then unpause time")

  while True:
    choice = input().lower().strip()
    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
      break
    else:
      print ("BRO I GAVE YOU SIX OPTIONS! YOU JUST HAD TO PICK 1 2 3 4 5 or 6 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")

  if choice == "1":
    print("As you pull out your sniper to 360 one of the boys says\nsheeeeeeeeeeeeeeeeeeesh a little too early and one of the guards 180 no-scopes you")
    health = 0
  if choice == "2" and specialist_class == "assassin": #:| <-- waffle head
    print("YOU SLICE ALL OF THEIR NECKS OUT AND SHOVE THEIR FACES INTO THEIR BLOOD")
    tbh_Idk_What_Choice()
  if choice == "2":
    print("Bruh what are you gonna slice their necks out with?\nYour hands? LMAO U DIE.")
    health = 0
  if choice == "3":
    print("Bro... That only works in disney movies. You die.")
    health = 0
  if choice == "4":
    print("People that don't carry around flamethrowers are 🤡  🤡  🤡.\nYou flamethrower them to death!!!")
    tbh_Idk_What_Choice()
  if choice == "5":
    print("What did you think would happen... NEVER GONNA GIVE YOU UP\nNEVER GONNA LET YOU DOWN\nNEVER GONNA RUN AROUND AND DESERT YOU\nNEVER GONNA MAKE YOU CRY\nNEVER GONNA SAYYYYYYY GOODBYE\nNEVER GONNA TELL A LIEEEEE\nAND HURT YOU")
    health = 0
  if choice == "6":
    print ("As you reach for your time travel watch you realise you don't have one lol git gud.")
    health = 0

def first_choice():
  global health
  #animation()
  print ("Now you have two choices, go left or go right.\nPretty simple right? 1 (Left) or 2 (right)")

  choice = input()

  if choice == '1':
    print ("Left is always lucky...")
    tbh_Idk_What_Fight()


  elif choice == '2':
    print ("You walk into a hallway that you have never explored before")
    first_fight()

def break_in():
  global health
  while True:
    print ("\n\nLets get started...\nMake sure, not just for this question but for all of them you INPUT THE NUMBER NOT THE TEXT\nChoose your way to break into the white house:\n1:Climb using rope\n2:Climb using helicopter\n3:Sneak in using cloaking device\n4:Sneak in using sewers")


    choice = input()

    if choice == '1':

      print ("Why did you think that you could climb the white house using a rope?\nI mean like that is literally the worst way to sneak into the white house.\nI put that option out as a joke... nice try but you get shot down.")

      health = 0

      break
    elif choice == '2':

      print ("Okay I mean honestly sneaking into the white house using a helicopter? How stupid are you?!\nSomebody 360 no scopes you out of the driver seat")

      health = 0

      break
    elif choice == '3':

      animation()
      print ("Okay well you went with the 50% of the population that played my game that are actually smart...\nAnyway you end up walking through the front door LOL")
      first_choice()
      break
    elif choice == '4':

      animation()
      print ("Okay well you sneak through the sewer successfully but you are covered in yucky stuff and you smell very bad...\nYou end up in the main hall right next to the front door.")
      first_choice()
      break
    else:

      print ("BRO I GAVE YOU FOUR OPTIONS! YOU JUST HAD TO PICK 1 2 3 OR 4 NOW TRY AGAIN...\nNEXT TIME I WONT BE SO GENEROUS.")



def animation():
  def frame_one():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \             /  |")
    print("|   \           /   |")
    print("|    \         /    |")
    print("|     \       /     |")
    print("|      \     /      |")
    print("|       \   /       |")
    print("|        \_/        |")
    print("|        |.|        |")
    print("|         -         |")
    print("|       /   \       |")
    print("|      /     \      |")
    print("|     /       \     |")
    print("|    /         \    |")
    print("|   /           \   |")
    print("|  /             \  |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_two():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \             /  |")
    print("|   \           /   |")
    print("|    \         /    |")
    print("|     \       /     |")
    print("|      \     /      |")
    print("|       \___/       |")
    print("|       |   |       |")
    print("|       | . |       |")
    print("|       |   |       |")
    print("|        ---        |")
    print("|      /     \      |")
    print("|     /       \     |")
    print("|    /         \    |")
    print("|   /           \   |")
    print("|  /             \  |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_three():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \             /  |")
    print("|   \           /   |")
    print("|    \         /    |")
    print("|     \       /     |")
    print("|      \_____/      |")
    print("|      |     |      |")
    print("|      |  ~  |      |")
    print("|      |  =  |      |")
    print("|      |     |      |")
    print("|      |     |      |")
    print("|       -----       |")
    print("|     /       \     |")
    print("|    /         \    |")
    print("|   /           \   |")
    print("|  /             \  |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_four():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \             /  |")
    print("|   \           /   |")
    print("|    \         /    |")
    print("|     \_______/     |")
    print("|     |       |     |")
    print("|     |       |     |")
    print("|     | ~~~~~ |     |")
    print("|     |   ->  |     |")
    print("|     |   <-  |     |")
    print("|     |       |     |")
    print("|     |       |     |")
    print("|      -------      |")
    print("|    /         \    |")
    print("|   /           \   |")
    print("|  /             \  |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_five():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \             /  |")
    print("|   \           /   |")
    print("|    \_________/    |")
    print("|    |         |    |")
    print("|    |         |    |")
    print("|    | ~~~~~~~ |    |")
    print("|    |   -->   |    |")
    print("|    |   <--   |    |")
    print("|    |         |    |")
    print("|    |         |    |")
    print("|    |         |    |")
    print("|    |         |    |")
    print("|     ---------     |")
    print("|   /           \   |")
    print("|  /             \  |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_six():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \             /  |")
    print("|   \___________/   |")
    print("|   |           |   |")
    print("|   |           |   |")
    print("|   |           |   |")
    print("|   |           |   |")
    print("|   |  ~~~~~~~  |   |")
    print("|   |    --->   |   |")
    print("|   |    <---   |   |")
    print("|   |           |   |")
    print("|   |           |   |")
    print("|   |           |   |")
    print("|   |           |   |")
    print("|    -----------    |")
    print("|  /             \  |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_seven():
    print("---------------------")
    print("|\                 /|")
    print("| \               / |")
    print("|  \_____________/  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |  ~~~~~~~~~~ |  |")
    print("|  |     --->    |  |")
    print("|  |     <---    |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|  |             |  |")
    print("|   -------------   |")
    print("| /               \ |")
    print("|/                 \|")
    print("---------------------")



  def frame_eight():
    print("---------------------")
    print("|\                 /|")
    print("| \_______________/ |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |  ~~~~~~~~~~~  | |")
    print("| |     ---->     | |")
    print("| |     <----     | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("| |               | |")
    print("|  ---------------  |")
    print("|/                 \|")
    print("---------------------")



  def frame_nine():
    print("---------------------")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|    ~~~~~~~~~~~    |")
    print("|      ------>      |")
    print("|      <------      |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("|                   |")
    print("---------------------")


  clear()
  frame_one()
  sleep(0.4)
  clear()
  frame_two()
  sleep(0.4)
  clear()
  frame_three()
  sleep(0.4)
  clear()
  frame_four()
  sleep(0.4)
  clear()
  frame_five()
  sleep(0.4)
  clear()
  frame_six()
  sleep(0.4)
  clear()
  frame_seven()
  sleep(0.4)
  clear()
  frame_eight()
  sleep(0.4)
  clear()
  frame_nine()

def juggernaut():
  print("       .---.")
  print("      /_____\ ")
  print("      ( '.' )")
  print("       \_-_/_")
  print("    .--`'V'//-. ")
  print("   / ,   |// , \ ")
  print("  / /|Ll //Ll|\ \ ")
  print(" / / |__//   | \_\ ")
  print(" \ \/---|[]==| / /")
  print("  \/\__/ |   \/\/")
  print("   |/_   | Ll_\|")
  print("     |`^   ^`| ")
  print("     |   |   |")
  print("     |   |   |")
  print("     |   |   |")
  print("     |   |   |")
  print("     L___l___J")
  print("      |_ | _|")
  print("     (___|___)")

break_in()
death()
