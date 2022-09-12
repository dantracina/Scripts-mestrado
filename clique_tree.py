import networkx as nx


f_v = []

def create_graph_with_n_vertices(n):
    """Esta função cria um grafo com 1 a n vértices com nenhuma aresta"""
    G = nx.Graph()
    vertices = list(range(1,n+1))
    G.add_nodes_from(vertices)
    return(G)


def link_all_vertices(G, list_vertices):
    """Função cria uma clique no grafo G com os vértices da lista list_vertices"""
    length = len(list_vertices)
    edges = []
    
    for x in range(0,length-1):
        for y in range(x+1,length):
            edges.append((list_vertices[x],list_vertices[y]))

    G.add_edges_from(edges)

    return(G)

def link_all_vertices_pesos(G, list_vertices):
    """Função cria uma clique no grafo G com os vértices da lista list_vertices"""
    length = len(list_vertices)
    
    for x in range(0,length-1):
        for y in range(x+1,length):
        	frase = "Peso da aresta (" + str(list_vertices[x]) + ", " + str(list_vertices[y]) + "):"
        	print(frase, end = ' ')
        	peso = float(input())
        	G.add_edge(list_vertices[x],list_vertices[y], weight = peso)


    return(G)
    
def fiedler_vector(G, nome):
    """Grava no arquivo nome uma lista organizada com a entrada do vetor de Fiedler indexada pelo label do vértice"""
    arquivo = open(nome,"w")

    f_v = nx.fiedler_vector(G, tol = 1e-05)
    
    vert_caracteristicos = []
    
    arquivo.write("ASSOCIAÇÕES DO VETOR DE FIEDLER\n\n\n")
    for x in range(1,len(f_v)+1):
        frase = str(x) + "  :  %.2f" % f_v[x-1] + "\n"
        arquivo.write(frase)
        
     #   if(f_v[x-1] < 0.00000001):
     #   	vert_caracteristicos.append(x)
        	
        	    		
    #arquivo.write("\n################ VÉRTICES CARACTERÍSTICOS ################ \n\n")
    #
    #for x in range(0, len(vert_caracteristicos)):     
	#arquivo.write(str(vert_caracteristicos[x]) + "; ")    
    arquivo.close()
        
def fiedler_vector_pesos(G, nome):
    """Grava no arquivo nome uma lista organizada com a entrada do vetor de Fiedler indexada pelo label do vértice"""
    arquivo = open(nome,"w")

    f_v = nx.fiedler_vector(G, weight = 'weight', tol = 1e-10)
    
    
    arquivo.write("ASSOCIAÇÕES DO VETOR DE FIEDLER\n\n\n")
    for x in range(1,len(f_v)+1):
        frase = str(x) + "  :  " + str(f_v[x-1]) + "\n"
        arquivo.write(frase)
        
    arquivo.close()

