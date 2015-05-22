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
        menu.entryconfigure(1, label="Auswahl1")
        m.set(0)


mt=IntVar()
def manutemp(menu):
    if mt.get()==0:
        menu.entryconfigure(1, label="☑ Manuelle Temperatureingabe")
        manutemplabel.grid(row=1, columnspan=2) 
        temregel.grid(row=2, columnspan=2)
        mt.set(1)
    elif mt.get() ==1:
        menu.entryconfigure(1, label="☐ Manuelle Temperatureingabe")
        manutemplabel.grid_forget()
        temregel.grid_forget()
        mt.set(0)

ausp=IntVar()
def autosprach(menu):
    if ausp.get()==0:
        menu.entryconfigure(2, label="☑ Sprachausgabe")
        print("Sprachausgabe aktiviert")
        ausp.set(1)
    elif ausp.get() ==1:
        menu.entryconfigure(2, label="☐ Sprachausgabe")
        print("Sprachausgabe deaktiviert")
        ausp.set(0)


#Temperatur.def
def gettemp(event):
    temp=temregel.get()
    print(temp)

    
#Licht.def
def licht(event,jein,name):
    if jein.get() == 0:
        print(name,"ist an")
        jein.set(1)
    elif jein.get() == 1:
        print(name,"ist aus")
        jein.set(0)
     
#Fenster.def
def fensterauf(event,jein,name):
    if jein.get() == 0:
        print(name,"geöffnet")
        jein.set(1)
    elif jein.get() == 1:
        print(name,"geschlossen")
        jein.set(0)

#Tür.def
def tür(event,jein,name):
    if jein.get() == 0:
        print(name,"geöffnet")
        jein.set(1)
    elif jein.get() == 1:
        print(name,"geschlossen")
        jein.set(0)

        

#Menu
menu = Menu(root)
root.config(menu=menu)
Menus1=Menu(menu)
menu.add_cascade(label="Menus1", menu=Menus1)
Menus1.add_command(label="Auswahl1",command=lambda: menutest(Menus1))
Menus2=Menu(menu)
menu.add_cascade(label="Einstellungen", menu = Menus2)
Menus2.add_command(label="☐ Manuelle Temperatureingabe",command=lambda: manutemp(Menus2))
Menus2.add_command(label="☐ Sprachausgabe",command=lambda:autosprach(Menus2))


#Frames
Temp=Frame(root, cursor= "watch")
Licht=Frame(root, cursor="spider")
Fenster=Frame(root,cursor="pirate")
Tuer=Frame(root,cursor="star")

#Temperatur.Widget
settempein = Entry(Temp)
temregellable = Label(Temp, text = "Temperatur")
temregel = Scale(Temp, from_ = -10, to= 40, orient = HORIZONTAL,length=200,tickinterval=10, cursor="watch")
manutemplabel=Label(Temp, text="Manuelle Temperatursteuerung",font=("Arial",10,"normal","underline"))
#Licht.Widgets
wohnlicht=Button(Licht, text="Wohnzimmer")

#Fenster.Widgets
dachfenster=Button(Fenster,text="Dach")
badfenster=Button(Fenster,text="Bad")

#Tür.Widgets
garage=Button(Tuer,text="Garagentor")

#Temperatur.Variablen

#Licht.Variablen
wls="Wohnzimmerlicht"
wl=IntVar()

#Fenster.Variablen
dfs="Dachfenster"
df=IntVar()
bfs="Badezimmerfenster"
bf=IntVar()

#Tür.Variablen
gts="Garagentor"
gt=IntVar()

#Label
templabel= Label(Temp,text="Temperatur",font=("Arial",15,"bold","underline"))
lichtlabel = Label(Licht, text="Licht",font=("Arial",15,"bold","underline"))
fensterlabel = Label(Fenster, text="Fenster",font=("Arial",15,"bold","underline"))
tuerlabel = Label(Tuer, text="Türen und Tore",font=("Arial",15,"bold","underline"))



#Temperatur.bind
temregel.bind("<ButtonRelease-1>", gettemp)
#Licht.bind
wohnlicht.bind("<Button-1>",lambda e: licht(e,wl,wls))

#Fenster.bind
dachfenster.bind("<Button-1>",lambda e: fensterauf(e,df,dfs))
badfenster.bind("<Button-1>",lambda e: fensterauf(e,bf,bfs))

#Tür.bind
garage.bind("<Button-1>",lambda e: tür(e,gt,gts))


#Label.grid
templabel.grid(row=0,columnspan=3)
lichtlabel.grid(row=0,columnspan=3)
fensterlabel.grid(row=0,columnspan=3)
tuerlabel.grid(row=0,columnspan=3)




#Temperatur.grid
Temp.grid(row=1,column=0,sticky=N)
#Licht.grid
Licht.grid(row=1,column=1,sticky=N)
wohnlicht.grid(row=1, column=0)
#Fenster.grid
Fenster.grid(row=2, column=0,sticky=N)
dachfenster.grid(row=1,column=0)
badfenster.grid(row=1,column=1)
#Tür.grid
Tuer.grid(row=2,column=1,sticky=N)
garage.grid(row=1,column=0)


              

root.mainloop()
