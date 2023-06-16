import cv2

#opencv has a set of "cascades" that help the interface learn and recognize features; 
# "frontal face" is a cascade that identifies a front facing face
faceCascade = cv2.CascadeClassifier("/Users/loaner/Library/Mobile Documents/com~apple~CloudDocs/Desktop/compsci/eoy project/eoy/lib/python3.10/site-packages/cv2/data/haarcascade_frontalface_default.xml")
image = cv2.imread("stock.jpeg")

facesquare = faceCascade.detectMultiScale(image, 1.1, 4)

for(x,y,w,h) in facesquare:
    cv2.rectangle(image, (x,y), (x+w,y+h),(255,0,0),  2)
cv2.imshow("Output", image) 
cv2.waitKey(0)

