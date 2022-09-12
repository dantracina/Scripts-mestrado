import math
import numpy as np
import sys


def pontilhado():
	print("-----------------------------------")

def funcao(inteiro):
	return 2*(1-math.cos(math.pi/(2*inteiro+1)))	

def cria_Lista():
	
	lista = list()
	for n in range(2,300):
		lista.append(funcao(n))
	
	return lista
	
def define_limite(n, folhas):
	
	if(n == "impar"):
		return int(k/2)
	else:
		if(folhas%2 == 1):
			return int(k/2)
		else:
			return int(k/2)-1
		
	
def redefine_var_iniciais(n, posicao, folhas, lim_superior):
	n = "ímpar"
	posicao = 2
	limite_superior = define_limite(folhas+1)

def verifica_Limite(n, posicao, folhas, lim_superior):
	if(i > limite_superior):
		if(n != "par"):
			print("Resultado verificado.")
			sys.exit()
					
		redefine_var_iniciais(n, posicao, folhas, lim_superior) 


	
def calc_pol_seq(l, pai = 0, avo = 0):
	if (l == 1):
		return np.array([1])
	if (l == 2):
		return np.array([1, 0])
	
	p0 = np.array([0])
	p1 = np.array([0, 0])
	
	p = np.concatenate((pai,p0), axis = None) 
	p += np.concatenate((p0,pai), axis = None)
	p -= np.concatenate((p1,avo), axis = None)
	
	return p

def aumenta_dimensao(p):
	return np.concatenate((np.array([0]),p), axis = None)
		  
def calc_polinomio(ordem, posicao, folhas):
	
	b = 0
	if(ordem != "par"):
		b = 1
	
	p = np.array(list())
	pai = np.array(list())
	avo = np.array(list())
	q = np.array(list())
	
	#print(folhas+2+b-2*posicao)
	for l in range(1,folhas+2+b-2*posicao):
		p = calc_pol_seq(l,pai,avo)
		
		
		if(l == 1):
			q = p
		else:
			q = aumenta_dimensao(q) + p
			
		if(l == 2):
			avo = np.array([1])
			pai = np.array([1, 0])
		elif(l >= 3):
			avo = pai
			pai = p	
	
	
	p = calc_pol_seq(folhas+2+b-2*posicao,pai,avo)
	
	
	return folhas*p+aumenta_dimensao(q)		
			
def calc_raizes(p):
	l = list()
	
	raizes = np.roots(p)
	
	for elem in raizes:
		if(elem > 0 and elem < 1):
			l.append(1-elem)
	return l

def define_primeiro(ordem):
	if(ordem == "par"):
		return 1
	else:
		return 2		

def verifica_existencia(lista):
	indice = 2
	teste = True
	for elem in lista:
		if(not np.iscomplex(elem)):
			while(elem < funcao(indice)):
				indice +=1
			if(abs(elem - funcao(indice)) < 1e-8 and abs(elem - funcao(indice-1)) < 1e-08):
				pontilhado()
				print(elem)
				print(funcao(indice))
				pontilhado()
				
				teste = False
			indice = 2
	
	return teste
			


n = ["par","impar"]

lista = cria_Lista()


for k in range(4,5):
	print("k = " + str(k) + ":") 
	
	for ordem in n:
		primeiro = define_primeiro(ordem) 
		limite = define_limite(ordem, k)
	
		for i in range(primeiro, limite+1):
			p = calc_polinomio(ordem,i,k)
			print(i)
			print(calc_raizes(p))
			pontilhado()
			if(not verifica_existencia(calc_raizes(p))):
				print("Falhou! para " + str(i))
	
	pontilhado()


pontilhado()
