class ExamException(Exception):
    pass

class MovingAverage:

    def __init__(self,w_length):
        if (not isinstance(w_length,int) or w_length <=0):
            raise ExamException("valore finestra non valido")
        self.w_length = w_length



    def compute(self,data):
        if not isinstance(data,list) or not data:
            raise ExamException("Argomento di compute non valido, inserire lista non vyuota di interi")
        if not all(isinstance(i,int) for i in data):
            raise ExamException("lista non valida, non sono tutti interi")
        if(self.w_length>len(data)):
            raise ExamException("lista piu piccola dell'ampiezza della finestra")
        
        medie = []
        somma = 0
        for i in range(self.w_length):
            somma += data[i]

        medie.append(somma/self.w_length)

        for i in range(1,len(data)-self.w_length+1):
            somma -= data[i-1]
            somma += data[i+self.w_length-1]
            medie.append(somma/self.w_length)

        return medie

    
mvavg=MovingAverage(4)
print(mvavg.compute([2,4,8,16]))

