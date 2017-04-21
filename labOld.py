import numpy as np
from copy import deepcopy


#Define your xprime as a function
def xVal(paraList):
	x = paraList[0]
	t = paraList[1]
	dxdt = (4*(np.exp(0.8*t))) - (0.5*x)

	return dxdt


'''@param: xPrime the function for the xPrime equations
   @param: xPara is a list of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @param: adaptBit -> set to 0
   @return: returns a list of the values of the slope using forward
   			euler method
'''
def fEuler(xPrime, xPara, h, adaptBit):

	xEqn = xPrime 
	slope =  xEqn(xPara)
	
	return slope



'''@param: xPrime the function for the xPrime equations
   @param: xPara is a list of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @param: adaptBit -> set to 0
   @return: returns a list of the values of the slope using trapezoidal
   			euler method
'''
def tEuler(xPrime, xPara, h, adaptBit):	
	
	xEqn = xPrime  
	numPara = len(xPara)
			
	#oldX = xPara[0]

	oldT = xPara[numPara -1]
	paraList = deepcopy(xPara)
	
	del paraList[numPara -1]
	slope0 =  xEqn(xPara)
	#newX = oldX + slope0*h
	
	paraList = list(map(lambda x: x + slope0*h, paraList))
	#print paraList
	newT = oldT + 1
	#print newT

	paraList.append(newT)
	#print slope1List
	#slope1 = xEqn([newX, newT])
	slope1 = xEqn(paraList)
	realSlope = (slope0 + slope1)/2
		
	return realSlope



'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @param: adaptBit -> set to 0
   @return: returns a list of the values of the slope using backward
   			euler method
'''	
def bEuler(xPrime, xPara, h, adaptBit):	
	
	xEqn = xPrime  #Get the eqn for each dependent variable
	#xEqnPara = xPara #Get the parameters for each equation
	numPara = len(xPara)
	oldT = xPara[numPara -1]
	paraList = deepcopy(xPara)

	del paraList[numPara -1]
	slope0 =  xEqn(xPara)
	#oldX = xEqnPara[0]
	#oldT = xEqnPara[1]
	#slope0 =  xEqn(Para)
	paraList = list(map(lambda x: x + slope0*h, paraList))
	#print paraList
	newT = oldT + 1
	#print newT

	paraList.append(newT)
	
	slope1 = xEqn(paraList)
	realSlope = slope1
	
	return realSlope	



'''@param: xPrime is a list of functions for the xPrime equations
   @param: xPara is a list of lists of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @param: adaptBit- 0 = no time adaptation, 1 = time adaptation
   @return: returns a list of the values of the slope using RK34
   			method and no time adaptation
'''	
def rk4(xPrime, xPara, h, adaptBit):
	
	xEqn = xPrime #Get the eqn for each dependent variable
	xEqnPara = xPara 
	numPara = len(xPara)
	oldT = xPara[numPara -1]
	paraList = deepcopy(xPara)
	
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

	Err = ((-5*k1 + 6*k2 + 8*k3 - 9*k4)*h)/72

	slope = (k1 + 2*k2 + 2*k3 + k4)/6	

	

	if not adaptBit:	
		return slope

	else:
		return [slope, Err]		


'''@param: odeMethod is the odeMethod to be used
   @param: eqnList is a list of functions for the xPrime equations
   @param: eqnPara is a list of lists of inputs  to the xPrime functions
   @param: h is the step size, should be floating point
   @param: tol is the tolerance if time adaptation is used
   @param: adaptBit -> 1 = adaptation, 0 = no adaptation
   @param: timeRange tells how many times to use assuming timestep of 1
   @return: returns a list of the values of the slope using RK34
   			method with time adaptation
'''	

def odeSolver(odeMethod, eqnList, eqnPara, h, tol1, tol2 , adaptBit , timeRange):
	nDependent = len(eqnList) #number of dependent variables
	dependentList = [] #List of lists of final values for dependent
	
	
	for dependent in range(nDependent):
		xPrime = eqnList[dependent]
		xPara = eqnPara[dependent]
		numPara = len(xPara)
		#t0 = xPara[numPara - 1] #t0 is always last in the list
		xList = []
		#xList.append(xPara)
		
		for time in range(1,timeRange + 1):
			if not adaptBit:
				#print 'no adapt'
				slope = odeMethod(xPrime, xPara, h, adaptBit)

				x = xPara[0]
				xList.append(x)
				x = x + slope*h
				
				xPara = [x, time]

			else:
				result = odeMethod(xPrime, xPara, h, adaptBit)
				slope = result[0]
				x = xPara[0]
				xList.append(x)
				x = x + slope*h

				E	= result[1]
				Err = abs(E)/abs(x)	
				
				
				if Err > tol1:
					
					h = h/2
				
				elif Err < tol2:
					
					h = 2*h

				elif tol2 <Err < tol1:
					h = h	

				xPara = [x, time]	


		dependentList.append(xList)

		



	return dependentList	













xList = []
xPrime = [xVal]
xPara = [[2.0,0]]
xList.append(xPara[0])
slope = []
tol1 = 1e-1
tol2 = 1e-3

'''for t in range(1,5):
	

	
	slopeVal = (rk4(xPrime,xPara,1.0))

	x = xPara[0] + slopeVal*1
#print x 
	xPara = [x,t]
	xList.append(x)'''

#(odeMethod, eqnList, eqnPara, h, tol1, tol2 , adaptBit , timeRange):
xList = odeSolver(rk4,xPrime,xPara, 1.0, tol1, tol2, 0, 5)


print  xList

