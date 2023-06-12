import cv2

#reading image: 

#image = cv2.imread("eficlosed.jpg")

#cv2.imshow("Output", image) 
#cv2.waitKey(0)

#reading video camera:
video = cv2.VideoCapture(0)
video.set(3, 640)

while True:
    success, image = video.read()
    cv2.imshow("Video", image)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break




