import numpy as np


#Define your xprime as a function
def xVal(paraList):
	x = paraList[0]
	t = paraList[1]
	dxdt = (4*(np.exp(0.8*t))) - (0.5*x)

	return dxdt



'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @return: returns a list of the values of the slope using forward
   			euler method
'''
def fEuler(xPrime, xPara):

	slopeList = []
	nDependent = len(xPrime) #Number of dependent variables
	for dependent in range(nDependent):
		xEqn = xPrime[dependent]
		xEqnPara = xPara[dependent]
		slope =  xEqn(xEqnPara)
		
		slopeList.append(slope)
	
	return slopeList


'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @return: returns a list of the values of the slope using forward
   			euler method
'''	
def bEuler(xPrime, xPara):	









'''
xList = []
xPrime = [xVal]
xPara = [[2.0,0]]
xList.append(xPara[0][0])
slope = []


for t in range(1,5):
	

	
	slopeVal = (fEuler(xPrime,xPara))[0]

	x = xPara[0][0] + slopeVal*1
	
	xPara = [[x,t]]
	xList.append(x)




print  xList
'''
