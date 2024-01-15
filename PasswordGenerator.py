# Imported necessary libraries and modules
from tkinter import *
import string
import random

"""
To those who are viewing my code. Welcome to my password generator which I built after being inspired by a password generator website called Norton Password
Generator. The link to the website: https://my.norton.com/extspa/passwordmanager?path=pwd-gen. I used tkinter to built the GUI part of the project to give it a 
vibrant look and imported the string and random modules to generate a random string consisting of letters, digits, and punctuation.
"""

"""
The slide function is called to call the password function to display the password as a string based on the number selected from the slider.
It also disables the sliderButton when it has been clicked so that there won't be multiple clicks.
"""
def slide():
    password()
    sliderButton["state"] = DISABLED

"""
The password function is called from the slide function to generate a set of random characters including ascii letters (both lowercase and uppercase) as well
as numbers and other characters. The GUI also displays different colors based on the strength of the password and once the password has been generated it is
printed out in the terminal for the user to access.
"""
def password():
    global passwordLabel
    if slider.get() <= 5 :
        win.configure(bg = "dark red")
        generatedPassword = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for number in range(slider.get()))
        passwordLabel = Label(win, text = "Bad password! Please select a higher number for maximum security. Your password is: \n" + generatedPassword, font = 20)
        passwordLabel.pack()
        print(generatedPassword)
    elif slider.get() >= 6 and slider.get() < 11:
        win.configure(bg = "dark orange")
        generatedPassword = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for number in range(slider.get()))
        passwordLabel = Label(win, text = "Weak password! Please select a higher number for maximum security. Otherwise your password is: \n" + generatedPassword, font = 20)
        passwordLabel.pack()
        print(generatedPassword)
    else:
        win.configure(bg = "green")
        generatedPassword = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for number in range(slider.get()))
        passwordLabel = Label(win, text = "Strong password! Your password is: \n" + generatedPassword, font = 20)
        passwordLabel.pack()
        print(generatedPassword)

"""
The clearButton function is used to destroy the label, changing the state of the sliderButton
"""
def clearButton():
    passwordLabel.destroy()
    sliderButton["state"] = NORMAL

"""
The main function is used to create the window, the name of the GUI app, the size of the GUI app, and to create the base of the whole GUI like labels,
slider, buttons, and string variables.
"""  
if __name__ == "__main__":
    win = Tk()  
    win.title("Password Generator")
    win.geometry("1920x1080")
    
    photo = PhotoImage(file = "C:/Users/ashwa/OneDrive/Desktop/Python project/password.png")
    photoLabel = Label(win, image = photo)
    photoLabel.pack()

    label = Label(win, text = "Use the slider to select the length of the password. You can copy and paste your generated password from the terminal.\n If you want a new password, click the clear button and generate the password again.", font = ("Ubuntu", 20, "bold"), relief = RAISED, fg = "sky blue", bg = "black")
    label.pack()
    
    slider = Scale(win, from_ = 4, to = 64, tickinterval = 1, orient = "horizontal", relief = GROOVE, length = 1000, fg = "black", bg = "sky blue")
    slider.pack()
    
    sliderButton = Button(win, text = "Click button to register number", command = slide)
    sliderButton.pack() 
    
    passwordLabel = StringVar()
    
    clear = Button(win, text = "Clear", command = clearButton)
    clear.pack()
    

    win.mainloop()
    print("Thank you for using my password generator!")