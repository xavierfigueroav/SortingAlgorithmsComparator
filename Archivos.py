import random
import os.path

def lecArc(nombreA):
    #C:\\Users\\luis8\\Desktop\\ejemplo.txt
    archivo = open(nombreA, "r")
    array = []
    cn = 0
    ver=True;
    while ver:
        numl = input("Introduzca la cantidad de datos a leer:")
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
        na = random.randint(1, 100)
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

ingnom=input("Ingrese el nombre del archivo: ")
lecArc(ingnom)
#crearArc()
nom=["Primero","Segundo","Tercero"]
val={}
val[2]=[1,2,3]
val[3]=[2,7,2]
val[4]=[3,8,5]
val[5]=[4,9,6]
escRes(val,nom)


