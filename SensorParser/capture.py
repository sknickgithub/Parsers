import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

url_str = 'http://205.221.97.102/Iowa.Sims.AllSites.C2C/IADOT_SIMS_AllSites_C2C.asmx/OP_ShareTrafficDetectorInventoryInformation?MSG_TrafficDetectorInventoryRequest=string%HTTP/1.1'

request = urllib2.Request(url_str,headers={"Accept":"text/xml"})

contents = urllib2.urlopen(request).read()

f = open('stream.xml','w')
f.write(contents)
f.close()