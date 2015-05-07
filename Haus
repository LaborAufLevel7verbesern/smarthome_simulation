from visual import *

anzeige = display(x=0, y=0, width=1000, height=1000)

class Hausboden:
    def __init__(self,x,z):
        Boden1 = box(pos=(0,0,0),size=(x,5,z), material = materials.wood)
        Boden2 = box(pos=(250+x*3/8,0,250),size=(x*3/4,5,z/2),material = materials.rough)
        

class HWand:
    def __init__(self,x,y,z):
        p1 = Polygon([(0,0),(x,0),(x,y),(0,y)])
        p2 = Polygon([(10,10),(x-10,10),(x-10,y-10),(10,y-10)])
        p3 = Polygon ([(x,330),(x,400),(x-20,400),(x-20,330)])
        Wand1 = extrusion(pos=[(-x/2,2.5,-y/2),(-x/2,z,-y/2)],shape=(p1-p2-p3),material = materials.rough)
        

class Wand:
    def __init__ (self,a,b,c,x,y,z):
        Wand = box(pos=(a,b,c),size=(x,y,z), material = materials.rough)

if __name__ == "__main__":
    Hausgrundriss = Hausboden(500,1000)
    Wand1 = HWand(500,1000,100)
    Wand2 = Wand (500*3/8+250,50,495,500*3/4,100,10)
    Wand3 = Wand (620,50,245,10,100,490)
    
