# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def addFaceDetectionServiceLog (GuidTest, Item, file, Timeline, Frame, Took, InfoLog):

    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create a new record
                         
            sql = "INSERT INTO `FaceDetectionService` ( `GuidTest`, `Item`, `file`, `Timeline`, `Frame`,  `Took`,  `InfoLog`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (GuidTest, Item, file, Timeline, Frame, Took, InfoLog))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("")
            print ("*******************************************************************")
            print ("///////////////////////////////////////////////////////////////////")
            print ("   --  Se realizo Registro del Log FaceDetectionService  Para el Frame", Frame)
            print ("*******************************************************************")
            print ("///////////////////////////////////////////////////////////////////")
            print ("")
            
            

    finally:
        connection.close()