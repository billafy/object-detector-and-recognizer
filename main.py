from object_recognizer import ObjectRecognizer
import cv2

capture = cv2.VideoCapture(0)
capture.set(3,1280)
capture.set(4,720)
capture.set(10,70)

obj_recognizer = ObjectRecognizer()
 
while True:
    is_playing, frame = capture.read()

    frame = obj_recognizer.recognize(frame)
 
    cv2.imshow('Object', frame)
    if cv2.waitKey(1) & 0xFF == ord('d') : 
        break

capture.release()
cv2.destroyAllWindows()