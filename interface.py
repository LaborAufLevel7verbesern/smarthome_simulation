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
        manutemplabel.grid(row=3, columnspan=2) 
        settempein.grid(row=4, columnspan=2)
        mt.set(1)
    elif mt.get() ==1:
        menu.entryconfigure(1, label="☐ Manuelle Temperatureingabe")
        settempein.grid_forget()
        manutemplabel.grid_forget()
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
    elif frederick == "":
        karlgustav=Tk()
        arnold="Error-404 Not Found"
        nab=Message(karlgustav,text=arnold)
        nab.config(bg="white",fg="black",font=("aral",20,"bold"),borderwidth=2)
        nab.grid(rowspan=2,columnspan=3)

    
    
    else:
        temregel.set(frederick)
        print(frederick)
        


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
        print(dfs.get(),"geöffnet")
        df.set(1)
       # dfs.set(dfse)
    elif df.get() == 1:
        print(dfs.get(),"geschlossen")
        df.set(0)

#Tür.def
ga=IntVar()
def gar(event):
    if ga.get() == 0:
        print("Garagentor geöffnet")
        ga.set(1)
    elif ga.get() == 1:
        print("Garagentor geschlossen")
        ga.set(0)

        

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

#Tür.Widgets
garage=Button(Tuer,text="Garagentor")

#Temperatur.Variablen

#Licht.Variablen
wms=StringVar()
wms.set("Wohnzimmerlicht")

#Fenster.Variablen
dfs=StringVar()
dfs.set("Dachfenster")





#Label
templabel= Label(Temp,text="Temperatur",font=("Arial",15,"bold","underline"))
lichtlabel = Label(Licht, text="Licht",font=("Arial",15,"bold","underline"))
fensterlabel = Label(Fenster, text="Fenster",font=("Arial",15,"bold","underline"))
tuerlabel = Label(Tuer, text="Türen und Tore",font=("Arial",15,"bold","underline"))



#Temperatur.bind
temregel.bind("<ButtonRelease-1>", gettemp)
settempein.bind("<Return>",settemp)
#Licht.bind
wohnlicht.bind("<Button-1>",lichtan)

#Fenster.bind
dachfenster.bind("<Button-1>",dachf)

#Tür.bind
garage.bind("<Button-1>",gar)


#Label.grid
templabel.grid(row=0,columnspan=3)
lichtlabel.grid(row=0,columnspan=3)
fensterlabel.grid(row=0,columnspan=3)
tuerlabel.grid(row=0,columnspan=3)




#Temperatur.grid
Temp.grid(row=1,column=0,sticky=N)
temregellable.grid(row=1, column=0)
temregel.grid(row=1, column=1)
#Licht.grid
Licht.grid(row=1,column=1,sticky=N)
wohnlicht.grid(row=1, column=0)
#Fenster.grid
Fenster.grid(row=2, column=0,sticky=N)
dachfenster.grid(row=1,column=0)
#Tür.grid
Tuer.grid(row=2,column=1,sticky=N)
garage.grid(row=1,column=0)


              

root.mainloop()
