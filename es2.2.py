class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self,name):
        self.name=name

    def get_data(self):

        try:
            time_series=open(self.name,'r')
        except FileNotFoundError:
            raise ExamException('file non trovato:"{}"'.format(self.name))
        next(time_series) #saltiamo l'header del file

        data=[] 

        for line in time_series:
            list_linea=line.strip().split(',')
# Verifichiamo che la data non sia duplicata
            if data:       
                for el in data:
                    if el[0] == list_linea[0]:
                        raise ExamException('Errore, data duplicata')

# Verifichiamo che la data corrente sia maggiore della precedente
            if data:
                if list_linea[0][:4] < data[-1][0][:4]:
                    raise ExamException('csv non ordinato')
                if list_linea[0][:4] == data[-1][0][:4] and list_linea[0][:4] < data[-1][0][:4]:
                    raise ExamException('csv non ordinato')


            try:
                data.append([list_linea[0],int(list_linea[1])])
            except Exception:
                pass


        return data
    
def compute_list_years(time_series): #crea un diz anno:lista passeggeri per mese
    current_year = time_series[0][0][:4]
    lista_y=[]
    diz={}
    for i,data in enumerate(time_series):
        if current_year == data[0][:4]:
            lista_y.append(data[1])

            #se sono all'ultimo elemento allora aggiorno il dizionario

            #se sono alla fine aggiorno il dizionario
            
            if i == len(time_series)-1:
                diz[current_year]=lista_y
            elif current_year != time_series[i+1][0][:4]:
                diz[current_year]=lista_y
                current_year=time_series[i+1][0][:4]
                lista_y=[]
    return diz

def compute_media(time_series,first_year,last_year):  #creo un dizionario Anno:media psg
    diz_year=compute_list_years(time_series)
    diz={}
    #creo una lista di stringhe di anni che voglio considerare
    primo=int(first_year)
    ultimo=int(last_year)
    anni_da_considerare = [str(primo+x) for x in range(ultimo-primo+1)]
    for el in diz_year:
        if el in anni_da_considerare:  #aggiorno dizionario
            diz[el]=sum(diz_year[el])/len(diz_year[el])
    return diz


def is_in_time_series(time_series,first_year,last_year):#verifico che gli anni inseriti siano nella time_series
    fy=False
    ly=False
    for data in time_series:

        if data[0][:4] == first_year:
            fy=True
        if data[0][:4] == last_year:
            ly=True
        if fy and ly:
            return True
    return False




def compute_variation(time_series,first_year,last_year):

    if int(first_year) >= int(last_year):
        raise ExamException('errore, anno iniziale >= anno finale')

    if not is_in_time_series(time_series,first_year,last_year):
        raise ExamException('anni inseriti non presenti')

    diz_medie=compute_media(time_series,first_year,last_year)
    diz={}

    lista_anni=list(diz_medie.keys())
    lista_medie=list(diz_medie.values())
    for i in range(len(lista_anni)-1):

        diz[lista_anni[i+1]+'-'+lista_anni[i]] = lista_medie[i+1] - lista_medie[i]

    return diz

ts=CSVTimeSeriesFile('data.csv')
#print(ts.get_data())
print(compute_variation(ts.get_data(),'1950','1960'))
            