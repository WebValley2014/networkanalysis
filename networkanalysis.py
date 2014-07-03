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

def netanalysis(setCol)	#FIXME

	mdata = np.loadtxt('data.txt')
	setnames = np.loadtxt('names.txt')
	setfeatures = np.loadtxt('features.txt')
	setlabels = np.loadtxt('labels.txt')

	if len(setnames), len(setfeatures) == mdata.shape and len(setnames) == len(setlabels):

		bol = np
                for i in range(len(setlabels)):
			if setlabels[i] == 0:
                                


		mNet1 = np.array([])


		adjNet1 = mknetfeatures(mNet1,setCol) # usa le features, non i samples!
		adjNet2 = mknetfeatures(mNet2,setCol)
		hamming, ipsen, him = df.him(mNet1,mNet2)

	else print 'invalid input: data non coherent'

	return him

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

def mknetfeatures(M, setCol):  #M is our dear big matrix
		       #setCol is the array of column indexes chosen

	nRow, nCol = M.shape #define dimensions

	### let's create the network matrix
	
	mNet = np.zeros([len(setCol),len(setCol)])

	#FIXME check of missing elements in the matrix
	if nRow == 0 or nCol == 0:
		print 'null input'
		return None

	for i in setCol: #loop on feature indexes

		for k in setCol: #loop on feature indexes, again

                        if i < k: #not repeated nodes of features
			        L1 = [M[j,i] for j in range(nRow)]
			        L2 = [M[j,k] for j in range(nRow)]

			        pear = pearsonr(L1,L2)    #output as array

				if pear > 0.1:  #FIXME is 0.1 fine?
					mNet[i,k] = abs(pear[0])
					mNet[k,i] = abs(pear[0])
	### mNet is now our network matrix

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



if __name__ == '__main__':
	a = np.matrix([[0,1,2,3],[7,6,5,4],[12,45,3,25]])
	tst = [0,1,2,3]
