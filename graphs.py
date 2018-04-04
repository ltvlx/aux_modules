# %matplotlib Qt5
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def create_positions_2level(array_0, array_1):
    dL = 2 # distance between 2 nodes in same level
    n_0 = len(array_0)
    n_1 = len(array_1)
    
    if (n_0 >= n_1):
        x0_0 = 0.0
        x0_1 = dL * 0.5 * (n_0 - n_1)
        y_1 = dL * 0.5 * n_0
    else:
        x0_0 = dL * 0.5 * (n_1 - n_0)
        x0_1 = 0.0
        y_1 = dL * 0.5 * n_1

    position = {}
    for i in range(0,n_0):
        position[array_0[i]] = (x0_0 + i * dL, 0.0)
    for i in range(0,n_1):
        position[array_1[i]] = (x0_1 + i * dL, y_1)
    return position


def create_edges_from_matrix(input_matrix, array_0, array_1):
    ## input_matrix is non-symmetrical binary matrix (n_0,n_1)
    ## that connects n_0 elements of array_0 with n_1 elements of array_1
    n_0 = len(array_0)
    n_1 = len(array_1)

    #check that input is correct
    assert(input_matrix.shape == (n_0, n_1))
    
    edge = []
    for i in range(0, n_0*n_1):
        #print("i % n_0 = ", i % n_0)
        #print("i // n_0 = ", i // n_0)
        if (input_matrix[i % n_0][i // n_0] == 1):
            edge.append((array_0[i % n_0], array_1[i // n_0]))
    return edge


def draw_2layer_supply_network(input_matrix, array_0, array_1):
    edges = create_edges_from_matrix(input_matrix, array_0, array_1)
    position = create_positions_2level(array_0, array_1)
    labels = create_labels(array_0, array_1)
    
    B = nx.Graph()
    B.add_nodes_from(array_0, level=0)
    B.add_nodes_from(array_1, level=1)
    B.add_edges_from(edges)
    
    nx.draw_networkx_edges(B, position, width=4, alpha=0.7)
    nx.draw_networkx_nodes(B, position, nodelist = array_0, node_color = 'b', node_size=1000, alpha=1)
    nx.draw_networkx_nodes(B, position, nodelist = array_1, node_color = 'r', node_size=1500, alpha=1)
    nx.draw_networkx_labels(B, position, labels, font_size=10)
    
    plt.axis('off')
    plt.show()

    

def create_colors(array_0, array_1):
    color_list = []
    n_0 = len(array_0)
    n_1 = len(array_1)
    for i in range(0, n_0+n_1):
        if i < n_0:
            color_list.append('c')
        else:
            color_list.append('r')
    return color_list
    
    
def create_labels(array_0, array_1):
    labels = {}
    n_0 = len(array_0)
    n_1 = len(array_1)
    for i in range(0, n_0+n_1):
        if i < n_0:
#            labels[i] = "$"+array_0[i]+"$"
            labels[i] = array_0[i]
        else:
            labels[i] = array_1[i - n_0]
    return labels


def create_sizes_from_degree(G):
    degree_dict = nx.degree(G)
    sizes_list = []
    for i in range(0,len(degree_dict)):
        sizes_list.append(400 + 500 * degree_dict[i])
    return sizes_list


    
def degree_distribution(input_graph):
    degrees_list = list(nx.degree(input_graph).values())
    degrees_set = list(set(nx.degree(input_graph).values()))

    probability_list = [0] * len(degrees_set)
    for i in degrees_list:
        probability_list[degrees_set.index(i)] += 1.0 / len(input_graph.nodes())

    plt.plot(degrees_set, probability_list, "b--")
    plt.scatter(degrees_set, probability_list, s=200)
    plt.xlabel('Connectivity $k$', fontsize=18)
    plt.ylabel('Cumulative probability $P(k)$', fontsize=18)
    plt.show()
    return