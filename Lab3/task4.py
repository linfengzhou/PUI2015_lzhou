import json
import sys

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']

    for s in stations:
        if s['statusKey'] !=1 and s['stationName'].startswith('Coming soon'):
            stationName = s['stationName']
            stationLat  = s['latitude']
            stationLon  = s['longitude']

            print '% 30s : %s, %s' % (stationName, stationLat, stationLon)

