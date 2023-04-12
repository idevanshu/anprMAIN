from tkinter import *
import os
import Number_plate_detection
root = Tk()

root.title("Rakshak Drishti")
root.iconbitmap(f"{os.getcwd()}\\favicon.ico")
root.geometry("600x400")
root.iconbitmap()

def run():
    Number_plate_detection.detect()


my_button = Button(root, text="Number Plate", command=run)
my_button.pack(pady=20)

root.mainloop()