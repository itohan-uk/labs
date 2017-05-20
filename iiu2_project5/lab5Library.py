###############################
#   ITOHAN UKPONMWAN (iiu2)   #
#		   ECE 4960			  #
#	    LAB 5 Library	      #
###############################


import numpy as np
from operator import add
from numpy import linalg as la





##################################################################
# 				TASK 3: VALIDATION EQUATION				         #
##################################################################

'''@param: InitialVal is the initial parameter value at t0
   @param: t0 is the time at t0
   @return: ode value
'''
def xVal(InitialVal, t0):
	x = InitialVal
	dxdt = (4*(np.exp(0.8*t0))) - (0.5*x)

	return dxdt




##################################################################
# 				TASK 4: CIRCUIT 1 EQUATION				         #
##################################################################

'''@param: InitialVal is a list of all the dependent variables
		   to be passed to the ode eqn
   @param: t0 is the time
   @return: vector for the slopes of V1 and V2
'''
def circuitOde(initialVal, t0):
	V1 = initialVal[0]
	V2 = initialVal[1]
	m = (0.1e-3)/(1e-9)
	R1 = R2 = R3 = 10.0e3
	C1 = C2 = 1e-12
	
	if ((t0 == 0) or (11e-9 <= t0 < 21e-9) or (31e-9 <= t0 < 41e-9) or
		(51e-9 <= t0 < 61e-9) or (71e-9 <= t0 < 81e-9) or
		(91e-9 <= t0 < 101e-9)):
	
		i = 0.0
		
	elif ((1e-9 <= t0 < 11e-9) or (21e-9 <= t0 < 31e-9) or
		(41e-9 <= t0 < 51e-9) or (61e-9 <= t0 < 71e-9) or
		(81e-9 <= t0 < 91e-9)):

		i = 0.1e-3

	else:
		i = m*t0


	A  = -((1/(C1*R1)) + (1/(C1*R2)))
	B  = 1/(C1*R2)
	C = 1/(C2*R2)
	D = -((1/(C2*R2)) + (1/(C2*R3)))


	mat = [[A, B], [C, D]]

	vec = [V1, V2]
	

	addition = [(i/C1), 0]

	
	Mat = np.array(mat)
	Vec = np.array(vec)

	dV1dV2dt = np.dot(Mat, Vec) + np.array(addition)


	return dV1dV2dt


##################################################################
# 				TASK 5: CIRCUIT 2 EQUATION				         #
##################################################################

'''@param: InitialVal is a list of all the dependent variables
		   to be passed to the ode eqn
   @param: t0 is the time
   @return: vector for the slopes of V1 and V2
'''
def ekvOde(initialVal, t0):
	V1 = Vgb = initialVal[0]
	V2 = Vdb = initialVal[1]
	Is = 5e-6
	k = 0.7
	Vth = 1.0
	Vdd = 5.0
	Vt = 26e-3
	Rg = Rl = 10e3
	C1 = C2 = 1e-12
	m = (0.1e-3)/(1e-9)

	if ((t0 == 0) or (11e-9 <= t0 < 21e-9) or (31e-9 <= t0 < 41e-9) or
		(51e-9 <= t0 < 61e-9) or (71e-9 <= t0 < 81e-9) or
		(91e-9 <= t0 < 101e-9)):
	
		i = 0.0
		
	elif ((1e-9 <= t0 < 11e-9) or (21e-9 <= t0 < 31e-9) or
		(41e-9 <= t0 < 51e-9) or (61e-9 <= t0 < 71e-9) or
		(81e-9 <= t0 < 91e-9)):

		i = 0.1e-3

	else:
		i = m*t0

	Vin = i*Rg

	IdekvA = Is*((np.log10(1 + (np.exp((k*(Vgb - Vth))/2*Vt))))**2)
	IdekvB = Is*((np.log10(1 + (np.exp((k*((Vgb - Vth) - Vdb))/2*Vt))))**2)

	IdEKV = IdekvA - IdekvB

	dV1dt = -((1/(Rg*C1))*V1) + (Vin/(Rg*C1))
	dV2dt = -(IdEKV/C2) - ((1/(Rl*C2))*V2) + (Vdd/(Rl*C2))

	dV1dV2dt = [dV1dt, dV2dt]

	return dV1dV2dt


	

##################################################################
# 					PROJECT 5: RLC CIRCUIT				         #
##################################################################

'''@param: InitialVal is a list of all the dependent variables
		   to be passed to the ode eqn
   @param: t0 is the time
   @return: vector for the slopes of V1, V2 and iL
'''
def rlcParallel(initialVal, t0):
	V1 = initialVal[0]
	V2 = initialVal[1]
	iL = initialVal[2]
	m = (0.1e-3)/(1e-9)
	R1 = R2 =  10.0e3
	C1 = C2 = 1e-12
	L1 =  1e-6


	
	if t0 < 1e-9:
		i = 0.1e-3

	else:
		i = 0	



	dV1dt = (V2/R1*C1) - (V1/R1*C1) - iL/C1 + i/C1
	dV2dt = (V1/R1*C2) - (V2/R2*C2) - (V2/R1*C2)
	diLdt = V1/L1

	slope = [dV1dt, dV2dt, diLdt]

	return slope


##################################################################
# 				 PROJECT 5: BRIDGE RECTIFIER				     #
##################################################################

'''@Param: V is the voltage across the diode
   @return: returns the current through the diode
'''
def diodeCurrent(V):
	Io= 5e-6
	k = 1.38e-23
	e = 1.602e-19
	temp = 298.15 #Room temperature in degree kelvin

	Id = Io * (np.exp((e*V)/(k*temp))  -  1)

	return Id



'''@param: InitialVal is a list of all the dependent variables
		   to be passed to the ode eqn
   @param: t0 is the time
   @return: vector for the slopes of V1 - V5
'''
def bridgeRectifier(initialVal, t0):
	V1 = initialVal[0]
	V2 = initialVal[1]
	V3 = initialVal[2]
	V4 = initialVal[3]
	V5 = initialVal[4]

	C1 = C2 = C3 = C4 = C5 = C6 = C7 = C8 = 1e-12
	R1 = R2 =  10.0e3

	id1 = diodeCurrent(V1)
	id2 = diodeCurrent(V2)
	id3 = diodeCurrent(V3)
	id4 = diodeCurrent(V4)
	id5 = diodeCurrent(V5)

	if t0 < 1e-9:
		i = 0.1e-3

	else:
		i = 0	


	dV1dt = (i/C1) - (V1/(R1*C1)) - (id1/C1) + (id3/C1)
	dV2dt = (id2 + id1 - id5)/ (C2 + C5 + C6)
	dV3dt = (-id3 -id4)/C3
	dV4dt = (id4 - id2)/C4
	dV5dt = (id5/(C7 + C8)) - (V5/(R2*(C7 + C8)))

	slope = [dV1dt, dV2dt, dV3dt, dV4dt, dV5dt]

	return slope


##################################################################
# 				     PROJECT 5: PUMP CIRCUIT				     #
##################################################################



'''@param: InitialVal is a list of all the dependent variables
		   to be passed to the ode eqn
   @param: t0 is the time
   @return: vector for the slopes of V1 - V3
'''
def pumpCircuit(initialVal, t0):
	V1 = initialVal[0]
	V2 = initialVal[1]
	V3 = initialVal[2]

	#V1 = Vgb = initialVal[0]
	#V2 = Vdb = initialVal[1]

	R1 = 1.0e3
	C1 = C2 = 5e-12
	C3 = C4 = 1e-12

	Is = 5e-6
	k = 0.9
	Vth = 0.3
	Io = 0.5e-3
	f = 50e6
	Vt = 26e-3

	i = Io * np.sin(2*3.142*f*t0)

	In1A = Is*((np.log10(1 + (np.exp((k*(V2 - Vth))/2*Vt))))**2)
	In1B = Is*((np.log10(1 + (np.exp((k*((V2 - Vth) - V2))/2*Vt))))**2)

	In1 = In1A - In1B


	In2A = Is*((np.log10(1 + (np.exp((k*((V2 - V3) - Vth))/2*Vt))))**2)
	In2B = Is*((np.log10(1 + (np.exp((k*((V2 -V3) - Vth) - (V2 - V3))/2*Vt))))**2)

	In2 = In2A - In2B

	matInv = (la.inv(np.array([[(C1 + C2), -C2], [C2, -(C2 + C3)]])))
	vec = [(i - V1/R1), (In2 - In1)]

	[dV1dt, dV2dt] = np.dot(matInv, vec)

	dV3dt = In2/C4

	slope = [dV1dt, dV2dt, dV3dt]


	return slope















#################################################################
# 			      ODE METHOD: FORWARD EULER				        #
#################################################################

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




#################################################################
# 			      ODE METHOD: TRAPEZOIDAL EULER				    #
#################################################################

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





#################################################################
# 			      ODE METHOD: BACKWARD EULER				    #
#################################################################


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




#################################################################
# 			           ODE METHOD: RK4				            #
#################################################################

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
	tk3 = t0 + (3*h)/4
	tk4 = t0 + h


	#if there is only one dependent variable
	if not isinstance(xParaInitial, list):
		xK1 = xParaInitial
		k1 = xEqn(xParaInitial, t0)

	 	xK2 = xK1 + ((k1*h)/2)
		k2 = xEqn(xK2, tk2)
	
		xK3 = xK1 + ((3*k2*h)/4)
		k3 = xEqn(xK3, tk3)

		
		xK4 = xK1 + ((2*k1 + 3*k2 + 4*k3)*h)/9
		k4 = xEqn(xK4, tk4)	

		Err = ((-5*k1 + 6*k2 + 8*k3 - 9*k4)*h)/72

		realSlope = (7*k1 + 6*k2 + 8*k3 + 3*k4)/24	


	#More than one dependent variable
	else:
		
		k1List = xEqn(xParaInitial, t0)
		k1Mod = list(map(lambda x: ((x*h)/2), k1List))
		
		xParaK2 = map(add, xParaInitial, k1Mod)
		k2List = xEqn(xParaK2, tk2)
		k2Mod = list(map(lambda x: ((3*x*h)/4), k2List))

		xParaK3 = map(add, xParaInitial, k2Mod)
		k3List = xEqn(xParaK3, tk3)
		k3Mod = list(map(lambda x: (x*h), k3List))


		xk1k4 = list(map(lambda x: (2*x*h)/9, k1List))
		xk2k4 = list(map(lambda x: (3*x*h)/9, k2List))
		xk3k4 = list(map(lambda x: (4*x*h)/9, k3List))

		sumX1 = map(add, xk1k4, xk2k4)
		xParaK4 = map(add, sumX1, xk3k4)
		k4List = xEqn(xParaK4, tk4)


		#Caluculating slope using the k values
		k1Slope = list(map(lambda x: ((x*7)/24), k1List))
		k2Slope = list(map(lambda x: ((x*6)/24), k2List))
		k3Slope = list(map(lambda x: ((x*8)/24), k3List))
		k4Slope = list(map(lambda x: ((x*3/24)), k4List))

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


	#Checks if time adaptation is required
	if not adaptBit:	
		return realSlope

	else:
		return [realSlope, Err]		


#################################################################
# 			       		ODE SOLVER			                    #
#################################################################

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

	
	timeList = np.arange(t0, (timeStop), h)


	for time in range(int(t0), len(timeList)):
		t0 = timeList[time]
		
		#If time adaptation is not enabled
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
		
		#Time Adaptation enabled
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
				
			Err = (la.norm(E))/(la.norm(xParaInitial))

			if Err > tol1:
					
				h = h/2
				
			elif Err < tol2:
					
				h = 2*h

			elif tol2 <Err < tol1:
				h = h		

				
		


	return finalValues










