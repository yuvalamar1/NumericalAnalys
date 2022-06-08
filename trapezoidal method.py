import math
from sympy import *

def simpson(f,a,b,n):
	h = float((b-a)*1.0/n*1.0)
	print("H---->",h)
	m = int(n/2)
	print("M---->", m)
	s0 = f(a)+f(b)
	print("f(a)+f(b)", s0)
	s1 = 0
	for i in range(1,2*m,2):
			s1=s1+f(a+h*i)
			print("Interin resulet for an odd section = ",s1)
	s2=0
	for i in range(2,2*m,2):
			s2=s2+f(a+h*i)
			print("Interin resulet for an even section = ", s1)
	return h/3*(s0+4*s1+2*s2)

def Trapezoidal(f, a, b, n):
    h = float(b - a)/n
    s = 0.0
    s += f(a)+f(b)
    for i in range(1, n):
        s += sum([2* f(a + i*h)])
    s *= h/2.0
    return s

e=math.e
x = symbols('x')
f=simplify(sin(e**(-2*x)+e**(-2*x))/(2*(x**3)+5*(x**2)-6))
f=lambdify(x,f)
print(simpson(f,-0.5,0.5,20))