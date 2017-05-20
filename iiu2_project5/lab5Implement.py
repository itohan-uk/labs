import lab5Library as l5
import matplotlib.pyplot as plt
import numpy as np
import time

def plotter(timeList, v1List, v2List, title):
	fig = plt.figure(title)
	plt.xlabel("time")
	plt.ylabel("voltage")

	plt.plot(timeList, v1List, label = 'V1(t)')
	plt.plot(timeList, v2List, label = 'V2(t)')

	plt.legend()
	#plt.ion()
	plt.show()
	#plt.draw()
	#plt.pause(0.001)



#ode = raw_input("Please enter the ode method you want to use: \n")

odeMethod = l5.rk4
#stringOdeMethod = "l5.%s" %ode
#exec("%s = %d" % (x,2))
#odeMethod = eval(stringOdeMethod)
xEqn = l5.pumpCircuit
xParaInitial = [0, 0, 0]
t0 = 0
h = 1e-10
tol1 = 1e-1
tol2 = 1e-3
adaptBit = 0
timeStop = 100e-9


xList = l5.odeSolver(odeMethod, xEqn, xParaInitial, t0, h, tol1, tol2 ,
 adaptBit , timeStop)

print xList
v1List = []
v2List = []
v3List = []
v4List = []
v5List = []


timeList1 = np.arange(0.0,timeStop,h)


for val in xList:
	v1List.append(val[0])
	v2List.append(val[1])
	v3List.append(val[2])
	#v4List.append(val[1])
	#v5List.append(val[2])


# plotter(timeList1, v1List, v2List, "uuu")
#print v1List
#print 'kkkkk'
#print v2List
#print 'ttttt'
#print iLList 