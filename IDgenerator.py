import pandas as pd
from random import randint
import random

data = pd.read_csv(r'C:\Users\mateu\Documents\UFRN\Monitoria SD\IDS.csv', encoding = 'latin-1', sep = ';')

ID = "000000"

for i in range (0, len(data.Turma)):
    for j in range (0,5):
        d = randint(0, 9)
        s = str(d)
        new = list(ID)
        new[j] = s
        ID = (''.join(random.sample(new,len(new))))
    print(ID)
    data.ID[i] = ID
print (data)

for i in range (0, len(data.ID)):
    j = i+1
    for j in range (j, len(data.ID)-1):
        if(data.ID[i] == data.ID[j]):
            print("IGUAL" , j, i)

data.to_csv(r'C:\Users\mateu\Documents\UFRN\Monitoria SD\IDSp.csv')
