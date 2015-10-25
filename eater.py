#TODO
# display three links out
# chronological map

import json
import numpy
from scipy import io as spio
import StringIO

#adjacency fetcher, needs path to adjacency matrix
path_to_mat = "/Users/Chrisantha/Work/resources/"
adjMat = spio.loadmat(path_to_mat)['M']

# returns array of citations given a recid
def citations(source):
  sourcearray = numpy.unique(adjMat[source - 1].toarray())
  if (sourcearray[0]!=0.0):
    return sourcearray
  return sourcearray[1:]

linklist = []
# Create list of these:  {source: "1", target: "3", type: "cites"}
# Each paper is listed by its recid
def linkpaper(recid):
  for cited in citations(recid):
    linkstr = "{source: \""+str(recid)+"\", target: \""+str(cited)+"\", type: \"cite\"}"
    linklist.append(linkstr)
print linklist

rec_list = []

def threeLevelMap(recid):
  level2 = []
  level1 = citations(recid)
  used = set(level1)
  for cite in level1:
    used.add(citations(cite))
    linkpaper(cite)


