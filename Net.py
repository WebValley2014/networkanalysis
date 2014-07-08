						pear = pearsonr(L1,L2)    #output as array
				
					if pear > thre:
						self.mNet[i,k] = abs(pear[0])
						self.mNet[k,i] = abs(pear[0])
		### mNet is now our network matrix

		return self.mNet

########

	def mkoutput(self):	# saves the list of him adjacency matrices in the outputpath
				# WARNING: it has to be a .pkl file!!!
		outfile = open(self.outputpath, 'w+b')
		pkl.dump(self.himadjmatrixes, outfile)
		outfile.close()

########

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
        
        output:
        """
        # manage args
        matrix = kwargs.get('matrix')*3
        nodeColor = kwargs.get('nodeColor', 'red')
        lineColor = kwargs.get('lineColor', '#787878')
        outDir = kwargs.get('outDir', 'networks') 
        outFile = kwargs.get('outFile', 'testNetwork.png')
        g = igraph.Graph.Weighted_Adjacency(list(matrix),mode=igraph.ADJ_MAX)
        visual_style = {}
        visual_style["vertex_size"] = 20
        visual_style["vertex_color"] = nodeColor
        visual_style["vertex_label"] = ('111', '222', '333', '444')
        visual_style["edge_width"] = g.es["weight"]
        #visual_style["layout"] = layout_kamada_kawai
        visual_style["bbox"] = (900, 900)
        visual_style["margin"] = 20
        #plotting the network
        igraph.plot(g, **visual_style)

########

    def labelReader(srcFileLabel=''):
        """
        read the labels of the 
        
        args:
        *srcLabel*
            (str)
            the source of the file
        
        out:
            (str)
            a list of strings of each samples
        """
        flabels = open(srcFileLabel)
        txtlabels = flabels.read()
        flables.close()
        txtlabels.split('\n')
        txtlabels.pop(-1)
        for i in range(len(txtlabels)):
            j = t[i].index('d') #in labels.txt there should be just a list of 'merged#number#'
            t[i] = t[i][j+1:]
        # now, txtlabels is a list of string which are, actually, numbers
        return txtlabels

##############

    def networkListFromPickle(srcListMatrix=r'C:\pythontmp\numpyArray.pkl'):#, srcFileName=''):
        """
        set the data for create the network

        args:
        *srcListMatrix*
            (str)
            sorce file of the list of matrixs. File '*.pkl' need  
        """
        infile1 = open(srcListMatrix, 'r+b')
        file1 = pickle.load(infile1)
        infile1.close()
        
        myConf = {}
        for mtr in file1:
            print mtr
            myConf['matrix'] = mtr
            myConf['nodeColor'] = get_randColor()
            myConf['lineColor'] = '#787878'
            #myConf['listNames'] = labelReader(srcFileName)
            drawNetwork(**myConf)


