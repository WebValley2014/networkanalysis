import numpy as np
from scipy.stats import pearsonr
import pickle as pkl
import distance_functions_2 as df ### him(G,H) with output (hamming, ipsen, him)!

class NETANALYSIS:
	def __init__(self, dataname, labelsname, samplesname, featuresname, setCol, outputpath):	### X.txt, Y.txt, sampleIDs.txt, names.txt, np.array([]), outlstadjmtr.pkl
		self.dataname = dataname
		self.labelsname = labelsname
		self.samplesname = samplesname
		self.featuresname = featuresname
		self.setCol = setCol
		self.outputpath = outputpath

########

	def run(self):
		self.loadfiles()
		self.findsubmatrixes()
		self.mkadjmatrixes()
		self.mkoutput()

########

	def loadfiles(self):
		self.mdata = np.loadtxt(self.dataname)
		self.setlabels = np.loadtxt(self.labelsname)


		self.setsamples = open(self.samplesname)
		self.setsamples = self.setsamples.read()
		self.setsamples = self.setsamples.split('\n')	#now, setsamples is a list of (the right) strings
		self.setsamples.pop(-1)	#fixes an error due to the split function

		self.setfeatures = open(self.featuresname)
		self.setfeatures = self.setfeatures.read()
		self.setfeatures = self.setfeatures.split('\n')
		self.setfeatures.pop(-1)

		q = len(self.setfeatures)
		for i in range(q):
			j = self.setfeatures[i]
			s = j.index('\t')
			self.setfeatures[i] = self.setfeatures[i][s+1:]

		lsmpl, lsftr = self.mdata.shape
		if len(self.setsamples) != len(self.setlabels) or lsmpl != len(self.setlabels) or lsftr != len(self.setfeatures):
			print 'error, invalid input: data not coherent'

########

	def findsubmatrixes(self):

		self.aunilabels = np.unique(self.setlabels)	### array of different labels which are in setlabels

		self.alabels = []	# list of 2d-matrixes (i.e. one sub-matrix for each label)

		ok = 0	# for the condition of the while loop
		while ok < len(self.aunilabels):
			r2 = 0
			maux = np.zeros((len(np.where(self.setlabels == self.aunilabels[ok])[0]), len(self.setCol)))
			for r in np.where(self.setlabels == np.array(list(set(self.setlabels)))[ok])[0]:	#this is a very strange 2d-array with the positions of the ok-th different element of setlabels in setlabels itself
				#print aunilabels
				c2 = 0
				for c in self.setCol:
					maux[r2, c2] = self.mdata[r, c]
					c2 += 1
				r2 += 1
			self.alabels.append(maux)
			ok += 1
		### alabels is now the complete list of the sub-matrices of each label!

########

	def mkadjmatrixes(self):
		self.adjmatrixes = []
		for i in range(len(self.aunilabels)):	# sgrulla down le labels
			self.adjmatrixes.append(self.mknetfeatures(self.alabels[i],0.1))	#FIXME uses features, not samples! 0.1 is the threshold: check it!
		self.adjmatrixes = np.array(self.adjmatrixes)
				### now, the list adjmatrixes is filled in with the adjacency matrices of each different label
		self.himadjmatrix = np.zeros((len(self.aunilabels), len(self.aunilabels)))
			
		for i in range(1, len(self.aunilabels)): #loop on label indexes

			for j in range(i):	#loop on previous labels
				hamming, ipsen, self.himadjmatrix[i, j] = df.him(self.adjmatrixes[i], self.adjmatrixes[j])	#calculates the him distance between two networks
				self.himadjmatrix[j, i] = self.himadjmatrix[i, j]	#makes symmetric the 'adjacency' matrix
		
		return (self.himadjmatrix)	#, aunilabels)

########

	def mknetfeatures(self,M,thre):	#M is our dear big matrix
				#attempt: to make it work on all columns, instead than on a given set
		nRow, nCol = M.shape #define dimensions

		### let's create the network matrix
		self.mNet = np.zeros((nCol, nCol))

		# check of missing elements in the matrix
		if nRow == 0 or nCol == 0:
			print 'null input'
			return None

		for i in np.arange(nCol): #loop on feature indexes

			for k in np.arange(nCol): #loop on feature indexes, again

				if i < k: #not repeated nodes of features
					L1 = [M[j,i] for j in range(nRow)]
					L2 = [M[j,k] for j in range(nRow)]
				
					if np.var(L1)==0 and np.var(L2)==0:
						pear=[1.0,123]
					elif np.var(L1)==0 or np.var(L2)==0:
						pear=[0.,123]
					else:
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
