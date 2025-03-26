
def spawnroom():
    print("You awaken in a room. There is a dimly lit torch on a wall to your left side, but otherwise there is no lighting. There is a door in front of you as well as one to your left.")
    print("What shall you do? \n 1. Enter the room in front of you \n 2. Enter the room to your left \n 3. Stand \n 4. Inspect the room \n 5. Sit down \n 6. ??? \n 7. Quit")
    actions = ["Enter the room in front of you","Enter the room to your left","Stand","Inspect the room", "Sit down", "???", "Quit"]
    actions = input()
    if actions == "Enter the room in front of you":
        room1()
    elif actions == "Enter the room to your left":
        room2()
    elif actions == "Stand":
        print("Nothing happens.")
        spawnroom()
    elif actions == "Inspect the room":
        print("You look around the room for any possible clues. However, all you can find is a dimly lit torch engraved to the wall.")
        spawnroom()
    elif actions == "Sit down":
        print("You simply sit down. Nothing happens.")
        spawnroom()
    elif actions == "???":
        ALEXCLARKBOSSFIGHT()
    elif actions == "Quit":
        return
    elif actions != "":
        print("Invalid command.")
        spawnroom()

def room1():
    print("You entered the room in front of you.")
    print("You look around the room. You notice another torch hanging on the wall on your left. On your right, you notice a dull blade. There is also a door in front of you.")
    print("What shall you do? \n 1. Dance \n 2. Pick up the dull sword \n 3. Sit down \n 4. Go toward the door in front of you \n 5. Go back to the original room \n 6. Quit")
    room1actions = ["Dance", "Pick up the dull sword", "Sit down", "Go toward the door in front of you", "Go back to the original room" , "Quit"]
    room1actions = input()
    if room1actions == "Dance":
        print("You danced.")
        room1()
        return
    elif room1actions == "Pick up the dull sword":
        print("You simply picked up the dull sword. You don't know what you're going to do with it, but it provides you protecion.")
        room1()
    elif room1actions == "Sit down":
        print("You simply sit down. Nothing happens. What did you think was going to happen?")
        room1()
    elif room1actions == "Go toward the door in front of you":
        print("You walk over towards the door in front of you. And suddenly a ray of sunlight lands across your face. You look around as your visions come back. Trees, birds, rivers, grass. You're finally free.")
        return
    elif room1actions == "Go back to the original room":
        print("You head back to the original room.")
        spawnroom()
    elif room1actions == "Quit":
        return
    elif room1actions != "":
        print("Invalid command.")
        room1()

def room2():
    print("You entered the room to your left.")
    print("As soon as you walked into the room you notice a massive cobra in front of you.")
    print("The cobra looks very menacing... \n 1. Fight it with your fist \n 2. Attempt to befriend the Cobra \n 3. Run back to the original room \n 4. Begin crying \n 5. Sit down \n 6. Quit")
    room2actions = ["Fight it with your fist", "Attempt to befriend the Cobra", "Run back to the original room", "Begin crying", "Sit down", "Quit"]
    room2actions = input()
    if room2actions == "Fight it with your fist":
        print("You charged at the Cobra and landed your fist against the ferocious snake. The Cobra backs up as if it seems scared. However it fooled you and landed a attack on you. \nSince you didn't expect the attack you fail to withstand the attack and unfortnately that is the end for you.")
        return
    elif room2actions == "Attempt to befriend the Cobra":
        print("You greet them and offered a handshake to the Cobra. Suprisingly, the cobra accepts your handshake and uses it's head as a form of handshake.")
        print("You spend plenty of time together playing fetch that you found on the ground and eventually, the both of you found the way out. You sucessfully escape with the cobra.")
        return
    elif room2actions == "Run back to the original room":
        print("In a state of panic, you quickly rush back to the room and slammed the door behind you.")
        spawnroom()
    elif room2actions == "Begin crying":
        print("You suddenly starts crying due to the fact you were so scared you didn't know what to do. Suddenly the Cobra comes up to you and comforts you.")
        print("You stop crying and start to smile. The Cobra did not mean any harm, and tells you the way out of the place.")
        print("You follow behind the Cobra as it leads you to the other room and the door within it. You open the doors and suddenly you feel the rain drops onto your face. You're free.")
        print("You made it to the real world.")
        return
    elif room2actions == "Sit down":
        print("You sat down. The cobra continues to stare at you as it's waiting for your first move.")
        room2()
    elif room2actions == "Quit":
        return
    elif room2actions != "":
        print("Invalid command.")
        room2()

def ALEXCLARKBOSSFIGHT():
    print("You discover a hidden trap door at the very corner of the room.")
    print("You open up the trap door.")
    print("You discover a ladder that leads to somewhere. Where could that possibly go to? With your curiosity in mind, you climb down the ladder. \n . \n . \n .")
    print("You look around the room, but there is one thing that truly concerns you.")
    print("Alex Clark, the very person himself.")
    print("His face does not look happy. I think he wants to eliminate you idk")
    print("What do you do? \n 1. Challenge him to a quiz \n 2. Bring out a golden sword that suddenly came out of your pocket and get ready to take action \n 3. Run")
    bossfight = ["Challenge him to a quiz", "Bring out a golden sword that suddenly came out of your pocket and get ready to take action", "Run"]
    bossfight = input()
    if bossfight == "Challenge him to a quiz":
        bossfightquiz()
    elif bossfight == "Run":
        print("Did you actually think you could run away from Alex? You turn around attempt to climb the ladder. As soon as you got up back to the original room, you notice Alex standing right in front of you.")
        print("You realize this is your demise. You can never outrun Alex Clark.")
        return
    elif bossfight == "Bring out a golden sword that suddenly came out of your pocket and get ready to take action":
        print("Alex:(Heh. You really think you stand any chance against me?) He laughs for a good 30 seconds before coming to a straight face. Suddenly, your weapon disappears.")
        print("What do you do now? Alex really taunted you. \n 1. Beg for mercy. \n 2. Challenge him to a quiz \n 3. Run \n 4. Quit")
        choices2 = ["Beg for mercy", "Challenge him to a quiz", "Run", "Quit"]
        choices2 = input()
        if choices2 == "Beg for mercy":
            print("Alex laughs at you again.")
            print("Alex:(Alright. It's time to get serious. No mister nice guy.)")
            print("He puts you out of your misery.")
            return
        if choices2 == "Challenge him to a quiz":
            bossfightquiz()
        if choices2 == "Run":
            print("Did you actually think you could run away from Alex? You turn around attempt to climb the ladder. As soon as you got up back to the original room, you notice Alex standing right in front of you.")
            print("You realize this is your demise. You can never outrun Alex Clark.")
            return
        if choices2 == "Quit":
            return
        if choices2 != "":
            print("Invalid command.")
            ALEXCLARKBOSSFIGHT()



def bossfightquiz():
    print("I think you severely underestimated Alex's intellectual.")  
    print("You both decided that you both will take turns asking each other questions until someone answer a question incorrectly. If you answer a question incorrectly, you lose.")
    print("Alex:(Who was the first person to dress up as Santa and started the tradition of mall Santas?)")
    print("Here is your options. \n 1. James Edgar \n 2. Otis Rozema \n 3. Saint John \n 4. Mr. Price \n 5. Jacob Pincher \n 6. Vincent Vuong \n 7. Bobby Fisher \n 8. Parth Chaudhari \n 9. Tyler Blevins \n 10. Stuart Perry \n 11. Quit")
    quizquestion1 = ["James Edgar", "Otis Rozema", "Saint John", "Mr. Price", "Jacob Pincher", "Vincent Vuong", "Bobby Fisher", "Parth Chaudhari", "Tyler Blevins", "Stuart Perry", "Quit"]
    quizquestion1 = input()
    if quizquestion1 == "Quit":
        return
    if quizquestion1 == "James Edgar":
        print("Correct!")
        print("You gave him of what you think a equally hard question for Alex. But to your suprise, he answers you within milliseconds.")
        print("Alex:(My turn again!) You notice his smile begins to widen.")
        print("Alex:(How many times have I blinked during the lifetime of my existence?)")
        quizquestion2 = int(79432931)
        quizquestion2 = input()
        if quizquestion2 == "Quit":
            return
        else:
            print("Alex:(Heh, just as I expected. I'll see you off then.)")
            print("You look at your arms and suddenly you notice that you hands are fading away. Looks like this is your end. Goodbye world.")
            return
    else:
        print("WRONG. You suffered intellectal loss against Alex, and therefore lost. Alex once again stand victorous.")
        return



spawnroom()
