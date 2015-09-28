import json
import sys
import urllib2

if __name__ == '__main__':
    #key = 'f4e96393-2edf-4f19-af57-a254ca7f26b3'
    #bus = 'B52'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (
        sys.argv[1], sys.argv[2])

    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())

    count = len(metadata['Siri']['ServiceDelivery'][
                'VehicleMonitoringDelivery'][0]['VehicleActivity'])
    print "Bus Line : %s" % (sys.argv[2])
    print "Number of Active Buses : %d" % (count)

    for i in range(count):
        latitude = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0][
            'VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0][
            'VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %d is at latitude: %f and longitude %f." % (i, latitude, longitude)
