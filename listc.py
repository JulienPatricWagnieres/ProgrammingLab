'''
quadrati=[x**2 for x in range(10)]
print(quadrati)

x=[x for x in range(1,6)]
print(x)

lista_uno=[1,2,3]
lista_due=[3,1,4]

mix=[(x,y) for x in lista_uno for y in lista_due if x != y]
print(mix)

lettere= [x for x in "banana"]
print(lettere)
'''

class MyNumbers:

    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a +=1
        return x
'''    
myclass= MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''

class Series:

    def __init__(self,low,high):
        self.current=low
        self.top=high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.current>self.top:
            raise(StopIteration)
        else:
            self.current += 1
            return self.current -1

  
myclass=Series(0,6)
myiter=iter(myclass)
'''
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

[print(s) for s in myiter]
n_list=Series(1,10)
print(list(n_list))
'''

class PowTwo:

    def __init__(self,max):
        self.max=max

    def __iter__(self):
        self.current=0 # partiamo da 2**0
        return self
    
    def __next__(self):
        if self.current>self.max:
            raise(StopIteration)
        else:
            self.current +=1
            return 2**(self.current-1)

'''      
myclass=PowTwo(4)
myiter=iter(myclass)
for x in myiter:
    print(x)
'''

class SuPari:

    def __init__(self,lista):
        self.lista=[x for x in lista if x%2 == 0]

    def __iter__(self):
        self.current=0
        return self

    def __next__(self):
        if self.current <= len(self.lista)-1:
            self.current +=1
            return self.lista[self.current-1]
        else:
            raise StopIteration

lista=[1,2,3,4,5,6,6,1,3,2]
myclass=SuPari(lista)
myiter=iter(myclass)
[print(s) for s in myiter]
