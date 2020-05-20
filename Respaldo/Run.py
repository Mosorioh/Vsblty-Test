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

from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

Duracion = 60
Cliclos = 4
Num_Ciclo = 1

#ahora = date.now()
#Fecha =  ahora.strftime("%Y-%m-%d")

PathLogs = "C:/ProgramData/Vsblty/KingSalmon/"


#/////////////////////////////////////////////
# Crear Folder Test
#//////////////////////////////////////////////
try:
    # change the destination path
    FolderTest = "C:/ProgramData/Vsblty-Test/Json-Test/" + GuidTest 
    makedirs(FolderTest)
    print (" - Creating Folder of Test-",  GuidTest )
except FileExistsError:
    print (" - Folder Exists")

try:
    # change the destination path
    FolderTestKingSalmon = FolderTest + "/KingSalmon/"
    FolderTestUsage = FolderTest + "/Usage/"
    makedirs(FolderTestKingSalmon)
    makedirs(FolderTestUsage)
    print (" - Creating Folder Resplados")

except FileExistsError:
    print (" - Folder Exists")

#///////////////////////////////////////////////////////////////////////////////////////////////
# Cerra Proceso Anterior
#///////////////////////////////////////////////////////////////////////////////////////////////
os.system('taskkill -f -im vsb*')

#///////////////////////////////////////////////////////////////////////////////////////////////
# Detener el Servicio de Windows
#///////////////////////////////////////////////////////////////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
print ("Deteniendo El Servicio de Windows" )
# Siguiente linea detiene el Servicio de Windowns
os.system('net stop VisionCaptorServices')
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
print("")
time.sleep(5)

#///////////////////////////////////////////////////////////////////////////////////////////////
#Remover  carpeta`
#///////////////////////////////////////////////////////////////////////////////////////////////
try:
    # Remove path Folder KingSalmon
    PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
    rmtree(PathLog)
    print (" - La Carpeta de Logs ha sido Eliminada")
    time.sleep(.100)
    
except FileNotFoundError:
    print (" - Folder KingSalmon No Exists")

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
# El Cliente se incia llamando a un archivo .bat  
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

#///////////////////////////////////////
# Ejecutar el Cliente
#///////////////////////////////////////
#ahora = date.now()
os.startfile('C:/Start-Client.bat')
print ("")
print ("************************")
print ("  -- Start Client")
print ("************************")
print ("")

#///////////////////////////////////////
# Tiempo de Duracion del CLiente
#///////////////////////////////////////
time.sleep(Duracion)

#///////////////////////////////////////
# Close Client  
#///////////////////////////////////////
#ahora = date.now()
print ("")
os.system('taskkill -f -im vsb*')
print ("************************")
print ("  -- Stop Client")
print ("************************")
print ("")


################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

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

    parametro = "[EDGE Detection] Analysis Function took"
    parametro = "Complete analysis for frame"
    
    
    for ClientLine in lineas_texto:

        if parametro in ClientLine:
            Item += 1
            Parametro = 1
            Timeline = ClientLine[0:19] 
            InfoLog = ClientLine
            posiciontook =  ClientLine.find("took") + 5
            took = ClientLine[posiciontook:-17] 

            posicionFrame =  ClientLine.find("frame") + 6
            posiciontook2 =  ClientLine.find("took")
            Frame = ClientLine[posicionFrame:posiciontook2] 

            posicionfound =  ClientLine.find("found") + 7
            FacesFound = ClientLine[posicionfound:]
            # Completamos la cadena con una fecha X ('2020-01-01 '), solo para convertir a time
            Tookdate = '2020-01-01 ' + took
            
            #Tookdate = '2020-01-01 00:00:00.000927'
            Tookdate = Tookdate[0:26]
            #print (Tookdate)
            # convertimos Tookdate en datetime
            date_time_obj = datetime.datetime.strptime(Tookdate, '%Y-%m-%d %H:%M:%S.%f')
            # tomamos el tiempo de la funcion Took ya convertido
            TookTime = date_time_obj.time()
            
            
            """print ("Item: ",Item)
            print ("File: ", file)
            print ("Time: ", Timeline)
            print ("Frame: ", Frame)
            print ("Took: ", TookTime)
            print ("Log: ",InfoLog)"""
            #input()
            

            Took = [Item, file, Parametro, Timeline, Frame, TookTime, FacesFound]
            TookList.append(Took)



print("Complete analysis for frame")
TotalTook = []
i = 0
TookList = sorted(TookList)
for Element in TookList:
    print ("Item: ",TookList[i][0])
    print ("File: ",TookList[i][1])
    print ("Parametro: ",TookList[i][2])
    print ("Time: ",TookList[i][3])
    print ("Frame: ",TookList[i][4])
    print ("Took: ",TookList[i][5])
    print ("Faces: ",TookList[i][6])
    print("")
    TotalTook.append(TookList[i][5])
    
    i += 1


################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

#///////////////////////////////////////
# Mover Folder Log
#///////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print ("")
try:
    # change the destination path
    PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
    dirs = os.listdir(PathLog)
    for file in dirs:
        Archivo = PathLog + file
        print (" - Copiando Archivo Log: ", Archivo)

        shutil.copy(Archivo, FolderTestKingSalmon)
        time.sleep(.100)
except FileExistsError:
    print (" - Folder Exists")

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#///////////////////////////////////////
# Mover Folder Usage
#///////////////////////////////////////
print ("")
try:
    # change the destination path
    PathLog = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"
    dirs = os.listdir(PathLog)
    for file in dirs:
        Archivo = PathLog + file
        print (" - Copiando Archivo Log: ", Archivo)
        
        shutil.copy(Archivo, FolderTestUsage)
        time.sleep(.100)
except FileExistsError:
    print (" - Folder Exists")
except PermissionError:
    print ("PermissionError")

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")





    
FilePdfName =  GuidTest + ".pdf"

doc = canvas.Canvas(FilePdfName)

doc.setTitle("Test")
doc.setFont("Helvetica", 10)
doc.drawString(270, 785, "Test Summary")




doc.line(20,730,580,730) #Creación de una linea recta
doc.line(20,725,580,725) #Creación de una linea recta


# ###################################
# 2) Sub Title 
# RGB - Red Green and Blue

i = 0
linea = 600
for Element in TookList:
    #
    print ("Frame PDF: ",TookList[i][4])
    print ("Frame PDF: ",TookList[i][5])
    print ("Frame PDF: ",TookList[i][6])
    Deteccion = "FRame: " + str(TookList[i][4])
    PersonDetection = "Took - " + str(TookList[i][5]) 
    #
    doc.drawString(50, linea, str(Deteccion))
    linea = linea - 15
    #
    doc.drawString(80, linea, str(PersonDetection))
    linea = linea - 5
    #
    doc.line(20,linea,580,linea) #Creación de una linea recta
    linea = linea - 15
    i += 1

doc.save()

print (" -- End Test")


