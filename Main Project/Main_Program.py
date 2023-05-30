import tkinter.messagebox
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import numpy
import pytesseract #Python wrapper for Google-owned OCR engine known by the name of Tesseract.
import cv2
from PIL import Image, ImageTk
import os

# Before starting, please note that you have to specify the path to tesseract-ocr
# in order for pytesseract to work correctly. Path to tesseract-ocr is specified
# as: pytesseract.pytesseract.tesseract_cmd = r'\Tesseract-OCR\tesseract.exe'
# To know the path to the tesseract.exe, note down the path when installing
# tesseract-ocr from https://github.com/UB-Mannheim/tesseract/wiki
# Specify that path in "pytesseract.pytesseract.tesseract_cmd"

pytesseract.pytesseract.tesseract_cmd = r'..\Tesseract-OCR\tesseract.exe'

root = tk.Tk()
root.title("Object Character Recognizer")
root.geometry("1280x720")
test_image = None


def browse_image():
    fin = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All Files",  "*.*")))
    global test_image
    image = Image.open(fin)
    test_image = image
    img = ImageTk.PhotoImage(image.resize((650, 400)))
    lb = tk.Label(image=img)
    lb.place(x=25, y=50)
    root.mainloop()

def use_ocr_default():
    try:
        global test_image
        messge = None
        #OEM stands for OCR Engine Mode and PSM stands for Page Segmentation Mode.
        #OEM defines what kind of OCR engine is to be used (this defines the dataset that would be used to cross-match
        #the available data with the testing data).
        #PSM defines how Tesseract will treat the image that supposedly contains characters and how it will extract the
        #data from the image.
        tess = pytesseract.image_to_string(test_image, config='-l eng --oem 1 --psm 3')
        label = Label(messge, text='Result:')
        label.place(x=850, y=320)
        display_message = Text(messge, width=46, height=15)
        display_message.insert(END, str(tess))
        display_message.config(state=DISABLED)
        display_message.delete(0, END)
        display_message.place(x=890, y=330)

    except: #Print a error message when the user inputs an incompatible image.
        tkinter.messagebox.showinfo('Something\'s Wrong!', 'Your picture may not contain English characters or you may have not selected a picture. Please select a picture with detectable English characters.')

def use_ocr_handwriting():
    try:
        global test_image
        opencv_img = numpy.array(test_image)
        opencv_img = opencv_img[:, :, ::-1].copy() #This line is used to convert RGB PIL image file to BGR cv2 image file.
        blurred_img = cv2.medianBlur(opencv_img, 5)
        gray_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2GRAY)
        thresh, binary = cv2.threshold(gray_img, 122, 255, cv2.THRESH_BINARY)
        messge = None
        tess = pytesseract.image_to_string(binary, config='-l eng --oem 1 --psm 3')
        label = Label(messge, text='Result:')
        label.place(x=850, y=320)
        display_message = Text(messge, width=46, height=15)
        display_message.insert(END, str(tess))
        display_message.config(state=DISABLED)
        display_message.delete(0, END)
        display_message.place(x=890, y=330)

    except:
        tkinter.messagebox.showinfo('Something\'s Wrong!', 'Your picture may not contain English characters or you may have not selected a picture. Please select a picture with detectable English characters.')

def use_ocr_singletext():
    try:
        global test_image
        messge = None
        tess = pytesseract.image_to_string(test_image, config='-l eng --oem 1 --psm 7')
        label = Label(messge, text='Result:')
        label.place(x=850, y=320)
        display_message = Text(messge, width=46, height=15)
        display_message.insert(END, str(tess))
        display_message.config(state=DISABLED)
        display_message.delete(0, END)
        display_message.place(x=890, y=330)

    except:
        tkinter.messagebox.showinfo('Something\'s Wrong!', 'Your picture may not contain English characters or you may have not selected a picture. Please select a picture with detectable English characters.')

w = tk.LabelFrame(root, text="Image:", width=768, height=600)
w.place(x=20, y=10)
w.pack_propagate(0)
w1 = tk.LabelFrame(root, text="Extracted Text:", width=500, height=310)
w1.place(x=800, y=300)
w2 = tk.LabelFrame(root, text="Operations:", width=350, height=280)
w2.place(x=800, y=10)
btn1 = tk.Button(w2, text="Load Image", padx=40, pady=10, command=browse_image)
btn1.place(x=22, y=20)
btn1 = tk.Button(w2, text="Run Handwritten OCR", padx=40, pady=10, command=use_ocr_handwriting)
btn1.place(x=22, y=80)
btn1 = tk.Button(w2, text="Run Default OCR", padx=40, pady=10, command=use_ocr_default)
btn1.place(x=22, y=140)
btn1 = tk.Button(w2, text="Run Single Text OCR", padx=40, pady=10, command=use_ocr_singletext)
btn1.place(x=22, y=200)
root.mainloop()
