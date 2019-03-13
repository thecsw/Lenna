from urllib import request
import os, sys
import pytesseract
import cv2
from PIL import Image


def text_recognition(post):
    meme_name = "temp"  # We would just call all the temporary images as "temp"
    request.urlretrieve(post.url, filename=meme_name)  # Here we are downloading the appropriate image (png, jpg, jpeg, bmp)
    image = cv2.imread(meme_name)  # We load up the image using opencv
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Turning the image to grayscale
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # Making a threshold for the image, text will be more apparent
    gray = cv2.medianBlur(gray, 3)  # Adding some blur, useful for really noisy images
    filename = "{}-ocr.png".format(meme_name)  # Making the temporary, ready file for text recognition
    cv2.imwrite(filename, gray)  # Now, we will save the image
    img = Image.open(filename)  # Open the processed image with pillow
    recognized_text = pytesseract.image_to_string(img).encode('utf-8')  # As a means of exceptions, need to read out as UTF-8, so no encoding errors would occur
    os.remove(filename)  # Deleting all temporary image
    os.remove(meme_name)
    return recognized_text  # Returns the recognized text in UTF-8 encodign and with capital and lower letters
