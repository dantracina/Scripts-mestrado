#!/usr/bin/env python3
import arv_brum 
import gerenciador_arquivos as ger_arquivos

# Chamadas do programa						
op = input('Deseja fazer a simulação (Y/N)? ')

if(op == 'n' or op == 'N'):
	n = int(input('Quantos vértices o grafo terá? '))
	k = int(input('Quantos vértices pendentes terá a estrela? '))		
	
	
	G = arv_brum.create_brum(n, k) # gera a árvore brum
	lista_vert_carac, limite = arv_brum.find_charac_vertices_brum(G, n, k) # Encontra os vértices característicos e o nó limite		
	arv_brum.show_brum(G, lista_vert_carac, limite, n, k) # Exibe a imagem da brum	
else:
	n = int(input('Quantos vértices o caminho terá? '))
	k_max = int(input('Quantas folhas máximas terá a estrela? '))
	
	end_pasta = ger_arquivos.gerencia_pasta_simu_kmax(n,k_max)
	
	for d in range(2,k_max+1):
		G = arv_brum.create_brum(n+d, d)
		lista_vert_carac, limite = arv_brum.find_charac_vertices_brum(G, n+d, d) # Encontra os vértices característicos e o nó limite		
		arv_brum.show_brum(G, lista_vert_carac, limite, n+d, d, endereco = end_pasta) # Exibe a imagem da brum
