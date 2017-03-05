# AGL-Phishing-Campaign
A quick and dirty script I made to monitor when the actors uploaded new droppers (which lead to new domains hosting the malicous payload) in a AGL phishing/ransomware campaign. This will most likely need to be modified to suit another AGL/AusPost campaign if it comes around.

It posts the captcha to the server and writes the downloaded zip to disk.

## Usage
Modify the url to suit the new campaign. If the new campaign uses the same captcha validation then the captchas won't need to be changed.
```
python AGLDownloader.py
```
