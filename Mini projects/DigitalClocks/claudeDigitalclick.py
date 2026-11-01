import tkinter as tk
from time import strftime  # time function

root = tk.Tk()  # create object
root.title("Digital Clock")

# define function
def time():
    # create string variable
    string = strftime('%I:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()          # start the clock
root.mainloop() # keep the window open