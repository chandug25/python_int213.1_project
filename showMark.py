import tkinter as tk
from tkinter import *
import sys

def showMark(mark):
		sh = Tk()
		sh.title('Your Marks')
		
		st = "Your score is "+str(mark)+"/15"
		mlabel = Label(sh,text=st,fg="black", bg="white")
		mlabel.pack()
		
		
		from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
		from matplotlib.backend_bases import key_press_handler
		from matplotlib.figure import Figure

		import numpy as np

		fig = Figure(figsize=(5, 4), dpi=100)
		labels = 'Marks Obtained','Total Marks'
		sizes = [int(mark),5-int(mark)]
		explode = (0.1,0)
		fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
		

		canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		
		def destroy():
			try:
				import os
				os._exit(0)
			finally:
					pass
				

		b23=Button(text="Sign Out",command=destroy,fg="white", bg="black")
		b23.pack()
		

		sh.mainloop()