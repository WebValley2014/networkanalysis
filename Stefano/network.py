from igraph import Graph
import pickle
import numpy as np

def drawNetwork(srcListMatrix=r'C:\pythontmp\numpyArray.pkl')
    """
    read the adjacency matrix and plot, thanks to igraph, 
    the graph of the network

    args:
    *srcListMatrix*
        (str)
        sorce file of the list of matrixs. File '*.pkl' need
        
    """
    infile1 = open(srcListMatrix, 'r+b')
    file1 = pickle.load(infile1)                           # This is LISTADIMATRICI
    infile1.close()
      
