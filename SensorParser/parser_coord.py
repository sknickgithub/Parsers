import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('stream.xml')
root = tree.getroot()

Stream_data = open('streamdata_lanesall.csv', 'w')

csvwriter = csv.writer(Stream_data)

for detector in root[2].findall('{http://www.dummy-temp-address}detector'):
	stream = []
	name = detector.find('{http://www.dummy-temp-address}detector-id').text
	stream.append(name)
	coordinates = detector.find('{http://www.dummy-temp-address}detector-location')
	if coordinates is None:
		continue
	latitude = float(coordinates.find('{http://www.dummy-temp-address}latitude').text)/1000000
	stream.append(latitude)
	longitude = float(coordinates.find('{http://www.dummy-temp-address}longitude').text)/1000000
	stream.append(longitude)
	csvwriter.writerow(stream)

Stream_data.close()