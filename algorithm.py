"""

The algorithm from
'A FAST & EFFECTIVE HEURISTIC FOR THE FEEDBACK ARC SET PROBLEM'
article
Peter Eades
Xuemin Lin
W. F. Smyth

"""


import networkx as nx
#from graphGenerator import DG as GD
from visualization import write_in_file
from cyclic import is_cyclic
from graphGenerator import graph_generator
from visualization import benchmark
from visualization import nc, diameter
GG = nx.MultiDiGraph()


@benchmark
def algorithm1(GG):
    G = GG.copy()


    S1 = []
    S2 = [] #REVERSED!!!!


    while G.nodes:
        A = list(G.out_degree(G.nodes()))
        B = list(G.in_degree(G.nodes()))

        for u in A:
            if u[1] == 0:
                S2.append(u[0])
                G.remove_node(u[0])
                A.remove(u)
                for i in B:
                    if i[0] == u[0]:
                        B.remove(i)

                #dictionary changed size during iteration

        for u in B:
            if u[1] == 0:
                S1.append(u[0])
                G.remove_node(u[0])
                B.remove(u)
                for i in A:
                    if i[0] == u[0]:
                        A.remove(i)


        delta_max = 0
        node_to_delete = -1

        " May be for non weighted "

        for out_deg in A:
            for in_deg in B:
                if out_deg[0] == in_deg[0]:
                    a = out_deg[0]
                    b = (out_deg[1]-in_deg[1])
                    #                delta.append((a, b))
                    if b >= delta_max:
                        delta_max = b
                        node_to_delete = a


        for u in G.nodes:
            if G.out_degree(u)-G.in_degree(u) > delta_max:
                delta_max = G.out_degree(u)-G.in_degree(u)
                node_to_delete = u


        if node_to_delete != -1:
            S1.append(node_to_delete)
            G.remove_node(node_to_delete)



    S2.reverse()
    S1.extend(S2)

    remove=[]

    for u in GG.edges():
        a = u[0]
        b = u[1]
        if S1.index(a) >= S1.index(b):
            remove.append(u)

    GG.remove_edges_from(remove)

    return GG

