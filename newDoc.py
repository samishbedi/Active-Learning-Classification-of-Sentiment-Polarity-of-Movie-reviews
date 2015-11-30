import nltkwordextraction as nl
import os,sys

posfile = open("posOr.txt",'w')
negfile = open("negOr.txt",'w')
unlabel = open("unlabeled.txt",'w')

posD=nl.make_token("Data/rt-polarity.pos")
negD=nl.make_token("Data/rt-polarity.neg")
pos = nl.make_token("Data/rt-polarity.pos").keys()
neg =  nl.make_token("Data/rt-polarity.neg").keys()

finalneg =[]
finalpos =[]

"""for f in pos:
	if f in neg:
		continue
	else:
		finalpos.append(f)

for f in neg:
	if f in pos:
		continue
	else:
		finalneg.append(f)"""

for f in pos:
  if(posD[f]>negD[f]):
    finalpos.append(f)

for f in neg:
  if(negD[f]>posD[f]):
    finalneg.append(f)

print finalpos  
print finalneg  

for w in finalpos:
	posfile.write(w+"\n")


for w in finalneg:
	negfile.write(w+"\n")

"""


#print finalpos
#print "******************************************************************"

#print finalneg """
