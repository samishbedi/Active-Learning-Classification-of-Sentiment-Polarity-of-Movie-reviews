import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

yaxis1=[74.92,75.24,73,72.66,72,73.88,75,76,78,81,84,85,87.67,91,94,96,97.093,98.093,99.093,99.093]
xaxis1=[969,1000,1030,1090,1120,1150,1180,1210,1240,1270,1300,1330,1360,1400,1450,1500,1566,1580,1600,1620]

  
plt.ylim(50,100)
plt.xlabel('No. of labeled instances')
plt.ylabel('Accuracy %')
plt.title('Learning Curve')
plt.plot(xaxis1,yaxis1,'r')
plt.show() 
         
