def somma():
    
    while True:
        try:
            a=float(input('inserisci un addendo\n'))
            b=float(input('inserisci un addendo\n'))
            return a+b
        except ValueError:
            print('numeri non validi')
        

def diff():
    while True:
        try:
            a=float(input('inserisci il primo termine\n'))
            b=float(input('inserisci il secondo termine\n'))
            return a-b
        except ValueError:
            print('numeri non validi')

def esci():
    print('ciao')
    return 'exit'

scelte={"1":somma,"2":diff,"3":esci}

while True:
    scelta=input('inserisci: \n 1.Somma\n 2.Differenza\n 3.Esci\n')
    azione= scelte.get(scelta)
    if azione:
        risultato=azione()
        if(risultato=='exit'):
            break
        print(risultato)
    else:
        print('non valida')
        
