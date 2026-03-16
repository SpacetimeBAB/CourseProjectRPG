# Jeremías Branger
# Date: 2/21/26
# Course project RPG


def main():
      mainMenuOption = 0
      slatanLastName = ""
      destination = 0

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
                  print(f"Slatan {slatanLastName} the great grabs his trusty axe Mikael and saves the village!")
               # dragonChoice = int(input(f"What will Slatan {slatanLastName} the great do?\n"
                #                         f"     [1] Befriend the dragon and become a dragonmaster\n"
                 #                        f"     [2] Grab your trust Axe 'Mikael' and slay the dragon\n"
                 #                        f"     [3] Do nothing and go to the town tavern\n\n"))

            # Chooses to go to save the Elves
            elif destination == 2:
                  print("You reach Regal Bay and see the despair in everyone's eyes.\n"
                        "You follow some trails left behind by the kidnappers and bring the queen to justice!")

            # Chooses to go save the Dwarves
            else:
                  print("You arrive to the Dwarves lair and bring an antidote to cure everyone, hooray!")






      # If doesn't choose any of the other 2 then assumes they want to quit game
      else:
            print("Athena thanks you for your time.")







main()


