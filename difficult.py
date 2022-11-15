import tkinter as tk
from tkinter import *
import random
import time
from showMark import showMark


def difficult():
    
       
    global h
    #count=0
    h = Tk()
    h.title('Quiz App - Hard Level')
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="#008080")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    hardQ = [
                [
       " Suppose d = {“john”:40, “peter”:45}, what happens when we try to retrieve a value using the expression d[“susan”]?",
        "Since “susan” is not a value in the set, Python raises a KeyError exception",
        "It is executed fine and no exception is raised, and it returns None",
        "Since “susan” is not a key in the set, Python raises a KeyError exception",
        "Since “susan” is not a key in the set, Python raises a syntax error"
    ],
    [
        " Which of the following is not a declaration of the dictionary?",
         "{1: 'A', 2: 'B'}",
         "dict([[1,”A”],[2,”B”]])",
         "{1,”A”,2”B”}",
         "{ }"
    ],
    [
     " Which of the following isn't true about dictionary keys?",
          "More than one key isn't allowed",
          "Keys must be immutable",
          "Keys must be integers",
          "When duplicate keys encountered, the last assignment wins"   
    ],
    [
        " To which of the following the 'in' operator can be used to check if an item is in it?",
          "Lists",
          "Dictionary",
          "Tuples",
          "All of the above " 
    ],
    [
        "Suppose t = (1, 2, 4, 3), which of the following is incorrect?",
         "Print(t[3])",
         "T[3] = 45",
         "Print(max(t))",
         "Print(len(t))"
    ],
    [
        "Suppose list1 is [1, 3, 2], What is list1 * 2?",
        "[2, 6, 4]",
        "[1, 3, 2, 1, 3]",
        "[1, 3, 2, 1, 3, 2]",
        "[1, 3, 2, 3, 2, 1]"
    ],
    [
        "Suppose list1 = [0.5 * x for x in range(0, 4)], list1 is:",

          "[0, 1, 2, 3]",
          "[0, 1, 2, 3, 4]",
          "[0.0, 0.5, 1.0, 1.5]",
          "[0.0, 0.5, 1.0, 1.5, 2.0] " 
    ],
    [
        "To add a new element to a list we use which command?",
         "list1.add(5)",
         "list1.append(5)",
         "list1.addLast(5)",
         "list1.addEnd(5) "

    ],
    [
        "To remove string “hello” from list1, we use which command?",
        "list1.remove(“hello”)",
        "list1.remove(hello)",
        "list1.removeAll(“hello”)",
        "list1.removeOne(“hello”)"

    ],
    [
        "Python supports the creation of anonymous functions at runtime, using a construct called",
         "lambda",
        "pi",
        "anonymous",
        "none of the mentioned"

    ],
    [
         "What is a variable defined outside a function referred to as?",
         "A static variable",
         "A global variable",
         "A local variable",
         "An automatic variable"

    ],
    [
        " What is a variable defined inside a function referred to as?",
        "A global variable",
        "A volatile variable",
        "A local variable",
        "An automatic variable"
    ],
    [
      
        " What is tail recursion?",
        "A recursive function that has two base cases",
        "A function where the recursive functions leads to an infinite loop",
        "A recursive function where the function doesn't return anything and just prints the values",
        "A function where the recursive call is the last thing executed by the function"


    ],
    [
        " What happens if the base condition isn't defined in recursive programs?",
        "Program gets into an infinite loop",
        "Program runs once",
        "Program runs n number of times where n is the argument given to the function",
        "An exception is thrown"
    ],
    [
        "Which of these is not true about recursion?"
            "It's easier to code some real-world problems using recursion than non-recursive equivalent",
            "Recursive functions are easy to debug",
            "Recursive calls take up a lot of memory",
            "Programs using recursion take longer time than their non-recursive equivalent"
    ]
            
]
    answer = [
            "Since “susan” is not a key in the set, Python raises a KeyError exception",
            "{1,”A”,2”B”}",
            "Keys must be integers",
            "All of the above"
            "T[3] = 45",
            "[1, 3, 2, 1, 3, 2]",
            "[0.0, 0.5, 1.0, 1.5]",
            "list1.append(5)",
            "list1.remove(“hello”)",
            "lambda",
            "A global variable",
            "A local variable",
            "A function where the recursive call is the last thing executed by the function"
            "Program gets into an infinite loop",
            "Recursive functions are easy to debug",
            ]
    
    li = ['',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =hardQ[x][0],font="calibri 12",bg="#A0DB8E")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="#008080",fg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="#008080",fg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="#008080",fg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="#008080",fg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
                exit(0)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        #count=count+1
        if (var.get() in answer):
            score+=1
        display()
    
   # def lastPage():
    #    h.destroy()
     #   showMark()
    
    submit = Button(hard_frame,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    # end=Button(hard_frame,command=showMark(), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()