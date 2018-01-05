# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image


img = Image.open('imagem2.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

result = pytesseract.image_to_string(img)


print("      A mágica do tesseract       ")
print("********************************\n")
print(result)

