import sys
import tkinter as tk
from math import sin,cos,tan,asin,acos,atan,log1p,log10,sqrt,pi,degrees
def onClick(key):  
    if key == "EXIT":
        quit()
    if key == "C":
        entry.delete(0,tk.END)
    elif key == "=":
        try:
            ans = eval(entry.get())
            entry.delete(0,tk.END)
            entry.insert(0,ans)
        except SyntaxError:
            entry.delete(0,tk.END)
            entry.insert(0,"check your calculation")
        except ZeroDivisionError:
            entry.delete(0,tk.END)
            entry.insert(0,"you know thats impossible")
            
    else:
        entry.insert(tk.END,key)

root = tk.Tk()
root.title("SOLO Q Calculator")
root.background="blue"
buttons = [
"/","degrees","**","log1p","log10",
"sin","cos","tan","(",")",
"asin","acos","atan","sqrt","",
"7","8","9","C","AC",
"4","5","6","*","/",
"1","2","3","+","-",
".","0","00","pi","=",
]
r = 1
c = 0
for buttons in buttons:
    cmd = lambda key=buttons: onClick(key)
    tk.Button(root,text=buttons,width=6,relief="groove",command=cmd).grid(row=r,column=c)
    c += 1
    if c > 4:#no of row
        r += 1
        c = 0
entry = tk.Entry(root, width=30, bg="lightblue")
entry.grid(row=0,column=0,columnspan=5)
