print("Hello! I have an exciting superhero story to share. I can't wait to tell it.")
print("Before the story begins, I have a few questions I need you to answer.")
print("After typing your answer, be sure to press the enter key.")
input("\nPress the enter key to continue...")



keepGoing = "yes"
while keepGoing.lower() == "yes":

    newValues = "no"
    while newValues.lower() == "no":

        heroName = input("\nWho is your favorite superhero:  ")
        while (len(heroName) == 0) or (len(heroName) >= 24):
            if (len(heroName) == 0):
                heroName = input("Hero cannot be blank. Please enter your favorite hero:  ")
            else:
                heroName = input("Answer is too long. Please keep answer under 24 characters:  ")
        villainName = input("\nWho is your favorite supervillain:  ")
        while (len(villainName) == 0) or (len(villainName) >= 24):
            if (len(villainName) == 0):
                villainName = input("Villain cannot be blank. Please enter your favorite villain:  ")
            else:
                villainName = input("Answer is too long. Please keep answer under 24 characters:  ")
        lastBand = input("\nWhat was the last band you listened to:  ")
        while (len(lastBand) == 0) or (len(lastBand) >= 16):
            if (len(lastBand) == 0):
                lastBand = input("Band cannot be blank. Please enter the last band you have listened to:  ")
            else:
                lastBand = input("Answer is too long. Please keep answer under 16 characters:  ")
        storeName = input("\nWhat is the closest store to you:  ")
        while (len(storeName) == 0) or (len(storeName) >= 16):
            if (len(storeName) == 0):
                storeName = input("Store cannot be blank. Please enter the closest store to you:  ")
            else:
                storeName = input("Answer is too long. Please keep answer under 16 characters:  ")
        favNum = input("\nWhat is your favorite number:  ")
        while not favNum.isdigit():
            favNum = input("Value not recognized. Please enter a numeric value:  ")
        favNum = int(favNum)
        favSoda = input("\nWhat is your favorite soda:  ")
        while (len(favSoda) == 0) or (len(favSoda) >= 16):
            if (len(favSoda) == 0):
                favSoda = input("Soda cannot be blank. Please enter your favorite soda:  ")
            else:
                favSoda = input("Answer is too long. Please keep answer under 16 characters:  ")
        newValues = input("\nDo you like your answers? Type yes to continue, or no to change your answers:  ")
        while newValues.lower() != "yes" and newValues.lower() != "no":
            newValues = input("Invalid value. Please enter yes or no:  ")

    print("\nHere we go!!!")

    keepValues = "yes"
    while keepValues.lower() == "yes":

        
        print("\nYou are very excited about the upcoming", lastBand, "concert.")
        print("The city has decided to celebrate the", favNum, "years that", heroName) 
        print("has been protecting citizens, and you can’t wait to join the")
        print("festivities. You are walking down one of the old streets in town,")
        print("as you know traffic will be a nightmare to get through otherwise.")

        print("\nAs you are walking down, you notice a strange light flicker")
        print("in an old abandoned", storeName + ". You remember that the building")
        print("has been condemned for over a year, and you find it odd that")
        print("there would be anything going on there.")

        enterStore = input("\nDo you investigate the abandoned store? Type yes or no and then press enter:  ")
        while enterStore.lower() != "yes" and enterStore.lower() != "no":
            enterStore = input("Invalid value. Please enter yes or no:  ")

        if enterStore.lower() == "yes":
            print("\nYou decide to investigate. After all, taking a quick look has")
            print("never hurt anyone before. As you enter the",storeName + ", you")
            print("discover that it is teeming with armed men. You quickly hide")
            print("behind some storage crates, realizing you have stumbled into")
            print("a lot more than you bargained for. Gratefully, no one seemed")
            print("to notice your entrance.")

            print("\nThe thought to leave quickly brushes your mind, but before you")
            print("can consider it, you hear a voice of someone speaking to the men.")
            print("You take a quick peek, and you instantly recognize", villainName +"!")
            print('“Do I have to do everything myself?” shouts',villainName + '. “We have') 
            print('only', favNum, 'minutes left, so hurry up!”')

            print("\nYou wonder what could be so important with that amount of time,")
            print("and then it suddenly dawns on you: They are planning on attacking")
            print("the concert! You know you need to warn someone, but you are also") 
            print("afraid of being caught. You see some of the henchman heading your way,")
            print("and you need to act fast!")

            
            hideSeek = input("\nDo you try to hide? Enter yes or no:  ")
            countDown = favNum
            while hideSeek.lower() != "yes" and hideSeek.lower() != "no":
                hideSeek = input("Invalid value. Please enter yes or no:  ")
            while hideSeek.lower() == "yes":
                countDown = countDown - 1
                print("\nYou continue to hide behind the boxes, and the henchmen don't seem to notice you.")
                print("You see an opporutinity to escape, though it still seems risky with the guards nearby.")
                print("However, you now only have", countDown, "minutes until", villainName, "attacks the concert!")
                if countDown <= 2:
                    break
                else:
                    hideSeek = input("\nDo you continue to hide? Enter yes or no:  ")
                    while hideSeek.lower() != "yes" and hideSeek.lower() != "no":
                        hideSeek = input("Invalid value. Please enter yes or no:  ")
            
            print("\nYou decide you cannot wait any longer and make a break for the exit.")
            print("and the henchmen seem surprised to seeyou jump out from the crates. Before")
            print("they even have a chance to react, you are already out the door and half")
            print("way down the block. You hurry over to the concert, desperate to warn anyone")
            print("and everyone about the danger. Most just laugh, believing you are just")
            print("pulling a prank.")
        else:
            print("\nYou decide it must be a demolition crew working on tearing down the old building.")
            print("You don't think anything more of it, as you realize you only have",favNum, "minutes")
            print("left before the concert starts.")
    
            print("\nYou arrive just in time for", lastBand + "'s performance. Everyone is having an amazing time.")
            print("There are many concession stands, surrounding the perimeter. There are many options available,")
            print("but you also don't want to miss out on listening to ", lastBand + ".")
            print("\nYou grab a can of", favSoda, "from one of the concession stands. It has been a while since you")
            print("have last had one, and you decide it is a good chance to get one to celebrate.")

        print("\nSuddenly there was a loud explosion! Everyone starts to panic,")
        print("as they suddenly see armed men surround them. Through the dust and")
        print("debris of the explosion, you see the vague hints of a foreboding")
        print("character. It is", villainName + ", and they appear to be in an all too")
        print("pleasing mood.")

        print("\nAs you realize the danger surrounding you, suddenly", heroName, "comes")
        print("dashing forth and takes down", villainName, "with a single punch, though only")
        print("for a moment. The rest of the henchmen seem to now start shaking in their")
        print("boots, for fear of what", heroName, "will do to them. Many still choose to take")
        print("their aim at", heroName + ". They are quickly dispatched by", heroName + ", and everyone")
        print("begins to cheer for their favorite superhero.")

        print("\nAfter taking down", villainName + "’s henchmen,", heroName, "pauses to show praise")
        print("for the crowd. As everyone continues to celebrate yet another victory for") 
        print(heroName + ", suddenly there is a loud scream.", villainName,"is back up, and they")
        print("want vengeance.", heroName," really struggles now with",villainName, "now that they")
        print("no longer have the surprise. Many make a quick dash away as the battle becomes")
        print("really heated, and you wonder whether", heroName, "will be able to beat", villainName, "this time.")

        helpHero = input("\nDo you help the hero? Type yes or no and then press enter:  ")
        while helpHero.lower() != "yes" and helpHero.lower() != "no":
            helpHero = input("Invalid value. Please enter yes or no:  ")

        if helpHero.lower() == "yes":

            print("\nYou notice a can of", favSoda, "near you, and you decide you would rather do")
            print("something to help than to flee away. You pick up the can, and you throw it")
            print("at", villainName + ", who is clearly disrupted by it. You begin to freeze")
            print("as", villainName, "turns his attention towards you, but you stand your")
            print("ground anyways. Just as you fear it may be all over for you,", heroName)
            print("comes from behind and takes out", villainName, "once and for all.")
        else:
            print("\nYou decide to flee the scene before anything ends up happening to you.")
            print("after all, you are just an ordinary citizen, and you can't do much") 
            print("compared to the likes of", heroName + ". You decide to make your escape")
            print("through the concession stands, spilling", favSoda, "all over the ground.")
            print("You manage to escape and arrive at home. You turn on the news to hear what")
            print("happened since you left, and", heroName, "was able to defeat ")
            print(villainName + ", and the city is safe once again.")

        if enterStore.lower() == "yes" and helpHero.lower() == "yes":
            print("\nAfter spending a fantastic day discovering", villainName + "’s plans")
            print("and helping", heroName, "to save the day, you have been awarded")
            print("the medal of bravery by the city for your actions. With the")
            print("concert up and running again, you get to watch", lastBand, "perform")
            print("from the front row, a perfect way to end the night.")
        elif helpHero.lower() == "yes":
            print("\nAfter helping to thwart", villainName + "'s plans, you are recognized")
            print("by the city for your bravery. You are glad you could be in the right place")
            print("at the right time. You decide to enjoy the concert, and hope that things")
            print("return to normal soon.")
        else:
            print("\nAfter the attack at the concert by ", villainName + ", you are grateful")
            print("for heroes like", heroName + ". You decide to enjoy the rest of the concert")
            print("at home, where it's safe. You have had enough adventure for a lifetime")
            print("and feel it is best to stick to places you know.")
     
        keepGoing = input("\nDo you wish to play again? Enter yes or no:  ")
        while keepGoing.lower() != "yes" and keepGoing.lower() != "no":
            keepGoing = input("Invalid value. Please enter yes or no:  ")

        if keepGoing.lower() == "yes":
            keepValues = input("\n Do you wish to keep the same answers? Enter yes or no:  ")
            while keepValues.lower() != "yes" and keepValues.lower() != "no":
                keepValues = input("Invalid value. Please enter yes or no:  ")
        else:
            keepValues = "no"

print("\nThank you for playing!")
