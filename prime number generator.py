from tkinter import *
import tkinter as tk
import math
from tkinter import messagebox
from tkinter import ttk

def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False


def ok(e1111):
    st=e.get()
    ed=e2.get()
    
    l=[]
    if st=="" or ed=="":
        v="Please fill the starting and ending number"
    elif st==ed:
        v="Please enter 2 distinct numbers"
    else:
        st=int(st)
        ed=int(ed)
        for i in range(st,ed+1):
            if isprime(i):
                l.append(str(i))
        v="The prime numbers are :"+", ".join(l)
    ans=messagebox.askretrycancel("prime generator",(v),icon='info')
    if ans==0:
        root.destroy()
        
def okk():
    st=e.get()
    ed=e2.get()
    
    l=[]
    if st=="" or ed=="":
        v="Please fill the starting and ending number"
    elif st==ed:
        v="Please enter 2 distinct numbers"
    else:
        st=int(st)
        ed=int(ed)
        for i in range(st,ed+1):
            if isprime(i):
                l.append(str(i))
        v="The prime numbers are :"+", ".join(l)
    ans=messagebox.askretrycancel("prime generator",(v),icon='info')
    if ans==0:
        root.destroy()
    
    
root=Tk()
root.title("prime number generator")
root.geometry("300x400")
root.configure(bg="white")

l=Label(root,text="prime numbers generator",bg="white",fg="red",font=("ink free",20))
l.grid(column=1,row=1)

l1=Label(root,text="Enter starting number",bg="white",fg="black")
l1.grid(column=1,row=2)

e=Entry(root,width=27)
e.grid(column=1,row=3)

l2=Label(root,text="Enter last number",bg="white",fg="black")
l2.grid(column=1,row=5)

e2=Entry(root,width=27)
e2.grid(column=1,row=6)
e.focus()


b=Button(root,command=okk,text="Generate",bg="red",height=1,width=20)
b.grid(column=1,row=8)
root.bind('<Return>', ok)
root.mainloop()
