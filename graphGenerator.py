import networkx as nx
from visualization import visualize
from visualization import write_in_file
from cyclic import is_cyclic
from visualization import benchmark

@benchmark
def graph_generator():
    """
    in_degrees = nx.utils.powerlaw_sequence(100, 2.1) #100 nodes, power-law exponent 2.5
    out_degrees = nx.utils.powerlaw_sequence(100, 2.1)

    GIN = nx.expected_degree_graph(in_degrees, selfloops=False)
    GOUT = nx.expected_degree_graph(out_degrees, selfloops=False)

    GD = nx.DiGraph()
    GD.add_weighted_edges_from(GIN.edges(data=True))
    GD.add_weighted_edges_from(GOUT.edges(data=True))

    GD.remove_edges_from(GD.selfloop_edges())

    """
    DG = nx.scale_free_graph(50, alpha=0.41, beta=0.54, gamma=0.05, delta_in=0.2, delta_out=0, create_using=None, seed=None)

    """Make graph weighted"""

    """
    GC = nx.Graph()
    for u, v, data in G.edges(data=True):
        w = data['weight'] if 'weight' in data else 1.0
        if GC.has_edge(u, v):
            GC[u][v]['weight'] += w
        else:
            GC.add_edge(u, v, weight=w)
    """



    """
    diExpect = GC.edges(data=True)
    GD = nx.DiGraph()
    GD.add_weighted_edges_from(diExpect)
    """

    """
    #Convert to directed
    GD = GC.to_directed()
    """


    """
    s = nx.utils.powerlaw_sequence(100, 2.5)
    l = nx.utils.powerlaw_sequence(100, 2.5)
    G = nx.directed_havel_hakimi_graph(s, l)
    """


    #visualize(DG, 'Cyclic')

    #write_in_file(DG, 'Cyclic graph')


    #print(type(G))
    #print(G.nodes(data=True))
    #print(G.nodes())
    #print(DG.edges(data=True))
    #print(type(DG.edges()))
    #print(nx.to_numpy_matrix(GC))
    #print(G.adj[1][2])
    #print('..............')



    #print(nx.info(GD))

    #print(DG.edges())
    #print(DG.size())
    """
    if not list(nx.simple_cycles(GD)):
        print("GD is acyclic")
    else:
        print("GD has cycles")
    """
    return DG