# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def GetEngagementService (GuidTest):
    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `Timeline`, `Frame`, `Took` FROM `EngagementService` WHERE `GuidTest` = %s ORDER BY Frame"
                cursor.execute(sql, (GuidTest)) 
                result = cursor.fetchall()
                #print ("Resultado:", result)
                #TestID = int(result.get('Id'))
                #print ("Id", TestID)
                #input ()
                
    finally:
        connection.close()

    return result

"""GuidTest = "df543912-bdc1-4e73-ad57-19e95f51ceb4"

print (GetTestId (GuidTest))"""
