import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="1926",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="DB_DATAWAREHOUSE")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT * FROM VIEW_SUICIDIO"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in mobile_records:
       print("Id = ", row[0], )
       print("country = ", row[1])
       print("year = ", row[2], )
       print("sex = ", row[3])
       print("age = ", row[4], )
       print("suicides_no = ", row[5])
       print("population = ", row[6])
       print("suicides 100 por mil = ", row[7])
       print("country year = ", row[8])
       print("hdi year = ", row[9])
       print("gdb for year = ", row[10])
       print("gdp per capita = ", row[11])
       print("generation  = ", row[12], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
