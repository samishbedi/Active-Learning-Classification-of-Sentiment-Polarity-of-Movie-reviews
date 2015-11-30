import nltkwordextraction as nl
import os,sys

posfile = open("posT.txt",'w')
negfile = open("negT.txt",'w')




pos = nl.make_token("Data/rt-polarity.pos")
neg =  nl.make_token("Data/rt-polarity.neg")

finalneg =[]
finalpos =[]

for f in pos.keys():
	if pos[f] > neg[f]:
		finalpos.append(f)




for f in neg.keys():
	if pos[f] < neg[f]:
		finalneg.append(f)

for w in finalpos:
	posfile.write(w+"\n")


for w in finalneg:
	negfile.write(w+"\n")






#print finalpos
#print "******************************************************************"

#print finalneg