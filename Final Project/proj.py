# -*- coding: utf-8 -*-
"""
COM530500 Network Science Final Project
"""

import numpy as np
import scipy.io
import networkx as nx
import matplotlib.pyplot as plt


def edge_removal(A, phi):
    '''Remove edges by the trick developed by Mollison and Grassberger
    Args:
        A: numpy.ndarray
            Adjacency matrix of the dataset
        phi: float
            prob. of the edge is present

    Returns:
        A_new: numpy.ndarray
            Adjacency matrix after edge removal
    '''
    P = np.triu(np.random.random_sample(A.shape),1)
    Prob = P+P.T
    A_new = ((A * Prob)> 1-phi).astype(int)
    return A_new

def statisticalInfo(G):
    print(nx.info(G))
    print(f'Average clustering coefficient: {nx.algorithms.average_clustering(G)}')
    print(f'Diameter: {nx.algorithms.diameter(G)}')
    deg = G.degree()
    avg_degree = 0
    max_degree, min_degree = -1, 1e6
    for i in range(len(deg)):
        avg_degree += deg[i]
        max_degree = max(max_degree, deg[i])
        min_degree = min(min_degree, deg[i])
    print(f'Average degree: {avg_degree/len(deg)}')
    print(f'  Maximum degree: {max_degree}')
    print(f'  Minimum degree: {min_degree}')
    print(f'Density: {nx.classes.density(G)}')

if __name__ == "__main__":
    mat = scipy.io.loadmat('./facebook-ego.mat')
    A = mat['A']  #Adjacency matrix A
    A = np.matrix(A)
    G = nx.from_numpy_matrix(A) #Read graph

    # Problem 1.
    # statisticalInfo(G)
    # nx.draw(G)
    # plt.savefig("visualize.png")


    # Problem 2.
    for i in range(100):
        pass
