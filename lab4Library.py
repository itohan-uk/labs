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
def fEuler(xPrime, xPara, h):

	slopeList = []
	nDependent = len(xPrime) #Number of dependent variables
	for dependent in range(nDependent):
		xEqn = xPrime[dependent]  #Get the eqn for each dependent variable
		xEqnPara = xPara[dependent] #Get the parameters for each equation
		slope =  xEqn(xEqnPara)
		
		slopeList.append(slope)
	
	return slopeList


'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @return: returns a list of the values of the slope using trapezoidal
   			euler method without iteration
'''	
def tEuler(xPrime, xPara, h):	
	slopeList = []
	nDependent = len(xPrime)
	#print nDependent

	for dependent in range(nDependent):
		xEqn = xPrime[dependent]  #Get the eqn for each dependent variable
		xEqnPara = xPara[dependent] #Get the parameters for each equation
		
		oldX = xEqnPara[0]
		oldT = xEqnPara[1]
		slope0 =  xEqn(xEqnPara)
		newX = oldX + slope0*h
		newT = oldT + 1
		#print newX
		#print newT
		slope1 = xEqn([newX, newT])
		realSlope = (slope0 + slope1)/2
		#print realSlope

		
		slopeList.append(realSlope)
	
	return slopeList


'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @return: returns a list of the values of the slope using backward
   			euler method
'''	
def bEuler(xPrime, xPara, h):	
	slopeList = []
	nDependent = len(xPrime)
	#print nDependent

	for dependent in range(nDependent):
		xEqn = xPrime[dependent]  #Get the eqn for each dependent variable
		xEqnPara = xPara[dependent] #Get the parameters for each equation
		
		oldX = xEqnPara[0]
		oldT = xEqnPara[1]
		slope0 =  xEqn(xEqnPara)
		newX = oldX + slope0*h
		newT = oldT + 1
		#print newX
		#print newT
		slope1 = xEqn([newX, newT])
		realSlope = slope1
		#print realSlope

		
		slopeList.append(realSlope)
	#print slopeList
	
	return slopeList	


'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @return: returns a list of the values of the slope using RK34
   			method and no time adaptation
'''	

def rk4Notime(xPrime, xPara, h):
	slopeList = []
	nDependent = len(xPrime)
	

	for dependent in range(nDependent):
		xEqn = xPrime[dependent]  #Get the eqn for each dependent variable
		xEqnPara = xPara[dependent] #Get the parameters for each equation
		
		xK1 = xEqnPara[0]
		tk1 = xEqnPara[1]

		k1 = xEqn(xEqnPara)

		xK2 = xK1 + ((k1*h)/2)
		tk2 = tk1 + (h/2)

		k2 = xEqn([xK2, tk2])
		
		xK3 = xK1 + ((k2*h)/2)
		tk3 = tk2
		k3 = xEqn([xK3, tk3])

		xK4 = xK1 + (k3*h)
		tk4 = tk1 + h	
		k4 = xEqn([xK4, tk4])	

		slope = (k1 + 2*k2 + 2*k3 + k4)/6		
		
		
		slopeList.append(slope)
	
	return slopeList	



'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @return: returns a list of the values of the slope using RK34
   			method with time adaptation
'''	
	
def rk4WithTime(xPrime, xPara, h):













xList = []
xPrime = [xVal]
xPara = [[2.0,0]]
xList.append(xPara[0][0])
slope = []


for t in range(1,5):
	

	
	slopeVal = (rk4Notime(xPrime,xPara,1.0))[0]

	x = xPara[0][0] + slopeVal*1
#print x 
	xPara = [[x,t]]
	xList.append(x)




print  xList

