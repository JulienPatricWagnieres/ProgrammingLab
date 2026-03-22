'''
class cat():

    nazione='italia'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return (f"sono un oggetto Cat di nome {self.name} e ho {self.age} anni")
    
    def miao(self):
        print(f"{gatto.name} dice miao")
        

gatto=cat("tom",5)
print(gatto)
print(gatto.name)
print(gatto.nazione)
gatto.miao()
'''

import random
'''
class coin():
    

    def __init__(self):
        self.face=random.randint(0,1)

    def __str__(self):
        return f"{self.face}"

    def face(self):
        return self.face
    
    def lancia(self):
        self.face=random.randint(0,1)
        return self.face
    
moneta=coin()
moneta2=coin()
moneta.lancia
print(moneta)
moneta2.lancia()
print(moneta2)
'''

class Veicolo():

    def __init__(self,modello,marca,anno):
        self.modello=modello
        self.marca=marca
        self.anno=anno
        self.speed=0

    def __str__(self):
        return f"modello:{self.modello}, marca:{self.marca}, anno:{self.anno}, velocità:{self.speed}"
    
    def accellerare(self):
        self.speed +=5

    def frenare(self):
        if self.speed <= 5: self.speed=0
        else: self.speed -=5 

    def get_speed(self):
        return self.speed
    

