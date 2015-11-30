To run the model:
----------------------------------------------
1. Open terminal
2. Install ntlk,matplotlibnumpy, if not installed already using:
	sudo pip install -U nltk
3. run the command:
	python run.py
4. Output will give learning curve values of notable iterations and accuracy of test cases on terminal and plot of learning curve in another window.  If you want to get output in file, type:
	python run.py 
	
-----------------------------------------------
	
# Active-Learning-Classification-of-Sentiment-Polarity-of-Movie-reviews
The project aims to classify movie reviews on the basis of sentiment polarity as positive or negative. Pool Based Active Learning approach along with Query By Committee as Query Strategy Framework and K-Nearest Neighbor and Naive Bayes classification models were used to efficiently classify the movie reviews with testing accuracy of 90.15% and training set of only 1581 reviews actively chosen as compared to 71.2% accuracy of a traditional passive learning active algorithm.
