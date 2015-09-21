import datetime
import json
import sys
from sys import argv
import urllib2

if __name__=='__main__':
    for dataId in argv[1:]:
        url = 'https://nycopendata.socrata.com/views/%s' % (dataId)
        #url = 'https://nycopendata.socrata.com/views/%s' % (sys.argv[1])
        #jsonFile = open(sys.argv[1], 'r');
        request = urllib2.urlopen(url)
        metadata = json.loads(request.read())
    print dataId,datetime.datetime.fromtimestamp(metadata['createdAt'])
    


