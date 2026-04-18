# Jeremías Branger
# Date: 4/18/26
# Course project RPG

#        PSEUDOCODE:
# Define main function
# Declare constants for options
# Declare constants for slatan's last name
# Declare constant for destination choice
# Declare constant for total points
# Display introduction to RPG and show game title Slatan
# Took away while true for a better loop that only runs until the user chooses to quit the game, instead of having to break out of it (NEW)
# Give Main Menu and give options to choose
# Depending on option chosen give output
# If choose rules send to rules and then back to main menu
# If choose to start game then prompt for name and begin adventure
# High score name for final points (NEW)
# Send to destination to help out
# Now has random assignation of points in some choices to give variety to points
# Added exceptions so users don't see error messages
# Only added to main as those are the ones that cause crashes, on other parts simply ignores and if does cause crash simply restarts with the error message I wrote.
# Chooses to go to Portsmouth
# Chooses how to save villagers
# Send to other 2 destinations
# Chooses to go to save the Elves
# Saves elf queen
# Sent to other 2 destinations
# Chooses to go save the Dwarves
# Cures Dwarves
# Sent to other 2 destinations
# Every time Slatan makes a decision points are given out
# At end displays total points made through their decisions and ends game
# First created a file called highscores.txt to hold highscores and who set them (NEW)
# Then, read the file to get current high score and name (NEW)
# Reads the name of highscorer (NEW)
# Reads highscorer's points (NEW)
# Compares current player's points to high scores to see if to congratulate and set new score or say sorry and to try again. (NEW)
# If points are high enough they beat the high score and congratulated (NEW)
# If points are high enough they beat the high score and congratulated (NEW)
# Rewrites highscores.txt with new high score and name (NEW)
# Breaks due to error I was getting where if they kept retrying after setting a high score the game kept it as their current score (NEW)
# Calls main function

from random import randrange

# Function to handle destination choices and points
def destinationChoice(slatanLastName, totalPoints):
    # Dictionary list for destinations
    destinations = {1: "Villagers in Portsmouth being attacked by a Dragon",
                    2: "Elves in Regal Bay whose Queen was kidnapped",
                    3: "Dwarves suffering a Plague"}
    # After choosing a destination, it will be added to visited and not chosen again
    visited = set()

    while len(visited) < 3:
        print("\nOh great hero, who would you want to help out next?")
        for key, value in destinations.items():
            if key not in visited:
                print(f"     [{key}] {value}")
        destination = int(input("\nChoose your destination: "))

        if destination in visited or destination not in destinations:
            print("Invalid or already visited destination. Try again.")
            continue
        # Adds chosen destination so not chosen again
        visited.add(destination)
        if destination == 1:
            print("You arrive to Portsmouth and see the dragon spouting fire all over the village!")
            totalPoints += randrange(10, 200)
            # Returns total points after dragon choice decision
            totalPoints = dragonChoiceDecision(slatanLastName, totalPoints)
        elif destination == 2:
            print("You make the long ardeous journey all the way to the Elves' side of the world")
            totalPoints += randrange(60, 350)
            # Returns points from the elves choice decision
            totalPoints = saveElves(totalPoints)
        elif destination == 3:
            print("You arrive to the Dwarves' lair and cure everyone with an antidote!")
            totalPoints += 600

        print(f"Total points: {totalPoints}")

    print("\nYou have visited all destinations. Your journey is complete!")
    return totalPoints

# Function handling the dragon choice and it's points
def dragonChoiceDecision(slatanLastName, totalPoints):
    # Choose what to do about the dragon
    dragonChoice = int(input(f"What will Slatan {slatanLastName} the great do?\n"
                             f"     [1] Befriend the dragon and become a dragonmaster\n"
                             f"     [2] Grab your trusty Axe 'Mikael' and slay the dragon\n"
                             f"     [3] Do nothing and go to the town tavern\n\n"))
    # Chooses peace
    if dragonChoice == 1:
        print(
            f"You spend hours showing it there's peace in the world and it finally lets you ride it and now you are known as Slatan {slatanLastName}, The Dragonmaster!\n")
        print("You have saved the village from its danger!\n\n")
        randPoints = randrange(600, 1200)
        totalPoints += randPoints
        print(f"Total points: {totalPoints}")
    # Choose War
    elif dragonChoice == 2:
        print(
            "After a long ardeous battle, you finally reach the dragon's weakpoint on its neck and boom, the head plops off!\n")
        print(
            "You have saved the village from its danger! However killing the dragon has made Drea the Goddess mad.\n\n")
        totalPoints += 600
        print(f"Total points: {totalPoints}")
    # Choose to do nothing
    elif dragonChoice == 3:
        print("The village burns and you are a terrible person.\n")
        totalPoints -= 200
    return totalPoints

# Function calling the choice to save the Elves
def saveElves(totalPoints):
    print("You reach Regal Bay and see the despair in everyone's eyes.\n")
    randPoints = randrange(15, 60)
    totalPoints += randPoints
    print(f"Total points: {totalPoints}")
    elvenChoice = int(input("Now what?\n"
                             "[1] Follow a trail and help rescue the queen\n"
                             "[2] Take a break from saving people\n\n"))
    if elvenChoice == 1:
        print("You follow some trails left behind by the kidnappers and bring the queen to justice!")
        totalPoints += 500
        print(f"Total points: {totalPoints}")
    elif elvenChoice == 2:
        print("You take a break while the elves suffer")
        totalPoints -= 100
        print(f"Total points: {totalPoints}")
    return totalPoints

# Function to display the intro
def displayIntro():
    print("-" * 7, "", "Slatan", "", "-" * 7)
    print("Once upon a time, in a world long, long ago \n"
          "There was a hero named 'Slatan'!")

# Overall main function handling the main menu and introduction to the game
def main():
    # Initialize total points, main menu option, and Slatan's last name
    totalPoints = mainMenuOption = 0
    slatanLastName = ""
    displayIntro()
    # Took away while true for a better loop that only runs until the user chooses to quit the game, instead of having to break out of it (NEW)
    while mainMenuOption != 3:
        try:
            mainMenuOption = int(input("     [1] Rules\n"
                                       "     [2] Start your adventure\n"
                                       "     [3] Quit Game\n"))
            if mainMenuOption == 1:
                print("Never, ever say the name of 'Drea the Goddess'\n"
                      "Furthermore, never look the big Swan in the eyes\n"
                      "If you ever get scared say the name of Slatan's love Athena to quit the game!")
            elif mainMenuOption == 2:
                # Adventure begins and present lore
                slatanLastName = input("What shall Slatan's last name be?")
                # High score name for final points (NEW)
                scoreName = input("What name do you want to be on the high score board?")
                # Sends to other function to handle destination choices and points
                totalPoints = destinationChoice(slatanLastName, totalPoints)

                # First created a file called highscores.txt to hold highscores and who set them (NEW)
                # Then, read the file to get current high score and name (NEW)
                with open("highscores.txt", "r") as infile:
                    # Reads the name of highscorer (NEW)
                    HighscoreName = infile.readline().strip()
                    # Reads highscorer's points (NEW)
                    HighscorePoints = int(infile.readline())
                    # Compares current player's points to high scores to see if to congratulate and set new score or say sorry and to try again. (NEW)
                    if totalPoints < HighscorePoints:
                        # If points not high enough they try again(NEW)
                        print(f"Sorry, you didn't beat a past Slatan's high score set by {HighscoreName} with {HighscorePoints} points. Better luck next time!")
                    else:
                        # If points are high enough they beat the high score and congratulated (NEW)
                        print(f"Congratulations, you beat the high score set by {HighscoreName} with {HighscorePoints} points! Your name and score have been added to the high score board!")

                        # Rewrites highscores.txt with new high score and name (NEW)
                        with open("highscores.txt", "w") as outfile:
                            outfile.write(f"{scoreName}\n")
                            outfile.write(f"{totalPoints}")
                        # Breaks due to error I was getting where if they kept retrying after setting a high score the game kept it as their current score (NEW)
                        break

            elif mainMenuOption == 3:
                # Quits the game after choosing to quit.
                print("Athena thanks you for your time.")
                break
            else:
                print("Invalid option, try again.")
        except ValueError:
            print("It needs to be a whole number. Try again.")
        except TypeError:
            print("You need to say something... Try again.")





# Optimized the hell out of the code
# Call main function
main()


