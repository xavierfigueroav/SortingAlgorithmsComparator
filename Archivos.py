import random
import os.path
import Algoritmos as al



def lecArc(nombreA):
    #C:\\Users\\luis8\\Desktop\\ejemplo.txt
    archivo = open(nombreA, "r")
    array = []
    cn = 0
    ver=True;
    while ver:
        numl = input("Introduzca la cantidad de datos a leer(si se escribe la palabra todos entonces se usara todo el archivo):")
        if(numl.isalpha()):
            if(numl.upper()=="TODOS"):
                for linea in archivo.readlines():
                    array.append(linea[0])
                ver=False
            else:
                print("Error: ingreso una palabra innecesaria")
                ver=True
        elif numl.isdigit():
            if(int(numl)>0):
                while cn < int(numl):
                    linea = archivo.readline()
                    if(linea==""):
                        print("El numero ingresado supera la cantidad de valores en el documento, por lo tanto se trabajara con todo el documento")
                        cn=int(numl)
                    else:
                        array.append(linea[0])
                        cn = cn + 1
                ver=False;
            else:
                print("Error: ingreso un numero negativo")
                ver=True
        else:
            print("Error: se ingreso un caracter innecesario")
            ver = True

    print(array)
    archivo.close()
    return array

def crearArc():
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
