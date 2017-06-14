import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('stream.xml')
root = tree.getroot()

Stream_data = open('streamdata_lane.csv', 'w')

csvwriter = csv.writer(Stream_data)

for detector in root[2].findall('{http://www.dummy-temp-address}detector'):
	stream = []
	name = detector.find('{http://www.dummy-temp-address}detector-id').text
	stream.append(name)
	approaches = detector.find('{http://www.dummy-temp-address}detector-approaches')
	if approaches is None:
		continue
	approach = approaches.find('{http://www.dummy-temp-address}detector-approach')
	if approach is None:
		continue
	direction = approach.find('{http://www.dummy-temp-address}approach-direction').text
	stream.append(direction)
	name2 = approach.find('{http://www.dummy-temp-address}approach-name').text
	stream.append(name2)
	typelane = approach.find('{http://www.dummy-temp-address}lanes-type').text
	stream.append(typelane)
	laneid = approach.find('{http://www.dummy-temp-address}detection-lanes').find('{http://www.dummy-temp-address}detection-lane').find('{http://www.dummy-temp-address}lane-id').text
	stream.append(laneid)
	csvwriter.writerow(stream)

Stream_data.close()