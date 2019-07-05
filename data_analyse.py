"""
delta_components11 = 0
delta_components22 = 0
j = 0
l0 = 8
l1 = 18
l2 = 28
i = 0
def read_from_file(which):
    with open(which) as file:
        for line in file:
            line = file.readline()
            if i == l0:
                components0 = line
                l0 += 30
                components00 = components0.replace('Number of connected components: ', '')
            elif i == l1:
                components1 = line
                l1 += 30
                components11 = components1.replace('Number of connected components: ', '')
            elif i == l2:
                components2 = line
                l2 += 30
                components22 = components0.replace('Number of connected components: ', '')
                j+=1
                delta_components11 += (components11 - components00)
                delta_components22 += (components22 - components00)

            i +=1

    file.close()


read_from_file('data.txt')
print(delta_components22/j)
print(delta_components11/j)


import csv


with open('speed.txt','r') as file:
    i = 0
    data = []
    for line in file:
        i+=1
        if i == 1 or i == 5 or i == 4 or i==7:
            print('o')

        elif i == 10:
            i=0
            with open('speed.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(data)

            data = []

        else:
            data
            data.append(line)
"""
import networkx as nx
import csv
from visualization import nc, diameter, average_path, visualize
from cyclic import is_cyclic
from algorithm4 import algorithm4
from algorithm import algorithm1
import re
pattern = r'\d+\+'


"""
data = [['Graph is cyclic', 'Graph components', 'Graph nodes', 'Graph edges', 'Graph diameter',
         'Graph average distance',

         'AlgorithmC is cyclic', 'AlgorithmC components', 'AlgorithmC nodes', 'AlgorithmC edges',
         'AlgorithmC diameter', 'AlgorithmC average distance', 'AlgorithmC time',

         'Algorithm1 is cyclic', 'Algorithm1 components', 'Algorithm1 nodes', 'Algorithm1 edges',
         'Algorithm1 diameter', 'Algorithm1 average distance', 'Algorithm1 time',

         'Algorithm4 is cyclic', 'Algorithm4 components', 'Algorithm4 nodes', 'Algorithm4 edges',
         'Algorithm4 diameter', 'Algorithm4 average distance', 'Algorithm4 time'
         ]]
"""
data = []

GC = nx.nx_pydot.read_dot('2018.10.5_18.24.33_Acyclic graph.dot')
G0 = nx.nx_pydot.read_dot('2018.10.5_18.24.33_Source graph.dot')
G4 = algorithm4(G0.copy())
G1 = algorithm1(G0.copy())

"""

for u, v, d in GC.edges(data = True):
    if re.search(pattern, d['label']):
        d['weight'] = d['label'][1:-2]

    else:
        u, v = v, u
        d['weight'] = d['label'][1:-2]
"""


data.append([is_cyclic(G0), nc(G0), G0.number_of_nodes(), G0.number_of_edges(), diameter(G0), average_path(G0),
             is_cyclic(GC), nc(GC), GC.number_of_nodes(), GC.number_of_edges(), diameter(GC), average_path(GC), 'sth',
             is_cyclic(G1), nc(G1), G1.number_of_nodes(), G1.number_of_edges(), diameter(G1), average_path(G1), 'sth',
             is_cyclic(G4), nc(G4), G4.number_of_nodes(), G4.number_of_edges(), diameter(G4), average_path(G4), 'sth',
             ])

with open('datacpp.csv', 'a') as file:
    writer = csv.writer(file)
    for d in data:
        writer.writerow(d)

data.clear()

#visualize(G0, 'cyclic')
#visualize(GC, 'algC')
#visualize(G1, 'alg1')
#visualize(G4, 'alg4')



