import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="1926",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="DB_DATAWAREHOUSE")
   cursor = connection.cursor()
   postgreSQL_select_Query = """SELECT                                                                    
                                       SUICIDIO.YEAR,                                                  
                                       SUICIDIO.SEX,                                                   
                                       SUICIDIO.AGE,                                                   
                                       SUICIDIO.SUICIDES_NO                                            
                                   FROM VIEW_SUICIDIO SUICIDIO                                         
                                         WHERE SUICIDIO.SEX = 'male' AND SUICIDIO.AGE = '15-24 years'  
                                       ORDER BY SUICIDIO.SUICIDES_NO ASC"""

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   num_suicidio = 0
   count = 0
   for row in mobile_records:
       print("YEAR = ", row[0], )
       print("SEX = ", row[1])
       print("AGE = ", row[2], )
       print("SUICIDES_NO = ", row[3], "\n")
       num_suicidio = num_suicidio+row[3]
       count = count+1
       #print("NÚMERO TOTAL: ", num_suicidio)

    #print("A MÉDIA É ", num_suicidio / count )

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

