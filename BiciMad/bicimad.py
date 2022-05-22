from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext
from datetime import datetime
import json
from pprint import pprint
from pyspark.sql.types import StructType, StringType, IntegerType, TimestampType
from pyspark import SparkContext
import sys

s = "2019-06-01T00:00:00.000+0200"
d = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f%z")
d

schema = StructType()\
    .add('_id', StructType().add('$oid', StringType(), False), False)\
    .add("user_day_code", StringType(), False)\
    .add("idunplug_station", IntegerType(), False)\
    .add("idplug_station", IntegerType(), False)\
    .add("ageRange", IntegerType(), False)\
    .add("user_type", IntegerType(), False)\
    .add("zip_code", StringType(), True)

files = ['201801_Usage_Bicimad.json','201802_Usage_Bicimad.json','201803_Usage_Bicimad.json']
    
#Esta función devuelve la probabilidad de que ocurra un suceso
def porcentaje(casos, total):
    return (casos/total)*100

#Función auxiliar que usaremos para filtrar usuarios
def filtro_usuarios(i,data):
    return data['user_type']==i

#Función auxiliar que usaremos para filtrar la edad de los usuarios
def filtro_edad(i,data):
    return data['ageRange']==i
    
#Función principal del análisis   
def main(sc, files):
    validos = 0 #Número de observaciones válidas
    anuales = 0 #Número de observaciones de clientes anuales
    ocasionales = 0 #Número de observaciones de clientes ocasioanles
    trabajadores = 0 #Número de observaciones de trabajadores
    edad1 = 0 #Número de usuarios entre 0 y 26 años dentro de los clientes ocasionales
    edad2 = 0 #Número de usuarios entre 27 y 40 años dentro de los clientes ocasionales
    edad3 = 0 #Número de usuarios entre 41 y 65 años dentro de los clientes ocasionales
    edad4 = 0 #Número de usuarios de 66 años o más dentro de los clientes ocasionales
    edadt1 = 0 #Número de usuarios entre 0 y 26 años dentro de los clientes totales
    edadt2 = 0 #Número de usuarios entre 27 y 40 años dentro de los clientes totales
    edadt3 = 0 #Número de usuarios entre 41 y 65 años dentro de los clientes totales
    edadt4 = 0 #Número de usuarios de 66 años o más dentro de los clientes totales
    centroT = 0 #Número de usuarios ocasionales que desenganchan en el centro
    centroO = 0 #Número total de usuarios que desenganchan en el centro
    for filename in files: #Repetiremos tod el proceso para cada fichero dentro de files
    
        print (filename)   
        data = spark.read.json(filename, schema=schema, timestampFormat="yyyy-MM-dd'T'HH:mm:ss.SSSZ")
        data0 = data.select("user_type","ageRange","idunplug_station") #Vamos a trabajar sólo con estos campos

        data1=data0.filter((data0['user_type'] != 0)) #Filtramos los datos de tipo de usuario válidos
        validos += data1.count() #Contamos el número total de datos válidos

        data_anual=data1.filter(filtro_usuarios(1,data1)) #Filtramos los clientes anuales
        anuales += data_anual.count()

        data_ocasional=data1.filter(filtro_usuarios(2,data1)) #Filtramos los clientes ocasionales
        ocasionales += data_ocasional.count()
        
        data_trabajador=data1.filter(filtro_usuarios(3,data1)) #Filtramos los trabajadores de la empresa
        trabajadores += data_trabajador.count()
        
        #Vemos ahora los clientes totales y los ocasionales en el centro
        cond1 = ((data1['idunplug_station']<=63) & (data1['idunplug_station']>=1)) #Filtramos los id de las estaciones en centro
        data_station_CentroT=data1.filter(cond1)
        centroT += data_station_CentroT.count()
        
        cond2 = ((data_ocasional['idunplug_station']<=63) & (data_ocasional['idunplug_station']>=1) )
        data_station_Centro=data_ocasional.filter(cond2)
        centroO += data_station_Centro.count()
        
        #Filtramos para ver los rangos de edad dentro de los usuarios ocasionales
        data_edad1 = data_ocasional.filter((data_ocasional['ageRange']>=0) & (data_ocasional['ageRange']<=3)) #Entre 0 y 26 años unimos los campos 0,1,2 y 3
        edad1 += data_edad1.count()
        
        data_edad2 = data_ocasional.filter(filtro_edad(4,data_ocasional)) #Entre 27 y 40 años
        edad2 += data_edad2.count()
        
        data_edad3 = data_ocasional.filter(filtro_edad(5,data_ocasional)) #Entre 41 y 65 años
        edad3 += data_edad3.count()
        
        data_edad4 = data_ocasional.filter(filtro_edad(6,data_ocasional)) #66 años o más
        edad4 += data_edad4.count()
        
        #Filtramos para ver los rangos de edad totales
        data_edadt1 = data1.filter((data1['ageRange']>=0) & (data1['ageRange']<=3)) #Entre 0 y 26 años unimos los campos 0,1,2 y 3
        edadt1 += data_edadt1.count()

        data_edadt2 = data1.filter(filtro_edad(4,data1)) #Entre 27 y 40 años
        edadt2 += data_edadt2.count()

        data_edadt3 = data1.filter(filtro_edad(5,data1))  #Entre 41 y 65 años
        edadt3 += data_edadt3.count()

        data_edadt4 = data1.filter(filtro_edad(6,data1)) #66 años o más
        edadt4 += data_edadt4.count()

        
        
    print(f"El porcentaje de clientes anuales es del {porcentaje(anuales,validos)}%")
    print(f"El porcentaje de clientes ocasionales es del {porcentaje(ocasionales,validos)}%")
    print(f"El porcentaje del uso por trabajadores de la empresa es del {porcentaje(trabajadores,validos)}%")
    
    print(f"El porcentaje de desenganches totales en el Centro es del {porcentaje(centroT,validos)}%")
    print(f"El porcentaje de desenganches por clientes ocasionales en el Centro es del {porcentaje(centroO,ocasionales)}%")
    
    print(f"El porcentaje de clientes ocasionales entre 0 y 26 años es del {porcentaje(edad1,ocasionales)}% frente al total que es del {porcentaje(edadt1,validos)}%")
    print(f"El porcentaje de clientes ocasionales entre 27 y 40 años es del {porcentaje(edad2,ocasionales)}% frente al total que es del {porcentaje(edadt2,validos)}%")
    print(f"El porcentaje de clientes ocasionales entre 41 y 65 años es del {porcentaje(edad3,ocasionales)}% frente al total que es del {porcentaje(edadt3,validos)}%")
    print(f"El porcentaje de clientes ocasionales de 66 años o más es del {porcentaje(edad4,ocasionales)}% frente al total que es del {porcentaje(edadt4,validos)}%")



if __name__ == "__main__":
    main(sc, files)
