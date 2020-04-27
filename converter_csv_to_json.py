import csv
import json

csvFilePath = 'db/suicide_rates_overview_1985_to_2016_1.csv'
jsonFilePath = 'db/suicide_rates_overview_1985_to_2016.json'

# read csv file and add to data
data = {} 
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        country = rows['country']   # Copio o dado da primeira coluna para ser o index do DICIONÁRIO
        data[country] = rows        # copio os resto dos dados
     
# create new json file and write data on it
with open(jsonFilePath, 'w') as jsonFile:
    # make it more readable and pretty
    jsonFile.write(json.dumps(data, indent=4)) 