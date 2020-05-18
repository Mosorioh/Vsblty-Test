import os 
import os, sys
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil
# intérprete para operaciones de entrada y salida basadas en archivos
from io import open
# Hostname
import socket 
# Json
import json
# Date Time
import time
from datetime import date
from datetime import datetime, timedelta
import datetime 
# DB
import pymysql
# GUID
import uuid 
# Group listas
from itertools import groupby

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)


PathLogs = "C:/ProgramData/Vsblty/KingSalmon/"

#print ("Ruta Folder: ", PathLogs)
dirs = os.listdir(PathLogs)
# variable (i) define el nuemro de identificaciones detectadas (item)

print("//////////////////////////////////////////////")
print("Face Analysis Function took")
print("//////////////////////////////////////////////")
TookList = []
Item = 0
for file in dirs:
    PathFileLog = PathLogs + file
    #print(PathFileLog)
    archivo_texto = open (PathFileLog, "r")
    lineas_texto = archivo_texto.readlines()

    parametro = "Face Analysis Function took"
    
    
    for ClientLine in lineas_texto:

        if parametro in ClientLine:
            Item += 1
            Timeline = ClientLine[0:19] 
            InfoLog = ClientLine
            posiciontook =  ClientLine.find("took") + 5
            took = ClientLine[posiciontook:-17] 

            posicionFrame =  ClientLine.find("frame") + 6
            Frame = ClientLine[posicionFrame:-1] 
            # Completamos la cadena con una fecha X ('2020-01-01 '), solo para convertir a time
            Tookdate = '2020-01-01 ' + took
            
            #Tookdate = '2020-01-01 00:00:00.000927'
            Tookdate = Tookdate[0:26]
            #print (Tookdate)
            # convertimos Tookdate en datetime
            date_time_obj = datetime.datetime.strptime(Tookdate, '%Y-%m-%d %H:%M:%S.%f')
            # tomamos el tiempo de la funcion Took ya convertido
            TookTime = date_time_obj.time()
            
            """
            print ("Item: ",Item)
            print ("File: ", file)
            print ("Time: ", Timeline)
            print ("Frame: ", Frame)
            print ("Took: ", TookTime)
            print ("Log: ",InfoLog)
            """
            

            Took = [Item, file, Timeline, Frame, TookTime]
            TookList.append(Took)



print("Result")
TotalTook = []
i = 0
for Element in TookList:
    print ("Item: ",TookList[i][0])
    print ("File: ",TookList[i][1])
    print ("Time: ",TookList[i][2])
    print ("Frame: ",TookList[i][3])
    print ("Took: ",TookList[i][4])
    print("")
    TotalTook.append(TookList[i][4])
    i += 1
    

c = groupby(TotalTook)
    # convertimos el Groupby en unDiccionario con las Personas agrupadas
dic = {} 
for k, v in c:
    dic[k] = list(v)
dic

# Get personas agrupadas
values= dic.values()

print("//////////////////////////////////////////////")
print (" - Max: ", max(TotalTook))
print (" - Min: ", min(TotalTook))
print (" - Elementos Detectados: ", len(TotalTook))
print (" - Elementos Agrupados: ", len(dic))
print("//////////////////////////////////////////////")
print("")

# 
DicTook = sorted(dic, reverse=True)
item  = 0
timeCount = '00:00:00.000000' 
date_time_obj = datetime.datetime.strptime(timeCount, '%H:%M:%S.%f')

for Element in DicTook:
    item += 1
    print (item, "- Took: ", Element)
    
  
    
    
            
            #print (Tookdate)
            # convertimos Tookdate en datetime
            
    ####

