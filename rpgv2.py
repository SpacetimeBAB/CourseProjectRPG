# Jeremías Branger
# Date: 3/8/26
# Course project RPG

#        PSEUDOCODE:
# Define main function
# Declare constants for options
# Declare constants for slatan's last name
# Declare constant for destination choice
# Declare constant for total points
# Display introduction to RPG and show game title Slatan
# Give Main Menu and give options to choose
# Depending on option chosen give output
# If choose rules send to rules and then back to main menu
# If choose to start game then prompt for name and begin adventure
# Send to destination to help out
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
# Calls main function


def main():
      mainMenuOption = totalPoints = destination = dragonChoice = destination2 = destination3 = 0
      slatanLastName = ""


      # Display introduction to RPG and show game title Slatan
      print("-" * 7, "", "Slatan", "", "-" * 7)
      print("Once upon a time, in a world long, long ago \n"
            "There was a hero named 'Slatan'!")

      # Give Main Menu and give options to choose
      mainMenuOption = int(input("     [1] Rules\n"
                                 "     [2] Start your adventure\n"
                                 "     [3] Quit Game"))
      # Depending on option chosen give output
      # If choose rules send to rules and then back to main menu
      if mainMenuOption == 1:
            print("Never, ever say the name of 'Drea the Goddess'\n"
                  "Furthermore, never look the big Swan in the eyes\n"
                  "If you ever get scared say the name of Slatan's love Athena to quit the game!")

      # If choose to start game then prompt for name and begin adventure
      elif mainMenuOption == 2:
            slatanLastName = input("What shall Slatan's last name be?")

            # Adventure begins and present lore
            print(f"Hello Slatan {slatanLastName}, welcome to the Gork, the land of wonder.\n"
                  f"In this land of wonder, there are many dangers and threats that you can slay\n\n")

            destination = int(input("Oh great hero, who would you want to help out?:\n"
                                    "     [1] Villagers in Portsmouth being attacked by a Dragon\n"
                                    "     [2] Elves in Regal Bay who's Queen was kidnapped\n"
                                    "     [3] Dwarves suffering a Plague\n\n"))

            # Send to destination to help out
            # Chooses to go to Portsmouth
            if destination == 1:
                  print("You arrive to Portsmouth and see the dragon spouting fire all over the village!")
                  totalPoints +=100
                  print(f"Total points: {totalPoints}")

                  # Choose what to do about the dragon
                  dragonChoice = int(input(f"What will Slatan {slatanLastName} the great do?\n"
                                         f"     [1] Befriend the dragon and become a dragonmaster\n"
                                         f"     [2] Grab your trusty Axe 'Mikael' and slay the dragon\n"
                                         f"     [3] Do nothing and go to the town tavern\n\n"))
                  # Chooses peace
                  if dragonChoice == 1:
                        print(f"You spend hours showing it there's peace in the world and it finally lets you ride it and now you are known as Slatan {slatanLastName}, The Dragonmaster!\n")
                        print("You have saved the village from its danger!\n\n")
                        totalPoints += 1000
                        print(f"Total points: {totalPoints}")

                        # Send to other destinations
                        destination2 = int(input(f"What will Slatan {slatanLastName} do now?\n"
                                                 f"[1] Help the elves in Regal Bay who's Queen was kidnapped\n"
                                                 f"[2] Help dwarves suffering a Plague\n\n"))
                        # Choose to save elves
                        if destination2 == 1:
                            print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                  "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                            totalPoints += 500
                            print(f"Total points: {totalPoints}")

                            destination3 = int(input("Now what?\n"
                                                     "[1] Save the Dwarves from the plague\n"
                                                     "[2] Take a break from saving people\n\n"))
                            if destination3 == 1:
                                print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                                totalPoints += 600
                                print(f"Total points: {totalPoints}")
                            elif destination3 == 2:
                                print("You take a break while the dwarves suffer")
                                totalPoints -= 100
                                print(f"Total points: {totalPoints}")
                            else:
                                print("Invalid selection, Drea the Goddess frowns on you.")
                        elif destination2 == 2:
                            print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                            totalPoints += 600
                            print(f"Total points: {totalPoints}")

                            destination3 = int(input("Now what?\n"
                                                     "[1] Help the elves in Regal Bay\n"
                                                     "[2] Take a break from saving people\n\n"))

                            if destination3 == 1:
                                print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                      "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                                totalPoints += 500
                                print(f"Total points: {totalPoints}")
                            elif destination3 == 2:
                                print("You take a break while the elves suffer")
                                totalPoints -= 100
                                print(f"Total points: {totalPoints}")
                            else:
                                print("Invalid selection, Drea the Goddess frowns on you.")

                        else:
                            print("Invalid selection, Drea the Goddess frowns on you.")

                  elif dragonChoice == 2:
                      print("After a long ardeous battle, you finally reach the dragon's weakpoint on its neck and boom, the head plops off!\n")
                      print("You have saved the village from its danger! However killing the dragon has made Drea the Goddess mad.\n\n")
                      totalPoints +=600
                      print(f"Total points: {totalPoints}")

                      destination2 = int(input(f"What will Slatan {slatanLastName} do now?\n"
                                               f"[1] Help the elves in Regal Bay who's Queen was kidnapped\n"
                                               f"[2] Help dwarves suffering a Plague\n\n"))

                      if destination2 == 1:
                          print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                          totalPoints += 500
                          print(f"Total points: {totalPoints}")

                          destination3 = int(input("Now what?\n"
                                                   "[1] Save the Dwarves from the plague\n"
                                                   "[2] Take a break from saving people\n\n"))
                          if destination3 == 1:
                              print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                              totalPoints += 600
                              print(f"Total points: {totalPoints}")
                          elif destination3 == 2:
                              print("You take a break while the dwarves suffer")
                              totalPoints -= 100
                              print(f"Total points: {totalPoints}")
                          else:
                              print("Invalid selection, Drea the Goddess frowns on you.")
                      elif destination2 == 2:
                          print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                          totalPoints += 600
                          print(f"Total points: {totalPoints}")

                          destination3 = int(input("Now what?\n"
                                                   "[1] Help the elves in Regal Bay\n"
                                                   "[2] Take a break from saving people\n\n"))

                          if destination3 == 1:
                              print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                    "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                              totalPoints += 500
                              print(f"Total points: {totalPoints}")
                          elif destination3 == 2:
                              print("You take a break while the elves suffer")
                              totalPoints -= 100
                              print(f"Total points: {totalPoints}")
                          else:
                              print("Invalid selection, Drea the Goddess frowns on you.")
                      else:
                          print("Invalid selection, Drea the Goddess frowns on you.")

                  elif dragonChoice == 3:
                      print("The village burns and you are a terrible person.\n")
                      totalPoints -= 200
                      print(f"Total points: {totalPoints}")

                      destination2 = int(input(f"What will Slatan {slatanLastName} do now?\n"
                                               f"[1] Help the elves in Regal Bay who's Queen was kidnapped\n"
                                               f"[2] Help dwarves suffering a Plague\n\n"))

                      if destination2 == 1:
                          print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                          totalPoints += 500
                          print(f"Total points: {totalPoints}")

                          destination3 = int(input("Now what?\n"
                                                   "[1] Save the Dwarves from the plague\n"
                                                   "[2] Take a break from saving people\n\n"))
                          if destination3 == 1:
                              print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                              totalPoints += 600
                              print(f"Total points: {totalPoints}")
                          elif destination3 ==2:
                              print("You take a break while the dwarves suffer")
                              totalPoints -= 100
                              print(f"Total points: {totalPoints}")
                          else:
                              print("Invalid selection, Drea the Goddess frowns on you.")
                      elif destination2 == 2:
                          print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                          totalPoints += 600
                          print(f"Total points: {totalPoints}")

                          destination3 = int(input("Now what?\n"
                                                   "[1] Help the elves in Regal Bay\n"
                                                   "[2] Take a break from saving people\n\n"))

                          if destination3 == 1:
                              print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                    "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                              totalPoints += 500
                              print(f"Total points: {totalPoints}")
                          elif destination3 == 2:
                              print("You take a break while the elves suffer")
                              totalPoints -= 100
                              print(f"Total points: {totalPoints}")
                          else:
                              print("Invalid selection, Drea the Goddess frowns on you.")

                      else:
                          print("Invalid selection, Drea the Goddess frowns on you.")



            # Chooses to go to save the Elves
            elif destination == 2:
                  print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                        "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                  totalPoints +=500
                  print(f"Total points: {totalPoints}")

                  destination2 = int(input(f"What will Slatan {slatanLastName} do now?\n"
                                           f"[1] Help the villagers in Portsmouth from the Dragon\n"
                                           f"[2] Save the Dwarves from the Plague\n\n"))

                  if destination2 == 1:
                      print("You arrive to Porstmouth and slay the dragon saving everyone")
                      totalPoints += 600
                      print(f"Total points: {totalPoints}")

                      destination3 = int(input("Now what?\n"
                                               "[1] Cure the Dwarves\n"
                                               "[2] Take a break from saving people\n\n"))
                      if destination3 == 1:
                          print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                          totalPoints += 600
                          print(f"Total points: {totalPoints}")
                      elif destination3 == 2:
                          print("You take a break while the everyone suffers")
                          totalPoints -= 100
                          print(f"Total points: {totalPoints}")
                      else:
                          print("Invalid selection, Drea the Goddess frowns on you.")
                  elif destination2 == 2:
                      print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                      totalPoints += 600
                      print(f"Total points: {totalPoints}")

                      destination3 = int(input("Now what?\n"
                                               "[1] Help the villagers from the dragon\n"
                                               "[2] Take a break from saving people\n\n"))

                      if destination3 == 1:
                          print("You arrive to Porstmouth and slay the dragon saving everyone")
                          totalPoints += 600
                          print(f"Total points: {totalPoints}")
                      elif destination3 == 2:
                          print("You take a break while the everyone suffers")
                          totalPoints -= 100
                          print(f"Total points: {totalPoints}")
                      else:
                          print("Invalid selection, Drea the Goddess frowns on you.")

                  else:
                      print("Invalid selection, Drea the Goddess frowns on you.")

            # Chooses to go save the Dwarves
            elif destination == 3:
                print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")
                totalPoints += 600
                print(f"Total points: {totalPoints}")

                destination2 = int(input(f"What will Slatan {slatanLastName} do now?\n"
                                         f"[1] Help the villagers in Portsmouth from the Dragon\n"
                                         f"[2] Help the elves from their missing queen\n\n"))

                if destination2 == 1:
                    print("You arrive to Porstmouth and slay the dragon saving everyone")
                    totalPoints += 600
                    print(f"Total points: {totalPoints}")

                    destination3 = int(input("Now what?\n"
                                             "[1] Save the elves' queen\n"
                                             "[2] Take a break from saving people\n\n"))
                    if destination3 == 1:
                        print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                                "You follow some trails left behind by the kidnappers and bring the queen to justice!")
                        totalPoints += 500
                        print(f"Total points: {totalPoints}")
                    elif destination3 == 2:
                        print("You take a break while the everyone suffers")
                        totalPoints -= 100
                        print(f"Total points: {totalPoints}")
                    else:
                        print("Invalid selection, Drea the Goddess frowns on you.")
                elif destination2 ==2:
                    print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                        "You follow some trails left behin""d by the kidnappers and bring the queen to justice!")
                    totalPoints += 500
                    print(f"Total points: {totalPoints}")

                    destination3 = int(input("Now what?\n"
                                             "[1] Help the villagers from the dragon\n"
                                             "[2] Take a break from saving people\n\n"))

                    if destination3 == 1:
                        print("You arrive to Porstmouth and slay the dragon saving everyone")
                        totalPoints += 600
                        print(f"Total points: {totalPoints}")
                    elif destination3 ==2:
                        print("You take a break while the everyone suffers")
                        totalPoints -= 100
                        print(f"Total points: {totalPoints}")
                    else:
                        print("Invalid selection, Drea the Goddess frowns on you.")
                else:
                    print("Invalid selection, Drea the Goddess frowns on you.")

            else:
                print("Invalid selection, Drea the Goddess frowns on you.")






      # If doesn't choose any of the other 2 then assumes they want to quit game
      else:
            print("Athena thanks you for your time.")






# I know there's definetly ways to optimize this code but didn't know how
# Call main function
main()


