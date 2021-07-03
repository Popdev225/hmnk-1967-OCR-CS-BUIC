#For Test Image 1
import pytesseract
import cv2

img = cv2.imread('/HandwritingTest.jpg')
thresh, binary = cv2.threshold(img, 123, 255, cv2.THRESH_BINARY)

tess = pytesseract.image_to_string(binary, config='-l eng --oem 1 --psm 7')

print(tess)
