#For Test Image 2
import pytesseract
import cv2

img = cv2.imread('/HandwritingTest2.jpg')
img = cv2.medianBlur(img, 5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binary = cv2.threshold(img, 121, 255, cv2.THRESH_BINARY)

tess = pytesseract.image_to_string(binary, config='-l eng --oem 1 --psm 7')

print(tess)
