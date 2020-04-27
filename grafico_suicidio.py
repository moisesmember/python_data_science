from matplotlib import pyplot as plt
import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="1926",
                                  host="127.0.0.1",
                                  port="5433",
                                  database="DB_DATAWAREHOUSE")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT * FROM public.view_statics_suicidio WHERE SEX = 'male'"

   cursor.execute(postgreSQL_select_Query)
   # print("Selecting rows from mobile table using cursor.fetchall")
   suicidio = cursor.fetchall() 
   
   faixa_etaria = []
   num_total_casos = []
   # print("Print each row and it's columns values")
   for row in suicidio:
       # print("FAIXA ETÁRIA = ", row[0], )
       # print("NÚMERO TOTAL DE CASOS  = ", row[3], "\n")
       faixa_etaria.append(row[0])
       num_total_casos.append(row[3])

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# barras possuem o tamanho padrão de 0.8, então adicionaremos 0.1 às
# coordenadas à esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(faixa_etaria)]

# as barras do gráfico com as coordenadas x à esquerda [xs], alturas [num_oscars]
plt.bar(xs, num_total_casos)

plt.ylabel("# Nº de suicídios")
plt.title("Número toral de casos de suicido no Brasil de 1985 a 2015 - MASCULINO")

# nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.5 for i, _ in enumerate(faixa_etaria)], faixa_etaria)

plt.show()