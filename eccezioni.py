class Errore(Exception):
    pass



my_var='ciao'
try:
    my_var=float(my_var)
except Exception as e:
    print('NO')
    print(f'{e}')

print(my_var)

raise Errore("MONA")