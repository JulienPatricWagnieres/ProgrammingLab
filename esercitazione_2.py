class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self,name = 'data.csv'):
        self.name=name

    def get_data(self):
        try:
            file = open(self.name,'r')
        except FileNotFoundError:
            raise ExamException("file non trovato")
        
        next(file)
        data = []
        for line in file:
            list_line = line.strip().split(',')

            #controllo data duplicata
            for el in data:
                if el[0] == list_line[0]:
                    raise ExamException("data duplicata")

            #controllo ordinamento. anno e mese corrente deve essere maggiore dell'ultimo el di data
            anno = int(list_line[0][:4])
            mese = int(list_line[0][5:7])
            
            if data:
                if anno < int(data[len(data)-1][0][:4]):
                    raise ExamException("time series non ordinata")
                if(anno == int(data[len(data)-1][0][:4]) and mese <= int(data[len(data)-1][0][5:7])):
                    raise ExamException("time series non ordinata")

            try: 
                list_line[1] = int(list_line[1])
                data.append([list_line[0],list_line[1]]) #ignoro altre possibili righe del csv
            except ValueError:
                pass

        return data

def annual_dist(t_s): # prende una time series e ritorna un dizionario {anno: lista passegeri}
    diz = {}
    anno = t_s[0][0][:4] # leggo il primo anno
    list_psg=[]  
    for i,el in enumerate(t_s):
        if str(anno) in el[0]: # l'anno corrisponde, devo agiungerlo al dizionario
            list_psg.append(el[1])
            if i == len(t_s)-1 :
                diz[str(anno)] = list_psg  #aggiungo l'ultimo anno
        else:
            diz[str(anno)] = list_psg
            anno = el[0][:4]
            list_psg = []
            list_psg.append(el[1])  #aggiungo alla prima variazione dell'anno
        
    return diz


def compute_variation(time_series,first_year,last_year):
    diz = annual_dist(time_series)
    diz_var = {}
    if not(first_year in diz and last_year in diz):
        raise ExamException("anni non validi")
    if first_year >= last_year:
        raise ExamException("primo anno inserito >= ultimo anno")
    

    # creiamo una lista di stringhe con gli anni compresi tra first e last year
    fy=int(first_year)
    ly=int(last_year)
    anni_da_considerare = [str(fy+i) for i in range(ly-fy+1)]

    #creiamo un nuovo dizionario con le medie dei psg per gli anni che mi interessano
    diz_media_anno = {}
    for el in diz:
        if el in anni_da_considerare:
            media = sum(diz[el])/len(diz[el])
            diz_media_anno[el] = media
    lista_anni=list(diz_media_anno.keys())
    lista_valori=list(diz_media_anno.values())
    #print(len(lista_anni))
    for i,el in enumerate(diz_media_anno):
        if  not i == (len(lista_valori)-1):
            #print(i)
            diz_var[lista_anni[i+1]+"-"+lista_anni[i]] = lista_valori[i+1]-lista_valori[i]

    return diz_var

file=CSVTimeSeriesFile()
time_s = file.get_data()
print(compute_variation(time_s,"1950","1960"))

help(reduce)
