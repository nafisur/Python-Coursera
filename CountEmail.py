import sqlite3

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox.txt"
handler = open(fname)

templist = list()
count = 0

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')           
cur.execute('''DELETE FROM Counts''') 

for line in handler:
         line = line.rstrip()
         if not line.startswith('From ') : continue
         words = line.split()
         domain = words[1].split("@")       
         cur.execute('''SELECT count FROM Counts where org = ?''',(domain[1],))
         count = cur.fetchone()
         if count is None: 
              cur.execute('''INSERT INTO Counts (org, count) VALUES (?,1)''',(domain[1],))
         else :
              cur.execute('''UPDATE Counts SET count = count + 1  WHERE org = ?''',(domain[1],))
         
conn.commit()

table = 'SELECT org, count FROM Counts ORDER BY count DESC'
for line in cur.execute(table): 
        print(str(line[0]), ":", str(line[1]))

conn.close()