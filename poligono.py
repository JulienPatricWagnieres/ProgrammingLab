class Poligono():

    def __init__(self,lati):
        self.lati=lati

    def __str__(self):
        return f'Sono un poligono con {self.lati} lati.'
    
class Quadrilatero(Poligono):

    def __init__(self):
        super().__init__(4)

    def __str__(self):
        return f'Sono un quadrilatero'
    
class Rettangolo(Quadrilatero):
    
    def __init__(self,b,a):
        super().__init__()
        self.b=b
        self.a=a
    
    def __str__(self):
        return f'Sono un rettangolo di base:{self.b} e altezza:{self.a}'
    
    def perimetro(self):
        return 2*self.b+2*self.a
    
    def area(self):
        return self.b*self.a
    
class Triangolo(Poligono):

    def __init__(self,a,b,c):
        super().__init__(3)
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        print(super().__str__())
        return f'sono un triangolo di lati {self.a}, {self.b} e {self.c}'
    
    def perimetro(self):
        return self.a+self.b+self.c
    
    def is_equilatero(self):
        return (self.a==self.b and self.b==self.c)
    
pol=Poligono(7)
print(pol)
quad=Quadrilatero()
rect=Rettangolo(4,5)
print(rect)
print(rect.area())
print(rect.perimetro())
tr=Triangolo(3,3,3)
print(tr)
print(tr.perimetro())
print(tr.lati)
print(tr.is_equilatero())
