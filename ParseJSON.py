from urllib.request import urlopen
import json

url = input("Enter URL: ")
address = urlopen(url)
data = address.read()

total = 0

while True:
	if len(url) <1 : break

	print(address)
	print("Length ", len(data))

	info = json.loads(data)
	info = info["comments"]
	for item in info:
		print("Count: ",item["count"])
		total += int(item["count"])
	print("Sum: ", total)
	break
