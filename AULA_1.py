import numpy
import math

print('--------------------------QUESTAO 1 E 2-----------------')
def erroVerdadeiro(val,x):
	Et= val-x
	return(Et)

def erroRelativo(val,Et):
	et=(Et/val)*100
	return(et)
z= 22/7
y= 355/113
pi= math.pi

Questao1= erroVerdadeiro(val= z, x= pi)
print(abs(Questao1))

Questao2= erroRelativo(val=y, Et= Questao1)
print(abs(Questao2))


print("-----------------------QUESTAO 3----------------------")

def erroRelativo2(val,x):
	solucao_ant= val; solucao_at= x;
	ea= abs((solucao_at-solucao_ant)/solucao_at)*100
	return(ea)

Questao3= erroRelativo2(val= 3.1415 , x= pi)
print(Questao3)


print('--------------------------QUSTAO 4---------------------')

