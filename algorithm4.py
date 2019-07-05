from cyclic import is_cyclic
from graphGenerator import graph_generator
from visualization import benchmark
from visualization import nc, diameter
import networkx as nx
from visualization import benchmark
from algorithm import algorithm1

G = nx.MultiDiGraph()

def make_weighted(G):
    add = []
    for u in G.edges():
        try:
            k = add.index(u)
            a, b, w = add[k]
            w += 1
            add[k] = (a, b, w)

        except:
            add.append((u[0], u[1], 1))

    G = nx.DiGraph()
    G.add_weighted_edges_from(add)

@benchmark
def algorithm4(G):

    T = nx.MultiDiGraph()

    for u in G.edges():
        if not(u[0] in T.nodes() and u[1] in T.nodes()):
            T.add_edge(u[0], u[1])

    G.remove_edges_from(T.edges())


    for u in G.edges():
        T.add_edge(u[0], u[1])
        if is_cyclic(T) == 'Graph is cyclic':
            T.remove_edge(u[0], u[1])


    return T

if __name__ == '__main__':
    G = graph_generator()
    #G = algorithm4(G)
    print(G.number_of_edges())

    make_weighted(G)
    print(G.number_of_edges())
