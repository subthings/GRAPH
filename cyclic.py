import networkx as nx

G = nx.DiGraph
def is_cyclic(G):
    try:
        nx.find_cycle(G, orientation='original')
        return  'Graph is cyclic'
    except:
        return 'No cycles found'
