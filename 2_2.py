#Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file
#passato come argomento

def somma_shampo():
    somma=0
    with open('shampoo_sales.csv','r') as file:
        next(file)  #salto la prima riga saltando l'header della tabella
        for line in file:
            elemento=line.split(',')
            somma += float(elemento[1])
    return somma

#print(somma_shampo())

#Definire una funzione che prende in input un file ed una parola e conta quante volte
#quella parola è presente sul file

def conta_presenza(percorso,parola):
    somma=0
    with open(percorso,'r') as file:
        for line in file:
            if parola in line:
                somma += 1

    return somma

print(conta_presenza("test.csv","test"))