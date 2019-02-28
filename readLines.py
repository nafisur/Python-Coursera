# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("Unable to open the file")
    quit()
for line in fh:
    print(line.rstrip().upper())
    


