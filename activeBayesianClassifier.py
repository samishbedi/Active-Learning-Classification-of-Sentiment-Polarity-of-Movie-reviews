def bayesianClassifier(pos,neg,tokens):
	prob = [1.0,1.0]
	posl = len(pos)
	negl = len(neg)
	V = len(pos)+len(neg)
	checkp = False
	checkn = False
	for w in tokens :
		if(w in pos or w in neg):
			if w in neg:
				checkn = True
				prob[0] = prob[0]*(2.0/(negl+V))
				prob[1] = prob[1]*(1.0/(posl+V))
			else:
				checkp = True
				prob[0] = prob[0]*(1.0/(negl+V))
				prob[1] = prob[1]*(2.0/(posl+V))
	if(checkp==1 or checkn==1):
		prob.append(1)
	else:
		prob.append(0)
	return prob