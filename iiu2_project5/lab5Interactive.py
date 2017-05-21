###############################
#   ITOHAN UKPONMWAN (iiu2)   #
#		   ECE 4960			  #
#	        LAB 5             #
###############################


import lab5Library as l5
import matplotlib.pyplot as plt
import numpy as np
import time






#======================== INPUT AN ODE METHOD ============================
ode = raw_input("Please select an ode method\
 you want to use: fEuler, tEuler, bEuler, rk4 \n> ")


if ode == "rk4":
	adaptBit = int(raw_input("Please enter the adaptBit\n> "))
else:
	adaptBit = 0	
stringOdeMethod = "l5.%s" %ode
odeMethod = eval(stringOdeMethod)

circuitNo = raw_input("Please enter a number to choose the circuit you want to \
simulate:\n \
	1: circuitOde\n \
	2: ekvOde\n \
	3: rlcParallel\n \
	4: bridgeRectifier\n \
	5: pumpCircuit\n \
> ")

if circuitNo == '1':
	circuitType = "circuitOde"
	numParameters = 2

elif circuitNo == '2':
	circuitType = "ekvOde"
	numParameters = 2

elif circuitNo == '3':
	circuitType = 'rlcParallel'
	numParameters = 3

elif circuitNo == '4':
	circuitType = "bridgeRectifier"
	numParameters = 5

elif circuitNo == '5':
	circuitType = 'pumpCircuit'	
	numParameters = 3			



stringCircuit = "l5.%s" %circuitType
xEqn = eval(stringCircuit)





#======================== GET THE INITIAL PARAMETERS =========================

initial = raw_input("Please enter %d Initial parameters seperate each one by\
 a space\n" %numParameters) 
initialString = initial.split(' ')
xParaInitial = map(int, initialString)


#======================== GET THE TIME PARAMETERS =============================

timeParameters = raw_input("Please enter the time start, time step and \
 time stop seperated by a space\n> ")	

timeListString = timeParameters.split(' ')
t0 = float(timeListString[0])
h = float(timeListString[1])
timeStop = float(timeListString[2])


#======================== SET THE TOLERANCE VALUES ============================
if adaptBit:
	tolerances = raw_input("Please enter the tolerances seperated by a space\
first value is the higher value and the second value is lower\
suggested Values: tol1: 1e-1, tol2: 1e-3\n> ")

	tolList = tolerances.split(" ")
	tol1 = float(tolList[0])
	tol2 = float(tolList[1])

else:
	tol1 = 1e-1
	tol2 = 1e-3


#=============================== USE THE ODE SOLVER ===========================
timeStart = time.clock()
xList = l5.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)

#Calculate simulation time
simulationTime = time.clock() - timeStart

#============================== DISPLAY OPTIONS ===============================
choiceBit = int(raw_input("Enter a number to select the way results should be\
 displayed\n 1: Display Graph\n 2: Display values\n 3: Display both graph and\
 results\n> "))

resultList = []
for x in range(numParameters):
	idxList = []
	resultList.append(idxList)

for val in xList:
	for x in range(numParameters):
		resultList[x].append(val[x])

if (choiceBit == 1 or choiceBit == 3):
	timeList = np.arange(0.0,timeStop,h)
	print "Please close the graph after viewing to proceed with the program"
	l5.plotter(timeList, numParameters, resultList, circuitType)	


if (choiceBit == 2 or choiceBit == 3):
	for i in range(numParameters):
		print("parameter %d results: %s \n"%(i, map(str, resultList[i])))


print("Total simulation time: %f seconds" %simulationTime)
