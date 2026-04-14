def quadrato():
    while True:
        try:
            n=int(input('inserisci un numero intero\n'))
            return n**2
        except ValueError:
            print('non è stato inserito un intero. riprova')

print(quadrato())
