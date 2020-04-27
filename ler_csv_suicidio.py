import csv
import psycopg2
'''
arquivo = open('db/suicide_rates_overview_1985_to_2016.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha)'''


try:
   connection = psycopg2.connect(user="postgres",
                                  password="1926",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="DB_DATAWAREHOUSE")
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO public.suicidio_1985_2016(
                                    country, year, sex, age, suicides_no, population, suicides_10ok, country_year, hdi_year, gdp_for_year, gdp_per_capita, generation)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

   record_to_insert = ('pais teste', '111', 'teste1', 'teste2', '123', '123', '12.25', 'teste5', 'teste6', '74', '58', 'teste100')
   
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
