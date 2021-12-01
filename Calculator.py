from tkinter import *
# Works in Pycharm IDE
operation=""
cal=Tk()
cal.title("Calculator")
text_input = StringVar()

# Click 
def Click(num):
    global operation
    operation = operation + str(num)
    text_input.set(operation)

# Equals
def EqualCalc():
    global operation
    sum=str(eval(operation))
    text_input.set(sum)
    operation = ""

# Clear
def ClearCalc():
    global operation
    operation = ""
    text_input.set("")

# Main Text
textDisplay = Entry(cal,font=("arial", 20, "bold"), textvariable=text_input, bd=30, insertwidth=4,bg="gray", justify="right").grid(columnspan=4)

# Btns 9-7
btn7=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="7", bg="gray", command=lambda: Click(7)).grid(row=1, column=0)
btn8=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="8", bg="gray", command=lambda: Click(8)).grid(row=1, column=1)
btn9=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="9", bg="gray", command=lambda: Click(9)).grid(row=1, column=2)
btnDivision=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="/", bg="gray", command=lambda: Click("/")).grid(row=1, column=3)
            
# Btns 6-4
btn4=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="4", bg="gray", command=lambda: Click(4)).grid(row=2, column=0)
btn5=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="5", bg="gray", command=lambda: Click(5)).grid(row=2, column=1)
btn6=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="6", bg="gray", command=lambda: Click(6)).grid(row=2, column=2)
btnMultiply=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="*", bg="gray", command=lambda: Click("*")).grid(row=2, column=3)

# Btns 3-1
btn1=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="1", bg="gray", command=lambda: Click(1)).grid(row=3, column=0)
btn2=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="2", bg="gray", command=lambda: Click(2)).grid(row=3, column=1)
btn3=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="3", bg="gray", command=lambda: Click(3)).grid(row=3, column=2)
btnSubtract=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="-", bg="gray", command=lambda: Click(0)).grid(row=3, column=3)

# Btns 0 + Oper
btn0=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="0", bg="gray", command=lambda: Click(0)).grid(row=4, column=0)
btnclear=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="C", bg="gray", command=ClearCalc).grid(row=4, column=1)
btnequals=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="=", bg="gray", command=EqualCalc).grid(row=4, column=2)
btnAddition=Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
            text="+", bg="gray", command=lambda: Click("+")).grid(row=4, column=3)
cal.mainloop()
