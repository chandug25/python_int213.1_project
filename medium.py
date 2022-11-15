import tkinter as tk
from tkinter import *
import random
import time
from showMark import showMark

def medium():
    
    global m
    m = Tk()
    m.title('Quiz App - Medium Level')
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="#A1A100")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQ = [
                
                
                [ 
                    "Which of the following creates a tuple?",
                      "tuple1=('a','b'')",
                      "tuple1[2]=('a','b'')",
                      "tuple1=(5)*2",
                      "None of the above"          
                ],
                [  " Choose the correct option with respect to Python",
                     "Both tuples and lists are immutable.",
                     "Tuples are immutable while lists are mutable.",
                     "Both tuples and lists are mutable.",
                     "Tuples are mutable while lists are immutable."         
                ],
                [
                    "Choose the correct option",
                     "In Python, a tuple can contain only integers as its elements.",
                     "In Python, a tuple can contain only strings as its elements.",
                     "In Python, a tuple can contain both integers and strings as its elements.",
                     "In Python, a tuple can contain either string or integer but not both at a time"
                ],
                
                [
                    "Which of the following options will not result in an error when performed on tuples in Python where tupl=(5,2,7,0,3)?",
                     "tupl[1]=2",
                     "tupl.append(2)",
                     "tupl1=tupl+tupl",
                     "tupl.sort()"         
                ],
                [
                    "Where is function defined?",
                      "Module",
                      "Class",
                      "Another function",
                      "All of the mentioned"          
                ], 
                [
                    "What is called when a function is defined inside a class?",
                    "Module",
                    "Class",
                    "Another function",
                    "Method"        
                ],
                [
                    " Which of the following is the use of id() function in python?",
                    "Id returns the identity of the object",
                    "Every object doesn't have a unique id",
                    "All of the mentioned",
                    "None of the mentioned"        
                ],
                [   "Which of the following refers to mathematical function?",
                     "sqrt",
                     "rhombus",
                     "add",
                     "rhombus"          
                ],
                [
                     "Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.reverse()?",
                     "[3, 4, 5, 20, 5, 25, 1, 3]",
                     "[1, 3, 3, 4, 5, 5, 20, 25]",
                     "[25, 20, 5, 5, 4, 3, 3, 1]",
                     "[3, 1, 25, 5, 20, 5, 4, 3]"         
                ],
                [
                  " Suppose listExample is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after listExample.extend([34, 5])?",
                   "[3, 4, 5, 20, 5, 25, 1, 3, 34, 5]",
                   "[1, 3, 3, 4, 5, 5, 20, 25, 34, 5]",
                   "[25, 20, 5, 5, 4, 3, 3, 1, 34, 5]",
                   "[1, 3, 4, 5, 20, 5, 25, 3, 34, 5]"       
                ],
                
                [
                    "Suppose listExample is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after listExample.pop(1)?",
                    "[3, 4, 5, 20, 5, 25, 1, 3]",
                    "[1, 3, 3, 4, 5, 5, 20, 25]",
                    "[3, 5, 20, 5, 25, 1, 3]",
                    "[1, 3, 4, 5, 20, 5, 25]"        

                ],
                [
                    "Suppose listExample is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after listExample.pop()?",
                      "[3, 4, 5, 20, 5, 25, 1]",
                      "[1, 3, 3, 4, 5, 5, 20, 25]",
                      "[3, 5, 20, 5, 25, 1, 3]",
                      "[1, 3, 4, 5, 20, 5, 25]"           

                ],
                [
                    "Which of the statements about dictionary values if false?",
                     "More than one key can have the same value",
                     "The values of the dictionary can be accessed as dict[key]",
                     "Values of a dictionary must be unique",
                     "Values of a dictionary can be a mixture of letters and numbers"         
                ],
                [
                    "If a is a dictionary with some key-value pairs, what does a.popitem() do?",
                    "Removes an arbitrary element",
                    "Removes all the key-value pairs",
                    "Removes the key-value pair for the key given as an argument",
                    "Invalid method for dictionary"        
                ],
                [
                     "If b is a dictionary, what does any(b) do?"                             
                       "Returns True if any key of the dictionary is true",
                      "Returns False if dictionary is empty",
                      "Returns True if all keys of the dictionary are true",
                      "Method any() doesn't exist for dictionary"          
                ],
            ] 
               
            
            
    answer =[

            "tuple1=('a','b')",
            "Tuples are immutable while lists are mutable.",
            "In Python, a tuple can contain both integers and strings as its elements.",
            "tupl1=tupl+tupl",
            "All of the mentioned",
            "Method",
            "Id returns the identity of the object",
            "sqrt",
            "[3, 1, 25, 5, 20, 5, 4, 3]",
            "[3, 4, 5, 20, 5, 25, 1, 3, 34, 5]",
            "[3, 5, 20, 5, 25, 1, 3]"
            "[3, 4, 5, 20, 5, 25, 1]",
            "Values of a dictionary must be unique",
            "Removes an arbitrary element",
            "Returns True if any key of the dictionary is true",
            ]
    
    li = ['',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =mediumQ[x][0],font="calibri 12",bg="#B26500")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="#A1A100")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="#A1A100")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="#A1A100")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="#A1A100")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()