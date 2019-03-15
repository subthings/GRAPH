import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
import datetime
from cyclic import is_cyclic

G = nx.DiGraph
which = ''
def visualize(G, name):
    """
    basename = name
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix]).dot
"""
    nx.draw_circular(G, nodecolor='light blue', edge_color='grey')
    write_dot(G, 'Cyclic.dot')
    plt.savefig("CycleGraph.png")  # Saved image graph
    plt.show()


def write_in_file(G, which):
    file = open('data.txt', 'a+')
    file.write( which + '\n')
    file.write(nx.info(G)+ '\n')
    """if is_cyclic(G):
        file.write('Cyclic graph')
    else:
        file.write('Acyclic graph')
"""
    file.write(str(is_cyclic(G)))
    file.write('\n')
    file.write('Number of connected components: ')
    GU = G.to_undirected()
    file.write(str(nx.number_connected_components(GU)))
    file.write(str(max(list(GU.degree(GU.nodes())))))

    file.write('\n\n')

    file.close()
    """f = open('datas.txt', 'a+')
    f.write(str(nx.number_connected_components(GU)))

    f.write('\n\n')

    f.close()
"""

def simple_write_in_file(G):
    file = open('datas.txt', 'a+')
    GU = G.to_undirected()
    file.write(str(nx.number_connected_components(GU)))

    file.write('\n\n')

    file.close()


"""
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
"""
#write graph in file
"""
k = DG.edges(data=True)
f = open('CycleGraph.txt', 'w')
f.write(k)
f.close()

"""