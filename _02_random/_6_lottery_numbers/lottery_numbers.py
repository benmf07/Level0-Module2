import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    loto=""
    for i in range(6):
        loto=loto+" "+str(random.randint(0,100))
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo("loto",loto)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
