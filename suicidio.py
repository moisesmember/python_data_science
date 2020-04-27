import psycopg2
import numpy

try:
   connection = psycopg2.connect(user="postgres",
                                  password="1926",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="DB_DATAWAREHOUSE")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT * FROM VIEW_STATICS_SUICIDIO"

   cursor.execute(postgreSQL_select_Query)
   #print("Selecting rows from mobile table using cursor.fetchall")
   suicidio = cursor.fetchall() 
      
   for row in suicidio:
        print("QTDE REGISTROS = ", row[0], )
        print("NUM TOTAL DE CASOS = ", row[1], )
        print("PERCIL DOS CASOS = ", row[2], )
        print("MODA DOS CASOS = ", row[3], )
        print("MEDIA DOS CASOS = ", row[4], )
        print("MEDIANA DOS CASOS = ", row[5], )
        print("AMPLITUDE = ", row[6], )
        print("AGE = ", row[7], "\n")
      
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

