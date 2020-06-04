 
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

print('Enter Faces Estimadas:')
FacesEstimadas = int(input())
print('Enter Identificacion Estimada:')
IdentificacionEstimada = int(input())

PathMetrics = "C:/ProgramData/Vsblty/Kiosk Framework/Usage-1/"
FileMain = 0
FileMultiple = 0
FileN = 0
FaceIdDetectados = 0
PersonasDetectas = []
IdentificacionesJson = []
ListFaceDetection = []
PersonasIdentificadas = 0
PersonasNoIdentificadas = 0 
FaceSinDemografica = 0 
FaceConDemografica = 0 

#FacesEstimadas = 1800
#IdentificacionEstimada = 1440


print ("********************************************")
print ("******************************************************")
print ("          Inicio Analisis de los Archivos Json Metrics")
print ("******************************************************")
print ("********************************************")

print ("Ruta Folder: ", PathMetrics)
dirs = os.listdir(PathMetrics)

for file in dirs:
    # Creamos la ruta y el archivo que vamos a trabajar
    PathFileMetrics = PathMetrics + file
    
    Filetype = file.find("000000000000.Usa")  
    if (Filetype > 0):
        FileMultiple += 1
    if (Filetype < 0): 
        FileMain += 1
    
    try:
        #///////////////////////////////////////////
        with open(PathFileMetrics) as contenido:
            FileN += 1
            datajson = json.load(contenido)

            #encoded
            data_string = json.dumps(datajson)

            #Decoded
            decoded = json.loads(data_string)

            data_string = json.dumps(datajson)

            # ///////////////////////////////////
            # Get data     "personEngagements"
            # ///////////////////////////////////
            try:
                personEngagements = decoded["personEngagements"]
                print ("***********************************************")
                print ("File #: ", FileN)
                print ("File:", file)
                print ("  - Verificando si el Archivo tiene Face")
                FaceIds = len(personEngagements) 
                
                if (FaceIds == 0):
                    print ("     -- El archivo no contine Faces")
                    File1K = File1K + 1
                else:
                    print ("     -- Faces Detectadas: ", FaceIds)
                    # Total de faces detectas En la prueba
                    FaceIdDetectados = FaceIdDetectados + FaceIds
                    for Person in personEngagements:
                        
                        try:
                            FaceId = Person["faceId"]
                            print ("        -- FaceId: ", FaceId)
                            localPersistedFaceId = Person["localPersistedFaceId"]
                            print ("        -- LocalPersistedFaceId: ", localPersistedFaceId)
                            demographics = Person["demographics"]
                            age = Person["demographics"]["age"]
                            sex = Person["demographics"]["sex"]
                            bioRecordId = Person["demographics"]["bioRecordId"]
                            if bioRecordId == "00000000-0000-0000-0000-000000000000":
                                print ("            -- Persona No identificada")
                                Name = None
                                Confidence = None
                                PersonasNoIdentificadas += 1
                            else:
                                print ("            -- Persona identificada Como:")
                                Name =  Person["demographics"]["IdentityName"]
                                Confidence = Person["demographics"]["identificationConfidence"]
                                PersonasDetectas.append(Name)
                                PersonasIdentificadas += 1

                            
                            print ("              -- Age: ", age)
                            print ("              -- Sex: ", sex)    
                            print ("              -- Name: ", Name)
                            print ("              -- Confidence: ", Confidence)
                            print ("              -- BioRecordId: ", bioRecordId)
                            
                            PersonaDetectada = [FileN, FaceId, localPersistedFaceId, age, sex, Name, Confidence, bioRecordId]
                            ListFaceDetection.append(PersonaDetectada)
                            
                            FaceConDemografica += 1
                        except:
                            FaceSinDemografica += 1
                    

            except:
                print ("Error El Archivo Json no es Metrica,", file)
                FileMain -= 1
                FileN  -= 1
    except:
        print ("Error El Archivo no es de tipo Json")
        FileMain -= 1   

# calculo de efectividad
EfectividadFacesdetected = "{0:.2f}".format((FaceConDemografica * 100 / FacesEstimadas))
#print (EfectividadFacesdetected)
Efectividadidentidicaciones = "{0:.2f}".format((PersonasIdentificadas * 100 / IdentificacionEstimada))


#print (PersonasDetectas)
print (" - Files Procesados: ", FileN)
print (" - Archivos Tipo Main: ", FileMain)
print (" - Archivo Tipo Multiple", FileMultiple)
print (" - Faces Detectadas: ", FaceIdDetectados) 
print (" - Faces Sin Demografia: ", FaceSinDemografica)  
print (" - Faces Con Demografia: ", FaceConDemografica)  
print (" - Total Personas No Identificadas: ", PersonasIdentificadas)
print (" - Total Personas Identificadas: ", PersonasNoIdentificadas)
print ("    - Detecciones Estimadas:         ", FacesEstimadas)
print ("    - Identificaciones Estimadas:    ", IdentificacionEstimada)
print ("    - Efectividad Detecciones:       ", EfectividadFacesdetected, "%")
print ("    - Efectividad Identificaciones:  ", Efectividadidentidicaciones, "%")



PersonasAgrupadas = groupby(PersonasDetectas)
# convertimos el Groupby en unDiccionario con las Personas agrupadas
dic = {} 
for k, v in PersonasAgrupadas:
    dic[k] = list(v)
dic

# Get personas agrupadas
values= dic.values()
#print (values)

for Persona in values:
    Persona = str(Persona)[2:-2]
    VecesDetectada = PersonasDetectas.count(Persona)
    print ("       - ", Persona, ": ", VecesDetectada)
    ResumenIdentificacionPersona = [Persona, VecesDetectada]
    IdentificacionesJson.append(ResumenIdentificacionPersona)


print (IdentificacionesJson[2])          
print (ListFaceDetection[6])
            
# **************************************************************
# **************************************************************
# PDF
# **************************************************************
# **************************************************************

# Nombre del Archivo
FilePdfName =  GuidTest + ".pdf"
doc = canvas.Canvas(FilePdfName)

# Header 
doc.setTitle("Test")
doc.setFont("Helvetica", 10)
doc.drawString(270, 785, "Test Summary")
doc.drawString(200, 770, GuidTest)
doc.drawString(230, 755, "Verificacion de Archivos Json")


doc.line(20,730,580,730) #Creación de una linea recta
doc.line(20,725,580,725) #Creación de una linea recta
# Files procesados
doc.drawString(45, 710, " - Archivos Json generados: ")
doc.drawString(70, 695, " - Files Procesados: ")
doc.drawString(180, 695, str(FileN))
doc.drawString(70, 680, " - Archivos Tipo Main: ")
doc.drawString(180, 680, str(FileMain))
doc.drawString(70, 665, " - Archivo Tipo Multiple: ")
doc.drawString(180, 665, str(FileMultiple))
# Face detection
doc.drawString(45, 650, " - Detecciones: ")
doc.drawString(70, 635, " - Faces Detectadas: ")
doc.drawString(200, 635, str(FaceIdDetectados))
doc.drawString(70, 620, " - Faces Sin Demografia: ")
doc.drawString(200, 620, str(FaceSinDemografica))
doc.drawString(70, 605, " - Faces Con Demografia: ")
doc.drawString(200, 605, str(FaceConDemografica))
# Idenbtificacion 
doc.drawString(45, 590, " - Identificaciones: ")
doc.drawString(70, 575, " - Total Personas Identificadas: ")
doc.drawString(230, 575, str(PersonasIdentificadas))
doc.drawString(70, 560, " - Total Personas No Identificadas: ")
doc.drawString(230, 560, str(PersonasNoIdentificadas))
# Efectividad 
doc.drawString(45, 545, " - Efectividad: ")
doc.drawString(70, 530, " - Detecciones Estimadas: ")
doc.drawString(230, 530, str(FacesEstimadas))
doc.drawString(70, 515, " - Identificaciones Estimadas: ")
doc.drawString(230, 515, str(IdentificacionEstimada))
doc.drawString(70, 500, " - Efectividad Detecciones:                            %")
doc.drawString(230, 500, str(EfectividadFacesdetected))
doc.drawString(70, 485, " - Identificaciones Estimadas:                        %")
doc.drawString(230, 485, str(Efectividadidentidicaciones))
# Linea Division
doc.line(20,470,580,470) #Creación de una linea recta
doc.line(20,465,580,465) #Creación de una linea recta


# Personas Identificadas
doc.drawString(70, 450, " - Personas Identificadas: ")
doc.drawString(100, 435, "   NAME")
doc.drawString(250, 435, "   VECES")

linea = 420
for Element in IdentificacionesJson:

    doc.setFont("Helvetica", 8)
    doc.setFillColorRGB(0,0,0)

    Person = Element[0]
    Veces = Element[1]
    
    doc.drawString(100, linea, str(Person))
    doc.drawString(270, linea, str(Veces))
    linea = linea - 15

      
           


doc.save()