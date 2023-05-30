#For Test Image 3
import pytesseract
import cv2

# Before starting, please note that you have to specify the path to tesseract-ocr
# in order for pytesseract to work correctly. Path to tesseract-ocr is specified
# as: pytesseract.pytesseract.tesseract_cmd = r'\Tesseract-OCR\tesseract.exe'
# To know the path to the tesseract.exe, note down the path when installing
# tesseract-ocr from https://github.com/UB-Mannheim/tesseract/wiki
# Specify that path in "pytesseract.pytesseract.tesseract_cmd"

pytesseract.pytesseract.tesseract_cmd = r'..\Tesseract-OCR\tesseract.exe'

img = cv2.imread('/Test Model 2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, binary = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)

tess = pytesseract.image_to_string(binary, config='-l eng --oem 1 --psm 12')

print(tess)
