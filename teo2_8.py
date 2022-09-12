import networkx as nx
import numpy.linalg



################### FUNÇÕES ########################################################
def create_graph_with_n_vertices(n):
    """Esta função cria um grafo com 1 a n vértices com nenhuma aresta"""
    A = nx.Graph()
    vertices = list(range(1,n+1))
    A.add_nodes_from(vertices)
    return(A)
    
################### ALGORITMO "ZERA ARTICULAÇÃO" ###################################

# Passo 1
num_vert = 7
G = create_graph_with_n_vertices(num_vert)

# Passo 2
arestas_restantes = [[2,3],[3,4],[6,7]]
k = 5
# Passo 3
alfa = float(input("alfa: "))
gama = 1

for x in range(1,num_vert):
	for y in range(x+1,num_vert+1):
		e = [x,y]
		if(e in arestas_restantes):
			G.add_edge(x, y, weight = alfa)
		else:
			G.add_edge(x, y, weight = gama)        

# Passo 4
C1 = G.subgraph([1,2])
C2 = G.subgraph([4,5,6,7])

L1 = nx.normalized_laplacian_matrix(C1)
L2 = nx.normalized_laplacian_matrix(C2)

espectro_L1 = numpy.linalg.eigvals(L1.A)
espectro_L2 = numpy.linalg.eigvals(L2.A)

min_C1 = min(espectro_L1)
min_C2 = min(espectro_L2)

# Passo 5
if(min_C1 <= min_C2):
	B2 = C2
	beta = min_C1/min_C2
else:
	B2 = C1
	beta = min_C2/min_C1
	
# Passo 6
lista_vert = list(B2.nodes)
lista_vert.append(k)

subgrafo = G.subgraph(lista_vert)
lista_arestas = list(subgrafo.edges)

length = len(lista_vert)

for x in range(0,length-1):
	for y in range(x+1,length):
		e = (lista_vert[x], lista_vert[y])
		
		if(subgrafo.has_edge(e[0],e[1])):
			G[e[0]][e[1]]['weight'] *= beta

# Passo 7
a_G = nx.algebraic_connectivity(G, weight = 'weight')	

#Passo 8
if(num_vert * alfa < a_G):
	# Passo 9
	f_v = nx.fiedler_vector(G, weight = 'weight', tol = 1e-5)
    
	print("\n\nASSOCIAÇÕES DO VETOR DE FIEDLER\n\n")
	for x in range(1,len(f_v)+1):
		frase = str(x) + "  :  " + str(f_v[x-1])
		print(frase)		
else:
	print("Diminua o alfa.")

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	