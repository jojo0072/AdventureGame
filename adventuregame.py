def main():
    print("Escape from the Haunted Mansion")
    print("\nYou wake up in a dark, spooky, locked mansion with no memory of how you got there.\nAs you explore, you realize the mansion is haunted by ghosts and traps.\nYour goal is to escape the mansion alive.")
    dark_hallway()
def dark_hallway():
    print("\n\nThe Dark Hallway\n\nYou awaken in a dimly lit hallway.\nMoonlight filters through the dusty windows, casting eerie shadows on the walls.")
    while True:
        choice=input("\nWhat do you want to do?\n(1) Examine surroundings\n(2) Check nearby door\n(3) Listen for any sounds\n\nYour decision: ")
        if choice=="1":
            print("You notice a flickering light at the end of the hallway.")
            mysterious_room()
        elif choice=="2":
            print("It's locked, but you hear faint whispers emanating from the other side.")
            room_of_doom()
        elif choice=="3":
            print("You hear distant footsteps echoing through the corridor.")
            exploring_hallway()
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def exploring_hallway():
    print("\n\nExploring the Dark Hallway\n\nYou continue to explore the dark hallway, searching for clues.")
    while True:
        choice=input("\nWhat do you want to do?\n(1) Move towards the flickering light\n(2) Return to the starting point\n\nYour decision: ")
        if choice=="1":
            mysterious_room()
        elif choice=="2":
            dark_hallway()
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def mysterious_room():
    print("\n\nThe Mysterious Room\n\nYou enter a room shrouded in darkness.\nThe air feels heavy with the scent of decay.\nCobwebs cling to the corners, and a single candle flickers on a dusty table.")
    while True:
        choice=input("\nWhat do you want to do?\n(1) Light the candle\n(2) Search the room for clues\n\nYour decision: ")
        if choice=="1":
            print("The room illuminates, revealing old furniture covered in dusty sheets.\nContinue exploring the room.")
            dusty_furniture()   
        elif choice=="2":
            print("You find a hidden compartment under the floorboards, containing a mysterious key")
            final_confrontation()
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def dusty_furniture():
    print("\n\nInspect the Dusty Furniture\n\nYou approach the dusty furniture and carefully inspect it for any hidden items or clues.")
    while True:
        choice=input("\nWhat do you want to do?\n(1) Examine the drawers\n(2) Lift the sheets covering the furniture\n\nYour decision: ")
        if choice=="1":
            print("You find an old journal containing cryptic writings.")
            cryptic_journal()   
        elif choice=="2":
            print("You uncover a rusty key hidden beneath one of the cushions.")
            final_confrontation()
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def cryptic_journal():
    print("\n\nThe Cryptic Journal\n\nYou open the old journal and attempt to decipher its cryptic writings.")
    while True:
        choice=input("\nWhat do you want to do?\n(1) Attempt to decode the hidden messages.\n(2) Read the journal entries\n\nYour decision: ")
        if choice=="1":
            print("You decipher a clue leading to a hidden compartment in the room.")
            final_confrontation()
        elif choice=="2":
            print("You uncover clues about the history of the haunted house and its previous inhabitants.\nContinue exploring.")
            examine_paintings()   
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def examine_paintings():
    print("\n\nExamine the Paintings on the Wall\n\nYou study the paintings hanging on the walls, searching for any hidden meanings or clues.")   
    while True:
        choice=input("\nWhat do you want to do?\n(1) Remove a painting from the wall\n(2) Inspect the frames for hidden compartment\n\nYour decision: ")
        if choice=="1":
            print("You find a safe hidden behind it.")
            secret_safe()
        elif choice=="2":
            print("You discover a small key taped to the back of one of the frames. ")
            final_confrontation()   
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def secret_safe():
    print("\n\nThe Secret Safe\n\nYou discover a safe hidden behind one of the paintings on the wall.")  
    while True:
        choice=input("\nWhat do you want to do?\n(1) Search for the combination\n(2) Try to open the safe\n\nYour decision: ")
        if choice=="1":
            print("You find a hidden note with the code, open the safe and discover a key.")
            final_confrontation()
        elif choice=="2":
            print("You realize it's locked and requires a combination.\nSearch for clues in the house to unlock the safe.")
            room_of_doom()   
        else:
            print("Invalid Input! Try again...")
            continue        
        break
def final_confrontation():
    print("\n\nThe Final Confrontation\n\nArmed with the key, you approach the locked door.\nYou escape the haunted house and emerge victorious.\nYou win.")    
def room_of_doom():
    print("\n\nThe Room of Doom\n\nYou open a door and step into a dimly lit room.\nThe air feels heavy, and an eerie silence fills the space.\nSuddenly, the door slams shut behind you, and you realize you're trapped.")
    while True:
        choice=input("\nWhat do you want to do?\n(1) Look for an exit\n(2) Inspect the walls for hidden passages.\n\nYour decision: ")
        if choice=="1":
            print("You frantically search for a way out but find none.\nAs time passes, the air grows thin, and panic sets in.\nYou lose.")
        elif choice=="2":
            print("You run your hands along the cold stone walls, hoping to find a hidden escape route.\nBut as you search, the walls begin to close in, trapping you further.\nYou lose.")
        else:
            print("Invalid Input! Try again...")
            continue        
        break                                                                                     
main()        