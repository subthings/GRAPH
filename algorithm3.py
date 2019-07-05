"""

The algorithm from
"APPROXIMATIONS FOR THE MAXIMUM ACYCLIC SUBGRAPH
PROBLEM"
Refael Hassin and Shlomi Rubinstein
1994
Algorithm 3.1
"""

import random
import networkx as nx
from graphGenerator import graph_generator
from visualization import write_in_file
from cyclic import is_cyclic
from algorithm2 import algorithm2
from visualization import benchmark

G = graph_generator()
@benchmark
def algorithm3(G):
    V1 = []
    V2 = []
    G1 = nx.DiGraph()
    G2 = nx.DiGraph()
    E1 = []
    E2 = []

    for u in G.nodes():
        random.choice([V1, V2]).append(u)

    G1.add_nodes_from(V1)
    G2.add_nodes_from(V2)

    for u in G.edges():
        if u[0] in V1 and u[1] in V1:
            E1.append(u)

        elif (u[0] in V2 and u[1] in V2):
            E2.append(u)


    G1.add_edges_from(E1)
    G2.add_edges_from(E2)


    G1 = algorithm2(G1)
    G2 = algorithm2(G2)

    G_fin1 = nx.DiGraph()
    G_fin2 = nx.DiGraph()

    G_fin1.add_nodes_from(G1)
    G_fin1.add_nodes_from(G2)
    G_fin2.add_nodes_from(G1)
    G_fin2.add_nodes_from(G2)

    G_fin1.add_edges_from(G1.edges)
    G_fin1.add_edges_from(G2.edges)
    G_fin2.add_edges_from(G1.edges)
    G_fin2.add_edges_from(G2.edges)


    for u in G.edges():
        if u[0] in V1 and u[1] in V2:
            G_fin1.add_edge(u[0], u[1])
        elif u[0] in V2 and u[1] in V1:
            G_fin2.add_edge(u[0], u[1])


    if G_fin1.number_of_edges() > G_fin2.number_of_edges():
        return G_fin1

    else:
        return G_fin2
