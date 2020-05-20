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

Duracion = 3600

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