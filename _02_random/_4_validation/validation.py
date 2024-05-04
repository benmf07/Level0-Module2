import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)
    for i in range(10):
    # TODO 1) Use each value of random_number to give the user a random compliment
        random_number = random.randint(1, 5)
        if random_number==1:
            messagebox.showinfo("compliment", "you are funny")
        if random_number==2:
            messagebox.showinfo("compliment", "you are pretty")
        if random_number==3:
            messagebox.showinfo("compliment", "you are nice")
        if random_number==4:
            messagebox.showinfo("compliment","you are fun to talk to")
        if random_number==5:
            messagebox.showinfo("compliment", "you are a good friend")
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
