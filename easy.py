import tkinter as tk
from tkinter import *
import random
import time
from showMark import showMark

def easy():
    
		global e
		e = Tk()
		e.title('Quiz App - Easy Level')
		
		easy_canvas = Canvas(e,width=720,height=440,bg="orange")
		easy_canvas.pack()

		easy_frame = Frame(easy_canvas,bg="#BADA55")
		easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

		
		def countDown():
				check = 0
				for k in range(10, 0, -1):
						
						if k == 1:
								check=-1
						timer.configure(text=k)
						easy_frame.update()
						time.sleep(1)
						
				timer.configure(text="Times up!")
				if check==-1:
						return (-1)
				else:
						return 0
		global score
		score = 0
		
		easyQ = [
									[
											" Which of the following is a Python tuple?",
										  "[1, 2, 3]",
                                          "(1, 2, 3)",
                                          "{1, 2, 3}",
                                          "{}"
									] ,
									[
											" If a=(1,2,3,4), a[1:-1] is" ,
			 							"Error, tuple slicing doesn't exist",
                                        "[2,3]",
                                        "(2,3,4)",
                                        "(2,3)"
											
									],
								[
										"What is the data type of (1)?" ,
										 
                                         "Tuple",
                                         "Integer",
                                         "List",
                                         "Both tuple and integer"
								],
								[
										"Which of the following commands will create a list?" ,
										 "list1 = list()",
                                         "list1 = []",
                                         "list1 = list([1, 2, 3])",
                                         "all of the mentioned"
								],
								[
										" Suppose list1 is [2445,133,12454,123], what is max(list1)?" ,
										 "2445",
                                         "133",
                                         "12454",
                                         "123"
								],
								[
									"  Suppose list1 is [1, 5, 9], what is sum(list1)? Suppose list1 is [1, 5, 9], what is sum(list1)?" ,
                                      "1",
                                      "9",
                                      "15",
                                      "Error"



								],
								[
									"Which of the following statements create a dictionary?"  ,
                                     "d = {}",
                                     "d = {“john”:40, “peter”:45}",
                                     "d = {40:”john”, 45:”peter”}",
                                     "All of the mentioned"


								],
								[
									"Which of the following functions is a built-in function in python?"  ,
                                     "seed()",
                                     "sqrt()",
                                     "factorial()",
                                     "print()"


								],
								[
									"round(4.576) is equal to"  ,
                                      "4.5",
                                      "5",
                                      "4",
                                      "4.6"                          

								],
								[
									" Which is the most appropriate definition for recursion?"  ,
                                     "A function that calls itself",
                                     "A function execution instance that calls another execution instance of the same function",
                                     "A class method that calls another class method",
                                     "An in-built method that is automatically called"


								],
								[
  									"Which of these is false about recursion?"  ,
                                    "Recursive function can be replaced by a non-recursive function",
                                    "Recursive functions usually take more memory space than non-recursive function",
                                    "Recursive functions run faster than non-recursive function",
                                    "Recursion makes programs easier to understand"


								],
								[
									"Which of the following statements is false about recursion?" ,
                                      "Every recursive function must have a base case",
                                      "Infinite recursion can occur if the base case isn't properly mentioned",
                                      "A recursive function makes the code easier to understand",
                                      "Every recursive function must have a return value"

								],
								[
									" Which of the following is the use of function in python?"  ,
									 "Functions are reusable pieces of programs",
                                     "Functions don't provide better modularity for your application",
                                     "you can't also create your own functions",
                                     "All of the mentioned"
								],
								[
									"Which keyword is used for function?"  ,
                                     "Fun",
                                     "Define",
                                     "Def",
                                     "Function"

								],
								[
									" What are the two main types of functions?"  ,
									 "Custom function",
                                     "Built-in function & User defined function",
                                     "User function",
                                     "System function"
								]
		]
		answer = [
								   "(1, 2, 3)",
								   "(2,3)"
							       "Integer",
								   "all of the mentioned",
								   "12454",
								   "15",
								   "All of the mentioned",
									"print()",
									"5",
									"A function execution instance that calls another execution instance of the same function",
									"Recursive functions run faster than non-recursive function",
									"Every recursive function must have a return value",
									"Functions are reusable pieces of programs",
									"Def",
									"Built-in function & User defined function",

							]
		         


		li = ['',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
		x = random.choice(li[1:])
		
		ques = Label(easy_frame,text =easyQ[x][0],font="calibri 12",bg="orange")
		ques.place(relx=0.5,rely=0.2,anchor=CENTER)

		var = StringVar()
		
		a = Radiobutton(easy_frame,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="#BADA55")
		a.place(relx=0.5,rely=0.42,anchor=CENTER)

		b = Radiobutton(easy_frame,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="#BADA55")
		b.place(relx=0.5,rely=0.52,anchor=CENTER)

		c = Radiobutton(easy_frame,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="#BADA55")
		c.place(relx=0.5,rely=0.62,anchor=CENTER) 

		d = Radiobutton(easy_frame,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="#BADA55")
		d.place(relx=0.5,rely=0.72,anchor=CENTER) 
		
		li.remove(x)
		
		timer = Label(e)
		timer.place(relx=0.8,rely=0.82,anchor=CENTER)
		
		
		
		def display():
					
					if len(li) == 1:
							e.destroy()
							showMark(score)
							exit(0)
					if len(li) == 2:
							nextQuestion.configure(text='End',command=calc)
									
					if li:
							x = random.choice(li[1:])
							ques.configure(text =easyQ[x][0])
							
							a.configure(text=easyQ[x][1],value=easyQ[x][1])
				
							b.configure(text=easyQ[x][2],value=easyQ[x][2])
				
							c.configure(text=easyQ[x][3],value=easyQ[x][3])
				
							d.configure(text=easyQ[x][4],value=easyQ[x][4])
							
							li.remove(x)
							y = countDown()
							if y == -1:
									display()


						
		def calc():
				global score
				if (var.get() in answer):
						score+=1
				display()
		
		submit = Button(easy_frame,command=calc,text="Submit", fg="white", bg="black")
		submit.place(relx=0.5,rely=0.82,anchor=CENTER)
		
		nextQuestion = Button(easy_frame,command=display,text="Next", fg="white", bg="black")
		nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
		
		
		y = countDown()
		if y == -1:
				display()
		e.mainloop()