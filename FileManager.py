from Algorithms import SortingAlg
from random import randint


def readUserFile(nombreA, whole, inputSize=None):
    archivo = open(nombreA, "r")
    lines = archivo.readlines()
    archivo.close()
    array = []
    cn = 0

    if whole:
        for linea in lines:
            linea = linea.strip()
            array.append(int(linea))
    else:
        while cn < inputSize and cn < len(lines):
            linea = lines[cn].strip()
            array.append(int(linea))
            cn = cn + 1
    SortingAlg.array = array
    return len(array)


def generateFile(size):

    path = 'generated%d.txt' % randint(100, 1000)

    array = []

    with open(path, 'w', encoding='utf-8') as file:
        for i in range(size):
            n = randint(-100, 100)
            array.append(n)
            file.write("%d\n" % n)
    SortingAlg.array = array

    return path


def writeResults(agthms):
    path = "results%d.txt" % randint(100, 1000)
    file = open(path, "w", encoding='utf-8')
    file.write("n,")
    file.write(",".join(agthms))
    file.write('\n')

    SortingAlg.insertionsort(SortingAlg.array.copy())
    SortingAlg.mergeSort(SortingAlg.array.copy())
    SortingAlg.quicksort(SortingAlg.array.copy())

    any = agthms.pop()
    inputs = SortingAlg.agthms[any].keys()
    agthms.add(any)

    for n in inputs:
        file.write(str(n))
        for k, v in SortingAlg.agthms.items():
            if k in agthms:
                file.write(",%d" % v[n])
        file.write('\n')
    file.close()
    SortingAlg.reset()
    return path


"""

def crearDicr(ins,sto,mer,qui):
    dicR={}
    for n in al.SortingAlg.dicqs:
        if ins:
            if(dicR.keys().__contains__(n)):
                if not isinstance(dicR[n], int):
                    temp=list(dicR[n]).copy()
                else:
                    temp=[]
                    temp.append(dicR[n])
                temp.append(al.SortingAlg.dicis[n])
                dicR[n]=temp
            else:
                dicR[n] =al.SortingAlg.dicis[n]
        if qui:
            if (dicR.keys().__contains__(n)):
                if not isinstance(dicR[n], int):
                    temp=list(dicR[n]).copy()
                else:
                    temp=[]
                    temp.append(dicR[n])
                temp.append(al.SortingAlg.dicqs[n])
                dicR[n]=temp
            else:
                dicR[n] =al.SortingAlg.dicqs[n]
        if mer:
            if (dicR.keys().__contains__(n)):
                if not isinstance(dicR[n], int):
                    temp=list(dicR[n]).copy()
                else:
                    temp=[]
                    temp.append(dicR[n])
                temp.append(al.SortingAlg.dicms[n])
                dicR[n]=temp
            else:
                dicR[n]=al.SortingAlg.dicms[n]
        if sto:
            if (dicR.keys().__contains__(n)):
                if not isinstance(dicR[n], int):
                    temp=list(dicR[n]).copy()
                else:
                    temp=[]
                    temp.append(dicR[n])
                temp.append(al.SortingAlg.dicsts[n])
                dicR[n]=temp
            else:
                dicR[n] =al.SortingAlg.dicsts[n]
    return dicR



i=arrT.copy()
al.SortingAlg.insertionsort(i)
print(al.SortingAlg.dicis)
m=arrT.copy()
al.SortingAlg.mergeSort(m)
print(al.SortingAlg.dicms)
q=arrT.copy()
al.SortingAlg.quicksort(q)
print(al.SortingAlg.dicqs)
res=crearDicr(True,False,True,True)
print(res)
nom=["Insertion","Quicsort","MergeSort"]
escRes(res,nom)
#al.SortingAlg.stoogesort(arrT,0,len(arrT)-1)

"""