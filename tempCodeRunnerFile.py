
button = tk.Button(root, text = "Detect number plate")

def on_button_click():
    lable.configure(text="Number plate")

button.configure(command=on_button_click)

root.mainloop()