import tkinter as tk
from tkinter import *
import math

root = Tk()
root.title("CODSOFT CALCULATOR")
root.geometry("450x620")
root.configure(bg="black")

calculation = ""

def add_to_calculation(symbol):
  global calculation
  calculation += str(symbol)
  labelEntery.delete(1.0,"end")
  labelEntery.insert(1.0,calculation)
  labelEntery.see(tk.END)
  

def evaluate_calculation():
  global calculation
  try:
    if "√" in calculation:
      squareEN = calculation.replace("√","")
      square = math.sqrt(float(squareEN))
      calculation = str(square)
    elif "%" in calculation:
      squareEN = calculation.replace("%","")
      square = float(squareEN)/100
      calculation = str(square)
    elif "B" in calculation:
      squareEN = calculation.replace("B","")
      square = int(squareEN)
      binary = bin(square)
      calculation = str(binary)
    else:
      calculation = str(eval(calculation))
    labelEntery.delete(1.0,"end")
    labelEntery.insert(1.0,calculation)
  except:
    clear_field()
    labelEntery.insert(1.0,"Error")

def clear_field():
  global calculation
  calculation = ""
  labelEntery.delete(1.0,'end')


labelEntery = tk.Text(root,width=11,height=0,border=2,borderwidth=3,font=("arial",50,"bold"),bg="#ADFF2F")
labelEntery.place(x=15,y=10)

buttoncl = Button(root,text="C\nCLEAR",width=8,height=3,font=("arial",12,"bold"),bg="#FFE4C4",command=clear_field)
buttoncl.place(x=15,y=135)

buttonsq = Button(root,text="√\nSQRT",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("√"))
buttonsq.place(x=120,y=135)

buttondiv = Button(root,text="/\nDIVISION",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("/"))
buttondiv.place(x=228,y=135)

buttongr = Button(root,text="%\npct.",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("%"))
buttongr.place(x=339,y=135)

button7 = tk.Button(root,text="7\nSEVEN",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(7))
button7.place(x=15,y=230)

button8 = Button(root,text="8\nEIGHT",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(8))
button8.place(x=120,y=230)

button9 = Button(root,text="9\nNINE",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(9))
button9.place(x=230,y=230)

buttonmu = tk.Button(root,text="*\nMULTIPL",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("*"))
buttonmu.place(x=340,y=230)


buttonc4 = Button(root,text="4\nFOUR",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(4))
buttonc4.place(x=15,y=329)

buttonc5 = Button(root,text="5\nFIVE",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(5))
buttonc5.place(x=120,y=329)

buttonc6 = Button(root,text="6\nSIX",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(6))
buttonc6.place(x=228,y=329)

buttonmin = Button(root,text="-\nMINUS",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("-"))
buttonmin.place(x=340,y=329)

buttonc1 = Button(root,text="1\nONE",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(1))
buttonc1.place(x=15,y=430)

buttonc1 = Button(root,text="2\nTWO",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(2))
buttonc1.place(x=120,y=430)

buttonc1 = Button(root,text="3\nTHREE",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(3))
buttonc1.place(x=228,y=430)

buttonc1 = Button(root,text="+\nPLUS",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("+"))
buttonc1.place(x=340,y=430)

buttonnot = Button(root,text="B\nBINARY",width=8,height=3,font=("arial",12,"bold"),bg="#DEB887",command=lambda:add_to_calculation("B"))
buttonnot.place(x=15,y=530)

buttonnot = Button(root,text="0\nZERO",width=8,height=3,font=("arial",12,"bold"),bg="#FFBBFF",command=lambda:add_to_calculation(0))
buttonnot.place(x=120,y=530)

buttonnot = Button(root,text=".\nDOT",width=8,height=3,font=("arial",12,"bold"),bg="#EEB4B4",command=lambda:add_to_calculation("."))
buttonnot.place(x=228,y=530)

buttonres = tk.Button(root,text="=",width=8,height=3,font=("arial",12,"bold"),bg="#FF0000",command=lambda:evaluate_calculation())
buttonres.place(x=340,y=533)




root.mainloop()