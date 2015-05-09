from tkinter import *

root = Tk()
#Menus.def
def menutest():
    print("Test")


#Temperatur.def
def gettemp(event):
    karl=temregel.get()
    print(karl)

def settemp():
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
        settemp.grid(row=3, column=0, sticky=E)
        settempein.grid(row=3, column=1)
    elif arnold.get()==1:
        settemp.grid_forget()
        settempein.grid_forget()


#Licht.def
##def lichtan(event):
##    if l==1:
##        print("licht ist an")
##        l=0
##    elif l==0:
##        print("licht ist aus")
##        l=1
    
#Fenster.def
def dachf(event):
    print("Dachfenster geöffnet")


#Menu
menu = Menu(root)
root.config(menu=menu)
Menus1=Menu(menu)
menu.add_cascade(label="Menus1", menu=Menus1)
Menus1.add_command(label="Auswahl1",command=menutest)




#Frames
Temp=Frame(root, cursor= "watch")
Licht=Frame(root, cursor="spider")
Fenster=Frame(root,cursor="pirate")



#Temperatur.Widget
arnold=IntVar()
setmanu=Checkbutton(Temp, text="Manuelle Temperatureingabe?", variable = arnold)
settempein = Entry(Temp)
temregellable = Label(Temp, text = "Temperatur")
temregel = Scale(Temp, from_ = -10, to= 40, orient = HORIZONTAL,length=200,tickinterval=10, cursor="watch")
gettempknopf=Button(Temp, text="Hans Günther")
settemp = Button(Temp, text="Karl Gustav", command= settemp)

#Licht.Widgets
lichtmain=Button(Licht, text="Lichthauptschalter")

#Fenster.Widgets
dachf=Button(Fenster,text="Dach")




#Temperatur.bind
setmanu.bind("<Button-1>", manutemp)
gettempknopf.bind("<Button-1>", gettemp)
#settemp.bind("<Button-1>",settemp)

#Licht.bind
lichtmain.bind("<Button-1>",lichtan)

#Fenster.bind






#Temperatur.grid
Temp.grid(row=0,column=0)
setmanu.grid(row=2, column=1)
temregellable.grid(row=0, column=0)
temregel.grid(row=0, column=1)
gettempknopf.grid(row=1, columnspan=2)
#Licht.grid
Licht.grid(row=0,column=1)
lichtmain.grid(row=0, column=0)
#Fenster.grid


root.mainloop()
