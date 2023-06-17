import cv2 #cv2: opencv
import cvzone #cvzone: gives us access to more detection, and will allow us to easily identify hand shapes
from cvzone.HandTrackingModule import HandDetector
import time
import random

#instantiates timer, whether the round has started, and if the round has a winner/loser/draw
start = False
result = False
playerS = 0
aiS = 0
preHands = None
randAi = None
timer = 0

initialTime = 0

#captures video; "0" signifies which webcam we want to use, since some PCs have multiple cameras
#also resizes to 360x360
webcam = cv2.VideoCapture(0)
webcam.set(3,640)
webcam.set(4,480)

hand = HandDetector(maxHands= 1) #establishes the maximum amount of hands that we can detect, in this case we don't want more than 1.

while True:
    #reads video frame by frame, stores it in the boolean "boolean", and displays it
    boolean, video = webcam.read()
    bkg = cv2.imread("final/background.jpg")

    #resizes webcam and embeds it in the background
    webScaled = cv2.resize(video, (480,360))
    webScaled = webScaled[:,60:420]
    bkg[312:672, 872:1232] = webScaled 

    #checks if there is a hand in the webcam, displays on screen
    hands, video = hand.findHands(webScaled)


    if start:
        if result is False:
            timer = int(time.time()) - initialTime
            cv2.putText(bkg, str(int(timer)), (610,630), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 4)
    
            if timer > 3:
                timer = 0
                result = True

                #is it rock, paper, scissors, or spiderman?
                if hands:
                    playerMove = 0
                    thisHand = hands[0] # the hands variable that we made from earlier is stored as an Array
                    fingCount = hand.fingersUp(thisHand)

                    if(fingCount) == [0,0,0,0,0]: #all fingers down: "rock" is assigned to the number 1
                        playerMove = 1

                    if(fingCount) == [1,1,1,1,1]: #all fingers up: "paper" is assigned to the number 2
                            playerMove = 2

                    if(fingCount) == [0,1,1,0,0]: #index and middle finger up: scissors is assigned to the number 3
                        playerMove = 3

                     #the user cannot play spiderman twice in a row; so, we have to check if the previous move was 4
                    if(preHands != 4 ):

                        if(fingCount) == [1,1,0,0,1]: #thumb, index, and pinky up: spiderman is assigned to the number 4
                            playerMove = 4
                    
                    #the AI is not able to use the spider man function, since the player is the real spiderman!
                    randAi = random.randint(1, 3)
                    ai = cv2.imread(f'final/{randAi}.png', cv2.IMREAD_UNCHANGED)
                    bkg = cvzone.overlayPNG(bkg,ai,(48,48))
                    preHands = playerMove

            
            #establishes winner:
                    print(randAi)
                    print(playerMove)
                    if(randAi == 1 and playerMove == 4):
                        playerS += 1
                    elif (randAi == 1 and playerMove == 2):
                        playerS +=1
                    elif(randAi == 2 and playerMove == 1):
                        aiS += 1
                    elif(randAi == 1 and playerMove == 3):
                        aiS += 1
                    elif(randAi == 3 and playerMove == 1):
                        playerS +=1
                    elif(randAi == 2 and playerMove == 3):
                        playerS +=1
                    elif(randAi == 3 and playerMove == 2):
                        aiS += 1
                    elif(randAi == 2 and playerMove == 4):
                        playerS += 1
                    elif(randAi == 3 and playerMove == 4):
                        aiS += 1

    if result:
        bkg = cvzone.overlayPNG(bkg, ai, (48,48))
    cv2.putText(bkg, str(aiS), (155,465), cv2.FONT_HERSHEY_PLAIN, 4, (161,57,128), 6)
    cv2.putText(bkg, str(playerS), (1105,300), cv2.FONT_HERSHEY_PLAIN, 4, (167,57,128), 6)

    cv2.imshow("Background", bkg)
    if cv2.waitKey(1) == ord('q'):
        start = True
        result = False
        initialTime = time.time()

