import nltkwordextraction as nl
import os,sys

unlabel = open("Data/unlabeled.txt",'w')
label = open("Data/labeled.txt",'w') 

pos = open("Data/rt-polarity.pos",'r')
neg = open("Data/rt-polarity.neg",'r')
poslist = []
neglist = []
for l in pos:
  poslist.append(l)

for l in neg:
  neglist.append(l)

for i in range(0,len(poslist)):
	unlabel.write(poslist[i])
	label.write("1"+poslist[i])

	unlabel.write(neglist[i])
	label.write("0"+neglist[i])


#print finalpos
#print "******************************************************************"

#print finalneg
