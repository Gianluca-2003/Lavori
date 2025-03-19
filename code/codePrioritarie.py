import datetime
import random


class CodaPrioritaria:
    def __init__(self):
        self._lista = []

    def put(self, x):
        '''
        Aggiungo un nuovo elemento alla coda
        :param x:
        :return:
        '''
        self._lista.append(x)

    def get(self):
        '''
        Restituisce l'elemento piu piccolo presente nella coda e lo elimina
        :return:
        '''
        index, val = min(enumerate(self._lista), key=lambda x: x[1])
        self._lista.pop(index)
        return val[1]


    def __len__(self):
        return len(self._lista)

c = CodaPrioritaria()
c.put((3,"Ciao"))
c.put((1,"Hello"))
c.put((2,"Test"))

print(c.get())

c1 = CodaPrioritaria()
tic = datetime.datetime.now()
for i in range(1000):
    c1.put((random.randint(0,100), random.randint(0,100)))

for i in range(len(c1)):
    c1.get()

toc = datetime.datetime.now()

print(f"La tua implementazione ci ha messo {toc - tic} secondi")






