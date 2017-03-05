import urllib
import urllib2
import time
from random import randint

captcha = ["0116194","4372694","1185019","8573775","5110348","5416170","3426690","3890434","9532960"]

url = 'http://ylag.aglbill-server.net/fjvh.php?id=YXNtZGxhbUBrc21mbGRtc2QuY29tCg=='

data = urllib.urlencode({'captcha_code' : captcha[randint(0,8)]})

req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
zipfile = response.read()

filename = "AGL-"+str(time.clock())+".zip"

print "filename: ",filename
print "length of file: ",len(zipfile)

with open(filename, "w") as file:
    file.write(zipfile)
