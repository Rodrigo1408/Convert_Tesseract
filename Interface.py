#coding: utf8

from tkinter import *

root = Tk()

theLabel = Label(root, text="Bem Vindo - Tesseract")
theLabel.pack()


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button OCR", fg="red")

button1.pack(side=BOTTOM)

root.mainloop()

