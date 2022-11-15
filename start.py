import tkinter as tk
from tkinter import *
from signUpPage import signUpPage

def start():
		root = Tk()
		root.title('Welcome To Quiz App')
		canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
		canvas.grid(column = 0 , row = 1)
		img = PhotoImage(file="img/output-onlinepngtools.png")
		canvas.create_image(50,10,image=img,anchor=NW)

		button = Button(root, text='Start',command =lambda: signUpPage(root),bg="red",fg="yellow") 
		button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
		button.grid(column = 0 , row = 2)

		root.mainloop()

if __name__=='__main__':
    start()


	