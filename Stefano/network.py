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
    matrix = kwargs.get('matrix')*100
    matrix[0,1]=150
    nodeColor = kwargs.get('nodeColor', 'red')
    lineColor = kwargs.get('lineColor', '#787878')
    outDir = kwargs.get('outDir', 'networks') 
    outFile = kwargs.get('outFile', 'testNetwork.png')

    visual_style = {}
    visual_style["vertex_size"] = 20
    visual_style["vertex_color"] = nodeColor
    visual_style["vertex_label"] = ''
    visual_style["edge_width"] = True
    #visual_style["layout"] = layout_kamada_kawai
    visual_style["bbox"] = (300, 300)
    visual_style["margin"] = 20
    #plotting the network
    g = igraph.Graph.Weighted_Adjacency(list(matrix),mode=igraph.ADJ_MAX)
    igraph.plot(g, **visual_style)

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

networkListFromPickle('fakedata/outarrmtr.pkl')
