import os 
import os, sys
from datetime import date
from datetime import datetime, timedelta
import datetime 

################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////// 
#/////////////////////////////////////////////////////////////////////////////////////////////// 
################################################################################################



def CompleteAnalysisLog (PathLogs, GuidTest):

    # Variables de entorno
    CompleteAnalysisTookList = []
    Item = 0

    # Obtenemos todos los Archivos que estan dentro del directorio KingSalmon
    dirs = os.listdir(PathLogs)

    # Por cada Archivo leemos y buscamos el parametro
    for file in dirs:

        # armamos el archivos que vamos a leer
        PathFileLog = PathLogs + file
        archivo_texto = open (PathFileLog, "r")
        lineas_texto = archivo_texto.readlines()

        # Parametro de Busqueda
        parametro = "Complete analysis took"

        # Por cada Linea del archivos buscamos el parametro definido
        for ClientLine in lineas_texto:

            if parametro in ClientLine:
                Item += 1
                Timeline = ClientLine[0:19] 

                posiciontook =  ClientLine.find("Complete") 
                InfoLog = ClientLine[posiciontook:-1]
                #
                posiciontook =  ClientLine.find("took") + 5
                posicionfor =  ClientLine.find("for")-1

                took = ClientLine[posiciontook:posicionfor] 

                posicionFrame =  ClientLine.find("frame") + 6
                posicionCarater =  ClientLine.find(">>") -1
                
                Frame = ClientLine[posicionFrame:posicionCarater]

                PosicionFaces =  ClientLine.find("found:") + 7
                Faces = ClientLine[PosicionFaces:-1]
                
              
                # Completamos la cadena con una fecha X ('2020-01-01 '), solo para convertir a time
                Tookdate = '2020-01-01 ' + took
                
                #Tookdate = '2020-01-01 00:00:00.000927'
                Tookdate = Tookdate[0:26]
                #print (Tookdate)
                # convertimos Tookdate en datetime
                date_time_obj = datetime.datetime.strptime(Tookdate, '%Y-%m-%d %H:%M:%S.%f')
                # tomamos el tiempo de la funcion Took ya convertido
                TookTime = date_time_obj.time()
                
                print ("Guid: ",GuidTest)
                print ("Item: ",Item)
                print ("File: ", file)
                print ("Time: ", Timeline)
                print ("Frame: ", Frame)
                print ("Took: ", TookTime)
                print ("Faces: ", Faces)
                print ("Log: ",InfoLog)
                print ("")
                
                
                # Creamos una Lista
                Took = [GuidTest, Item, file, Timeline, Frame, TookTime, Faces, InfoLog]
                try:
                    if int(Frame) > 0:
                        CompleteAnalysisTookList.append(Took) 
                except ValueError:
                    print ("Error") 
    
    return (CompleteAnalysisTookList)   

"""PathLogs = "C:/ProgramData/Vsblty/KingSalmon/"
#PathLogs = "C:/Users/Mijail/Desktop/Los VM/KingSalmon-vm-1/KingSalmon/"
GuidTest = "5214-8963231-254-2836"  

CompleteAnalysisLog (PathLogs, GuidTest)
"""
