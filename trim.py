import json

DATA_FILE = 'C:\Users\kpk47_000\Desktop\\records-2015-09-07.json'
#DATA_FILE = 'C:\Users\kpk47_000\Documents\Workspace\shd2015\\tiny.json'

OUTPUT_FILE = 'C:\Users\kpk47_000\Desktop\\post-1990.json'
inf = open(DATA_FILE, 'r')
out = open(OUTPUT_FILE, 'w+')

for line in inf:
    if (line.find('\"creation_date": "20') != -1
        and line.find('"abstract": ""') == -1
        and line.find('withdrawn') == -1):
        ''' line.find('\"creation_date": "1995') != -1 or
        line.find('\"creation_date": "1996') != -1 or
        line.find('\"creation_date": "1997') != -1 or
        line.find('\"creation_date": "1998') != -1 or
        line.find('\"creation_date": "1999') != -1 or'''
        out.write(line)
    else:
        continue

inf.close()
out.close()
