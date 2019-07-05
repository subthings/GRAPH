from algorithm import algorithm1
from algorithm2 import algorithm2
from algorithm3 import algorithm3
from algorithm4 import algorithm4
from algorithm5 import algorithm5
from graphGenerator import graph_generator
import csv
from visualization import nc, diameter, average_path, visualize
from cyclic import is_cyclic


data = [['Graph is cyclic', 'Graph components', 'Graph nodes', 'Graph edges', 'Graph diameter',
         'Graph average distance',

         'Algorithm1 is cyclic', 'Algorithm1 components', 'Algorithm1 nodes', 'Algorithm1 edges',
         'Algorithm1 diameter', 'Algorithm1 average distance', 'Algorithm1 time',

         'Algorithm2 is cyclic', 'Algorithm2 components', 'Algorithm2 nodes', 'Algorithm2 edges',
         'Algorithm2 diameter', 'Algorithm2 average distance', 'Algorithm2 time',

         'Algorithm3 is cyclic', 'Algorithm3 components', 'Algorithm3 nodes', 'Algorithm3 edges',
         'Algorithm3 diameter', 'Algorithm3 average distance', 'Algorithm3 time',

         'Algorithm4 is cyclic', 'Algorithm4 components', 'Algorithm4 nodes', 'Algorithm4 edges',
         'Algorithm4 diameter', 'Algorithm4 average distance', 'Algorithm4 time'

         'Algorithm5 is cyclic', 'Algorithm5 components', 'Algorithm5 nodes', 'Algorithm5 edges',
         'Algorithm5 diameter', 'Algorithm5 average distance', 'Algorithm5 time'
         ]]

for i in range(1):

    G0 = graph_generator()
    edges0 = G0.number_of_edges()
    G1 = G0.copy()
    G2 = G0.copy()
    G33 = G0.copy()
    G44 = G0.copy()
    G55 = G0.copy()

    algorithm1(G1)
    algorithm2(G2)
    G3 = algorithm3(G33)
    G4 = algorithm4(G44)
    G5 = algorithm5(G55)


    data.append([is_cyclic(G0), nc(G0), G0.number_of_nodes(), G0.number_of_edges(), diameter(G0), average_path(G0),
                 is_cyclic(G1), nc(G1), G1.number_of_nodes(), G1.number_of_edges(), diameter(G1), average_path(G1),'sth',
                 is_cyclic(G2), nc(G2), G2.number_of_nodes(), G2.number_of_edges(), diameter(G2), average_path(G2),'sth',
                 is_cyclic(G3), nc(G3), G3.number_of_nodes(), G3.number_of_edges(), diameter(G3), average_path(G3),'sth',
                 is_cyclic(G4), nc(G4), G4.number_of_nodes(), G4.number_of_edges(), diameter(G4), average_path(G4),'sth',
                 is_cyclic(G5), nc(G5), G5.number_of_nodes(), G5.number_of_edges(), diameter(G5), average_path(G5),'sth'])


    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        for d in data:
            writer.writerow(d)

    data.clear()

    visualize(G0, 'cyclic')
    visualize(G1, 'alg1')
    visualize(G2, 'alg2')
    visualize(G3, 'alg3')
    visualize(G4, 'alg4')
    visualize(G5, 'alg5')

"""

data = [['Graph components', 'Graph nodes', 'Graph edges', 'Graph diameter',
         'Graph average distance',

         'Algorithm1 components', 'Algorithm1 nodes', 'Algorithm1 edges',
         'Algorithm1 diameter', 'Algorithm1 average distance', 'Algorithm1 time',

         'Algorithm5 components', 'Algorithm5 nodes', 'Algorithm5 edges',
         'Algorithm5 diameter', 'Algorithm5 average distance', 'Algorithm5 time'
         ]]

for i in range(30):

    G0 = graph_generator()
    G1 = G0.copy()
    G55 = G0.copy()

    algorithm1(G1)
    G5 = algorithm5(G55)


    data.append([nc(G0), G0.number_of_nodes(), G0.number_of_edges(), diameter(G0), average_path(G0),
                 nc(G1), G1.number_of_nodes(), G1.number_of_edges(), diameter(G1), average_path(G1),'sth',
                 nc(G5), G5.number_of_nodes(), G5.number_of_edges(), diameter(G5), average_path(G5),'sth'])


    with open('dataBIG.csv', 'a') as file:
        writer = csv.writer(file)
        for d in data:
            writer.writerow(d)

    data.clear()
"""