fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  res = line.rstrip().split()
  for element in res:
        if element in lst: 
            continue
        else:
        	lst.append(element)
lst.sort()
print(lst)



