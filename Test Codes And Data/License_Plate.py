#For Test Image 3
import pytesseract
import cv2

img = cv2.imread('/Test Model 2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binary = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)

tess = pytesseract.image_to_string(binary, config='-l eng --oem 1 --psm 12')

print(tess)
