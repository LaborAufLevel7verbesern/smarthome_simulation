from tkinter import *

root = Tk()
#Menus.def 

m=IntVar()
def menutest(menu):
    if m.get()==0:
        print("Test")
        menu.entryconfigure(1, label="Auswahl2")
        m.set(1)
    elif m.get() ==1:
        print("Test2")
        +
        menu.entryconfigure(1, label="Auswahl1")
        m.set(0)

#Temperatur.def
def gettemp(event):
    karl=temregel.get()
    print(karl)

def settemp(event):
    frederick = settempein.get()
    peter= "sneaky"
    if frederick == peter:
        hans=Tk()
        sepp="sneaky sneaky"
        sneaky=Message(hans,text=sepp)
        sneaky.config(bg="white",fg="black",font=("aral",30,"bold"),borderwidth=2)
        sneaky.grid(rowspan=2,columnspan=3)
    else:
        temregel.set(frederick)

def manutemp(event):
    #print(arnold.get())
    if arnold.get()==0:
        settempknopf.grid(row=4, column=0, sticky=E)
        settempein.grid(row=4, column=1)
    elif arnold.get()==1:
        settempknopf.grid_forget()
        settempein.grid_forget()


#Licht.def
l=IntVar()
def lichtan(event):
    if l.get() == 0:
        print("licht ist an")
        l.set(1)
    elif l.get() == 1:
        print("licht ist aus")
        l.set(0)
     
#Fenster.def
df=IntVar()
def dachf(event):
    if df.get() == 0:
        print("Dachfenster geöffnet")
        df.set(1)
    elif df.get() == 1:
        print("Dachfenster geschlossen")
        df.set(0)

#Tür.def

        

#Menu
menu = Menu(root)
root.config(menu=menu)
Menus1=Menu(menu)
menu.add_cascade(label="Menus1", menu=Menus1)
Menus1.add_command(label="Auswahl1",command=lambda: menutest(Menus1))




#Frames
Temp=Frame(root, cursor= "watch")
Licht=Frame(root, cursor="spider")
Fenster=Frame(root,cursor="pirate")
Tür=Frame(root,cursor="star")



#Temperatur.Widget
arnold=IntVar()
setmanu=Checkbutton(Temp, text="Manuelle Temperatureingabe?", variable = arnold)
settempein = Entry(Temp)
temregellable = Label(Temp, text = "Temperatur")
temregel = Scale(Temp, from_ = -10, to= 40, orient = HORIZONTAL,length=200,tickinterval=10, cursor="watch")
gettempknopf = Button(Temp, text="Hans Günther")
settempknopf = Button(Temp, text="Karl Gustav")

#Licht.Widgets
lichtmain=Button(Licht, text="Lichthauptschalter")

#Fenster.Widgets
dachfenster=Button(Fenster,text="Dach")

#Tür.Widgets

#Label
templabel= Label(Temp,text="Temperatur",font=("Arial",15,"bold","underline"))
lichtlabel = Label(Licht, text="Licht",font=("Arial",15,"bold","underline"))
fensterlabel = Label(Fenster, text="Fenster",font=("Arial",15,"bold","underline"))
türlabel = Label(Tür, text="Türen",font=("Arial",15,"bold","underline"))



#Temperatur.bind
setmanu.bind("<Button-1>", manutemp)
gettempknopf.bind("<Button-1>", gettemp)
settempknopf.bind("<Button-1>",settemp)

#Licht.bind
lichtmain.bind("<Button-1>",lichtan)

#Fenster.bind
dachfenster.bind("<Button-1>",dachf)

#Tür.bind



#Label.grid
templabel.grid(row=0,columnspan=3)
lichtlabel.grid(row=0,columnspan=3)
fensterlabel.grid(row=0,columnspan=3)
türlabel.grid(row=0,columnspan=3)




#Temperatur.grid
Temp.grid(row=1,column=0,sticky=N)
setmanu.grid(row=3, column=1)
temregellable.grid(row=1, column=0)
temregel.grid(row=1, column=1)
gettempknopf.grid(row=2, columnspan=2)
#Licht.grid
Licht.grid(row=1,column=1,sticky=N)
lichtmain.grid(row=1, column=0)
#Fenster.grid
Fenster.grid(row=2, column=0,sticky=N)
dachfenster.grid(row=1,column=0)
#Tür.grid
Tür.grid(row=2,column=1,sticky=N)



              

root.mainloop()



