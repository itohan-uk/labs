import numpy as np
from copy import deepcopy
from operator import add
from numpy import linalg as la


#Define your xprime as a function

'''@param: InitialVal is the initial parameter value at t0
   @param: t0 is the time at t0
   @return: ode value
'''
def xVal(InitialVal, t0):
	x = InitialVal
	dxdt = (4*(np.exp(0.8*t0))) - (0.5*x)

	return dxdt



'''@param: InitialVal is a list of all the values to be passed to the eqn
		   V1 and V2 are the first and second term in the list
		   R1, R2, R3 are the 3rd, 4th and 5th terms respectively
		   C1, C2 are the 6th and 7th terms
		   i(t)List is the 8th term in the list and is a list of all the 
		   current at various times
		   timeIdx is the 9th term in the list used to index  i(t)List
   @param: t0 is the time
'''
'''@param: InitialVal is a list of all the values to be passed to the eqn
		   V1 and V2 are the first and second term in the list
   @param: t0 is the time
   @return: vector for the slopes of V1 and V2
'''
def circuitOde(initialVal, t0):
	V1 = initialVal[0]
	V2 = initialVal[1]
	m = (0.1e-3)/(1e-9)
	global R1
	global R2
	global R3
	global C1
	global C2

	if ((t0 == 0) or (t0 in np.arange(11e-9, 20e-9, 1e-9)) or
		(t0 in np.arange(31e-9, 40e-9, 1e-9)) or 
		(t0 in np.arange(51e-9, 60e-9, 1e-9)) or
		(t0 in np.arange(71e-9, 80e-9, 1e-9)) or
		(t0 in np.arange(91e-9, 100e-9, 1e-9))):

		i = 0.0

	elif ((t0 in np.arange(1e-9, 10e-9, 1e-9)) or 
		(t0 in np.arange(21e-9, 30e-9, 1e-9)) or
		(t0 in np.arange(41e-9, 50e-9, 1e-9)) or
		(t0 in np.arange(61e-9, 70e-9, 1e-9)) or
		(t0 in np.arange(81e-9, 90e-9, 1e-9))):
		i = 0.1e-3

	else:
		i = m*t0	


	# R1 = initialVal[2]
	# R2 = initialVal[3]
	# R3 = initialVal[4]
	# C1 = initialVal[5]
	# C2 = initialVal[6]
	#i = initialVal[7]	
	#iList = initialVal[7]
	#timeIdx = initialVal[8]
	#i = iList[timeIdx]

	A  = -((1/(C1*R1)) + (1/(C1*R2)))
	B  = 1/(C1*R2)
	C = 1/(C2*R2)
	D = -((1/(C2*R2)) + (1/(C2*R3)))

	mat = [[A, B], [C, D]]

	vec = [V1, V2]
	

	addition = [(i/C1), 0]

	#Solving the matrix with 
	Mat = np.array(mat)
	Vec = np.array(vec)

	dV1dV2dt = (la.solve(Mat, Vec) + np.array(addition))

	return dV1dV2dt



'''@param: xEqn is the function  for the equation of the ODE
   @param: xParaInitial is a list of inputs  to the xEqn functions
   @param: t0 is the value of t at time 0
   @param: h is the value of the step size to be used
   @param: adaptBit -> set to 0
   @return: returns a list of the values of the slope using forward
   			euler method
'''
def fEuler(xEqn, xParaInitial, t0, h, adaptBit):

	 
	slope =  xEqn(xParaInitial, t0)
	
	return slope



'''@param: xEqn is the function for the equation of the ODE
   @param: xParaInitial is a list of inputs to the xEqn functions
   @param: t0 is the value of t at time 0
   @param: h is the value of the step size to be used
   @param: adaptBit -> set to 0
   @return: returns the values of the slope using trapezoidal
   			euler method
'''
def tEuler(xEqn, xParaInitial, t0, h, adaptBit):

	slope0 = xEqn(xParaInitial, t0)	
	t1 = t0 + h
	if not isinstance(xParaInitial, list):
		newParas = xParaInitial + slope0*h
		slope1 = xEqn(newParas, t1)
		realSlope = (slope0 + slope1)/2


	else:
		slope0h = list(map(lambda x: x*h, slope0))
		newParas = 	map(add, xParaInitial, slope0h)
		slope1 = xEqn(newParas, t1)
		realSlope = map(add, slope0, slope1)
		realSlope = list(map(lambda x: x/2, realSlope))

	return realSlope



'''@param: xEqn is the function for the equation of the ODE
   @param: xParaInitial is a list of inputs to the xEqn functions
   @param: t0 is the value of t at time 0
   @param: h is the value of the step size to be used
   @param: adaptBit -> set to 0
   @return: returns the values of the slope using backward
   			euler method
'''
def bEuler(xEqn, xParaInitial, t0, h, adaptBit):

	slope0 = xEqn(xParaInitial, t0)	
	t1 = t0 + h
	if not isinstance(xParaInitial, list):
		newParas = xParaInitial + slope0*h
		realSlope = xEqn(newParas, t1)


	else:
		slope0h = list(map(lambda x: x*h, slope0))
		newParas = 	map(add, xParaInitial, slope0h)
		realSlope = xEqn(newParas, t1)
		
	return realSlope



'''@param: xEqn is the function for the equation of the ODE
   @param: xParaInitial is a list of inputs to the xEqn functions
   @param: t0 is the value of t at time 0
   @param: h is the value of the step size to be used
   @param: adaptBit-> 0 = no time adaptation, 1 = time adaptation
   @return: returns a list of the values of the slope using RK34
   			method and no time adaptation
'''	
def rk4(xEqn, xParaInitial, t0, h, adaptBit):

	tk2 = t0 + (h/2)
	tk3 = tk2
	tk4 = t0 + h

	# print "t0 %f "  %t0
	# print "tK2 %f "  %tk2
	# print "tK3 %f "  %tk3
	# print "tK4 %f "  %tk4
	# print "\n"

	if not isinstance(xParaInitial, list):
		xK1 = xParaInitial
		k1 = xEqn(xParaInitial, t0)

	 	xK2 = xK1 + ((k1*h)/2)
		k2 = xEqn(xK2, tk2)
	
		xK3 = xK1 + ((k2*h)/2)
		k3 = xEqn(xK3, tk3)

		xK4 = xK1 + (k3*h)
		k4 = xEqn(xK4, tk4)	

		Err = ((-5*k1 + 6*k2 + 8*k3 - 9*k4)*h)/72

		realSlope = (k1 + 2*k2 + 2*k3 + k4)/6	



		# print "K1 %d "  %k1
		# print "K2 %d "  %k2
		# print "K3 %d "  %k3
		# print "K4 %d "  %k4


	else:
		
		k1List = xEqn(xParaInitial, t0)
		k1Mod = list(map(lambda x: ((x*h)/2), k1List))
		
		xParaK2 = map(add, xParaInitial, k1Mod)
		k2List = xEqn(xParaK2, tk2)
		k2Mod = list(map(lambda x: ((x*h)/2), k2List))

		xParaK3 = map(add, xParaInitial, k2Mod)
		k3List = xEqn(xParaK3, tk3)
		k3Mod = list(map(lambda x: (x*h), k3List))

		xParaK4 = map(add, xParaInitial, k3Mod)
		k4List = xEqn(xParaK4, tk4)


		#Caluculating slope using the k values
		k1Slope = list(map(lambda x: ((x/6)), k1List))
		k2Slope = list(map(lambda x: ((x*2)/6), k2List))
		k3Slope = list(map(lambda x: ((x*2)/6), k3List))
		k4Slope = list(map(lambda x: ((x/6)), k4List))

		sum1 = map(add, k1Slope, k2Slope)
		sum2 = map(add, sum1, k3Slope)
		realSlope = map(add, sum2, k4Slope) 

		#Caluculating Err using the k values
		k1Err = list(map(lambda x: (-5*x), k1List))
		k2Err = list(map(lambda x: (6*x), k2List))
		k3Err = list(map(lambda x: (8*x), k3List))
		k4Err = list(map(lambda x: (-9*x), k4List))

		err1 = map(add, k1Err, k2Err)
		err2 = map(add, err1, k3Err)
		err3 = map(add, err2, k4Err)

		Err = list(map(lambda x: ((h*x)/72), err3))


	
	if not adaptBit:	
		return realSlope

	else:
		return [realSlope, Err]		





'''@param: odeMethod is the odeMethod to be used
   @param: xEqn is the function for the equation of the ODE
   @param: xParaInitial is a list of inputs to the xEqn functions
   @param: t0 is the value of t at time 0
   @param: h is the value of the step size to be used
   @param: tol1 is the tolerance1 if time adaptation is used
   @param: tol2 is the tolerance2 if time adaptation is used
   @param: adaptBit -> 1 = adaptation, 0 = no adaptation
   @param: timeStop is the last time value to be used
   @return: returns a list of the calculated parameter values
'''	

def odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop):

	finalValues = []

	#bEuler(xEqn, xParaInitial, t0, h, adaptBit)
	timeList = np.arange(t0, (timeStop), h)

	#for time in range((t0 + 1), len(timeList)):
	for time in range(t0, len(timeList)):
		t0 = timeList[time]

		if not adaptBit:
			slope = odeMethod(xEqn, xParaInitial, t0, h, adaptBit)
			if not isinstance(xParaInitial, list):
				finalValues.append(xParaInitial)
				newX = xParaInitial + slope*h
				xParaInitial = newX

			else:
				finalValues.append(xParaInitial)
				slope0h = list(map(lambda x: x*h, slope))
				newParas = map(add, xParaInitial, slope0h)
				xParaInitial = newParas
		
		elif adaptBit:
		
			result = odeMethod(xEqn, xParaInitial, t0, h, adaptBit)
			slope = result[0]
			if not isinstance(xParaInitial, list):
				finalValues.append(xParaInitial)
				newX = xParaInitial + slope*h
				xParaInitial = newX

			else:
				finalValues.append(xParaInitial)
				slope0h = list(map(lambda x: x*h, slope))
				newParas = map(add, xParaInitial, slope0h)
				xParaInitial = newParas

			
			E	= result[1]
			Err = abs(E)/abs(xParaInitial)

			if Err > tol1:
					
				h = h/2
				
			elif Err < tol2:
					
				h = 2*h

			elif tol2 <Err < tol1:
				h = h			
		


	return finalValues









R1 = R2 = R3 = 10e3
C1 = C2 = 1e-12


odeMethod = rk4
#xEqn = xVal
xEqn = circuitOde
#xParaInitial = 2.0
xParaInitial = [0,0]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 1
#timeStop =5
timeStop = 100e-9

xList = odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)

print  xList

