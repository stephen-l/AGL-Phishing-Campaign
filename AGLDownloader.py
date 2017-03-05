import urllib
import urllib2
import time
from random import randint

# different static captchas found on site
# the captchas appeared to only be validated on the client side, POSTing any value to captcha_code would be accepted
captcha = ["0116194","4372694","1185019","8573775","5110348","5416170","3426690","3890434","9532960"]

# malicous phishing site with fake base64 encoded email address
url = 'http://ylag.aglbill-server.net/fjvh.php?id=YXNtZGxhbUBrc21mbGRtc2QuY29tCg=='

# not needed but kept this so i could use it down the track one day. Selects 1 of the 9 static captchas
data = urllib.urlencode({'captcha_code' : captcha[randint(0,8)]})

# perform the POST and read the server response
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
zipfile = response.read() # store the download in zipfile

# give each file a unique name with time (it is possible to collide names but not really much of a concern)
# this might be better if it was saved as [MD5 hash].zip
filename = "AGL-"+str(time.clock())+".zip"

# these were added to quickly visualise if a differnt zip was found
print "filename: ",filename
print "length of file: ",len(zipfile)

# write the zip to disk
with open(filename, "w") as file:
    file.write(zipfile)

    
# TODO:
# - check the response hash of the hashes on disk. if duplicate, then dont save
# - change file name to MD5 hash
