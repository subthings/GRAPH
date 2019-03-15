from algorithm import algorithm1
from algorithm2 import algorithm2
from graphGenerator import graph_generator

delta_edges1 = 0
delta_edges2 = 0
j = 0
for i in range(100):
    try:
        G = graph_generator()
        edges0 = G.number_of_edges()
        GG = G.copy()
        algorithm2(G)
        algorithm1(GG)

        delta_edges1 += (edges0 - GG.number_of_edges())
        delta_edges2 += (edges0 - G.number_of_edges())

        j +=1
        print(delta_edges1/j)
        print(delta_edges2/j)


    except:
        print('Did not work :(')

