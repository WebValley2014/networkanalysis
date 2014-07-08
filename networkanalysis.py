#############################################################
## proudly imagined by Davide Leonessi & Stefano Valentini ##
## happily coded by Davide Leonessi                        ##
## deeply inspired by Giuseppe Jurman                      ##
## slightly inspired by a lot of people, too :P            ##
## still #WaitingFor #Visintainer                          ##
#############################################################

import numpy as np
from scipy.stats import pearsonr
import distance_functions_2 as df ### him(G,H) with output (hamming, ipsen, him)!

def na(setCol,mdata):#netanalysis(setCol):	#FIXME

	mdata = np.loadtxt('data.txt')
	setlabels = np.loadtxt('labels.txt')

	setsamples = open('samples2.txt')
	setsamples = setsamples.read()
	setsamples = setsamples.split('\n')	#now, setsamples is a list of (the right) strings
						#there is (shoud be?) no title
	setfeatures = open('features.txt')
	setfeatures = setfeatures.read()
	setfeatures = setfeatures.split('\n')
	setfeatures.pop(-1)	#FIXME
	setsamples.pop(-1)	#FIXME

	q = len(setfeatures)
	for i in range(q):
		j = setfeatures[i]
		s = j.index('\t')
		setfeatures[i] = setfeatures[i][s+1:]

	lsmpl, lsftr = mdata.shape
	if len(setsamples) == len(setlabels):

		if lsmpl == len(setlabels) and lsftr == len(setfeatures):

			aunilabels = np.unique(setlabels)	### array of different labels which are in setlabels

			alabels = []	# list of 2d-matrixes (i.e. one sub-matrix for each label)

			ok = 0	# for the condition of the while loop
			while ok < len(aunilabels):
				#setaux = np.zeros(len(setCol))
				#setaux2 = np.zeros(len(setCol))	#auxiliar arrays
				r2 = 0
				maux = np.zeros((len(np.where(setlabels == aunilabels[ok])[0]), len(setCol)))
				for r in np.where(setlabels == np.array(list(set(setlabels)))[ok])[0]:	#this is a very strange 2d-array with the positions of the ok-th different element of setlabels in setlabels itself
					#print aunilabels
					
					c2 = 0
					for c in setCol:
						maux[r2, c2] = mdata[r, c]
						c2 += 1
					r2 += 1
				alabels.append(maux)
				ok += 1

				### alabels is now the complete list of the sub-matrixes of each label!
			adjmatrixes = []

			for i in range(len(aunilabels)):	# sgrulla down le labels
				adjmatrixes.append(mknetfeatures(alabels[i]))	# uses features, not samples!
				### now, the list adjmatrixes is filled in with the adjacency matrixes of each different label
			himadjmatrix = np.zeros((len(aunilabels), len(aunilabels)))
			
			for i in range(1, len(aunilabels)): #loop on label indexes

				for j in range(i): #loop on previous labels
					print adjmatrixes[i]
					print adjmatrixes[j]
					hamming, ipsen, himadjmatrix[i, j] = df.him(adjmatrixes[i], adjmatrixes[j])	#calculates the him distance between two networks
					himadjmatrix[j, i] = himadjmatrix[i, j]	#makes symmetric the 'adjacency' matrix

		else:
			print 'invalid input: data non coherent'
			return None

	else:
		print 'error: samples.txt and features.txt are not shaped in the same way'
		return None

	return (himadjmatrix)#, aunilabels)

########

def mknetsamples(M, setCol):  #M is our dear big matrix
		       #setCol is the array of column indexes chosen

	nRow, nCol = M.shape #define dimensions  

	### let's create the network matrix
	
	mNet = np.zeros([nRow,nRow])

	#check of missing elements in the matrix
	if nRow == 0 or nCol == 0:
		print 'null input'
		return None

	for i in range(1,nRow): #loop on samples indexes

		for k in range(i): #loop on previous samples

			L1 = [M[i,j] for j in setCol]
			L2 = [M[k,j] for j in setCol]

			pear = pearsonr(L1,L2)      #output as array

			if pear > 0.1:  #FIXME is 0.1 fine?
				mNet[i,k] = abs(pear[0])
				mNet[k,i] = abs(pear[0])
	### mNet is now our network matrix

	return mNet

########

def mknetfeatures(M,thre):#M is our dear big matrix
			#attempt: to make it work on all columns, instead than on a given set
	nRow, nCol = M.shape #define dimensions

	### let's create the network matrix
	mNet = np.zeros((nCol, nCol))

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
				
				if pear > thre:  #FIXME is 0.1 fine?
					mNet[i,k] = abs(pear[0])
					mNet[k,i] = abs(pear[0])
	### mNet is now our network matrix

	return mNet

########

def isthisadj(m): #checks whether a 2d array is an adjacency matrix or not
	nRow, nCol = m.shape #take dimensions
	#checking
	if nRow != nCol or nRow == 0 or nCol == 0:
		return False

	for i in range(nRow):
		if m[i,i] != 0:
			return False
		if i > 0:
			for j in range(i):
				if m[i,j] != m[j,i]:
					return False
	#ok, I give up, it's fine
	return True

########
