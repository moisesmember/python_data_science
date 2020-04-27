import psycopg2
import numpy

try:
   connection = psycopg2.connect(user="postgres",
                                  password="1926",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="DB_DATAWAREHOUSE")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT YEAR ANO, SUICIDES_NO NUM_SUICIDIO FROM VIEW_SUICIDIO WHERE AGE = '15-24 years' ORDER BY SUICIDES_NO ASC"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   num_suicidio = 0
   count = 0
   array_suicidio = []

   for row in mobile_records:
        #print("YEAR = ", row[0], )
        #print("NUMERO SUICIDIOS = ", row[1], "\n")
        array_suicidio.append(row[1])
      
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

