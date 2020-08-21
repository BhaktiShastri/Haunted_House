# 27th October 2019
# My First Text Adventure Game
#*****************************************************************


name = input("What's your first name? ")
print("Hi " + name + ", are you ready to for new exiting adventure?")
print()
input("If so, press ENTER to start this scary but thrilling adventure.")
print()
print("OK, here we go.")
print("into the world of...")
print()
print("Haunted House Game(1.0)")
print("\n")
input("Press ENTER to continue")
print("""


SCENARIO:

   It's Halloween and you've just walked into what you thought was a fun haunted house.

   However, you realise this is no fun haunted house .. and the front door has just closed and locked.

   There are ghosts in the hallways and real monster danger.

   It's very dark, and dangerous...and you have to get out - quickly !!

   I'm your voice in your head, and I'll help you if I can.

""")
print()

input("Press ENTER to continue\n\n")


#Function for the start of the main part of the game
def main_dining_hall():
        print ()
        print("You are in the main dining hall of the creepy house, standing alone, in the dark.")
        print("You see three heavy doors.")
        print("Do you go through the north door (N), south door (S) or east door (E)?")
        print()
        choice = input("Enter either N, S or E? ")
        
        if choice == "N":
                dark_hallway()
                
        elif choice == "S":
                long_corridor()
                
        elif choice == "E":
                stairway()
                
        else:
                print ("I didn't understand. Let's try this again, you have to get out NOW !!")
                main_dining_hall()



# The Dark Hallway function
def dark_hallway():
        print("\nYou are now in a creepy dark hallway where a ghost floats aimlessly through the air.")
        print("You notice there are doors to the north (N), east (E) and south (S).")
        choice = input("Which door will you go through?  Type your choice? (don't go East!!) ")
        
        if choice == "N":
                print()
                print("You push on the door.  It's locked.")
                print("There's a keypad.  You need to type a code into it to unlock the door and escape.")
                print("(The code is in one of the rooms in the house).")
                enter_find = input("Do you want to enter the code (E) or find the code (F)? \n")
                
                if enter_find == "E":
                        escape()
                        
                elif enter_find == "F":
                        main_dining_hall()
                        
                else:
                        print("I didn't understand.  Please answer either E or F.")
                        dark_hallway()

                    
        elif choice == "S":
                print()
                main_dining_hall()
                    
        elif choice == "E":
                print("\nYou push the door open, it creeks as it opens.")
                print("This is a very strange, dark room, but you walk in.")
                print("The door slams shut !!\n")
                print("ZOMBIES !!!\n")
                print("You're ...DEAD !!\n")
                print("Oh dear " + name + ".  Never mind.  Do you want to play again? ")
                play_again = input('Type "YES" (and press ENTER) to play again, or just press ENTER to end the program. \n')
                    
                if play_again == "YES":
                        print("\nGreat! Just remember not to go east this time (I did try to warn you).")
                        main_dining_hall()
                        
                else:
                        exit()
 
        else:
                print ("Umm, I didn't quite get that. Try again. ")
                dark_hallway()
                        


# Long corridor function
def long_corridor():
        print("You are in a long corridor.")
        print("You see heavy wooden doors to the north (N) and west (W).")
        print()
        print()
        choice = input("Which door will you go in?  Make your choice: ")
        
        if choice == "N":
                main_dining_hall()
                
        elif choice == "W":
                spooky_lab()
                
        else:
                print ("Sorry, I don't understand.  Let's try again.")
                long_corridor()

            
                
# The stairway function
def stairway():
        print()
        print()
        print("This is a creeky wooden stairway. Shhhh! Be careful.")
        print("You see heavy wooden doors at the bottom of the stairs and back to the west.")
        print()
        print()
        choice = input("Will you take the door at the bottom of the stairs (S) or back to the west (W)? ")
        
        if choice == "S":
                dungeon()
                
        elif choice == "W":
                main_dining_hall()
                
        else:
                print ("Umm, I didn't quite get that. Try again.")
                stairway()       



# The dungeon function, where the user sees the skeleton
def dungeon():
        print()
        print()
        print("You've found a dungeon, with a skeleton chained to the wall.")
        print("Remember what you've seen.  This will help you to get out of the house.")
        input("Press ENTER to head back up the stairs to the main hall.\n")
        main_dining_hall()



# Spooky lab function, where you can open a drawer to find instructions on how to get out of the house.
def spooky_lab():
        print()
        print()
        print("You're in a spooky lab with bubbling tubes of phosphorous liquids.")
        print("There's also a monstrous figure in the far corner.  It hasn't seen you yet.")

        input("Press ENTER to continue.\n")
        
        print("There's a table with a drawer.\n")
        print("You open the drawer and find instructions on how to get out of the front door.")
        print('The instructions say "There is a keypad on the front door.  To get out, ... ')
        print('enter the name of what you saw in the dungeon".\n')
        
        instructions = ""
                    
        while instructions != "Yes":
                instructions = input("Confirm (Yes) that you have read the instructions: ")
                        
        print("\nWell done " + name + ", you're doing great.")
        input("Press ENTER to leave the room.\n")
        long_corridor()
        


# Trying to enter the code on the keypad to escape through the main door
def escape():

        code = ""                                                      
        while code != "skeleton":
                code = input("Enter the code: ")

                if code == "skeleton":
                        print("You are FREE !!!!!!!!")
                        input("Press ENTER and click OK to end the program")
                        exit()

                else:
                        print("Incorrect")
                        look_for_code = input("Press Y to look for the code again, or ENTER to try again: ")

                        if look_for_code == "Y":
                                main_dining_hall()
                        
                        else:
                                look_for_code == ""

                
# Start of the game
main_dining_hall()
