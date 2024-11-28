from tkinter import *
from PIL import Image, ImageTk  # Image handling

# Initialize the root window
root = Tk()
root.title("Sign Language Recognition System")
root.minsize(height=700, width=1000)

def tab1():
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#FFE4B5")  # Moccasin background

    # Page 1
    label1 = Label(root, text='WELCOME TO SIGN LANGUAGE RECOGNITION SYSTEM\nFOR SPECIAL EDUCATION STUDENTS',
                   font=('Times New Roman', 26), justify='center', bg="#FFE4B5", fg="#8B4513") 
    label1.pack(pady=150)  # Center vertically with padding

    # Button to navigate to Page 2
    button1 = Button(root, text='START', font=('Times New Roman', 25), command=tab2, bg="#8B4513", fg="white")
    button1.pack(pady=20)

def tab2():
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#FFE4B5")  # Moccasin background

    # Title at the top
    title_label = Label(root, text='GOOD DAY STUDENTS, WELCOME TO\nSIGN LANGUAGE RECOGNITION SYSTEM',
                        font=('Times New Roman', 25), justify='center', bg="#FFE4B5", fg="#8B4513")
    title_label.pack(pady=(20, 40))  # Padding: top=20, bottom=40

    # Frame for category buttons
    button_frame = Frame(root, bg="#FFE4B5")
    button_frame.pack(expand=True)  # Center the grid in the available space

    # Create square buttons for categories
    categories = [
        ("Learning Materials", tab_materials),
        ("Helpful Videos", tab_videos),
        ("Interactive Game", tab_game),
        ("Practice FSL", tab_practice),
    ]
    for i, (category, action) in enumerate(categories):
        button = Button(button_frame, text=category, font=('Times New Roman', 15), width=30, height=7, command=action, bg="#8B4513", fg="white")
        button.grid(row=i // 2, column=i % 2, padx=20, pady=20)

    # Back button at the bottom
    back_button = Button(root, text='BACK', font=('Times New Roman', 25), command=tab1, bg="#8B4513", fg="white")
    back_button.pack(side=BOTTOM, pady=20)

def tab_materials():
    navigate_to_category("Learning Materials")

def tab_videos():
    navigate_to_category("Helpful Videos")

def tab_game():
    navigate_to_category("Interactive Game")

def tab_practice():
    navigate_to_category("Practice FSL")

def navigate_to_category(category_name):
    
    # Clear existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#FFE4B5")  

    # Back button at the top-left corner
    back_button = Button(root, text='BACK', font=('Times New Roman', 15), command=tab2, bg="#8B4513", fg="white")
    back_button.place(x=20, y=20)  # Place the button at the top-left corner

    # Title at the top
    title_label = Label(root, text=f"Welcome to the {category_name}",
                        font=('Times New Roman', 23), justify='center', bg="#FFE4B5", fg="#8B4513")
    title_label.pack(pady=(50, 40))  # Padding: top=50, bottom=40

    # Placeholder content #BURAHIN TO POTANGINBMO
    #placeholder_label = Label(root, text=f"This is the {category_name} page.",
    placeholder_label = Label(root, text=f"KANTUTAN SEX IYOT.",
                              font=('Times New Roman', 18), justify='center', bg="#FFE4B5", fg="#8B4513")
    placeholder_label.pack(expand=True)

# Start with the first page
tab1()

# Run the Tkinter main loop
root.mainloop()

