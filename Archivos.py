import random
import os.path
import Algoritmos as al


def lecArc(nombreA, inputSize, whole=True):
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
    return array

def crearArc(path, size):
    archivo2 = open("aleatorio.txt", "w+")
    numc = input("Introduzca la cantidad de datos a crear:")
    i = 0
    arraya = []
    while (i < int(numc)):
        na = random.randint(1, 200)
        arraya.append(na)
        i = i + 1
    for n in arraya:
        archivo2.write(str(n) + "\n")
    archivo2.close()
    return arraya

def escRes(dicR,arrN):
        archivo3 = open("resultados.txt", "w")
        archivo3.write("n")
        for nombre in arrN:
            archivo3.write("    "+nombre)
        archivo3.write("\n")
        for n in dicR:
            archivo3.write(str(n))
            for valro in dicR[n]:
                archivo3.write("         "+str(valro))
            archivo3.write("\n")
        archivo3.close()

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


"""
#ingnom=input("Ingrese el nombre del archivo: ")
arrT=crearArc()


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