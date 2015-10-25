import json
import numpy as np
from scipy.sparse import lil_matrix
from scipy import io

#DATA_FILE = 'C:\Users\kpk47_000\Desktop\\with_abstracts.json'
#DATA_FILE = 'C:\Users\kpk47_000\Desktop\\train.json'
DATA_FILE = 'C:\Users\kpk47_000\Desktop\\records-2015-09-07.json'
#DATA_FILE = 'C:\Users\kpk47_000\Documents\Workspace\shd2015\\tiny.json'

f = open(DATA_FILE, 'r')

max_id = 1391956 # current max found
'''
for line in f:
    line = line[0:-1] #trim newline
    rec = json.loads(line)
    if rec['recid'] > max_id:
        max_id = rec['recid']
    else:
        continue
f.close()
'''
M = lil_matrix((max_id, max_id))
f = open(DATA_FILE, 'r')

for line in f:
    line = line[0:-1]
    rec = json.loads(line)
    for i in rec['references']:
        M[rec['recid']-1,i-1] = 1
#        M[rec['recid']-1,i-1] = i
f.close()

io.savemat('C:\Users\kpk47_000\Desktop\\full-new.mat', dict(M=M))
#print M        
