from tkinter import *
from tkinter import messagebox
import os
import Number_plate_detection
import csv

root = Tk()

root.title("Rakshak Drishti")
root.iconbitmap(f"{os.getcwd()}\\favicon.ico")
root.geometry("800x600")

# Adding data in csv file
def save_number_plate():
    number_plate = entry.get()
    with open('plates.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number_plate])
    entry.delete(0, 'end')

# Create a frame for the image and the form
frame1 = Frame(root)
frame1.pack(side=LEFT, padx=20)

# Image displaying
img = PhotoImage(file="logo.png")
img = img.subsample(4)
img_label = Label(frame1, image=img)
img_label.pack(pady=20)

# Form for entering number plate
label = Label(frame1, text='Enter Number Plate:')
label.pack(pady=10)

entry = Entry(frame1)
entry.pack(pady=10)

button = Button(frame1, text='Save', command=save_number_plate, bg='#3498db', fg='white')
button.pack(pady=10)

# Create a frame for the buttons
frame2 = Frame(root)
frame2.pack(side=RIGHT, padx=20)

def run():
    Number_plate_detection.detect()

my_button = Button(frame2, text="Number Plate", command=run, bg='#2ecc71', fg='white')
my_button.pack(pady=20)

# Thief detected
visited = []

def write_in_thief_csv():
    with open("plates.csv", "r") as f:
        reader = csv.reader(f)
        for lines in reader:
            visited.append(lines[0])


root.mainloop()
