"""
Algorithm 2 BergerShorFAS from
Efficient Computation of feedback arc cet at web-scale

"""

from cyclic import is_cyclic
from graphGenerator import graph_generator
from visualization import benchmark
from visualization import nc, diameter
import networkx as nx
from visualization import benchmark


G = nx.MultiDiGraph()

@benchmark
def algorithm5(G):
    remove = []
    for u, v in G.edges():
        if u == v:
            remove.append((u, v))

    G.remove_edges_from(remove)
    """
    
    print(G.edges())
    GW = nx.DiGraph(G)
    
    G = nx.DiGraph()
    
    adj = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 5), (6, 8), (7, 1), (8, 2), (8, 3)]
    G.add_edges_from(adj)
    """
    GG = G.copy()


    def adjacent(G, u):
        adjacents = []
        for e in G.edges():
            if e[0]==u or e[1]==u:
                adjacents.append((e[0], e[1]))

        return adjacents

    print(G.number_of_edges())
    F = []

    for v in G.nodes():


        if G.in_degree(v) > G.out_degree(v):
            for u in G.successors(v):
                F.append((v, u))

        else:
            for u in G.predecessors(v):
                F.append((u, v))

        remove = adjacent(G, v)
        G.remove_edges_from(remove)

    for u in F:
        while u in GG.edges():
            GG.remove_edge(*u)

    return GG

