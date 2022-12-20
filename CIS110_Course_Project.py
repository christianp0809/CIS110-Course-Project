import sys
import time

def slowprint(string):
    for char in range(len(string)):
        print(string[char], end="")
        time.sleep(1./100)

slowprint("Hello! I have an exciting superhero story to share. I can't wait to tell it.")
slowprint("\nBefore the story begins, I have a few questions I need you to answer.")
slowprint("\nAfter typing your answer, be sure to press the enter key.")
input("\n\nPress the enter key to continue...")


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
        while (len(lastBand) == 0) or (len(lastBand) >= 20):
            if (len(lastBand) == 0):
                lastBand = input("Band cannot be blank. Please enter the last band you have listened to:  ")
            else:
                lastBand = input("Answer is too long. Please keep answer under 20 characters:  ")
        storeName = input("\nWhat is the closest store to you:  ")
        while (len(storeName) == 0) or (len(storeName) >= 20):
            if (len(storeName) == 0):
                storeName = input("Store cannot be blank. Please enter the closest store to you:  ")
            else:
                storeName = input("Answer is too long. Please keep answer under 20 characters:  ")
        favNum = input("\nWhat is your favorite number:  ")
        while not favNum.isdigit():
            favNum = input("Value not recognized. Please enter a numeric value:  ")
        favSoda = input("\nWhat is your favorite soda:  ")
        while (len(favSoda) == 0) or (len(favSoda) >= 20):
            if (len(favSoda) == 0):
                favSoda = input("Soda cannot be blank. Please enter your favorite soda:  ")
            else:
                favSoda = input("Answer is too long. Please keep answer under 20 characters:  ")
        newValues = input("\nDo you like your answers? Type yes to continue, or no to change your answers:  ")
        while newValues.lower() != "yes" and newValues.lower() != "no":
            newValues = input("Invalid value. Please enter yes or no:  ")

    slowprint("\nHere we go!!!\n")

    keepValues = "yes"
    while keepValues.lower() == "yes":

        
        slowprint("\nYou are very excited about the upcoming " + lastBand + " concert.")
        slowprint("\nThe city has decided to celebrate the " + favNum + " years that " + heroName) 
        slowprint("\nhas been protecting citizens, and you can’t wait to join the")
        slowprint("\nfestivities. You are walking down one of the old streets in town,")
        slowprint("\nas you know traffic will be a nightmare to get through otherwise.")

        slowprint("\n\nAs you are walking down, you notice a strange light flicker")
        slowprint("\nin an old abandoned " + storeName + ". You remember that the building")
        slowprint("\nhas been condemned for over a year, and you find it odd that")
        slowprint("\nthere would be anything going on there.")

        enterStore = input("\n\nDo you investigate the abandoned store? Type yes or no and then press enter:  ")
        while enterStore.lower() != "yes" and enterStore.lower() != "no":
            enterStore = input("Invalid value. Please enter yes or no:  ")

        if enterStore.lower() == "yes":
            slowprint("\nYou decide to investigate. After all, taking a quick look has")
            slowprint("\nnever hurt anyone before. As you enter the " + storeName + ", you")
            slowprint("\ndiscover that it is teeming with armed men. You quickly hide")
            slowprint("\nbehind some storage crates, realizing you have stumbled into")
            slowprint("\na lot more than you bargained for. Gratefully, no one seemed")
            slowprint("\nto notice your entrance.")

            slowprint("\n\nThe thought to leave quickly brushes your mind, but before you")
            slowprint("\ncan consider it, you hear a voice of someone speaking to the men.")
            slowprint("\nYou take a quick peek, and you instantly recognize " + villainName +"!")
            slowprint('\n“Do I have to do everything myself?” shouts ' + villainName + '. “We have') 
            slowprint('\nonly ' + favNum + ' minutes left, so hurry up!”')

            slowprint("\n\nYou wonder what could be so important with that amount of time,")
            slowprint("\nand then it suddenly dawns on you: They are planning on attacking")
            slowprint("\nthe concert! You know you need to warn someone, but you are also") 
            slowprint("\nafraid of being caught. You see some of the henchman heading your way,")
            slowprint("\nand you need to act fast!")

            
            hideSeek = input("\n\nDo you try to hide? Enter yes or no:  ")
            favNum = int(favNum)
            countDown = favNum
            favNum = str(favNum)
            while hideSeek.lower() != "yes" and hideSeek.lower() != "no":
                hideSeek = input("Invalid value. Please enter yes or no:  ")
            while hideSeek.lower() == "yes":
                countDown = countDown - 1
                countDown = str(countDown)

                slowprint("\nYou continue to hide behind the boxes, and the henchmen don't seem to notice you.")
                slowprint("\nYou see an opportunity to escape, though it still seems risky with the guards nearby.")
                slowprint("\nHowever, you now only have " + countDown + " minutes until " + villainName + " attacks the concert!")
                countDown = int(countDown)
                if countDown <= 2:
                    break
                else:
                    hideSeek = input("\n\nDo you continue to hide? Enter yes or no:  ")
                    while hideSeek.lower() != "yes" and hideSeek.lower() != "no":
                        hideSeek = input("Invalid value. Please enter yes or no:  ")
            
            slowprint("\nYou decide you cannot wait any longer and make a break for the exit.")
            slowprint("\nand the henchmen seem surprised to seeyou jump out from the crates. Before")
            slowprint("\nthey even have a chance to react, you are already out the door and half")
            slowprint("\nway down the block. You hurry over to the concert, desperate to warn anyone")
            slowprint("\nand everyone about the danger. Most just laugh, believing you are just")
            slowprint("\npulling a prank.")
        else:
            slowprint("\nYou decide it must be a demolition crew working on tearing down the old building.")
            slowprint("\nYou don't think anything more of it, as you realize you only have " + favNum + " minutes")
            slowprint("\nleft before the concert starts.")
    
            slowprint("\n\nYou arrive just in time for " + lastBand + "'s performance. Everyone is having an amazing time.")
            slowprint("\nThere are many concession stands, surrounding the perimeter. There are many options available,")
            slowprint("\nbut you also don't want to miss out on listening to " + lastBand + ".")
            slowprint("\n\nYou grab a can of " + favSoda + " from one of the concession stands. It has been a while since you")
            slowprint("\nhave last had one, and you decide it is a good chance to get one to celebrate.")

        slowprint("\n\nSuddenly there was a loud explosion! Everyone starts to panic,")
        slowprint("\nas they suddenly see armed men surround them. Through the dust and")
        slowprint("\ndebris of the explosion, you see the vague hints of a foreboding")
        slowprint("\ncharacter. It is " + villainName + ", and they appear to be in an all too")
        slowprint("\npleasing mood.")

        slowprint("\n\nAs you realize the danger surrounding you, suddenly " + heroName + " comes")
        slowprint("\ndashing forth and takes down " + villainName + " with a single punch, though only")
        slowprint("\nfor a moment. The rest of the henchmen seem to now start shaking in their")
        slowprint("\nboots, for fear of what " + heroName + " will do to them. Many still choose to take")
        slowprint("\ntheir aim at " + heroName + ". They are quickly dispatched by " + heroName + ", and everyone")
        slowprint("\nbegins to cheer for their favorite superhero.")

        slowprint("\n\nAfter taking down " + villainName + "’s henchmen, " + heroName + " pauses to show praise")
        slowprint("\nfor the crowd. As everyone continues to celebrate yet another victory for") 
        slowprint("\n" + heroName + ", suddenly there is a loud scream. " + villainName + " is back up, and they")
        slowprint("\nwant vengeance. " + heroName + " really struggles now with " + villainName + " now that they")
        slowprint("\nno longer have the surprise. Many make a quick dash away as the battle becomes")
        slowprint("\nreally heated, and you wonder whether " + heroName + " will be able to beat " + villainName + " this time.")

        helpHero = input("\n\nDo you help the hero? Type yes or no and then press enter:  ")
        while helpHero.lower() != "yes" and helpHero.lower() != "no":
            helpHero = input("Invalid value. Please enter yes or no:  ")

        if helpHero.lower() == "yes":

            slowprint("\nYou notice a can of " + favSoda + " near you, and you decide you would rather do")
            slowprint("\nsomething to help than to flee away. You pick up the can, and you throw it")
            slowprint("\nat " + villainName + ", who is clearly disrupted by it. You begin to freeze")
            slowprint("\nas " + villainName + " turns his attention towards you, but you stand your")
            slowprint("\nground anyways. Just as you fear it may be all over for you, " + heroName)
            slowprint("\ncomes from behind and takes out " + villainName + " once and for all.")
        else:
            slowprint("\nYou decide to flee the scene before anything ends up happening to you.")
            slowprint("\nafter all, you are just an ordinary citizen, and you can't do much") 
            slowprint("\ncompared to the likes of " + heroName + ". You decide to make your escape")
            slowprint("\nthrough the concession stands, spilling " + favSoda + " all over the ground.")
            slowprint("\nYou manage to escape and arrive at home. You turn on the news to hear what")
            slowprint("\nhappened since you left, and " + heroName + " was able to defeat ")
            slowprint("\n" + villainName + ", and the city is safe once again.")

        if enterStore.lower() == "yes" and helpHero.lower() == "yes":
            slowprint("\n\nAfter spending a fantastic day discovering " + villainName + "’s plans")
            slowprint("\nand helping " + heroName + " to save the day, you have been awarded")
            slowprint("\nthe medal of bravery by the city for your actions. With the")
            slowprint("\nconcert up and running again, you get to watch " + lastBand + " perform")
            slowprint("\nfrom the front row, a perfect way to end the night.")
        elif helpHero.lower() == "yes":
            slowprint("\n\nAfter helping to thwart " + villainName + "'s plans, you are recognized")
            slowprint("\nby the city for your bravery. You are glad you could be in the right place")
            slowprint("\nat the right time. You decide to enjoy the concert, and hope that things")
            slowprint("\nreturn to normal soon.")
        else:
            slowprint("\n\nAfter the attack at the concert by " + villainName + ", you are grateful")
            slowprint("\nfor heroes like " + heroName + ". You decide to enjoy the rest of the concert")
            slowprint("\nat home, where it's safe. You have had enough adventure for a lifetime")
            slowprint("\nand feel it is best to stick to places you know.")
     
        keepGoing = input("\n\nDo you wish to play again? Enter yes or no:  ")
        while keepGoing.lower() != "yes" and keepGoing.lower() != "no":
            keepGoing = input("Invalid value. Please enter yes or no:  ")

        if keepGoing.lower() == "yes":
            keepValues = input("\n Do you wish to keep the same answers? Enter yes or no:  ")
            while keepValues.lower() != "yes" and keepValues.lower() != "no":
                keepValues = input("Invalid value. Please enter yes or no:  ")
        else:
            keepValues = "no"

slowprint("\nThank you for playing!\n\n")
