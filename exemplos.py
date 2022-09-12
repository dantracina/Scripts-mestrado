import clique_tree as ct


################### Example 1A ###################################
G = ct. create_graph_with_n_vertices(19)


G = ct.link_all_vertices(G,[1,2,3,4])
G = ct.link_all_vertices(G,[4,5,6,19])
G = ct.link_all_vertices(G,[19,18,17,16])
G = ct.link_all_vertices(G,[16,15,14,13])
G = ct.link_all_vertices(G,[19,12,11,10])
G = ct.link_all_vertices(G,[10,9,8,7])


ct.fiedler_vector(G,"Ex_fiedler_1.txt")



