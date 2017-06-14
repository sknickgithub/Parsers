import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('camerastream.xml')
root = tree.getroot()

Stream_data = open('streamdata.csv', 'w')

csvwriter = csv.writer(Stream_data)

##for i in range(1,1500,1):
	##stream = []
	##y = root.getchildren()[i]
	##detector = y.getchildren()[0].getchildren()[3].text
	##stream.append(detector)
	##latitude = y.getchildren()[0].getchildren()[2].getchildren()[0].text
	##stream.append(latitude)
	##longitude = y.getchildren()[0].getchildren()[2].getchildren()[1].text
	##stream.append(longitude)
	##csvwriter.writerow(stream)

for detector in root.findall('cctv-inventory-item'):
	stream = []
	name = detector.find('device-inventory-header').find('device-name').text
	stream.append(name)
	coordinates = detector.find('device-inventory-header').find('device-location')
	if coordinates is None:
		continue
	latitude = float(coordinates.find('latitude').text)/1000000
	stream.append(latitude)
	longitude = float(coordinates.find('longitude').text)/1000000
	stream.append(longitude)
	csvwriter.writerow(stream)

Stream_data.close()
