import math

def x3(x, a=1, b=0, c=0, q=0):
	#y = ax^3 + bx^2 + cx + q
	return a*x**3 + b*x**2 + c*x + q

def exponential(x, a=math.e, b=1, c=1, q=0):
	#y = c*a^bx + q
	return c*(a**(b*x)) + q

def logarithm(x, a=math.e, b=0, c=1, q=0):
	#y = c*log(x + b, a) + q
	result=[]
	if type(x) not in (int, float):
		for x0 in x:
			result.append(c*math.log(x0 + b, a) + q)
		return result
	return c*math.log(x + b, a) + q

def sin(x, a=1, b=0, q=0,c=0):
	#y = a *sin(x + b) + c
	result=[]
	if type(x) not in (int, float):
		for x0 in x:
			result.append(a * math.sin(x0 + b) + q)
		return result
	return a * math.sin(x + b) + q

def cosin(x, a=1, b=0, q=0, c=0):
	#y = a *sin(x + b) + c
	result=[]
	if type(x) not in (int, float):
		for x0 in x:
			result.append(a * math.cos(x0 + b) + q)
		return result
	return a * math.cos(x + b) + q

