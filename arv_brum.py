import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os
from math import ceil  



def create_brum(n_vert, k_folhas):
	""" Esta função cria uma árvore brum, cuja quantidade de folhas 
	    pendentes da estrela é k_folhas e o número de vértices é n_vert"""
	   
	G = nx.Graph()
	estrela = nx.star_graph(k_folhas) # cria um grafo estrela com k folhas, ou seja, uma estrela com k+1 vértices
	caminho = nx.path_graph(n_vert-k_folhas) # cria um grafo caminho com n-k vértices
	G = nx.disjoint_union(estrela,caminho)  # cria o grafo desconexo G que é a união da estrela e caminho
	G = nx.algorithms.minors.contracted_nodes(G,k_folhas+1,0) # faz com que o nó central da estrela seja coincidente com o vertice pendente do caminho
 
	return G


def find_charac_vertices_brum(G, n_vert, k_folhas):
	""" Esta função encontra os vértices característicos da brum, através dos valores de Perron
	    dos ramos resultantes da remoção iterativa do segundo vértice do caminho até o vértice do meio.
	    Além disso, retorna também o nó limite, isto é, o último nó possível a ser analisado"""
	    
	laplaciana = nx.laplacian_matrix(G).todense()
	
	limite = ceil((n_vert+k_folhas)/2)+1 # o vértice limite do caminho da brum que será analisado
	
	status_atual = status_anterior = 0 # variáveis utilizadas para encontrar os vertices característicos 
	lista_vert_caracteristicos = [] #lista com os vértice(s) característico(s)
	
	for i in range(k_folhas+2, limite):
		matriz_auxiliar = np.delete(laplaciana,i,0) # deleta a i-ésima linha da laplacina
		matriz_auxiliar = np.delete(matriz_auxiliar,i,1) # aqui é deletada a i-ésima coluna
		
		bottleneck = np.linalg.inv(matriz_auxiliar) # calcula a matriz bottleneck do grafo
		
		bn_star = bottleneck[ : i-1, : i-1] # extrai a submatriz diagonal correspodente a ramo que contém a estrela
		bn_path = bottleneck[i-1 : , i-1 : ] # aqui já extrai a submatriz do ramo que contém o caminho 
		 
		val_perron_star = np.linalg.eigvalsh(bn_star)[-1] # valor de Perron da matriz bn_star
		val_perron_path = np.linalg.eigvalsh(bn_path)[-1] # valor de Perron da matriz bn_path
		
		if(i == k_folhas+2):       #if para a primeira execução
			if(val_perron_path > val_perron_star):
				status_atual = status_anterior = 1
			elif(val_perron_path < val_perron_star):
				status_atual = status_anterior = -1
			else:
				status_atual = status_anterior = 0
		else:                                               
			if(val_perron_path > val_perron_star):
				status_atual = 1
			elif(val_perron_path < val_perron_star):
				status_atual = -1
			else:
				status_atual = 0
		
		if(status_atual == 0): #utiliza o Teorema 2 e a Proposição 2 do trabalho de Kirkland de 96
			lista_vert_caracteristicos.append(i)
			break
		elif(status_atual != status_anterior):
			lista_vert_caracteristicos.append(i)
			lista_vert_caracteristicos.append(i-1)
			break
		
		status_anterior = status_atual # atualiza a variável status_anterior
		
	return lista_vert_caracteristicos, limite



def show_brum(G, lista_vert_caracteristicos, limite, num_vert, k_folhas, endereco = os.getcwd()):
	""" Esta função gera a imagem da brum, destacando informações pertinentes como quantidade de vértices , número de folhas
	    do extremo da estrela, assim como os vértices característicos. Além disso, os vértices característicos são destacados
	    por uma cor diferente"""
	
	
	pos=nx.spring_layout(G) # positions for all nodes, sem interseção de arestas
	
	# cria a lista dos nós da brum que não são característicos e nem o nó limite
	lista_nos_restantes = list(G.node)
	for x in lista_vert_caracteristicos:
		lista_nos_restantes.remove(x)
	lista_nos_restantes.remove(limite)
	
	# configuração dos nós característicos
	nx.draw_networkx_nodes(G,pos,
	                       nodelist = lista_vert_caracteristicos,
	                       node_color='r',
	                       node_size=100,
	                   alpha=0.8)
	
	#configuração do nó limite
	nx.draw_networkx_nodes(G,pos,
	                       nodelist = [limite],
	                       node_color='g',
	                       node_size=100,
	                   alpha=0.8)	
	
	#configuração dos nós restantes do grafo
	nx.draw_networkx_nodes(G,pos,
	                       nodelist = lista_nos_restantes, # inclui os vértices que não são característicos
	                       node_color='b',
	                       node_size=100,
	                   alpha=0.8)

	#configuração das arestas 
	nx.draw_networkx_edges(G,pos,
	      	               edgelist= G.edges,
	      	               alpha=0.1)
	
	#configuração dos rótulos dos vértices
	label = {}
	for i in list(G.node):
		label[i] = i
	
	nx.draw_networkx_labels(G, pos, labels = label, font_size = 7, font_color = 'w')
	
	plt.axis('off')
	figure = plt.gcf() # get current figure
	figure.set_size_inches(12, 8) #  configura tamanho da figura para 12 por 8 polegadas
	
	#Gera titulo da figura
	titulo_fig = 'Brum_n_num1_k_num2'
	titulo_fig = titulo_fig.replace('num1', str(num_vert))
	titulo_fig = titulo_fig.replace('num2', str(k_folhas))
	plt.savefig(os.path.join(endereco,titulo_fig), dpi = 80) # save as png
	plt.clf()
	plt.cla()
	plt.close()
	#plt.show()	


		 
		 
				