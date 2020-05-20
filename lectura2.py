# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:28:31 2020

@author: Javier Ojeda Prieto
"""
from matplotlib.pyplot import figure, show
import pandas as pd
import subprocess
import os.path
import os
import shutil

def ejecucion(self):
    ENTORNO=self.parent().labelEstado.text() #Obtenemos de la interfaz de bienvenida el estado del interruptor
    if 'Windows' in ENTORNO:
        subprocess.call('grwave <entrada.dat >grwave.out', shell=True)
        return True
    elif 'MSDOS' in ENTORNO:
        homedir = os.path.expanduser("~") #Obtenemos nombre de carpeta de usuario extendida
        direccion=homedir+"\AppData\Local\DOSBox" #le añadimos el resto de direccion donde necesitamos
        #que exista un fichero de configuracion de DOSBox
        os.makedirs(direccion, exist_ok=True) #Creamos la carpeta, pero que no de fallo si ya existe
        shutil.copy("dosbox-0.74-3.conf", direccion) #copiamos el archivo a la direccion
        subprocess.call('DOSBox-0.74-3\DOSBox', shell=True) #llamamos al programa DOSBox
        fnew=open("grwave.out","r")
        contenedor=fnew.read()
        if("mode" in contenedor):
            self.lanzarWarning("No disponible en MS-DOS. \n Elija terminal de Windows.")
            return False
        else:
            return True
        fnew.close()

def lecturaSalida(self,inicial):
    #lee el archivo, salta primeras 31 filas
    fo = open("grwave.out", "r")
    if(inicial==0): #se llama a GRWAVE 4 veces por cada grafica (por temas de escala logaritmica)
        #asi que si no es la primera de esas 4, se abre el archivo continuar escribiendo al final, sin borrar nada
        f = open ("grwave2.out", "a")
    elif (inicial==1): #si es la primera de esas 4, abre el archivo para empezar a escribir desde cero
        f = open ("grwave2.out", "w")
    iteracion=(linea for i,linea in enumerate(fo) if i>=32) #descarta del grwave.out las primeras 31 lineas porque ese texto no vale
    for linea in iteracion:
        f.write(linea)
        
    f.close()
    fo.close()
    

    
def leerGRW2(archivoSal,tipo):
    #se lee el archivo y se separa en columnas: index, fs y pathloss, tratando los datos como data, con libreria pandas
    data = pd.read_csv(archivoSal, sep=r'\s+', index_col=0, names=['fs', 'pathloss'])
    data.dropna(how='all', axis=0, inplace=True) #elimina los renglones que contengan columna vacia
    data = data.drop(data[data['fs']=="*******"].index) #elimina renglones que tengan alguna columna con asteriscos
    data = data.drop(data[data['fs']=="0.00"].index) #elimina los elementos cuyo campo electrico sea 0.00, porque a veces GRWAVE devolvia eso y no lo queremos
    data = data.drop(data[data['pathloss']=="0.00"].index) #elimina los elementos cuyas perdidas sea 0.00
    if (tipo==2):
        data = data.drop(data[data.index=="*******"].index) #a veces tambien aparecian asteriscos en el indice, solo cuando calculamos un punto de distancia especifico demasiado alto
    data = data[~data.index.duplicated(keep='first')] #elimina los renglones duplicados, manteniendo el primero (a veces GRWAVE repetia varios)
    data.index = data.index.astype(float) #convierte columna indice a float
    d_km = data.index.values.astype(float) #convierte columna distancia a float
    data['fs'] = data['fs'].astype(float) 
    intensidad=data['fs'].values.astype(float) #convierte columna campo electrico a float
    perdidas=data['pathloss'].values.astype(float) #convierte perdidas a float
    return d_km, intensidad, perdidas



  