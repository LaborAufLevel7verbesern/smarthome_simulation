# -*- coding: cp1252 -*-
#Main
#Version 1.0

import time #, berechnung, wetterdaten
print("main geladen")

x=1

class Main:
    def __init__(self, wunschTemperatur, aktuelleTemperatur, regen):
        "Konstruktor"
        self.speed = 1
        self.aktuelleTemperatur = aktuelleTemperatur
        self.wunschTemperatur = self.aktuelleTemperatur


    def temperaturSetzen(self, wunschTemperatur):
        self.aktuelleTemperatur=(wunschTemperatur-self.aktuelleTemperatur)/2 + self.aktuelleTemperatur
        print(self.aktuelleTemperatur)

    def bewohnerSetzen(self, bool):
        pass

start = Main(20, 30, False)
while x:
    start.temperaturSetzen(20)
    time.sleep(x)
