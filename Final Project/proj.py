# -*- coding: utf-8 -*-
"""
COM530500 Network Science Final Project
"""

import numpy as np
import scipy.io
import networkx as nx


def edge_removal(A,phi):
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

mat = scipy.io.loadmat('facebook-ego.mat')
A = mat['A']  #Adjacency matrix A

G = nx.from_numpy_matrix(np.matrix(A)) #Read graph





