import numpy


def f(x):
	funcao= -4 + 8*x - 5 * x**2 + x**3
	return funcao

def bissecao(x_inf,x_sup,it_max,erro_abs):		
	it= 0	
	while (it <= it_max and abs(f(x_inf)*f(x_sup)) > erro_abs):
		it= it+1		
		Xn= (x_inf + x_sup)/2		
		if (f(Xn)*f(x_inf) < 0):
			x_sup= Xn
		else:
			x_inf=Xn
	return(x_inf,it)

result= bissecao(x_inf= 0.5, x_sup= 3, it_max= 1000, erro_abs=10e-10000000000000)

print(result)
