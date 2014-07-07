import igraph
import pickle
import numpy as np
import random

def get_randColor():
    #RETURN A EXADECIMAL RANDOM COLOR ie #ff45e2
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())

def drawNetwork(**kwargs):
    """
    Read the data stored in self.metrics, using column 0 as
    x axis values. Select the columns specified by *valueCol*,
    *minCol*, *maxCol* as Y values and print a png chart.
    
    args:
    *matrix*
        (numpy matrix)
        matrix of adjacency    
    -----------------------
    optional args:
    *nodeColor*
        (color)
        color of the nodes. Defaults to "red".
    *lineColor*
        (color)
        The color of the func line (Y values). It defaults to "grey - #787878".
    *oudDir*
        (str)
        output dir. Defaults to `networks'.
    *outFile*
        (str)
        output filename. Defaults to `testNetwork.png'.
    """
    # manage args
    matrix = kwargs.get('matrix')
    nodeColor = kwargs.get('nodeColor', 'red')
    lineColor = kwargs.get('lineColor', '#787878')
    outDir = kwargs.get('outDir', 'networks') 
    outFile = kwargs.get('outFile', 'testNetwork.png')
    g = igraph.Graph.Adjacency(list(matrix))
    #plotting the network
    
def networkListFromPickle(srcListMatrix=r'C:\pythontmp\numpyArray.pkl'):
    """
    set the data for create the network

    args:
    *srcListMatrix*
        (str)
        sorce file of the list of matrixs. File '*.pkl' need  
    """
    infile1 = open(srcListMatrix, 'r+b')
    file1 = pickle.load(infile1)                       # This is LISTADIMATRICI
    infile1.close()
    
    myConf = {}
    print len(file1)
    for mtr in file1:
        print mtr
        myConf['matrix'] = mtr
        myConf['nodeColor'] = get_randColor()
        myConf['lineColor'] = '#787878'
        drawNetwork(**myConf)

networkListFromPickle('fakedata/prova.pkl')
