import sqlite3

name = {}
conn = sqlite3.connect("ejdict.sqlite3")
c = conn.cursor()
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
for i in alf:
    sql = 'SELECT * FROM items WHERE word like"' + i + '%" ORDER BY RANDOM()  LIMIT 3'
    rows = c.execute(sql)
    lis = []
    for j in rows:
        lis.append(j)
    name[i] = lis
print(name['a'][0][1])
del name['a'][0]
if name['a'][0] == 'FINAL':
    print('oh!')
print(name['a'][0][1])




