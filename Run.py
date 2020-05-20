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

PathLogs = "C:/ProgramData/Vsblty/KingSalmon/"
#PathLogs = "C:/Users/Mijail/Desktop/Los VM/KingSalmon-vm-1/KingSalmon/"

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

from FaceDetectionLog import FaceDetectionLog
FaceDetectionService = FaceDetectionLog (PathLogs, GuidTest)
FaceDetectionService.reverse()

print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print(" FaceDetectionService Analysis for frame")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
i = 0
TotalTook = []
for Element in FaceDetectionService:

    print ("Guid: ",FaceDetectionService[i][0])
    print ("Item: ",FaceDetectionService[i][1])
    print ("File: ",FaceDetectionService[i][2])
    print ("Time: ",FaceDetectionService[i][3])
    print ("Frame: ",FaceDetectionService[i][4])
    print ("Took: ",FaceDetectionService[i][5])
    print ("Log: ",FaceDetectionService[i][6])
    print("")
    
    from AddFaceDetection import addFaceDetectionServiceLog
    addFaceDetectionServiceLog (
        FaceDetectionService[i][0], 
        FaceDetectionService[i][1], 
        FaceDetectionService[i][2],
        FaceDetectionService[i][3],
        FaceDetectionService[i][4],
        FaceDetectionService[i][5],
        FaceDetectionService[i][6])

    TotalTook.append(FaceDetectionService[i][5])
    i += 1

print ("Maximo", max(TotalTook))

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

from EngagementServiceLog import EngagementServiceLog
EngagementServiceLog = EngagementServiceLog (PathLogs, GuidTest)

print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print(" EngagementService Analysis for frame")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
i = 0
TotalTookEngagement = []
for Element in EngagementServiceLog:

    print ("Guid: ",EngagementServiceLog[i][0])
    print ("Item: ",EngagementServiceLog[i][1])
    print ("File: ",EngagementServiceLog[i][2])
    print ("Time: ",EngagementServiceLog[i][3])
    print ("Frame: ",EngagementServiceLog[i][4])
    print ("Took: ",EngagementServiceLog[i][5])
    print ("Log: ",EngagementServiceLog[i][6])
    print("")

    TotalTookEngagement.append(EngagementServiceLog[i][5])
    i += 1

print ("Maximo Face-Detection-Service", max(TotalTook))
print ("Maximo Engagement-ServiceLog ", max(TotalTookEngagement))

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

from FaceAnalysisLog import FaceAnalysisLog
FaceAnalysisLog = FaceAnalysisLog (PathLogs, GuidTest)

print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print(" Face Analysis Function took")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
i = 0
TotalTookFaceAnalysis = []
for Element in FaceAnalysisLog:

    print ("Guid: ",FaceAnalysisLog[i][0])
    print ("Item: ",FaceAnalysisLog[i][1])
    print ("File: ",FaceAnalysisLog[i][2])
    print ("Time: ",FaceAnalysisLog[i][3])
    print ("Frame: ",FaceAnalysisLog[i][4])
    print ("Took: ",FaceAnalysisLog[i][5])
    print ("Log: ",FaceAnalysisLog[i][6])
    print("")

    TotalTookFaceAnalysis.append(FaceAnalysisLog[i][5])
    i += 1

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

from CompleteAnalysisLog import CompleteAnalysisLog
CompleteAnalysisLog = CompleteAnalysisLog (PathLogs, GuidTest)

print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print(" Complete analysis took")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
i = 0
TotalTookCompleteAnalysis = []
for Element in CompleteAnalysisLog:

    print ("Guid: ",CompleteAnalysisLog[i][0])
    print ("Item: ",CompleteAnalysisLog[i][1])
    print ("File: ",CompleteAnalysisLog[i][2])
    print ("Time: ",CompleteAnalysisLog[i][3])
    print ("Frame: ",CompleteAnalysisLog[i][4])
    print ("Took: ",CompleteAnalysisLog[i][5])
    print ("Faces: ",CompleteAnalysisLog[i][6])
    print ("Log: ",CompleteAnalysisLog[i][7])
    print("")

    TotalTookCompleteAnalysis.append(CompleteAnalysisLog[i][5])
    i += 1

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################

from PersonIdClientServiceLog import PersonIdServiceLog
PersonIdServiceLog = PersonIdServiceLog (PathLogs, GuidTest)

print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print(" PersonIdClientService")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
i = 0
TotalTookPersonIdService = []
for Element in PersonIdServiceLog:

    print ("Guid: ",PersonIdServiceLog[i][0])
    print ("Item: ",PersonIdServiceLog[i][1])
    print ("File: ",PersonIdServiceLog[i][2])
    print ("Time: ",PersonIdServiceLog[i][3])
    print ("Frame: ",PersonIdServiceLog[i][4])
    print ("Took: ",PersonIdServiceLog[i][5])
    print ("Log: ",PersonIdServiceLog[i][6])
    print("")

    TotalTookPersonIdService.append(PersonIdServiceLog[i][5])
    i += 1



print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("Maximo Face-Detection-Service ", max(TotalTook))
print ("Maximo Engagement-ServiceLog  ", max(TotalTookEngagement))
print ("Maximo Complete analysis      ", max(TotalTookCompleteAnalysis))
print ("Maximo PersonIdClientService  ", max(TotalTookPersonIdService))
print ("Maximo Face-Analysis          ", max(TotalTookFaceAnalysis))
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")


################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################
from getFacedetection import GetFaceDetectionService
GetFaceDetectionService = GetFaceDetectionService (GuidTest)

FilePdfName =  GuidTest + ".pdf"

doc = canvas.Canvas(FilePdfName)

doc.setTitle("Test")
doc.setFont("Helvetica", 10)
doc.drawString(270, 785, "Test Summary")




doc.line(20,730,580,730) #Creación de una linea recta
doc.line(20,725,580,725) #Creación de una linea recta
