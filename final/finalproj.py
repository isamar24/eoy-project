#cv2: opencv
import cv2
#cvzone: gives us access to more detection, and will allow us to easily identify hand shapes
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random
#instantiates timer, whether the round has started, and if the round has a winner/loser/draw
timer = 0
start = False
result = False

#establishes the maximum amount of hands that we can detect, in this case we don't want more than 1.
hand = HandDetector(maxHands= 1)
 
#captures video; "0" signifies which webcam we want to use, since some PCs have multiple cameras
#also resizes to 360x360
webcam = cv2.VideoCapture(0)
webcam.set(3,360)
webcam.set(4,360)


while True: 

    bkg = cv2.imread("final/background.jpg")


    #reads video frame by frame, stores it in the boolean "boolean", and displays it
    boolean, video = webcam.read()

    playerMove = None #stores what the user's move is

    #checks if there is a hand in the webcam, displays on screen
    hands, video = hand.findHands(video)


    if start:

        if result is False:
           time = time.time() - initialTime #uses time library in order to find the time in the round

           if timer > 3:
              result = True
              timer = 0

               #is it rock, paper, scissors, or spiderman?
              if hands:
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
        
                    print(playerMove)

                    #the AI is not able to use the spider man function, since the player is the real spiderman!
                    randAI = random.randint(1, 3)

                    preHands = playerMove

            
            #establishes winner:
              if randAI == playerMove:
                  print("Draw!")
              if (randAI == 1 & playerMove == 2):
                  print("Player Wins!")
              if(randAI == 2 & playerMove == 1):
                  print("AI wins!")
              if(randAI == 1 & playerMove == 3):
                  print("AI wins!")
              if(randAI == 3 & playerMove == 1):
                  print("Player Wins!")
              if(randAI == 2 & playerMove == 3):
                  print("Player Wins!")
              if(randAI == 3 & playerMove == 2):
                  print("AI wins!")
              else:
                  print("Try Again!")
                

    cv2.imshow("Webcam", video)
    cv2.imshow("Background", bkg)
    trigger = cv2.waitKey(1)
    if trigger == ord('s'):
       start = True
       initialTime = time.time()
       result = False
