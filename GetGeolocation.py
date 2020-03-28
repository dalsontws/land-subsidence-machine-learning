import pandas as pd
import requests

inputFile = "data/mexico/Mexico2015-2016APR.txt"
outputFile = 'data/mexico-geocoded-output/output.csv'
data = pd.read_csv(inputFile, sep='\t')

# Set coherence limit
dataCoh = data[data["coh"] > 0.3]

df = pd.DataFrame()
locations = dataCoh

for index, row in locations.iterrows():

    # Replace YOUR_API_KEY_HERE with HEREMaps API
    apiKey = YOUR_API_KEY_HERE
    lat = str(row['Latitude'])
    long = str(row['Longitude'])

    response = requests.get('https://revgeocode.search.hereapi.com/v1/revgeocode?at=' + lat + '%2C' + long +
                            '&lang=en-US'+'&apiKey=' + apiKey)

    location = response.json()

    city = (location['items'][0]['address']['city'])
    print(city)
    df = df.append(row)

df.to_csv(outputFile)
