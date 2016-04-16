import fileinput
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pylab as pl

x = [] 
y = []

with open('../data/houseData') as f:
	for line in f.readlines():
		lineData = line.split()
		x.append(float(lineData[1]))
		y.append(float(lineData[0])/10000)

x = np.array(x)
y = np.array(y)

def func(x, r):
	return r[0] + r[1] * x 

def residuals(p):
	c0, c1 = p
	return y - (c0 + c1 * x)	

r = leastsq(residuals, [0, 0])	
print(r[0])

pl.plot(x, y, 'o', label=u"真实数据")
pl.plot(x, func(x, r[0]),  label=u"拟合数据")
pl.xlabel('面积(平方米)')
pl.ylabel('成交价(万元)')
pl.legend()
pl.show()