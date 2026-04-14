#1.Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il
#conteggio delle occorrenze.

def somma_l(lista):
    somma=0
    for item in lista:
        somma += item
    return somma

#print(somma_l([2,2,4,4]))

#2.Scrivere una funzione che prende in input una stringa e ritorna True se è un
#palindromo, False altrimenti.

def is_palindromo(stringa): #return stringa=stringa[::-1]
    for i in range(len(stringa)//2):
        if stringa[i]!=stringa[len(stringa)-1-i]: return False
    return True

#print(is_palindromo("cicaaic"))

#3.Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di
#A[i] con A[j].

def scambia_l(lista,i,j):
    #var=lista[i]
    #lista[i]=lista[j]
    #lista[j]=var
    lista[i],lista[j]=lista[j],lista[i]
'''
lista=["a","b","c","d","e"]
scambia_l(lista,0,4)
print(lista)
'''
#4.Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno
#almeno un elemento in comune

def in_comune(l1,l2):
    for item in l1:
        if item in l2: return True
    return False
    #return bool(set(l1) & set(l2))  #migliore prestazione... va come somma non prodotto

#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una
#lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] -
#>["uno","zero","sette","nove","otto"]

def in_cifra(list):
    dict = {1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove"}
    lista=[]
    for item in list:
        lista.append(dict[item])
    return lista

#print(in_cifra([1,2,3,1]))

# Scrivere una funzione che prende una lista di parole e restituisce un dizionario con il conteggio delle occorrenze. python

def conta_parole(lista):
    diz={}
    for parola in lista:
        if parola in diz:
            diz[parola] +=1
        else: diz[parola]=1
    return diz

#print(conta_parole(['ciao','ciao','mondo','ciao','cane']))

#Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file
#passato come argomento

def somma_shampoo(nome_file):
    somma=0
    file= open(nome_file,'r')
    for riga in file:
        riga=riga.strip()
        riga_l=riga.split(',')
        #print(riga_l[0],riga_l[1])
        if riga_l[0]!="Date":
            somma+=float(riga_l[1])
    file.close()
    return somma
         
print(somma_shampoo('shampoo_sales.csv'))

