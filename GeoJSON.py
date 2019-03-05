import urllib.request as ur
import urllib.parse as up
import json

geourl = "http://python-data.dr-chuck.net/json?"

place = input("Enter Place name : ")
params = {"address": place, "key": 42}
url = geourl + up.urlencode(params)
data = ur.urlopen(url).read().decode('utf-8')
obj = json.loads(data)

placeid = obj["results"][0]["place_id"]
print("id :", placeid)