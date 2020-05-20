
# GUID
import uuid 
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak



#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

# **************************************************************
# PDF
# **************************************************************

FilePdfName =  GuidTest + ".pdf"

doc = canvas.Canvas(FilePdfName)
doc.setTitle("Test")
doc.setFont("Helvetica", 10)
doc.drawString(270, 785, "Test Summary")


doc.line(20,730,580,730) #Creación de una linea recta
doc.line(20,725,580,725) #Creación de una linea recta
doc.drawString(100, 710, "Time")
doc.drawString(270, 710, "Frame")
doc.drawString(470, 710, "Took")
doc.line(20,700,580,700) #Creación de una linea recta
doc.line(20,695,580,695) #Creación de una linea recta

linea = 600
"""for Element in GetFaceDetectionService:
    Timeline = str(Element.get('Timeline'))
    Frame = str(Element.get('Frame'))
    Took = str(Element.get('Took'))

#
    doc.drawString(50, linea, str(Timeline))
    linea = linea - 15
    #
    doc.drawString(80, linea, str(Frame))
    linea = linea - 5
    #
    doc.drawString(80, linea, str(Took))
    linea = linea - 5
    #
    doc.line(20,linea,580,linea) #Creación de una linea recta
    linea = linea - 15
    i += 1"""

doc.save()