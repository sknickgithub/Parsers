import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

url_str = 'http://205.221.97.102/Iowa.Sims.C2C/IADOT_SIMS_C2C.asmx/OP_ShareCCTVInventoryInformation?MSG_CCTVInventoryRequest=string%HTTP/1.1'

request = urllib2.Request(url_str,headers={"Accept":"text/xml"})

contents = urllib2.urlopen(request).read()

f = open('camerastream.xml','w')
f.write(contents)
f.close()