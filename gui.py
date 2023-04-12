from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import Number_plate_detection
import csv
import shutil
from PIL import ImageTk, Image

root = Tk()

root.title("Rakshak Drishti")
root.iconbitmap(f"{os.getcwd()}\\favicon.ico")
root.geometry("800x600")

# Define frame1 and frame2
frame1 = Frame(root)
frame1.pack(side=LEFT, padx=20)

frame2 = Frame(root)
frame2.pack(side=RIGHT, padx=20)

# Adding data in csv file
def save_number_plate():
    number_plate = entry.get()
    with open('plates.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number_plate])
    entry.delete(0, 'end')

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

def run():
    Number_plate_detection.detect()

my_button = Button(frame2, text="Number Plate", command=run, bg='#2ecc71', fg='white')
my_button.pack(pady=20)

def select_file():
    # Ask the user to select a CSV file
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )

    # Create the csv folder if it doesn't exist
    csv_folder = "csv"
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    # Copy the selected file to the csv folder
    file_name = os.path.basename(file_path)
    target_path = os.path.join(csv_folder, file_name)
    shutil.copy(file_path, target_path)

    print("Selected file:", file_path)
    print("File saved to:", target_path)

def show_image():
    image_path = os.path.join(f"{os.getcwd()}", "Img0.png")
    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)
    label = Label(root, image=img_tk)
    label.pack()

button = Button(frame2, text="Show Enhanced Image", command=show_image, bg='#3498db', fg='white')
button.pack(pady=10)

select_button = Button(frame2, text="Select File", command=select_file, bg='#ffd700', fg='black')
select_button.pack(pady=20)

root.mainloop()
