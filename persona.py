class Persona():
    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome

    def saluta(self):
        print("ciao sono",self.ruolo + ",",self.nome, self.cognome)


class Studente(Persona):
    def __init__(self,nome,cognome,corsi):
        super().__init__("Studente UNItS",nome,cognome)
        self.corsi=corsi[:]
    
    def saluta(self):
        Persona.saluta(self)
        print(f"> Frequento i corsi {self.corsi}")

class Docente(Persona):
    def __init__(self,nome,cognome,corsi):
        super().__init__("Docente UNITS",nome,cognome)
        self.corsi=corsi[:]
    
    def saluta(self):
        Persona.saluta(self)
        print("> Docente dei corsi",self.corsi)

def insegna_corsi(docente,studente):
    return set(studente.corsi) <= set(docente.corsi)

def copertura(docenti,studenti):
    for studente in studenti:
        coperto=False

        for docente in docenti:
            if(insegna_corsi(docente,studente)):
                print(insegna_corsi(docente,studente))
                coperto=True
                break

        if not coperto:
            return False
    
    return True



doc1=Docente("Luca","Rondi",["Geometria","Analisi 1"])
doc2=Docente("Pippo","Culo",["Geometria","Programmazione"])
docenti=[doc1]
stud1=Studente("Jul","wag",["Geometria","Programmazione"])
stud2=Studente("Dario","Babbeo",["Geometria","Programmazione"])
studenti=[stud1]           
print(docenti[0].nome)
print(studenti)
print(insegna_corsi(doc1,stud1))
print(copertura(docenti,studenti))



