print("Hello! I have an exciting superhero story to share. I can't wait to tell it.")
print("Before the story begins, I have a few questions I need you to answer.")
print("After typing your answer, be sure to press the enter key.")
input("\nPress the enter key to continue...")

heroName = input("\nWho is your favorite superhero:  ")
villainName = input("\nWho is your favorite supervillain:  ")
lastBand = input("\nWhat was the last band you listened to:  ")
storeName = input("\nWhat is the closest store to you:  ")
favNum = input("\nWhat is your favorite number:  ")
favSoda = input("\nWhat is your favorite soda:  ")

print("\nHere we go!!!")

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
    print("and then it suddenly dawns on you: He is planning on attacking")
    print("the concert! You hurry over to the concert, desperate to warn anyone")
    print("and everyone about the danger. Most just laugh, believing it was")
    print("just another person pulling a prank.")
else:
    print("\nYou decide it must be a demolition crew working on tearing down the old building.")
    print("You don't think anything more of it, as you realize you only have",favNum, "minutes")
    print("left before the concert starts.")
    
    print("\nYou arrive just in time for", lastBand + "'s performance. Everyone is having an amazing time,")
    print("and you grab a", favSoda, "from one of the concession stands. You feel that nothing could be more")
    print("exciting than this!")

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

print("\nAfter taking down", villainName + "’s henchmen, heroName pauses to show praise")
print("for the crowd. As everyone continues to celebrate yet another victory for") 
print(heroName, "suddenly there is a loud scream.", villainName,"is back up, and they")
print("want vengeance.", heroName," really struggles now with",villainName, "now that they")
print("no longer have the surprise. Many make a quick dash away as the battle becomes")
print("really heated, and you wonder whether", heroName, "will be able to beat", villainName, "this time.")

helpHero = input("\nDo you help the hero? Type yes or no and then press enter:  ")

if helpHero.lower() == "yes":

    print("\nYou notice a can of", favSoda, "near you, and you decide you would rather do")
    print("something to help than to flee away. You pick up the can, and you throw it")
    print("at", villainName + ", who is clearly disrupted by it. You begin to freeze")
    print("as", villainName, "turns his attention towards you, but you stand your")
    print("ground anyways. Just as you fear it may be all over for you,", heroName)
    print("comes from behind and takes out", villainName, "once and for all.")
else:
    print("\nYou decide to flee the scene before anything ends up happening to you.")
    print("after all, you are just and ordinary citizen, and you can't do much") 
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
    print("and feel it is best to stick to place you know.")

