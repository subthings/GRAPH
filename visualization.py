import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
import datetime
from cyclic import is_cyclic
import csv

G = nx.MultiDiGraph()
which = ''
def visualize(G, name):
    """
    basename = name
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix]).dot
"""
    nx.draw_networkx(G, nodecolor='light blue', edge_color='grey')

    #write_dot(G, 'Cyclic.dot')
    #plt.savefig("CycleGraph.png")  # Saved image graph
    write_dot(G, name +'.dot')
    plt.savefig(name + '.png')  # Saved image graph

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
#    file.write(str(max(list(GU.degree(GU.nodes())))))

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

def nc(G):
    GU = G.to_undirected()
    components = nx.number_connected_components(GU)
    return components

def diameter(G):
    if nc(G) == 1:
        GU = G.to_undirected()
        return nx.diameter(GU)
    else: return 'infinite'

def average_path(G):
    if nc(G) == 1:
        GU = G.to_undirected()
        return nx.average_shortest_path_length(GU)
    else: return 'infinite'

def csv_writer(func):
    """Decorator which is writing data in csv file"""
    import csv
    def wrapper():

        with open('data.csv', 'a') as file:
            writer = csv.writer(file)


    return wrapper


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        with open('speed.txt', 'a') as file:
            file.write(func.__name__)
            file.write(' ')
            file.write(str(time.clock() - t))
            file.write('\n')
            file.close()
        return res
    return wrapper



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

