from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="white")

def BMI():
    h=float(height.get())
    w=float(weight.get())

    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="UnderWeight!")
        label3.config(text="You have lower weight than \n normal body!")

    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="It indicates that \n you are healthy!")

    elif bmi>25 and bmi<=30:
        label2.config(text="OverWeight!")
        label3.config(text="It indicates that a personis \n slightly overweight\n A doctor may advise some weight lose!")

    else:
        label2.config(text="Obes!")
        label3.config(text="Health may be at risk, if they \n do not lose weight!")

icon1=PhotoImage(file="icon.png")
root.iconphoto(False,icon1)

icon2=PhotoImage(file="top.png")
icon2_img=Label(root,image=icon2,background="white")
icon2_img.place(x=-10,y=-10)

bottom=Label(root,width=72,height=18,bg="lightgreen")
bottom.pack(side=BOTTOM)

icon3=PhotoImage(file="box.png")
b1=Label(root,image=icon3)
b1.place(x=20,y=100)
b2=Label(root,image=icon3)
b2.place(x=240,y=100)

icon4=PhotoImage(file="scale.png")
icon4_img=Label(root,image=icon4,background="lightgreen")
icon4_img.place(x=20,y=310)

currentvalue=tk.DoubleVar()

def get_curr():
    return '{: .2f}'.format(currentvalue.get())

def sliderch(event):
    height.set(get_curr())
    size=int(float(get_curr()))
    img=(Image.open("man.png"))
    resizedimg=img.resize((50,10+size))
    photo=ImageTk.PhotoImage(resizedimg)
    icon5_img.config(image=photo)
    icon5_img.place(x=70,y=550-size)
    icon5_img.image=photo

style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(root,from_=0,to=220,orient="horizontal",style="TScale",command=sliderch,variable=currentvalue)
slider.place(x=80,y=250)

currentvalue2=tk.DoubleVar()

def get_curr2():
    return '{: .2f}'.format(currentvalue2.get())

def sliderch2(event):
    weight.set(get_curr2())

style2=ttk.Style()
style2.configure("TScale",background="white")
slider2=ttk.Scale(root,from_=0,to=200,orient="horizontal",style="TScale",command=sliderch2,variable=currentvalue2)
slider2.place(x=300,y=250)


height=StringVar()
weight=StringVar()

h1=Entry(root,textvariable=height,width=5,font=("arial",50),bg="white",fg="black",bd=0,justify=CENTER)
h1.place(x=35,y=160)
height.set(currentvalue.get())

w1=Entry(root,textvariable=weight,width=5,font=("arial",50),bg="white",fg="black",bd=0,justify=CENTER)
w1.place(x=255,y=160)
weight.set(currentvalue2.get())

icon5_img=Label(root,background="lightgreen")
icon5_img.place(x=70,y=530)

but=Button(root,text="View Report",width=15,height=2,font=("arial",10,"bold"),bg="gray",fg="white",command=BMI)
but.place(x=280,y=340)

label1=Label(root,font=("arial",40,"bold"),bg="lightgreen",fg="black",pady=15)
label1.place(x=125,y=305)

label2=Label(root,font=("arial",20,"bold"),bg="lightgreen",fg="red")
label2.place(x=280,y=430)

label3=Label(root,font=("arial",10,"bold"),bg="lightgreen",fg="blue")
label3.place(x=200,y=500)

root.mainloop()