import json
import sys
import urllib2
import pandas as pd

if __name__ == '__main__':
    # key = 'f4e96393-2edf-4f19-af57-a254ca7f26b3'
    #  bus = 'M7'
    # url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key,bus)
    # python get_bus_info.py f4e96393-2edf-4f19-af57-a254ca7f26b3 M7 M7.csv
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (
        sys.argv[1], sys.argv[2])
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())

    data = metadata['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']

    busdata = {'Latitude': [],
               'Longitude': [],
               'Stop Name': [],
               'Stop Status': []}

    latitude = []
    longitude = []
    stopname = []
    stopstatus = []

    for i in data:
        latitude.append(
            i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
        longitude.append(
            i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        if i['MonitoredVehicleJourney']['OnwardCalls'] == {}:
            stopname.append('NA')
            stopstatus.append('NA')
        else:
            stopstatus.append(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][
                              0]['Extensions']['Distances']['PresentableDistance'])
            stopname.append(
                i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])

    busdata['Latitude'] = latitude
    busdata['Longitude'] = longitude
    busdata['Stop Name'] = stopname
    busdata['Stop Status'] = stopstatus
    bus = pd.DataFrame(busdata)

    bus.to_csv(sys.argv[3], index=False)

 #   with open(sys.argv[3], 'wb') as csvFile:
   #     writer = csv.writer(csvFile)
   #     headers = ['Latitude', 'Longitude','Stop Name','Stop Status']
    #    writer.writerow(headers)
    #   for i in bus:

    #  writer.writerow([busLat, busLon, stopName, stopStatus])
