import cv2
detect = cv2.CascadeClassifier('/Users/loaner/Library/Mobile Documents/com~apple~CloudDocs/Desktop/compsci/eoy project/eoy/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0) #note: "0" refers to which camera the interface should refer to
#sets dimensions of game to 720x1280
webcam.set(3,360)
webcam.set(4,360)


while True: 
    #reads video frame by frame, stores it in the boolean "boolean", and displays it
    boolean, video = webcam.read()
    # in order to run detectMultiScale, the image must be in grayscale
    grey = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    
    d = detect.detectMultiScale(grey, 1.1,4)
    cv2.waitKey(1)   #adds a delay of 1 ms

    for(x, y, w, h) in d:
        cv2.rectangle(video, (x, y), (x+w, y+h), (255,0,0), 2)
    
    cv2.imshow("Webcam", video)

    if ((cv2.waitKey(30) & 0xFF) == 27):
        break

webcam.release()


