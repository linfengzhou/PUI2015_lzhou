import json
import sys
import csv

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']

    with open(sys.argv[2], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['station Name', 'Latitude', 'Longitude']
        writer.writerow(headers)

        for s in stations:
            if s['statusKey'] !=1 and s['stationName'].startswith('Coming soon'):
                stationName = s['stationName']
                stationLat  = s['latitude']
                stationLon  = s['longitude']

                writer.writerow([stationName, stationLat, stationLon])

            #print('% 30s: %s, %s' % (stationName, stationLat, stationLon))

