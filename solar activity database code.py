from ast import Global
from cgitb import text
from doctest import master
from email.mime import image
from hashlib import sha3_224
from ssl import Options
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import CENTER, Canvas, ttk
import tkinter as tk
from tkinter.tix import COLUMN
from turtle import bgcolor, width
import customtkinter
import time
import tkinter.font as font
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
from scipy.ndimage.filters import gaussian_filter1d
import csv
import os
from tkinter.filedialog import asksaveasfile





global frame1
global frame2



root=tk.Tk()
root.title('Solar Activity Database')
p1=tk.PhotoImage(file = 'app icon.png')
root.iconphoto(False,p1)

def dircetions():
    helpwin=tk.Toplevel()
    global direction1
    global direction2
    global direction7
    global direction3
    global direction4
    global direction5
    global direction6
    
        
    container = ttk.Frame(helpwin)
    canvas = Canvas(container, highlightbackground="black", highlightthickness=1, width=900, height=700)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview, troughcolor="red")
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
      "<Configure>",
      lambda e: canvas.configure(
       scrollregion=canvas.bbox("all")
                          )
                          )             
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
            

    
    direction1=tk.PhotoImage(file='direction1.png')
    direction1label=tk.Label(scrollable_frame,image=direction1)
    direction1label.pack()
    
    direction2=tk.PhotoImage(file='direction2.png')
    direction2label=tk.Label(scrollable_frame,image=direction2)
    direction2label.pack()

    direction7=tk.PhotoImage(file='direction7.png')
    direction7label=tk.Label(scrollable_frame,image=direction7)
    direction7label.pack()

    direction3=tk.PhotoImage(file='direction3.png')
    direction3label=tk.Label(scrollable_frame,image=direction3)
    direction3label.pack()
    direction4=tk.PhotoImage(file='direction4.png')
    direction4label=tk.Label(scrollable_frame,image=direction4)
    direction4label.pack()
    direction5=tk.PhotoImage(file='direction5.png')
    direction5label=tk.Label(scrollable_frame,image=direction5)
    direction5label.pack()
    direction6=tk.PhotoImage(file='direction6.png')
    direction6label=tk.Label(scrollable_frame,image=direction6)
    direction6label.pack()


    
    #scrollbar.pack( side = RIGHT, fill = Y)
    #scrollbar.config(command=helpcanvas.yview)

menubar = Menu(root,background='#9abfe4')
Help = Menu(menubar, tearoff=False, background='#9abfe4')
Help.add_command(label="Directions",command=dircetions)
Help.add_separator()
Help.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Help", menu=Help)
root.config(menu=menubar)



customtkinter.set_default_color_theme("dark-blue")
background_ph=tk.PhotoImage(file='back_ground.png')
# back ground image
canves=tk.Canvas(root,width=1300,height=800)
canves.pack(fill='both',expand=True)
canves.create_image(0,0,image=background_ph,anchor='nw')

#portsaid university logo
psu_ph=tk.PhotoImage(file='pu3.png')
psu_label=tk.Label(canves,image=psu_ph,bg='white')
psu_label.place(relx=0.25,rely=0.05,relheight=0.22,relwidth=0.13)
#faculty logo
college=tk.PhotoImage(file='logo.png')
college_label=tk.Label(canves,image=college,bg='white')
college_label.place(relx=0.09,rely=0.05,relheight=0.22,relwidth=0.15)
#EgSA logo
Egsa=tk.PhotoImage(file='Egsa.png')
main_background_label=tk.Label(canves,image=Egsa,bg='white')
main_background_label.place(relx=0.63,rely=0.05,relheight=0.22,relwidth=0.15)



#functions
def openNewWindow():
    global psuph
    global Egsa
    global spbg
    global st 
    global sci
    global pb
    global psu_ph
    global canvas2
    global p1
    pb = ttk.Progressbar(
    root, 
    orient='horizontal',
    mode='determinate',
    length=280)
              
    pb.place(relx=0.4,rely=0.7,relwidth=0.3,relheight=0.02)
    for i in range(5):
        pb['value']+=20
        root.update_idletasks()
        time.sleep(0.5)

    
        


    top=tk.Toplevel()
    top.title('Solar Activity Database')
    p1=tk.PhotoImage(file = 'app icon.png')
    top.iconphoto(False,p1)
    spbg=tk.PhotoImage(file='spbg.png')
    x=tk.Canvas(top,width=1450,height=900)
    x.pack(fill='both',expand=True) 
    frame1=customtkinter.CTkFrame(top)
    frame1.configure(fg_color='white', bg_color='white', corner_radius=10)
    frame1.place(relx=0.15,rely=0,relheight=1,relwidth=0.85)
    wrapper2 = LabelFrame(frame1, text="Data")
    wrapper2.pack(fill="both", expand="yes", padx=50, pady=10)
    wrapper2.place(relx=0.03,rely=0.01,relwidth=0.9,relheight=0.5)
    wrapper3 = LabelFrame(frame1, text="Selection")
    wrapper3.pack(fill="both", expand="yes",padx=50, pady=10)
    wrapper3.place(relx=0.03,rely=0.51,relwidth=0.9,relheight=0.48)
    switch1=customtkinter.CTkSwitch(master=wrapper2,text='start date & end date',onvalue="on", offvalue="off")
    switch1.place(relx=0.02,rely=0.02)
    switch2=customtkinter.CTkSwitch(master=wrapper2,text='duration',onvalue="on", offvalue="off")
    switch2.place(relx=0.02,rely=0.1)
    switch3=customtkinter.CTkSwitch(master=wrapper2,text='date-SSN of max',onvalue="on", offvalue="off")
    switch3.place(relx=0.2,rely=0.02)
    switch4=customtkinter.CTkSwitch(master=wrapper2,text='date-SNN of min',onvalue="on", offvalue="off")
    switch4.place(relx=0.2,rely=0.1)
    switch5=customtkinter.CTkSwitch(master=wrapper2,text='spotlessdays',onvalue="on", offvalue="off")
    switch5.place(relx=0.42,rely=0.02)

    con =sqlite3.connect('solar cycles.db')
    cur = con.cursor()
    options = []
    cur.execute("SELECT CS FROM solar_cycle1")
    ids = cur.fetchall()
    for i in ids: 
        options.append(str(i[0]))

      

    def lookupCycle(event):
        option = mycombo.get()
        con=sqlite3.connect('solar cycles.db')
        cur=con.cursor()
        cur.execute("SELECT * FROM solar_cycle1 WHERE CS=?",(option,))
        rows = cur.fetchall()
        for i in rows:
            SMonth.set(i[1])
            SYear.set(i[2])            
            EMonth.set(i[3])
            EYear.set(i[4])
            D.set(i[5])
            SD.set(i[6])
            DOM.set(i[7])
            MSOM.set(i[8])
            DOMin.set(i[9])
            MSOMin.set(i[10])
            
      
    opts = StringVar()
    Label(wrapper3, text="Select Cycle:").grid(row=3, column=1, padx=10, pady=10)
    mycombo = ttk.Combobox(wrapper3, textvariable=opts)
    mycombo['values'] = options
    mycombo.grid(row=3, column=2,padx=10, pady=10)
    mycombo.bind("<<ComboboxSelected>>", lookupCycle)
     
    SMonth = StringVar()
    SYear = StringVar()
    EMonth = StringVar()
    EYear = StringVar()
    D = StringVar()
    DOM = StringVar()
    MSOM = StringVar()
    DOMin = StringVar()
    MSOMin= StringVar()
    SD= StringVar()


    lbl1 = Label(wrapper3,text="Start Month")
    lbl1.grid(row=0, column=5, padx=10, pady=10)
    ent1 = Entry(wrapper3, textvariable=SMonth)
    ent1.grid(row=0, column=6, padx=10, pady=10)

    lbl2 = Label(wrapper3,text="Start Year")
    lbl2.grid(row=0, column=7, padx=10, pady=10)
    ent2 = Entry(wrapper3, textvariable=SYear)
    ent2.grid(row=0, column=8, padx=10, pady=10)

    lbl3 = Label(wrapper3,text="End Month")
    lbl3.grid(row=1, column=5, padx=10, pady=5)
    ent3 = Entry(wrapper3, textvariable=EMonth)
    ent3.grid(row=1, column=6, padx=10, pady=5)

    lbl4 = Label(wrapper3,text="End Year")
    lbl4.grid(row=1, column=7, padx=10, pady=5)
    ent4 = Entry(wrapper3, textvariable=EYear)
    ent4.grid(row=1, column=8, padx=10, pady=5)

    lbl5 = Label(wrapper3,text="Duration")
    lbl5.grid(row=2, column=5, padx=10, pady=5)
    ent5 = Entry(wrapper3, textvariable=D)
    ent5.grid(row=2, column=6, padx=10, pady=5)

    lbl6 = Label(wrapper3,text="Date of max")
    lbl6.grid(row=3, column=5, padx=10, pady=5)
    ent6 = Entry(wrapper3, textvariable=DOM)
    ent6.grid(row=3, column=6, padx=10, pady=5)

    lbl7 = Label(wrapper3,text="Monthly SSN of max")
    lbl7.grid(row=4, column=5, padx=10, pady=5)
    ent7 = Entry(wrapper3, textvariable=MSOM)
    ent7.grid(row=4, column=6, padx=10, pady=5)

    lbl8 = Label(wrapper3,text="Date of min")
    lbl8.grid(row=5, column=5, padx=10, pady=5)
    ent8 = Entry(wrapper3, textvariable=DOMin)
    ent8.grid(row=5, column=6, padx=10, pady=5)

    lbl9 = Label(wrapper3,text="Monthly SSN of min")
    lbl9.grid(row=6, column=5, padx=10, pady=5)
    ent9 = Entry(wrapper3, textvariable=MSOMin)
    ent9.grid(row=6, column=6, padx=10, pady=5)

    lbl10 = Label(wrapper3,text="Spotless days")
    lbl10.grid(row=7, column=5, padx=10, pady=5)
    ent10 = Entry(wrapper3, textvariable=SD)
    ent10.grid(row=7, column=6, padx=10, pady=5)

    def intbut1():
        tv=ttk.Treeview(wrapper2)
        tv.place(relx=0.02,rely=0.18,relwidth=0.9,relheight=0.8)
                
        if switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="off" :
            tv['columns']=('solar cycle','start date','end date')
            tv.column('#0', width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle')
            tv.heading('start date',text='start date')
            tv.heading('end date',text='end date')

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute("SELECT CS,ST,ED FROM Solar_cycle")
            rows2 = cur2.fetchall()    
            

            for row in rows2:    
                global mydata
                mydata = []
                mydata = rows2
               

                tv.insert("", tk.END, values=row)  
                con2.close()
            

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration')
            tv.column('solar cycle',width=80)
            tv.column('duration')
            tv.column('#0',width=0,stretch='no')
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
             
                mydata = []
                mydata = rows2
              

                tv.insert("", tk.END, values=row)  
                con2.close()
        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off" :
            tv['columns']=('solar cycle','date of max','SSN of max')
            tv.column('#0',width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('date of max',width=80)
            tv.column('SSN of max',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
               
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()
        
        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off" :
            tv['columns']=('solar cycle','date of min','SSN of min')
            tv.column('#0',width=0,stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('date of min',width=80)
            tv.column('SSN of min',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
               

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','spotless days')
            tv.column('#0',width=0,stretch='no' )
            tv.column('spotless days',width=80)
            tv.column('solar cycle',width=80,anchor=CENTER)
            tv.heading('#0',text='',anchor=CENTER)
            tv.heading('solar cycle',text='solar cycle')
            tv.heading('spotless days',text='spotless days')

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off" :
            tv['columns']=('solar cycle','start date','end date','date of max','SSN of max')
            tv.column('#0', width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('date of max',width=80)
            tv.column('SSN of max',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on" :
            tv['columns']=('solar cycle','start date','end date','date of max','SSN of max','Spotless days')
            tv.column('#0', width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('date of max',width=80)
            tv.column('SSN of max',width=80)
            tv.column('Spotless days',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)
            tv.heading('Spotless days',text='Spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
          
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','duration')
            tv.column('#0', width=0,anchor='w')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=90)
            tv.column('end date',width=90)
            tv.column('duration',width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off" :
            tv['columns']=('solar cycle','start date','end date','date of min','SSN of min')
            tv.column('#0', width=0,anchor='w')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('date of min',width=80)
            tv.column('SSN of min',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on" :
            tv['columns']=('solar cycle','start date','end date','spotless days')
            tv.column('#0', width=0,anchor='w')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('spotless days',width=80)
            
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

            
        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration','date of max','SSN of max')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max',anchor=CENTER)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max', anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

            
        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=80,anchor=CENTER)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER)
            tv.heading('#0',text='',anchor='w')
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of min',text='date of min', anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('spotless days', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('spotless days',text='spotless days' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','date of max','SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER,width=90)
            tv.column('SSN of min', anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max' ,anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','date of max','SSN of max','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('spotless days',anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max' ,anchor=CENTER)
            tv.heading('spotless days',text='spotless days' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on" :
            tv['columns']=('solar cycle','date of min','SSN of min','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90,anchor=CENTER)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMIN,MIN,SP  FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','duration','date of max','SNN of max')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of max',anchor=CENTER,width=90)
            tv.column('SNN of max',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SNN of max',text='SNN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMAX,MAX  FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','duration','date of min','SNN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of min',anchor=CENTER,width=90)
            tv.column('SNN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SNN of min',text='SNN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','end date','duration','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','end date','date of min','SSN of min','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','date of max' ,'SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max',anchor=CENTER,width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()



        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration','date of max' ,'SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration', anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
            
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','date of max' ,'SSN of max','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration', text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max', anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','date of min','SSN of min','Spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('Spotless days', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('Spotless days',text='Spotless days' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
              
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()



        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','date of max' ,'SSN of max','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','date of max' ,'SSN of max','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','date of max' ,'SSN of max','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

            
        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','duration','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',anchor=CENTER,width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

           

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','duration','date of max' ,'SSN of max','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',anchor=CENTER,width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,DU,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','date of end','duration','date of max' ,'SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
              
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()


        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','duration','date of max' ,'SSN of max','date of min','SSN of min','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotless days',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMAX,MAX,DMIN,MIN,SP  FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
               
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

       
    def plotbutton1():
        if mycombo.get()=='19':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 255 and 265')
               data = cur3.fetchall()
               dates=([])
               values=([])
               for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])
                
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
               
       
             
               plt.title('Solar cycle 19')
               plt.xlabel('year')
               plt.ylabel('SSN') 
               plt.plot(x,ysmoothed)
               plt.show()
            
           
        elif mycombo.get()=='20':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 265 and 276')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 20')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='21':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 277 and 287')
               data = cur3.fetchall()
               dates=[]
               values=[]  
               for row in data:
                  dates.append(str(row[0]))
                  values.append(row[1])

               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
       
               plt.title('Solar cycle 21')
               plt.xlabel('year')
               plt.ylabel('SSN')
               plt.plot(x,ysmoothed)
               plt.show()
         
        elif mycombo.get()=='22':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 287 and 297')
               data = cur3.fetchall()
               dates=[]
               values=[]  
               for row in data:
                  dates.append(str(row[0]))
                  values.append(row[1])
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
       
               plt.title('Solar cycle 22')
               plt.xlabel('year')
               plt.ylabel('SSN')
               plt.plot(x,ysmoothed)
               plt.show()
    
        elif mycombo.get()=='23':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 297 and 309')
               data = cur3.fetchall()
               dates=[]
               values=[]  
               for row in data:
                  dates.append(str(row[0]))
                  values.append(row[1])
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
       
               plt.title('Solar cycle 23')
               plt.xlabel('year')
               plt.ylabel('SSN')
               plt.plot(x,ysmoothed)
               plt.show()

        elif mycombo.get()=='1':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 56 and 67')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 1')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='2':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 67 and 76')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 2')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='3':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 76 and 85')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 3')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='4':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 85 and 99')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 4')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='5':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 99 and 111')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 5')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='6':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 111 and 124')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 6')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='7':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 124 and 134')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 7')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='8':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 134 and 144')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 8')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='9':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 144 and 156')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 9')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='10':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 156 and 168')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 10')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='11':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 168 and 179')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 11')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='12':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 179 and 191')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 12')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='13':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 191 and 203')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 13')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='14':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 203 and 214')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 14')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='15':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 214 and 224')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 15')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='16':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 224 and 234')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 16')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='17':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 234 and 245')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 17')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='18':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 245 and 255')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 18')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

        elif mycombo.get()=='24':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 309 and 320')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 24')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()


      



    def export():
        if len(mydata) < 1:
            messagebox.showerror("No Data","No data available to export")
            return False
        
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File","*.csv"),("All Files","*.*")))
        with open(fln,mode='w') as myfile:
            exp_writer = csv.writer(myfile,delimiter=',')
            for i in mydata:
                exp_writer.writerow(i)
        messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

  
    expbtn = customtkinter.CTkButton(master=wrapper2, text ="Export CSV", command=export)
    expbtn.place(relx=0.83,rely=0.02)
    expbtn.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
           
            
        



    intbutton1=customtkinter.CTkButton(master=wrapper2,text='show data',command=intbut1)
    intbutton1.place(relx=0.67,rely=0.02)
    intbutton1.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
       
    plotbutton1=customtkinter.CTkButton(master=wrapper3,text='plot',command=plotbutton1)
    plotbutton1.place(relx=0.1,rely=0.5)
    plotbutton1.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
    frame2=customtkinter.CTkFrame(top)
    frame2.configure(fg_color='#9abfe4', bg_color='#ffffff', corner_radius=7)
    frame2.place(relx=0,rely=0,relwidth=0.17,relheight=1)
    



    def but1():
       canvas2=tk.Canvas(frame1,bg='white',width=1200,height=1000)
       canvas2.place(relx=0,rely=0)
       frame3=tk.Frame(canvas2,bg='white')
       frame3.place(relx=0,rely=0,relheight=1,relwidth=1)
       wrapper1 = LabelFrame(frame3, text="Data")
       wrapper1.pack(fill="both", expand="yes", padx=50, pady=10)
       wrapper1.place(relx=0.03,rely=0.01,relwidth=0.99,relheight=0.45)
       wrapper2 = LabelFrame(frame3, text="Selection")
       wrapper2.pack(padx=50, pady=10, fill="both", expand="yes")
       wrapper2.place(relx=0.03,rely=0.46,relwidth=0.994,relheight=0.4)
       switch1=customtkinter.CTkSwitch(master=wrapper1,text='start date & end date',onvalue="on", offvalue="off")
       switch1.place(relx=0.02,rely=0.02)
       switch2=customtkinter.CTkSwitch(master=wrapper1,text='duration',onvalue="on", offvalue="off")
       switch2.place(relx=0.02,rely=0.1)
       switch3=customtkinter.CTkSwitch(master=wrapper1,text='date-SSN of max',onvalue="on", offvalue="off")
       switch3.place(relx=0.2,rely=0.02)
       switch4=customtkinter.CTkSwitch(master=wrapper1,text='date-SNN of min',onvalue="on", offvalue="off")
       switch4.place(relx=0.2,rely=0.1)
       switch5=customtkinter.CTkSwitch(master=wrapper1,text='spotlessdays',onvalue="on", offvalue="off")
       switch5.place(relx=0.42,rely=0.02)

       con =sqlite3.connect('solar cycles.db')
       cur = con.cursor()
       options = []
       cur.execute("SELECT CS FROM solar_cycle1")
       ids = cur.fetchall()
       for i in ids: 
           options.append(str(i[0]))

      

       def lookupCycle(event):
           option = mycombo.get()
           con=sqlite3.connect('solar cycles.db')
           cur=con.cursor()
           cur.execute("SELECT * FROM solar_cycle1 WHERE CS=?",(option,))
           rows = cur.fetchall()
           for i in rows:
               SMonth.set(i[1])
               SYear.set(i[2])            
               EMonth.set(i[3])
               EYear.set(i[4])
               D.set(i[5])
               SD.set(i[6])
               DOM.set(i[7])
               MSOM.set(i[8])
               DOMin.set(i[9])
               MSOMin.set(i[10])
      

       opts = StringVar()
       Label(wrapper2, text="Select Cycle:").grid(row=3, column=1, padx=10, pady=10)
       mycombo = ttk.Combobox(wrapper2, textvariable=opts)
       mycombo['values'] = options
       mycombo.grid(row=3, column=2,padx=10, pady=10)
       mycombo.bind("<<ComboboxSelected>>", lookupCycle)
     
       SMonth = StringVar()
       SYear = StringVar()
       EMonth = StringVar()
       EYear = StringVar()
       D = StringVar()
       DOM = StringVar()
       MSOM = StringVar()
       DOMin = StringVar()
       MSOMin= StringVar()
       SD= StringVar()


       lbl1 = Label(wrapper2,text="Start Month")
       lbl1.grid(row=0, column=5, padx=10, pady=10)
       ent1 = Entry(wrapper2, textvariable=SMonth)
       ent1.grid(row=0, column=6, padx=10, pady=10)

       lbl2 = Label(wrapper2,text="Start Year")
       lbl2.grid(row=0, column=7, padx=10, pady=10)
       ent2 = Entry(wrapper2, textvariable=SYear)
       ent2.grid(row=0, column=8, padx=10, pady=10)

       lbl3 = Label(wrapper2,text="End Month")
       lbl3.grid(row=1, column=5, padx=10, pady=5)
       ent3 = Entry(wrapper2, textvariable=EMonth)
       ent3.grid(row=1, column=6, padx=10, pady=5)

       lbl4 = Label(wrapper2,text="End Year")
       lbl4.grid(row=1, column=7, padx=10, pady=5)
       ent4 = Entry(wrapper2, textvariable=EYear)
       ent4.grid(row=1, column=8, padx=10, pady=5)

       lbl5 = Label(wrapper2,text="Duration")
       lbl5.grid(row=2, column=5, padx=10, pady=5)
       ent5 = Entry(wrapper2, textvariable=D)
       ent5.grid(row=2, column=6, padx=10, pady=5)

       lbl6 = Label(wrapper2,text="Date of max")
       lbl6.grid(row=3, column=5, padx=10, pady=5)
       ent6 = Entry(wrapper2, textvariable=DOM)
       ent6.grid(row=3, column=6, padx=10, pady=5)

       lbl7 = Label(wrapper2,text="Monthly SSN of max")
       lbl7.grid(row=4, column=5, padx=10, pady=5)
       ent7 = Entry(wrapper2, textvariable=MSOM)
       ent7.grid(row=4, column=6, padx=10, pady=5)

       lbl8 = Label(wrapper2,text="Date of min")
       lbl8.grid(row=5, column=5, padx=10, pady=5)
       ent8 = Entry(wrapper2, textvariable=DOMin)
       ent8.grid(row=5, column=6, padx=10, pady=5)

       lbl9 = Label(wrapper2,text="Monthly SSN of min")
       lbl9.grid(row=6, column=5, padx=10, pady=5)
       ent9 = Entry(wrapper2, textvariable=MSOMin)
       ent9.grid(row=6, column=6, padx=10, pady=5)

       lbl10 = Label(wrapper2,text="Spotless days")
       lbl10.grid(row=7, column=5, padx=10, pady=5)
       ent10 = Entry(wrapper2, textvariable=SD)
       ent10.grid(row=7, column=6, padx=10, pady=5)

       def intbut1():
        tv=ttk.Treeview(wrapper1)
        tv.place(relx=0.02,rely=0.18,relwidth=0.9,relheight=0.8)
        
        
        if switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="off" :
            tv['columns']=('solar cycle','start date','end date')
            tv.column('#0', width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cylcle')
            tv.heading('start date',text='start date')
            tv.heading('end date',text='end date')

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute("SELECT CS,ST,ED FROM Solar_cycle")
            rows2 = cur2.fetchall()    

            for row in rows2:
                global mydata
                mydata = []
                mydata = rows2
               

                tv.insert("", tk.END, values=row)  
                con2.close()
            

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration')
            tv.column('solar cycle',width=80)
            tv.column('duration')
            tv.column('#0',width=0,stretch='no')
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
              

                tv.insert("", tk.END, values=row)  
                con2.close()
        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off" :
            tv['columns']=('solar cycle','date of max','SSN of max')
            tv.column('#0',width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('date of max',width=80)
            tv.column('SSN of max',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()
        
        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off" :
            tv['columns']=('solar cycle','date of min','SSN of min')
            tv.column('#0',width=0,stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('date of min',width=80)
            tv.column('SSN of min',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
               

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','spotless days')
            tv.column('#0',width=0,stretch='no' )
            tv.column('spotless days',width=80)
            tv.column('solar cycle',width=80,anchor=CENTER)
            tv.heading('#0',text='',anchor=CENTER)
            tv.heading('solar cycle',text='solar cycle')
            tv.heading('spotless days',text='spotless days')

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off" :
            tv['columns']=('solar cycle','start date','end date','date of max','SSN of max')
            tv.column('#0', width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('date of max',width=80)
            tv.column('SSN of max',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on" :
            tv['columns']=('solar cycle','start date','end date','date of max','SSN of max','Spotless days')
            tv.column('#0', width=0,anchor='w',stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('date of max',width=80)
            tv.column('SSN of max',width=80)
            tv.column('Spotless days',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)
            tv.heading('Spotless days',text='Spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','duration')
            tv.column('#0', width=0,anchor='w')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=90)
            tv.column('end date',width=90)
            tv.column('duration',width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off" :
            tv['columns']=('solar cycle','start date','end date','date of min','SSN of min')
            tv.column('#0', width=0,anchor='w')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('date of min',width=80)
            tv.column('SSN of min',width=80)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on" :
            tv['columns']=('solar cycle','start date','end date','spotless days')
            tv.column('#0', width=0,anchor='w')
            tv.column('solar cycle',width=80)
            tv.column('start date',width=80)
            tv.column('end date',width=80)
            tv.column('spotless days',width=80)
            
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

            
        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration','date of max','SSN of max')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=80)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max',anchor=CENTER)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max', anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

            
        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=80,anchor=CENTER)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER)
            tv.heading('#0',text='',anchor='w')
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of min',text='date of min', anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('spotless days', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('spotless days',text='spotless days' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','date of max','SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER,width=90)
            tv.column('SSN of min', anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max' ,anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','date of max','SSN of max','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('spotless days',anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max' ,anchor=CENTER)
            tv.heading('spotless days',text='spotless days' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on" :
            tv['columns']=('solar cycle','date of min','SSN of min','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90,anchor=CENTER)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMIN,MIN,SP  FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','duration','date of max','SNN of max')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of max',anchor=CENTER,width=90)
            tv.column('SNN of max',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max',anchor=CENTER)
            tv.heading('SNN of max',text='SNN of max',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMAX,MAX  FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','duration','date of min','SNN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of min',anchor=CENTER,width=90)
            tv.column('SNN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of min',text='date of min',anchor=CENTER)
            tv.heading('SNN of min',text='SNN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','end date','duration','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','end date','date of min','SSN of min','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotless days',text='spotless days',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','end date','date of max' ,'SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date', anchor=CENTER, width=90)
            tv.column('end date', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max',anchor=CENTER,width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('end date',text='end date',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()



        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','duration','date of max' ,'SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration', anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','date of max' ,'SSN of max','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration', text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max',text='SSN of max', anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','date of min','SSN of min','Spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('Spotless days', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('Spotless days',text='Spotless days' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()



        elif switch1.get()=="off" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','date of max' ,'SSN of max','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DMAX,MAX,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                 

                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="off" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','duration','date of max' ,'SSN of max','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('duration',text='duration',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)

            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,DU,DMAX,MAX,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="off" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','date of max' ,'SSN of max','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

            
        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="off" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','duration','date of min','SSN of min','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',anchor=CENTER,width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMIN,MIN,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

           

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="off" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','duration','date of max' ,'SSN of max','spotlessdays')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',anchor=CENTER,width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration',anchor=CENTER,width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('spotlessdays', anchor=CENTER, width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('spotlessdays',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DMAX,MAX,DU,SP FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()

        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="off":
            tv['columns']=('solar cycle','start date','date of end','duration','date of max' ,'SSN of max','date of min','SSN of min')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMAX,MAX,DMIN,MIN FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()


        elif switch1.get()=="on" and switch2.get()=="on" and switch3.get()=="on" and switch4.get()=="on" and switch5.get()=="on":
            tv['columns']=('solar cycle','start date','date of end','duration','date of max' ,'SSN of max','date of min','SSN of min','spotless days')
            tv.column('#0', width=0, stretch='no')
            tv.column('solar cycle',width=90)
            tv.column('start date',anchor=CENTER,width=90)
            tv.column('date of end',anchor=CENTER,width=90)
            tv.column('duration', anchor=CENTER, width=90)
            tv.column('date of max', anchor=CENTER, width=90)
            tv.column('SSN of max', anchor=CENTER, width=90)
            tv.column('date of min', anchor=CENTER, width=90)
            tv.column('SSN of min',anchor=CENTER,width=90)
            tv.column('spotless days',anchor=CENTER,width=90)
            tv.heading('#0',text='',anchor='w')
            tv.heading('solar cycle',text='solar cycle',anchor=CENTER)
            tv.heading('start date',text='start date',anchor=CENTER)
            tv.heading('date of end',text='date of end',anchor=CENTER)
            tv.heading('duration',text='duration' ,anchor=CENTER)
            tv.heading('date of max',text='date of max' ,anchor=CENTER)
            tv.heading('SSN of max' ,text='SSN of max', anchor=CENTER)
            tv.heading('date of min',text='date of min' ,anchor=CENTER)
            tv.heading('SSN of min',text='SSN of min',anchor=CENTER)
            tv.heading('spotless days',text='spotlessdays' ,anchor=CENTER)
            con2 =sqlite3.connect('solar cycles.db')
            cur2 = con2.cursor()
            cur2.execute('SELECT CS,ST,ED,DU,DMAX,MAX,DMIN,MIN,SP  FROM Solar_cycle')
            rows2 = cur2.fetchall()    

            for row in rows2:
                mydata = []
                mydata = rows2
                tv.insert("", tk.END, values=row)  
                con2.close()



       
       def plotbutton1():
         if mycombo.get()=='19':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 255 and 265')
               data = cur3.fetchall()
               dates=([])
               values=([])
               for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])
                
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
               
       
             
               plt.title('Solar cycle 19')
               plt.xlabel('year')
               plt.ylabel('SSN') 
               plt.plot(x,ysmoothed)
               plt.show()
            
           
         elif mycombo.get()=='20':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 265 and 276')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 20')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='21':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 277 and 287')
               data = cur3.fetchall()
               dates=[]
               values=[]  
               for row in data:
                  dates.append(str(row[0]))
                  values.append(row[1])

               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
       
               plt.title('Solar cycle 21')
               plt.xlabel('year')
               plt.ylabel('SSN')
               plt.plot(x,ysmoothed)
               plt.show()
         
         elif mycombo.get()=='22':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 287 and 297')
               data = cur3.fetchall()
               dates=[]
               values=[]  
               for row in data:
                  dates.append(str(row[0]))
                  values.append(row[1])
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
       
               plt.title('Solar cycle 22')
               plt.xlabel('year')
               plt.ylabel('SSN')
               plt.plot(x,ysmoothed)
               plt.show()
    
         elif mycombo.get()=='23':
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 297 and 309')
               data = cur3.fetchall()
               dates=[]
               values=[]  
               for row in data:
                  dates.append(str(row[0]))
                  values.append(row[1])
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
       
               plt.title('Solar cycle 23')
               plt.xlabel('year')
               plt.ylabel('SSN')
               plt.plot(x,ysmoothed)
               plt.show()

         elif mycombo.get()=='1':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 56 and 67')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 1')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='2':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 67 and 76')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 2')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='3':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 76 and 85')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 3')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='4':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 85 and 99')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 4')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='5':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 99 and 111')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 5')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='6':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 111 and 124')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 6')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='7':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 124 and 134')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 7')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='8':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 134 and 144')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 8')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='9':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 144 and 156')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 9')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='10':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 156 and 168')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 10')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='11':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 168 and 179')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 11')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='12':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 179 and 191')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 12')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='13':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 191 and 203')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 13')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='14':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 203 and 214')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 14')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='15':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 214 and 224')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 15')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='16':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 224 and 234')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 16')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='17':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 234 and 245')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 17')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()

         elif mycombo.get()=='18':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 245 and 255')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 18')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()
         elif mycombo.get()=='24':
             con3=sqlite3.connect('solar cycles.db')
             cur3=con3.cursor()
             sql=cur3.execute('SELECT * FROM Yearly_SSN where rowid between 309 and 320')
             data = cur3.fetchall()
             dates=[]
             values=[]  
             for row in data:
                 dates.append(str(row[0]))
                 values.append(row[1])

             x=np.array(dates)  
             y=np.array(values)
             ysmoothed = gaussian_filter1d(y, sigma=2)
       
             plt.title('Solar cycle 24')
             plt.xlabel('year')
             plt.ylabel('SSN')
             plt.plot(x,ysmoothed)
             plt.show()


       def export():
           if len(mydata) < 1:
               messagebox.showerror("No Data","No data available to export")
               return False
        
           fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File","*.csv"),("All Files","*.*")))
           with open(fln,mode='w') as myfile:
               exp_writer = csv.writer(myfile,delimiter=',')
               for i in mydata:
                   exp_writer.writerow(i)
           messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

  
       expbtn1 = customtkinter.CTkButton(master=wrapper1, text ="Export CSV", command=export)
       expbtn1.place(relx=0.83,rely=0.02)
       expbtn1.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')



          
       intbutton1=customtkinter.CTkButton(master=wrapper1,text='show data',command=intbut1)
       intbutton1.place(relx=0.67,rely=0.02)
       intbutton1.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
       
       plotbutton1=customtkinter.CTkButton(master=wrapper2,text='plot',command=plotbutton1)
       plotbutton1.place(relx=0.1,rely=0.5)
       plotbutton1.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
    


    def but2():
        canvas3=tk.Canvas(frame1,bg='white',width=1200,height=1000)
        canvas3.place(relx=0,rely=0)
        frame4=tk.Frame(canvas3,bg='white')
        frame4.place(relx=0,rely=0,relheight=1,relwidth=1)
        wrapper3 = LabelFrame(frame4, text="Data")
        wrapper3.pack(fill="both", expand="yes", padx=50, pady=10)
        wrapper3.place(relx=0.03,rely=0.01,relwidth=0.9,relheight=0.33)
        wrapper4 = LabelFrame(frame4, text="Selection")
        wrapper4.pack(padx=50, pady=10, fill="both", expand="yes")
        wrapper4.place(relx=0.03,rely=0.34,relwidth=0.9,relheight=0.34)
        q = StringVar()
       
        def update(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                global mydata
                mydata = []
                mydata = rows
                trv.insert('','end', values=i)
        

        conn = sqlite3.connect('solar cycles.db')
        cur = conn.cursor()

        def search():
            q2 = q.get()
            query = "SELECT * FROM Daily_SSN WHERE Year LIKE '%"+q2+"%'"
            cur.execute(query)
            rows = cur.fetchall()
            update(rows) 

        trv = ttk.Treeview(wrapper3, columns=(1,2,3,4), show="headings", height="15")
        trv.pack()

        trv.heading(1, text="Year")
        trv.heading(2, text="Month")
        trv.heading(3, text="Day")
        trv.heading(4, text="SSN")
        query = 'SELECT * from Daily_SSN'
        cur.execute(query)
        rows = cur.fetchall()
        update(rows)


         #search
        lbl = Label(wrapper4, text= "Select year:")
        lbl.pack(side=tk.LEFT, padx=10)
        lbl.place(relx=0.033, rely=0.25)
        ent = Entry(wrapper4, textvariable=q)
        ent.pack(side=tk.LEFT, padx=6)
        ent.place(relx=0.1, rely=0.25)
        btn = Button(wrapper4, text="Show data", command=search)
        btn.pack(side=tk.LEFT, padx=6)
        btn.place(relx=0.23, rely=0.25)

        def export():
            if len(mydata) < 1:
                messagebox.showerror("No Data","No data available to export")
                return False
        

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File","*.csv"),("All Files","*.*")))
            with open(fln,mode='w') as myfile:
                exp_writer = csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp_writer.writerow(i)
            messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

  
        expbtn = customtkinter.CTkButton(master=wrapper4, text ="Export CSV", command=export)
        expbtn.place(relx=0.1,rely=0.5)
        expbtn.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

        def plotbutton2():
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT "Year","SSN" FROM Daily_SSN' )
               data = cur3.fetchall()
               dates=([])
               values=([])
               for row in data:
                 dates.append((row[0]))
                 values.append(row[1])
                
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
               
       
               plt.xticks(np.arange(1818,2022,step=6), rotation ='vertical')
               plt.title('Daily sunspot number')
               plt.xlabel('year')
               
               plt.ylabel('SSN') 
               plt.plot(x,ysmoothed)
               plt.show()
 

        plotbutton2=customtkinter.CTkButton(master=wrapper4,text='plot',command=plotbutton2)
        plotbutton2.place(relx=0.1,rely=0.4)
        plotbutton2.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

    def but3():
       canvas4=tk.Canvas(frame1,bg='white',width=1200,height=1000)   
       canvas4.place(relx=0,rely=0,relheight=1,relwidth=1)
       frame5=tk.Frame(canvas4,bg='white')
       frame5.place(relx=0,rely=0,relheight=1,relwidth=1)
       wrapper5 = LabelFrame(frame5, text="Data")
       wrapper5.pack(fill="both", expand="yes", padx=50, pady=10)
       wrapper5.place(relx=0.03,rely=0.01,relwidth=0.9,relheight=0.5)
       wrapper6 = LabelFrame(frame5, text="Selection")
       wrapper6.pack(padx=50, pady=10, fill="both", expand="yes")
       wrapper6.place(relx=0.03,rely=0.51,relwidth=0.9,relheight=0.45)
       M = StringVar()
       
       
       def update(rows):
            trv1.delete(*trv1.get_children())
            for i in rows:
                global mydata
                mydata = []
                mydata = rows
                trv1.insert('','end', values=i)
        

       conn = sqlite3.connect('solar cycles.db')
       cur = conn.cursor()

       
       def search():
            M2 = M.get()
            query = ("SELECT * FROM Monthly_SSN WHERE Year LIKE '%"+M2+"%'" )
            cur.execute(query)
            rows = cur.fetchall()
            update(rows) 

       
       trv1 = ttk.Treeview(wrapper5, columns=(1,2,3), show="headings", height="15")
       trv1.pack()

       trv1.heading(1, text="Year")
       trv1.heading(2, text="Month")
       trv1.heading(3, text="SSN")
       query1 = 'SELECT * from Monthly_SSN'
       cur.execute(query1)
       rows = cur.fetchall()
       update(rows)


         #search
       lbl1 = Label(wrapper6, text= "Select year:")
       lbl1.pack(side=tk.LEFT, padx=10)
       lbl1.place(relx=0.04, rely=0.25)
       ent1 = Entry(wrapper6, textvariable=M)
       ent1.pack(side=tk.LEFT, padx=6)
       ent1.place(relx=0.1, rely=0.25)
       btn1 = Button(wrapper6, text="Show data", command=search)
       btn1.pack(side=tk.LEFT, padx=6)
       btn1.place(relx=0.23, rely=0.25)
      
       def export():
           if len(mydata) < 1:
               messagebox.showerror("No Data","No data available to export")
               return False
        

           fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File","*.csv"),("All Files","*.*")))
           with open(fln,mode='w') as myfile:
               exp_writer = csv.writer(myfile,delimiter=',')
               for i in mydata:
                    exp_writer.writerow(i)
           messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

  
       expbtn = customtkinter.CTkButton(master=wrapper6, text ="Export CSV", command=export)
       expbtn.place(relx=0.1,rely=0.5)
       expbtn.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

       def plotbutton3():
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT "Year","SSN" FROM Monthly_SSN' )
               data = cur3.fetchall()
               dates=([])
               values=([])
               for row in data:
                 dates.append((row[0]))
                 values.append(row[1])
                
               x=np.array(dates)  
               y=np.array(values)
               ysmoothed = gaussian_filter1d(y, sigma=2)
               
       
               plt.xticks(np.arange(1749,2022,step=7), rotation ='vertical')
               plt.title('Monthly sunspot number')
               plt.xlabel('year')
               
               plt.ylabel('SSN') 
               plt.plot(x,ysmoothed)
               plt.show()
   

 



      
       plotbutton3=customtkinter.CTkButton(master=wrapper6,text='plot',command=plotbutton3)
       plotbutton3.place(relx=0.1,rely=0.4)
       plotbutton3.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

    def but4():
        canvas5=tk.Canvas(frame1,bg='white',width=1200,height=1000)
        canvas5.place(relx=0,rely=0,relheight=1,relwidth=1)
        frame6=tk.Frame(canvas5,bg='white')
        frame6.place(relx=0,rely=0,relheight=1,relwidth=1)
        wrapper7 = LabelFrame(frame6, text="Selection")
        wrapper7.pack(fill="both", expand="yes", padx=50, pady=10)
        wrapper7.place(relx=0.03,rely=0.01,relwidth=0.9,relheight=0.5)
        wrapper8 = LabelFrame(frame6, text="Data")
        wrapper8.pack(padx=50, pady=10, fill="both", expand="yes")
        wrapper8.place(relx=0.03,rely=0.51,relwidth=0.9,relheight=0.45)
        def update(rows):
            trv5.delete(*trv5.get_children())
            for i in rows:
                global mydata
                mydata = []
                mydata = rows
                trv5.insert('','end', values=i)
        conn = sqlite3.connect('solar cycles.db')
        cur = conn.cursor()
        trv5 = ttk.Treeview(wrapper7, columns=(1,2), show="headings", height="18")
        trv5.pack()
        trv5.heading(1, text="Year")
        trv5.heading(2, text="Sunspot number")
        query = 'SELECT * from Yearly_SSN'
        cur.execute(query)
        rows = cur.fetchall()
        update(rows)

        con =sqlite3.connect('solar cycles.db')
        cur = con.cursor()
        options1 = []
        cur.execute("SELECT Year FROM Yearly_SSN")
        ids1 = cur.fetchall()
        for i in ids1: 
           options1.append(str(i[0]))

      

        def lookupYear(event):
           option1 = mycombo3.get()
           query2 = "SELECT * FROM Yearly_SSN WHERE Year LIKE '%"+option1+"%'"
           cur.execute(query2)
           rows1 = cur.fetchall()
           for i in rows1:
               SSN.set(i[1])
               
      
        opts1 = StringVar()
        Label(wrapper8, text="Select year:").grid(row=0, column=1, padx=10, pady=10)
        mycombo3 = ttk.Combobox(wrapper8, textvariable=opts1)
        mycombo3['values'] = options1
        mycombo3.grid(row=0, column=2,padx=10, pady=10)
        mycombo3.bind("<<ComboboxSelected>>", lookupYear)
     
        SSN = StringVar()


        lbl4 = Label(wrapper8,text="SSN")
        lbl4.grid(row=0, column=5, padx=10, pady=10)
        ent4 = Entry(wrapper8, textvariable=SSN)
        ent4.grid(row=0, column=6, padx=10, pady=10)

        def export():
            if len(mydata) < 1:
               messagebox.showerror("No Data","No data available to export")
               return False
        

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File","*.csv"),("All Files","*.*")))
            with open(fln,mode='w') as myfile:
               exp_writer = csv.writer(myfile,delimiter=',')
               for i in mydata:
                    exp_writer.writerow(i)
            messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

  
        expbtn = customtkinter.CTkButton(master=wrapper8, text ="Export CSV", command=export)
        expbtn.place(relx=0.08,rely=0.3)
        expbtn.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')


        def plotbutton4():
               con3=sqlite3.connect('solar cycles.db')
               cur3=con3.cursor()
               sql=cur3.execute('SELECT "Year","SSN" FROM Yearly_SSN' )
               data = cur3.fetchall()
               dates=([])
               values=([])
               for row in data:
                 dates.append((row[0]))
                 values.append(row[1])
                
               x=np.array(dates)  
               y=np.array(values)
                       
               plt.xticks(np.arange(1700,2021,step=8), rotation ='vertical')
               plt.title('Yearly sunspot number')
               plt.xlabel('year')
               
               plt.ylabel('SSN') 
               plt.plot(x,y)
               plt.show()
   
        plotbutton4=customtkinter.CTkButton(master=wrapper8,text='plot',command=plotbutton4)
        plotbutton4.place(relx=0.08,rely=0.2)
        plotbutton4.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

    def but5():
        canvas6=tk.Canvas(frame1,bg='white',width=1200,height=1000)
        canvas6.place(relx=0,rely=0,relheight=1,relwidth=1)
        frame7=tk.Frame(canvas6,bg='white')
        frame7.place(relx=0,rely=0,relheight=1,relwidth=1)
        wrapper9 = LabelFrame(frame7, text="Data")
        wrapper9.pack(fill="both", expand="yes", padx=50, pady=10)
        wrapper9.place(relx=0.03,rely=0.01,relwidth=0.9,relheight=0.5)
        wrapper01 = LabelFrame(frame7, text="Most powerful data")
        wrapper01.pack(padx=50, pady=10, fill="both", expand="yes")
        wrapper01.place(relx=0.03,rely=0.52,relwidth=0.9,relheight=0.55)
        switch_9 = customtkinter.CTkSwitch(master=wrapper9, text="start time & end time",
                                            onvalue="on", offvalue="off")
        switch_9.place(relx=0.02,rely=0.02)
        switch_10 = customtkinter.CTkSwitch(master=wrapper9, text="class",onvalue="on", offvalue="off")
        switch_10.place(relx=0.02,rely=0.1)
        switch_11 = customtkinter.CTkSwitch(master=wrapper9, text="Active region", onvalue="on", offvalue="off")
        switch_11.place(relx=0.2,rely=0.02)
        switch_12 = customtkinter.CTkSwitch(master=wrapper9, text="position",
                                                         onvalue="on", offvalue="off")
        switch_12.place(relx=0.2,rely=0.1)
        
  
        def intbutton5():
            global tv1
            tv1=ttk.Treeview(wrapper9)
            tv1.place(relx=0.02,rely=0.18,relwidth=0.9,relheight=0.8)
            if switch_9.get()=="on" and switch_10.get()=="off" and switch_11.get()=="off" and switch_12.get()=="off":
                tv1['columns']=('Date','start time','end time')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='start time',anchor=CENTER)
                tv1.heading('end time',text='end time',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  global mydata
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="off" and switch_10.get()=="on" and switch_11.get()=="off" and switch_12.get()=="off":
                tv1['columns']=('Date','class')
                tv1.column('Date',width=80)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)


                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,Cl FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="off" and switch_10.get()=="off" and switch_11.get()=="on" and switch_12.get()=="off":
                tv1['columns']=('Date','Active region')
                tv1.column('Date',width=80)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)
                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,AC FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()
                
            elif switch_9.get()=="off" and switch_10.get()=="off" and switch_11.get()=="off" and switch_12.get()=="on":
                tv1['columns']=('Date','position')
                tv1.column('Date',width=80)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,PO FROM Solar_flare')
                rows = cur.fetchall()    

                for row in rows:
                    mydata = []
                    mydata = rows5 
                    tv1.insert("", tk.END, values=row)  
                    con.close()

            elif switch_9.get()=="on" and switch_10.get()=="on" and switch_11.get()=="off" and switch_12.get()=="off":
                tv1['columns']=('Date','start time','end time','class')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='start time',anchor=CENTER)
                tv1.heading('end time',text='end time',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,Cl,St,En FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

                
            elif switch_9.get()=="on" and switch_10.get()=="off" and switch_11.get()=="on" and switch_12.get()=="off":
                tv1['columns']=('Date','start time','end time','Active region')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='start time',anchor=CENTER)
                tv1.heading('end time',text='end time',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En,AC FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="on" and switch_10.get()=="off" and switch_11.get()=="off" and switch_12.get()=="on":
                tv1['columns']=('Date','start time','end time','position')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='start time',anchor=CENTER)
                tv1.heading('end time',text='end time',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="off" and switch_10.get()=="on" and switch_11.get()=="on" and switch_12.get()=="off":
                tv1['columns']=('Date','class','Active region')
                tv1.column('Date',width=80)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,Cl,AC FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="off" and switch_10.get()=="on" and switch_11.get()=="off" and switch_12.get()=="on":
                tv1['columns']=('Date','class','position')
                tv1.column('Date',width=80)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,Cl,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="off" and switch_10.get()=="off" and switch_11.get()=="on" and switch_12.get()=="on":
                tv1['columns']=('Date','Active region','position')
                tv1.column('Date',width=80)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)
                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,AC,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="off" and switch_10.get()=="on" and switch_11.get()=="on" and switch_12.get()=="on":
                tv1['columns']=('Date','class','Active region','position')
                tv1.column('Date',width=80)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,Cl,AC,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="on" and switch_10.get()=="on" and switch_11.get()=="off" and switch_12.get()=="on":
                tv1['columns']=('Date','start time','end time','class','position')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='Start time',anchor=CENTER)
                tv1.heading('end time',text='End time',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En,Cl,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="on" and switch_10.get()=="off" and switch_11.get()=="on" and switch_12.get()=="on":
                tv1['columns']=('Date','start time','end time','Active region','position')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='Start time',anchor=CENTER)
                tv1.heading('end time',text='End time',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En,AC,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="on" and switch_10.get()=="on" and switch_11.get()=="on" and switch_12.get()=="off":
                tv1['columns']=('Date','start time','end time','class','Active region')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='Start time',anchor=CENTER)
                tv1.heading('end time',text='End time',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En,Cl,AC FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()

            elif switch_9.get()=="on" and switch_10.get()=="on" and switch_11.get()=="on" and switch_12.get()=="on":
                tv1['columns']=('Date','start time','end time','class','Active region','position')
                tv1.column('Date',width=80)
                tv1.column('start time',width=80,anchor=CENTER)
                tv1.column('end time',width=80,anchor=CENTER)
                tv1.column('class',width=80,anchor=CENTER)
                tv1.column('Active region',width=80,anchor=CENTER)
                tv1.column('position',width=80,anchor=CENTER)
                tv1.column('#0',width=0, stretch='no',anchor='w')
                tv1.heading('#0',text='',anchor='w')
                tv1.heading('Date',text='Date',anchor=CENTER)
                tv1.heading('start time',text='Start time',anchor=CENTER)
                tv1.heading('end time',text='End time',anchor=CENTER)
                tv1.heading('class',text='Class',anchor=CENTER)
                tv1.heading('Active region',text='Active region',anchor=CENTER)
                tv1.heading('position',text='Position',anchor=CENTER)

                con =sqlite3.connect('solar cycles.db')
                cur = con.cursor()
                cur.execute('SELECT Da,St,En,Cl,AC,Po FROM Solar_flare')
                rows5 = cur.fetchall()    

                for row in rows5:
                  mydata = []
                  mydata = rows5 
                  tv1.insert("", tk.END, values=row)
                  con.close()
    




        M1 = StringVar()
        def update(rows5):
            tv1.delete(*tv1.get_children())
            for i in rows5:
                tv1.insert('','end', values=i)
        

        conn = sqlite3.connect('solar cycles.db')
        cur = conn.cursor()

       
        def search():
                M3 = M1.get()
                query5 = "SELECT * FROM Solar_flare WHERE Da LIKE '%"+M3+"%'"
                cur.execute(query5)
                rows5 = cur.fetchall()
                update(rows5) 

      


                 #search
        lbl5 = Label(wrapper01, text= "Select Date:")
        lbl5.pack(side=tk.LEFT, padx=10)
        lbl5.place(relx=0.53, rely=0.25)
        ent5 = Entry(wrapper01, textvariable=M1)
        ent5.pack(side=tk.LEFT, padx=6)
        ent5.place(relx=0.6, rely=0.25)
        btn5 = Button(wrapper01, text="Show data", command=search)
        btn5.pack(side=tk.LEFT, padx=6)
        btn5.place(relx=0.75, rely=0.25)      

        intbutton5=customtkinter.CTkButton(wrapper9,text='show data',command=intbutton5)
        intbutton5.place(relx=0.7,rely=0.09)
        intbutton5.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
        
        #plotbutton5=customtkinter.CTkButton(master=frame7,text='plot')
        #plotbutton5.place(relx=0.75,rely=0.15)
        #plotbutton5.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')
        def showdata():
            M_10=tk.Toplevel()
            cM=tk.Canvas(M_10,width=1400,height=900)
            cM.pack()
            frame_M=tk.Frame(cM,bg='white')
            frame_M.place(relx=0,rely=0,relwidth=1,relheight=1)
            tv3=ttk.Treeview(M_10)
            tv3.place(relx=0.15,rely=0.2,relwidth=0.8,relheight=0.6)
            tvs3=tk.Scrollbar(tv3)
            tvs3.pack(side='right',fill='y')
            tv3['columns']=('Number of solar flare','Day','Month','Year','Start time','Peak time','End time','Class','Position','Active region')
            tv3.column('#0',width=0,anchor='w',stretch='no')
            tv3.column('Number of solar flare',width=60,anchor=CENTER)
            tv3.column('Day',width=60,anchor=CENTER)
            tv3.column('Month',width=60,anchor=CENTER)
            tv3.column('Year',width=60,anchor=CENTER)
            tv3.column('Start time',width=60,anchor=CENTER)
            tv3.column('Peak time',width=60,anchor=CENTER)
            tv3.column('End time',width=60,anchor=CENTER)
            tv3.column('Class',width=60,anchor=CENTER)
            tv3.column('Position',width=60,anchor=CENTER)
            tv3.column('Active region',width=60,anchor=CENTER)
            tv3.heading('#0',text='',anchor='w')
            tv3.heading('Number of solar flare',text='Number of solar flare',anchor=CENTER)
            tv3.heading('Day',text='Day',anchor=CENTER)
            tv3.heading('Month',text='Month',anchor=CENTER)
            tv3.heading('Year',text='Year',anchor=CENTER)
            tv3.heading('Start time',text='Start time',anchor=CENTER)
            tv3.heading('Peak time',text='Peak time',anchor=CENTER)
            tv3.heading('End time',text='End time',anchor=CENTER)
            tv3.heading('Class',text='Class',anchor=CENTER)
            tv3.heading('Position',text='Position',anchor=CENTER)
            tv3.heading('Active region',text='Active region',anchor=CENTER)

            con =sqlite3.connect('solar cycles.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM Powerful_flareS21")
            rows = cur.fetchall()    

            for row in rows:
                  tv3.insert("", tk.END, values=row)
            
            '''
            def update(rows):  
             trv5.delete(*trv5.get_children())
             for i in rows:  
                 mydata = []
                 mydata = rows
                 trv5.insert('','end', values=i)
             conn = sqlite3.connect('solar cycles.db')
             cur = conn.cursor()
             trv5 = ttk.Treeview(wrapper9, columns=(1,2,3,4,5,6,7,8,9), show="headings")
             trv5.pack()
             trv5.heading(1, text="Y")
             trv5.heading(2, text="M")
             trv5.heading(3, text="ED")
             trv5.heading(4, text="D")
             trv5.heading(5, text="ST")
             trv5.heading(6, text="PT")
             trv5.heading(7, text="P")
             trv5.heading(8, text="PO")
             trv5.heading(9, text="AC")
             query = 'SELECT * from Solar_flare'
             cur.execute(query)
             rows = cur.fetchall()
             mydata=rows
            update(rows)

            '''

            def export():
                if len(mydata) < 1:
                 messagebox.showerror("No Data","No data available to export")
                 return False
        
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File","*.csv"),("All Files","*.*")))
                with open(fln,mode='w') as myfile:
                  exp_writer = csv.writer(myfile,delimiter=',')
                  for i in mydata:
                    exp_writer.writerow(i)
                messagebox.showinfo("Data Exported", "Your data has been exported to "+os.path.basename(fln)+" successfully.")

  
        expbtn = customtkinter.CTkButton(master=wrapper9, text ="Export CSV", command=export)
        expbtn.place(relx=0.85,rely=0.09)
        expbtn.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')


        showdata=customtkinter.CTkButton(master=wrapper01,text='Most powerful 10 solar flares in solar cycle 21',command=showdata)
        showdata.place(relx=0.02,rely=0.1)
        showdata.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')      

        def showdata1():
            M_10=tk.Toplevel()
            cM=tk.Canvas(M_10,width=1400,height=900)
            cM.pack()
            frame_M=tk.Frame(cM,bg='white')
            frame_M.place(relx=0,rely=0,relwidth=1,relheight=1)
            tv3=ttk.Treeview(M_10)
            tv3.place(relx=0.15,rely=0.2,relwidth=0.8,relheight=0.6)
            tvs3=tk.Scrollbar(tv3)
            tvs3.pack(side='right',fill='y')
            tv3['columns']=('Number of solar flare','Day','Month','Year','Start time','Peak time','End time','Class','Position','Active region')
            tv3.column('#0',width=0,anchor='w',stretch='no')
            tv3.column('Number of solar flare',width=60,anchor=CENTER)
            tv3.column('Day',width=60,anchor=CENTER)
            tv3.column('Month',width=60,anchor=CENTER)
            tv3.column('Year',width=60,anchor=CENTER)
            tv3.column('Start time',width=60,anchor=CENTER)
            tv3.column('Peak time',width=60,anchor=CENTER)
            tv3.column('End time',width=60,anchor=CENTER)
            tv3.column('Class',width=60,anchor=CENTER)
            tv3.column('Position',width=60,anchor=CENTER)
            tv3.column('Active region',width=60,anchor=CENTER)
            tv3.heading('#0',text='',anchor='w')
            tv3.heading('Number of solar flare',text='Number of solar flare',anchor=CENTER)
            tv3.heading('Day',text='Day',anchor=CENTER)
            tv3.heading('Month',text='Month',anchor=CENTER)
            tv3.heading('Year',text='Year',anchor=CENTER)
            tv3.heading('Start time',text='Start time',anchor=CENTER)
            tv3.heading('Peak time',text='Peak time',anchor=CENTER)
            tv3.heading('End time',text='End time',anchor=CENTER)
            tv3.heading('Class',text='Class',anchor=CENTER)
            tv3.heading('Position',text='Position',anchor=CENTER)
            tv3.heading('Active region',text='Active region',anchor=CENTER)

            con =sqlite3.connect('solar cycles.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM Powerful_flareS22")
            rows = cur.fetchall()    

            for row in rows:

                 

                tv3.insert("", tk.END, values=row)  
                con.close()




        showdata1=customtkinter.CTkButton(master=wrapper01,text='Most powerful 10 solar flares in solar cycle 22',command=showdata1)
        showdata1.place(relx=0.02,rely=0.25)
        showdata1.configure(bg_color='#c3d9ef',fg_color='#c3d9ef') 

        def showdata2():
            M_10=tk.Toplevel()
            cM=tk.Canvas(M_10,width=1400,height=900)
            cM.pack()
            frame_M=tk.Frame(cM,bg='white')
            frame_M.place(relx=0,rely=0,relwidth=1,relheight=1)
            tv3=ttk.Treeview(M_10)
            tv3.place(relx=0.15,rely=0.2,relwidth=0.8,relheight=0.6)
            tvs3=tk.Scrollbar(tv3)
            tvs3.pack(side='right',fill='y')
            tv3['columns']=('Number of solar flare','Day','Month','Year','Start time','Peak time','End time','Class','Position','Active region')
            tv3.column('#0',width=0,anchor='w',stretch='no')
            tv3.column('Number of solar flare',width=60,anchor=CENTER)
            tv3.column('Day',width=60,anchor=CENTER)
            tv3.column('Month',width=60,anchor=CENTER)
            tv3.column('Year',width=60,anchor=CENTER)
            tv3.column('Start time',width=60,anchor=CENTER)
            tv3.column('Peak time',width=60,anchor=CENTER)
            tv3.column('End time',width=60,anchor=CENTER)
            tv3.column('Class',width=60,anchor=CENTER)
            tv3.column('Position',width=60,anchor=CENTER)
            tv3.column('Active region',width=60,anchor=CENTER)
            tv3.heading('#0',text='',anchor='w')
            tv3.heading('Number of solar flare',text='Number of solar flare',anchor=CENTER)
            tv3.heading('Day',text='Day',anchor=CENTER)
            tv3.heading('Month',text='Month',anchor=CENTER)
            tv3.heading('Year',text='Year',anchor=CENTER)
            tv3.heading('Start time',text='Start time',anchor=CENTER)
            tv3.heading('Peak time',text='Peak time',anchor=CENTER)
            tv3.heading('End time',text='End time',anchor=CENTER)
            tv3.heading('Class',text='Class',anchor=CENTER)
            tv3.heading('Position',text='Position',anchor=CENTER)
            tv3.heading('Active region',text='Active region',anchor=CENTER)

            con =sqlite3.connect('solar cycles.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM Powerful_flareS23")
            rows = cur.fetchall()    

            for row in rows:

                 

                tv3.insert("", tk.END, values=row)  
                con.close()




        showdata2=customtkinter.CTkButton(master=wrapper01,text='Most powerful 10 solar flares in solar cycle 23',command=showdata2)
        showdata2.place(relx=0.02,rely=0.4)
        showdata2.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

        def showdata3():
            M_10=tk.Toplevel()
            cM=tk.Canvas(M_10,width=1400,height=900)
            cM.pack()
            frame_M=tk.Frame(cM,bg='white')
            frame_M.place(relx=0,rely=0,relwidth=1,relheight=1)
            tv3=ttk.Treeview(M_10)
            tv3.place(relx=0.15,rely=0.2,relwidth=0.8,relheight=0.6)
            tvs3=tk.Scrollbar(tv3)
            tvs3.pack(side='right',fill='y')
            tv3['columns']=('Number of solar flare','Day','Month','Year','Start time','Peak time','End time','Class','Position','Active region')
            tv3.column('#0',width=0,anchor='w',stretch='no')
            tv3.column('Number of solar flare',width=60,anchor=CENTER)
            tv3.column('Day',width=60,anchor=CENTER)
            tv3.column('Month',width=60,anchor=CENTER)
            tv3.column('Year',width=60,anchor=CENTER)
            tv3.column('Start time',width=60,anchor=CENTER)
            tv3.column('Peak time',width=60,anchor=CENTER)
            tv3.column('End time',width=60,anchor=CENTER)
            tv3.column('Class',width=60,anchor=CENTER)
            tv3.column('Position',width=60,anchor=CENTER)
            tv3.column('Active region',width=60,anchor=CENTER)
            tv3.heading('#0',text='',anchor='w')
            tv3.heading('Number of solar flare',text='Number of solar flare',anchor=CENTER)
            tv3.heading('Day',text='Day',anchor=CENTER)
            tv3.heading('Month',text='Month',anchor=CENTER)
            tv3.heading('Year',text='Year',anchor=CENTER)
            tv3.heading('Start time',text='Start time',anchor=CENTER)
            tv3.heading('Peak time',text='Peak time',anchor=CENTER)
            tv3.heading('End time',text='End time',anchor=CENTER)
            tv3.heading('Class',text='Class',anchor=CENTER)
            tv3.heading('Position',text='Position',anchor=CENTER)
            tv3.heading('Active region',text='Active region',anchor=CENTER)

            con =sqlite3.connect('solar cycles.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM Powerful_flareS24")
            rows = cur.fetchall()    

            for row in rows:

                 

                tv3.insert("", tk.END, values=row)  
                con.close()




        showdata3=customtkinter.CTkButton(master=wrapper01,text='Most powerful 10 solar flares in solar cycle 24',command=showdata3)
        showdata3.place(relx=0.02,rely=0.55)
        showdata3.configure(bg_color='#c3d9ef',fg_color='#c3d9ef')

    #Buttons
    button1=customtkinter.CTkButton(master=frame2,
                                 width=234,
                                 height=90,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Solar Cycles",
                                 border_color='#9abfe4',
                                 command=but1
                                 )
    button1.configure(bg_color='#9abfe4',fg_color='#9abfe4',hover_color='#ffffff',compound='right')
    button1.configure(state=tk.NORMAL)
    button_state = button1.state
    button1.place(relx=0.,rely=0)


    button2=customtkinter.CTkButton(master=frame2,
                                 width=234,
                                 height=90,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Daily Sun Spot Number",
                                 border_color='#9abfe4',
                                 command=but2
                                 )
    button2.configure(bg_color='#9abfe4',fg_color='#9abfe4',hover_color='#ffffff',compound='right')
    button2.configure(state=tk.NORMAL)
    button_state = button2.state
    button2.place(relx=0,rely=0.13)

    button3=customtkinter.CTkButton(master=frame2,
                                 width=234,
                                 height=90,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Monthly Sun Spot Number",
                                 border_color='#9abfe4',
                                 command=but3
                            
                                 )
    button3.configure(bg_color='#9abfe4',fg_color='#9abfe4',hover_color='#ffffff',compound='right')
    button3.configure(state=tk.NORMAL)
    button_state = button3.state
    button3.place(relx=0,rely=0.28)
    button4=customtkinter.CTkButton(master=frame2,
                                 width=234,
                                 height=90,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Yearly Sun Spot Number",
                                 border_color='#9abfe4',
                                 command=but4
                                 )
    button4.configure(bg_color='#9abfe4',fg_color='#9abfe4',hover_color='#ffffff',compound='right')
    button4.configure(state=tk.NORMAL)
    button_state = button4.state
    button4.place(relx=0,rely=0.43)

    button5=customtkinter.CTkButton(master=frame2,
                                 width=234,
                                 height=90,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Solar Flares",
                                 border_color='#9abfe4',
                                 command=but5
                                 )
    button5.configure(bg_color='#9abfe4',fg_color='#9abfe4',hover_color='#ffffff',compound='right')
    button5.place(relx=0,rely=0.6)

#create a button and nested inside root
sun_icon=tk.PhotoImage(file='arrow.png').subsample(2,2)
button1=tk.Button(root,image=sun_icon,borderwidth=0,bg='white',activebackground='white',command=lambda:openNewWindow())
button1.place(relx=0.83,rely=0.85,relwidth=0.08,relheight=0.08)
#EUT trainig logo
trainingng_ph=tk.PhotoImage(file='EUT.png')
sub=tk.Label(canves,image=trainingng_ph,bg='white')
sub.place(relx=0.8,rely=0.05,relheight=0.22,relwidth=0.15)
#the text
#'Times 35 italic bold'
Font_tuple = ("Comic Sans MS", 20, "bold")
pro_name=canves.create_text(680,250,text=' SOLAR ACTIVITY DATABASE',font='Helvetica 35 italic bold',fill='#f2f2f2')
team48=canves.create_text(680,310,text='Team 48',font='Helvetica 35 italic bold',fill='#f2f2f2')
design=canves.create_text(180,450,text='Designed & Devolped By:',font='Helvetica 20 italic bold',fill='#e6e6e6')
name1= canves.create_text(180,490,text='  Khaled W.Elzend',font='Helvetica 16 italic bold',fill='#f2f2f2')
name2= canves.create_text(180,530,text='Manar A.Nofal',font='Helvetica 16 italic bold',fill='#f2f2f2')


insractour=canves.create_text(550,580,text='supervision: ',font='Helvetica 19 italic bold',fill='#e6e6e6')
dr=canves.create_text(590,620,text='Dr Wael Mohamed',font='Helvetica 16 italic bold',fill='#f2f2f2')

root.mainloop()
