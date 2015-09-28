import datetime
import json
import sys
from sys import argv

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r');
    metadata = json.load(jsonFile)
    print datetime.datetime.fromtimestamp(metadata['createdAt'])


