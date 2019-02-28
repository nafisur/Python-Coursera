name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
name = "mbox-short.txt"
handle = open(name)
text = handle.read()

words = list()

for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])


counts = dict()

for word in words:
           counts[word] = counts.get(word, 0) + 1 

        
maxval = None
maxkey = None
for key,val in counts.items() :
#   if maxval == None : maxval = val
  if val > maxval:
      maxval = val
      maxkey = key   

print(maxkey, maxval)
