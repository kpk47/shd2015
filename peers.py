from scipy import io
import numpy as np

M = None
MATRIX_FILE = 'C:\Users\kpk47_000\Desktop\\full-new.mat'

# Call me first!
def init():
    global M
    M = io.loadmat(MATRIX_FILE)['M']

# find peer papers for one citation
# recid = recid of citation
# peers = min. number of peers to cite return values
def find_paper(recid, peers=1):
    global M
    cols = [int(x) - 1 for x in np.unique(M[recid].toarray()).tolist()]
    refs = []
    for col in cols:
        refs += [int(x) for x in np.unique(M[:,col].indices)]
    recs = [x + 1 for x in set(refs) if refs.count(x) >= peers]
    recs.sort()
    return recs

# find peer papers for a list of citations
# recid_list = list of citations
# peers = min. number of peers to cite return values
# count = min. number of peer lists to recommend return values
def find_many(recid_list, peers=1, count=1):
    refs = []
    for recid in recid_list:
        refs += find_paper(recid, peers)
    recs = [x for x in set(refs) if refs.count(x) >= count and
            x not in recid_list]
    recs.sort()
    return recs
