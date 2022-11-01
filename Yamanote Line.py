# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:34:17 2022

@author: Emmanuel Maseruka
"""
##GUI

import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import Label



root=tk.Tk()
root.title("JR East Railway Cooperation")
#width, height = root.winfo_screenwidth(), root.winfo_screenheight()

#root.geometry('%dx%d+0+0' % (width,height))

#root.configure(bg='gray')
canvas = tk.Canvas(root, width=800, height =100)
canvas.grid(columnspan=3)

root.resizable(width=False, height=False)


#logo

logo= Image.open('C:/Users/Kevin Meng/OneDrive/Desktop/Python/logo.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

ike= Image.open('C:/Users/Kevin Meng/OneDrive/Desktop/Python/ike.png')
ike=ImageTk.PhotoImage(ike)
ike_label=tk.Label(image=ike)
ike_label.image = ike


tok= Image.open('C:/Users/Kevin Meng/OneDrive/Desktop/Python/tok.png')
tok=ImageTk.PhotoImage(tok)
tok_label=tk.Label(image=tok)
tok_label.image = tok

#instructions

welcome = tk.Label(root, text = "This is Yamanote line! ようこそ！！！",fg='black', font=('Arial',16,"bold"))
welcome.grid(columnspan=3, row=1)

instructions = tk.Label(root, text = "Current Location: ",fg='black', font=('Arial',14,'bold'))
instructions.grid(column=0, row=4)

current_loc=Label(root, fg='black', font=('Arial',14))
current_loc.grid(column=1, row=4)


instructions1 = tk.Label(root, text = "Destination: ",fg='black', font=('Arial',14,'bold'))
instructions1.grid(column=0, row=8)

last_loc=Label(root, fg='black', font=('Arial',14))
last_loc.grid(column=1, row=8)



#buttons
# 0.Ikebukuro 1.Ueno 2.Tokyo 3.Shinagawa 4.Shibuya 5.Shinjuku

start=""

def ikebukuro_start():
    global start
    current_loc.config(text="Ikebukuro") 
    ike_label.grid(column=1, row=0)
    start = 0
    print(start)     
ikebukuro=tk.StringVar()
ikebukuro_btn=tk.Button(root, textvariable = ikebukuro, command=lambda:ikebukuro_start(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
ikebukuro.set("Ikebukuro")
ikebukuro_btn.grid(column=0, row=5)

def ueno_start():
    global start
    current_loc.config(text="Ueno")
    start = 1
    print(start)     
ueno=tk.StringVar()
ueno_btn=tk.Button(root, textvariable = ueno, command=lambda:ueno_start(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
ueno.set("Ueno")
ueno_btn.grid(column=1, row=5)

def tokyo_start():
    global start
    current_loc.config(text="Tokyo")
    start = 2
    print(start)     
tokyo=tk.StringVar()
tokyo_btn=tk.Button(root, textvariable = tokyo, command=lambda:tokyo_start(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
tokyo.set("Tokyo")
tokyo_btn.grid(column=2, row=5)


def shinagawa_start():
    global start
    current_loc.config(text="Shinagawa")
    start = 3
    print(start)     
shinagawa=tk.StringVar()
shinagawa_btn=tk.Button(root, textvariable = shinagawa, command=lambda:shinagawa_start(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
shinagawa.set("Shinagawa")
shinagawa_btn.grid(column=0, row=6)

def shibuya_start():
    global start
    current_loc.config(text="Shibuya")
    start = 4
    print(start)     
shibuya=tk.StringVar()
shibuya_btn=tk.Button(root, textvariable = shibuya, command=lambda:shibuya_start(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
shibuya.set("Shibuya")
shibuya_btn.grid(column=1, row=6)


def shinjuku_start():
    global start
    current_loc.config(text="Shinjuku")
    start = 5
    print(start)     
shinjuku=tk.StringVar()
shinjuku_btn=tk.Button(root, textvariable = shinjuku, command=lambda:shinjuku_start(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
shinjuku.set("Shinjuku")
shinjuku_btn.grid(column=2, row=6)



end = ""


def ikebukuro_end():
    global end
    last_loc.config(text="Ikebukuro")
    end = 0
    print(end)     
ikebukuro=tk.StringVar()
ikebukuro_btn=tk.Button(root, textvariable = ikebukuro, command=lambda:ikebukuro_end(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
ikebukuro.set("Ikebukuro")
ikebukuro_btn.grid(column=0, row=10)


def ueno_end():
    global end
    last_loc.config(text="Ueno")
    end = 1
    print(end) 
ueno=tk.StringVar()
ueno_btn=tk.Button(root, textvariable = ueno, command=lambda:ueno_end(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
ueno.set("Ueno")
ueno_btn.grid(column=1, row=10)


def tokyo_end():
    global end
    last_loc.config(text="Tokyo")
    end = 2
    print(end)     
tokyo=tk.StringVar()
tokyo_btn=tk.Button(root, textvariable = tokyo, command=lambda:tokyo_end(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
tokyo.set("Tokyo")
tokyo_btn.grid(column=2, row=10)


def shinagawa_end():
    global end
    last_loc.config(text="Shinagawa")
    end = 3
    print(end)     
shinagawa=tk.StringVar()
shinagawa_btn=tk.Button(root, textvariable = shinagawa, command=lambda:shinagawa_end(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
shinagawa.set("Shinagawa")
shinagawa_btn.grid(column=0, row=11)

def shibuya_end():
    global end
    last_loc.config(text="Shibuya")
    end = 4
    print(end)     
shibuya=tk.StringVar()
shibuya_btn=tk.Button(root, textvariable = shibuya, command=lambda:shibuya_end(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
shibuya.set("Shibuya")
shibuya_btn.grid(column=1, row=11)


def shinjuku_end():
    global end
    last_loc.config(text="Shinjuku")
    end = 5
    print(end)     
shinjuku=tk.StringVar()
shinjuku_btn=tk.Button(root, textvariable = shinjuku, command=lambda:shinjuku_end(), font="Raleway",bg="green", height=1, width=8, cursor="hand2")
shinjuku.set("Shinjuku")
shinjuku_btn.grid(column=2, row=11)






A = [[0,8,12,18,23,26], 
    [22,0,4,10,15,19],[18,26,0,6,11,14],[12,20,24,0,5,8],[7,15,19,25,0,3],[4,12,16,22,27,0]]



names = ['ikebukuro','ueno','tokyo','shinagawa','shibuya','shinjuku']
df = pd.DataFrame(A, index=names, columns=names)


find_route = ""

def find_route():
    
    global find_route
    global platform2
    global platform1
    global plat1
    global plat2
    tok_label.grid(column=1, row=0)
    plat1=[start,end]
    plat2=[end,start]
    platform1=df.iat[plat1[0],plat1[1]]
    platform2=df.iat[plat2[0],plat2[1]]
    if platform1>platform2:
         emptylabel.config(text="Take platform 2 and ride for " + str(platform2)+ " stops to arrive at your destination")
    else:
        emptylabel.config(text="Take platform 1 and ride for " +str(platform1)+ " stops to arrive at your destination")   


route=tk.StringVar()
route_btn=tk.Button(root, textvariable = route, command=lambda:find_route(), font=("Raleway",12,"bold"),bg="red", height=2, width=8, cursor="hand2")
route.set("Find Route")
route_btn.grid(column=1, row=16)


emptylabel=Label(root, fg='black', font=('Arial',14))
emptylabel.grid(row =18, columnspan=3)



canvas = tk.Canvas(root, width=600, height =300)
canvas.grid(columnspan=3)

root.mainloop()






















    
    