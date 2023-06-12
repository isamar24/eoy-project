import cv2

video = cv2.VideoCapture(0)
video.set(3, 640)

while True:
    success, image = video.read()
    cv2.imshow("Video", image)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
