"""

The algorithm from
"APPROXIMATIONS FOR THE MAXIMUM ACYCLIC SUBGRAPH
PROBLEM"
Refael Hassin and Shlomi Rubinstein
1994
Algorithm 2.1
"""
import networkx as nx
#from graphGenerator import graph_generator
from visualization import write_in_file
from cyclic import is_cyclic
from visualization import benchmark
G = nx.MultiDiGraph()

@benchmark
def algorithm2(G):

    S = list(G.nodes())
    l = 1
    u = G.number_of_nodes()
    pi = []

    #while l!=n:
    for i in S[:]:
        w_out = 0
        w_in = 0
        S.remove(i)
        for j in S:
            if (j, u) in G.edges():
                w_out += 1

        for j in S:
            if (j, i) in G.edges():
               w_in += 1

        if w_in <= w_out:
            pi.append((i, l))
            l += 1
        else:
            pi.append((i, u))
            u -= 1



    remove = []
    for u in G.edges():
        a = u[0]
        b = u[1]
        a_pi = -1
        b_pi = -1
        for c in pi:
            if c[0] == a:
                a_pi = c[1]

            if c[0] == b:
                b_pi = c[1]

        if a_pi >= b_pi:
            remove.append(u)

    G.remove_edges_from(remove)

    return G