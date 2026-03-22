#Stampare l’equivalente di 538 minuti nel formato 8h:58min.

def min_to_h(min):
    print(f"{min//60}:{min%60}")

#min_to_h(538)

#2- Scrivere un programma che chiede all’utente un numero intero e stampa il suo quadrato e il suo cubo
def sq_cb(x):
    print(f"numero:{x}, quadrato:{x**2}, cubo:{x**3}")

#sq_cb(4)

#3 Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari.

def is_pari(x):
    if x%2==0: return True
    return False

#print(is_pari(5))

#4. Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte
#quella lettera è contenuta nella parola.

def conta_in(parola,lettera):
    cont=0
    for char in parola:
        if char==lettera: cont +=1

    return cont

#print(conta_in("123455","5" ))

#5.Scrivere un programma che verifica se un numero inserito dall’utente è primo.

def is_prime(x):
    for n in range(2,x):
        if x%n==0: return False
    return True

#print(is_prime(3))

#6.Scrivere un programma che fa la somma di n numeri inseriti dall’utente. Di all'utente di scrivere 0 per
#fermarsi.

def somma_n():
    somma=0
    while True:
        x=int(input("inserisci un valore intero o 0 per terminare la somma\n"))
        if x==0: return somma
        somma +=x

#print(somma_n())d

#7. Definire la funzione fattoriale (versione iterativa).

def fatt(x):
    fat=1
    for n in range(2,x+1):
        fat *=n
    return fat

#print(fatt(5))

#8. Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un
#triangolo e, se sì, di che tipo di triangolo.

def is_triangle(a,b,c):
    return (a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a)

#9.Definire una funzione che conta quante vocali sono presenti in una stringa.

def conta_vocali(stringa):
    conta=0
    for char in stringa:
        if char in "aeiouAEIOU": conta +=1
    return conta

#print(conta_vocali("ciao mi chiamo julien"))

