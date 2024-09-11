

from abstract_class import Vehicale
class Bike(Vehicale):
    def __int__(self,n,color):
        super().__int__(n)
        self.color=color
    def start(self):
        print("Start with kick")
class Scooty(Vehicale):
    def __int__(self,n):
        self.no_of_tyres=n
    def start(self):
        print("self start")
class Car(Vehicale):
    def __int__(self,n,x):
        super().__int__(n)
        self.no_of_gears=6
    def start(self):
        print("start with key")

v=Vehicale
