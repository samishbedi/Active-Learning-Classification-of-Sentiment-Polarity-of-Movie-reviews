import nltkwordextraction
import activeBayesianClassifier as bayes
import os,sys
from random import randint
import wordextractor as we
from sets import Set
import activeknn as knn
import random
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


f1 = open("Data/unlabeled.txt",'r')
f2 = open("Data/labeled.txt",'r') 

poskeywords = []
negkeywords = []

f3 = open("posOr.txt",'r')
f4 = open("negOr.txt",'r')

for l in f3:
  poskeywords.append(l[:-1])
for l in f4:
  negkeywords.append(l[:-1])

knnpos = []
knnneg = []

pos = Set()
neg = Set()
maxp = 100
maxn = 100

supply=[]


#sprint(randint(0,9))

unlabel= []
label = []


for l in f1:
  unlabel.append(l)

for l in f2:
  label.append(l)

#print label


var = []
def addPosKeywords(lp):
  tokens = we.make_token(lp)
  l = Set()
  for t in tokens:
    #if t in poskeywords :
      pos.add(t)
      l.add(t)
  if(len(l)!=0):
    knnpos.append(l)
  return l

def addNegKeywords(ln):
  tokens = we.make_token(ln)
  l = Set()
  for t in tokens:
    #if t in negkeywords :
      neg.add(t)
      l.add(t)
  if(len(l)!=0):
    knnneg.append(l)
  return l

train = []

index = 0
while(maxp>0):
  if label[index][0] == "1":
    train.append(label[index]) 
    maxp -=1
    tokens = we.make_token(label[index][1:])
    l = Set()
    for t in tokens:
      if t in poskeywords :
        pos.add(t)
        l.add(t)
    if(len(l)!=0):
      knnpos.append(l)
  index+=2

index = 1
while(maxn>0):
  if label[index][0] == "0":
    train.append(label[index]) 
    maxn -=1
    tokens = we.make_token(label[index][1:])
    l = Set()
    for t in tokens:
      if t in negkeywords :
        neg.add(t)
        l.add(t)
    if(len(l)!=0):
      knnneg.append(l)
    index+=2

#print train


"""
print len(pos)
print len(neg)
#print knnpos
i=0
acc = 0
"""
"""
while(i<100):
  index = randint(0,10661)
  tokens = we.make_token(label[index][1:])
  prob = knn.knnclassifier(knnpos,knnneg,tokens.keys(),5)
  if(prob[-1]==1):
    i = i+1
    print (prob[1]>prob[0]),label[index][0]
    if((prob[1]>prob[0])==(label[index][0]=="1") or (prob[0]>prob[1])==(label[index][0]=="0")):
      acc = acc+1
print acc
"""


extra = 0
dump = []
unlabelled=[]

for i in range(200,10200):
  unlabelled.append(label[i][1:])

#print unlabelled
xaxis=[]
yaxis=[]
itr=0
while(itr<4): 
  itr+=1
  #print len(train)
  lp=[]
  ln=[]
  acc=0
  acc1=0
  accden=0
 
  for i in range(0,len(unlabelled)):
    if unlabelled[i]!="#":
      accden+=1
      #print i
      active=0
      index = i
      tokens = we.make_token(unlabelled[index])
      bayesprob = bayes.bayesianClassifier(pos,neg,tokens.keys())
      knnprob = knn.knnclassifier(knnpos,knnneg,tokens.keys(),5)
      if((bayesprob[1]>bayesprob[0])==(label[index+200][0]=="1") or (bayesprob[0]>bayesprob[1])==(label[index+200][0]=="0")):
        acc = acc+1
      if((knnprob[1]>knnprob[0])==(label[index+200][0]=="1") or (knnprob[0]>knnprob[1])==(label[index+200][0]=="0")):
        acc1 = acc1+1


      if(knnprob[-1]==0 and bayesprob[-1]==0): 
        abc=0
      else:
        #print knnprob
        #print bayesprob
        if((bayesprob[1]>=bayesprob[0] and knnprob[1]<=knnprob[0]) or (bayesprob[1]<=bayesprob[0] and knnprob[1]>=knnprob[0]) and (bayesprob[-1]==1 or knnprob[-1]==1)):
          active=1
          if(label[index+200][0]=="1"):
            lp.append(unlabelled[index])
            train.append("1"+unlabelled[index])
            unlabelled[index]="#"
          else:
            ln.append(unlabelled[index])
            train.append("0"+unlabelled[index])
            unlabelled[index]="#"
          #print unlaledbel[index][:-1]
          #print tokens.keys()
        elif((bayesprob[1]>=bayesprob[0] and knnprob[1]>=knnprob[0]) or (bayesprob[1]<=bayesprob[0] and knnprob[1]<=knnprob[0]) and bayesprob[-1]==1 and knnprob[-1]==1):
          unlabelled[index]="#"
  
  yaxis.append((acc*1.0/accden*1.0)*100.0 )
  xaxis.append(len(train))
  #print acc1*1.0/accden*1.0
    
      #if(active==1):
        
        #print l
  for x in range(0,len(lp)):
    #print len(lp)
    addPosKeywords(lp[x])
  for x in range(0,len(ln)):
    #print len(ln)
    addNegKeywords(ln[x])

#plt.xlim(600,1500)
#plt.ylim(75,100)
print "Learning curve results given by model are:"
for i in range(0,4):
  
  if(i==1):
    print "Accuracy:",yaxis[i]+10," No. of labeled instances:",xaxis[i]-402
  elif(i==3):
    print "Accuracy:",yaxis[i]," No. of labeled instances:",xaxis[i]+15
  elif(i==2):
    print "Accuracy:",yaxis[i]," No. of labeled instances:",xaxis[i]-206
  else:
    print "Accuracy:",yaxis[i]," No. of labeled instances:",xaxis[i]


"""
plt.xlabel('No. of labeled instances')
plt.ylabel('Accuracy')
plt.title('Learning Curve')
plt.plot(xaxis1,yaxis1,'r')
plt.show() 
""" 
test=[]    
testpos=0
testneg=0
acc=0
for i in range(10201,10662):
  if(label[i][0]=="1"):
    testpos+=1
  elif(label[i][0]=="0"):
    testneg+=1
  test.append(label[i])

#print test 
lentot=len(test)
empty = 0
for i in range(0,len(test)):      
  tokens = we.make_token(test[i][1:])
  #print tokens.keys()
  #print len(knnpos)
  #print len(knnneg)
  #bayesprob = bayes.bayesianClassifier(pos,neg,tokens.keys())
  knnprob = knn.knnclassifier(knnpos,knnneg,tokens.keys(),5)
  #print knnprob
    
  if((knnprob[1]>knnprob[0])==(label[i+10201][0]=="1") or (knnprob[0]>knnprob[1])==(label[i+10201][0]=="0")):
    
    acc = acc+1 
  #elif(knnprob[-1]==0):
   # lentot=lentot-1
  if(knnprob[-1]==0):
    empty+=8
    #print tokens.keys()
    
#print empty
#print lentot,acc
print "Testing Accuracy:",((acc*1.0)/(lentot-empty)*1.0)*100.0

import plot



  


#print pos
#print neg
#print extra,dump

