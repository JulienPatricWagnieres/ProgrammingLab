class CSVFile():
    def __init__(self,name):
        self.name=name
        if not isinstance(name,str):
            raise TypeError('il nome del file non è una stringa')

    def get_data(self,inizio=None,fine=None):
        #if inizio < fine:
        #    raise ValueError('inizio < fine in get_data')


        data=[]
        try:
            with open('shampoo_sales.csv','r') as file:
                righe=file.readlines()
                if(inizio==None or inizio <0):
                    inizio=0
                if(fine==None or fine>len(righe)):
                    fine=len(righe)
                if(inizio>fine):
                    raise ValueError('inizio<fine')


                for line in righe[inizio:fine]:
                    data.append(line.strip().split(','))
            return data
        except FileNotFoundError:
            print("file non trovato")
        
class NumericalCSVFile(CSVFile):

    def __init__(self,name):
        super().__init__(name)

    def get_data(self):
        dati=[]
        data=super().get_data()
        for e in data:
            try:
                d,v=e[0],float(e[1])
                dati.append([d,v])
            except:
                pass  #ignoro quelli errati

        return dati

shampoo=CSVFile('ciao')
print(shampoo.get_data(9,7))


