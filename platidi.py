from random import randint

class Platipo():
    


    def __init__(self,nome):
        self.nome=nome
        self.l_uova=[]  #uova è una lista di interi

    @classmethod
    def con_uova(cls,nome,l_uova):
        self.nome=nome
        self.l_uova=l_uova
    
    
    def conta_uova(self):
        somma=0
        for uova in self.l_uova:
            somma +=uova
        return somma

    def stagioni_feconde(self):
        stagioni=0
        for uova in self.l_uova:
            if uova != 0:
                stagioni +=1
        return stagioni
    
    def deponi_uova(self):
        uova=randint(0,3)
        self.l_uova.append(uova)

    def riassunto(self):
        uova=self.conta_uova()
        stagioni=self.stagioni_feconde()
        print(f'{self.nome} ha depositato un totale di {uova} uova, in {stagioni} stagioni feconde')

def simula_stagioni(platipi,n): #platipi è una lista di Platipo
    for x in range(n):    
        for platipo in platipi:
            platipo.deponi_uova()

pippo=Platipo("Pippo")
paperino=Platipo("Paperino")
topolino=Platipo("Topolino")
platipi=[pippo,paperino,topolino]
simula_stagioni(platipi,10)

pippo.riassunto()
paperino.riassunto()
topolino.riassunto()

