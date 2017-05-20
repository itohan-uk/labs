###############################
#   ITOHAN UKPONMWAN (iiu2)   #
#		   ECE 4960			  #
#	LAB 4 Implementation	  #
###############################

import lab4Library as l4
import matplotlib.pyplot as plt
import numpy as np
import time


startTime = time.time()

##################################################################
# 				   FUNCTION TO PLOT GRAPHS				         #
##################################################################

'''Function to plot V1 and V2 against time
   @param: timeList- List of time values
   @param: v1List - List of voltage1 values
   @param: v2List - List of voltage2 values
   @param: title of grap
'''

def plotter(timeList, v1List, v2List, title):
	plt.figure(title)
	plt.xlabel("time")
	plt.ylabel("voltage")

	plt.plot(timeList, v1List, label = 'V1(t)')
	plt.plot(timeList, v2List, label = 'V2(t)')

	plt.legend()
	plt.show()


##################### TASK 1 BEGINS #############################
xReal = [2.0, 6.1946, 14.843, 33.677, 75.339]

def errorCalc(xReal, xFinal):
	
	diffList = (np.array(xReal) - np.array(xFinal))/np.array(xReal)
	errList = list(map(lambda x:abs(x*100), diffList))

	return errList




##################################################################
# 				TASK 1: ODE METHOD: FORWARD EULER				 #
##################################################################
odeMethod = l4.fEuler
xEqn = l4.xVal
xParaInitial = 2.0
t0 = 0
h = 1.0
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 5


xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)

errList = errorCalc(xReal, xList)

print "############ FORWARD EULER ##############"
print "xVals: {}" .format(xList)
print "error: {}" .format(errList)

print "\n"

##################################################################
# 				TASK 1: ODE METHOD: BACKWARD EULER				 #
##################################################################
odeMethod = l4.bEuler
xEqn = l4.xVal
xParaInitial = 2.0
t0 = 0
h = 1.0
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 5


xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)
errList = errorCalc(xReal, xList)

print "############ BACKWARD EULER ##############"
print "xVals: {}" .format(xList)
print "error: {}" .format(errList)

print "\n"


##################################################################
# 				TASK 1: ODE METHOD: TRAPEZOIDAL EULER		     #
##################################################################
odeMethod = l4.tEuler
xEqn = l4.xVal
xParaInitial = 2.0
t0 = 0
h = 1.0
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 5


xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)
errList = errorCalc(xReal, xList)

print "############ TRAPEZOIDAL EULER ##############"
print "xVals: {}" .format(xList)
print "error: {}" .format(errList)

print "\n"


##################################################################
# 				TASK 1: ODE METHOD: RK4 - NO ADAPTATION		     #
##################################################################

odeMethod = l4.rk4
xEqn = l4.xVal
xParaInitial = 2.0
t0 = 0
h = 1.0
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 5


xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)
errList = errorCalc(xReal, xList)

print "############ RK4 - NO ADAPTATION ##############"
print "xVals: {}" .format(xList)
print "error: {}" .format(errList)

print "\n"


##################################################################
# 			TASK 1: ODE METHOD: RK4 - WITH ADAPTATION		     #
##################################################################
odeMethod = l4.rk4
xEqn = l4.xVal
xParaInitial = 2.0
t0 = 0
h = 1.0
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 1
timeStop = 5


xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)

errList = errorCalc(xReal, xList)

print "############ RK4 - WTIH ADAPTATION ##############"
print "xVals: {}" .format(xList)
print "error: {}" .format(errList)

print "\n"

##################### TASK 1 ENDS #############################



####################### TASK 4 BEGINS #############################

##################################################################
# 				TASK 4: ODE METHOD: FORWARD EULER h = 1.0		 #
##################################################################
odeMethod = l4.fEuler
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: Forward Euler"	
# plotter(timeList1, v1List, v2List, title)

##################################################################
# 			TASK 4: ODE METHOD: FORWARD EULER h = 0.2			 #
##################################################################
odeMethod = l4.fEuler
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: Forward Euler h = 0.2ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 				TASK 4: ODE METHOD: BACKWARD EULER				 #
##################################################################
odeMethod = l4.bEuler
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: Backward Euler"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 			TASK 4: ODE METHOD: BACKWARD EULER	h = 0.2ns		#
##################################################################
odeMethod = l4.bEuler
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: Backward Euler h = 0.2ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 				TASK 4: ODE METHOD: TRAPEZOIDAL EULER			 #
##################################################################
odeMethod = l4.tEuler
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: Trapezoidal Euler"	
# plotter(timeList1, v1List, v2List, title)

##################################################################
# 			TASK 4: ODE METHOD: TRAPEZOIDAL EULER h=0.2ns		 #  
##################################################################
odeMethod = l4.tEuler
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: Trapezoidal Euler h= 0.2ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 			TASK 4: ODE METHOD: RK4 NO ADAPTATION h = 1.0 ns     #
##################################################################
odeMethod = l4.rk4
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: RK4 No Adaptation timeStep = 1.0ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 			TASK 4: ODE METHOD: RK4 NO ADAPTATION h = 0.2ns      #
##################################################################
odeMethod = l4.rk4
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 4: RK4 No Adaptation timeStep = 0.2ns"	
# plotter(timeList1, v1List, v2List, title)



##################################################################
# 			TASK 4: ODE METHOD: RK4 WITH ADAPTATION 			 #
##################################################################
odeMethod = l4.rk4
xEqn = l4.circuitOde
xParaInitial = [0,0]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 1
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])

# title = "Task 4: RK4 With Adaptation"	
# plotter(timeList1, v1List, v2List, title)

##################### TASK 4 ENDS #############################




##################### TASK 5 BEGINS #############################

##################################################################
# 				TASK 5: ODE METHOD: FORWARD EULER				 #
##################################################################
odeMethod = l4.fEuler
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: Forward Euler"	
# plotter(timeList1, v1List, v2List, title)



##################################################################
# 			TASK 5: ODE METHOD: FORWARD EULER	h=0.2ns			 #
##################################################################
odeMethod = l4.fEuler
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: Forward Euler h=0.2ns"	
# plotter(timeList1, v1List, v2List, title)



##################################################################
# 				TASK 5: ODE METHOD: BACKWARD EULER				 #
##################################################################
odeMethod = l4.bEuler
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: Backward Euler"	
# plotter(timeList1, v1List, v2List, title)




##################################################################
# 			TASK 5: ODE METHOD: BACKWARD EULER	h=0.2ns			 #
##################################################################
odeMethod = l4.bEuler
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: Backward Euler h=0.2ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 				TASK 5: ODE METHOD: TRAPEZOIDAL EULER			 #
##################################################################
odeMethod = l4.tEuler
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: Trapezoidal Euler"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 			ASK 5: ODE METHOD: TRAPEZOIDAL EULER	h=0.2ns		 #
##################################################################
odeMethod = l4.tEuler
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: Trapezoidal Euler h=0.2ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 			TASK 5: ODE METHOD: RK4 NO ADAPTATION h = 1.0 ns     #
##################################################################
odeMethod = l4.rk4
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 1.0e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


# title = "Task 5: RK4 No Adaptation timeStep = 1.0ns"	
# plotter(timeList1, v1List, v2List, title)


##################################################################
# 			TASK 5: ODE METHOD: RK4 NO ADAPTATION h = 0.2ns      #
##################################################################
odeMethod = l4.rk4
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


#title = "Task 5: RK4 No Adaptation timeStep = 0.2ns"	
#plotter(timeList1, v1List, v2List, title)



##################################################################
# 	     TASK 5: ODE METHOD: RK4 WITH ADAPTATION h = 0.2ns       #
##################################################################
odeMethod = l4.rk4
xEqn = l4.ekvOde
xParaInitial = [2.5, 2.5]
t0 = 0
h = 0.2e-9
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 1
timeStop = 100e-9

xList = l4.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)


v1List = []
v2List = []
timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])


#title = "Task 5: RK4 with Adaptation timeStep = 0.2ns"	
#plotter(timeList1, v1List, v2List, title)


############################## TASK 5 ENDS ##############################

totalTime = time.time() - startTime

print('################### TOTAL TIME ######################\n')
print ('Total Time: %f' %totalTime)









