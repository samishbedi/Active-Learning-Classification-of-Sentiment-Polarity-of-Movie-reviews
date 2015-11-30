def knnclassifier(posknn,negknn,token,k):
	
  tokenl=len(token)
	#print negknn
	
  checkp = False
  checkn = False
  prob=[0.0,0.0]

  posprob=[]
  negprob=[]

  for rev in posknn:
    posl = len(rev)
    freq=0.0
    for t in token:
        if(t in rev): 
				#print t," ",r
          checkp = True
          #print t," ",r
          freq +=1
    if (posl>0 and tokenl>0):
      freq=freq/(posl*tokenl*1.0)
      posprob.append(freq)


  for rev in negknn:
    negl = len(rev)
    freq=0.0
    for t in token:
      if(t in rev):
				#print t," ",r
          checkn = True
					#print t," ",r
          freq +=1
		#freq=freq/(negl*tokenl)
#    negprob.append(freq)
    if (negl>0 and tokenl>0):
      freq=freq/(negl*tokenl*1.0)
      negprob.append(freq)

	#print checkp," ",checkn
  posprob=sorted([w for w in posprob],reverse=True)
  negprob=sorted([w for w in negprob],reverse=True)
	#print posprob
	#print negprob
	
	#print checkn," ",checkp

  posindex=0
  negindex=0
  #print checkp,checkn
  if(checkp==1 or checkn==1):
    i=0
    while(i<k):
      if(posprob[posindex]>negprob[negindex]):
        prob[1]=prob[1]+posprob[posindex]*1.0
        posindex +=1
      else:
        prob[0]=prob[0]+negprob[i]*1.0
        negindex+=1
      i+=1
    prob.append(1)
  else:
    prob.append(0)

  return prob


