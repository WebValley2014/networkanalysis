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

def mknetsamples(M, setCol):  #M is our dear big matrix
		       #setCol is the array of column indexes chosen

	nRow, nCol = M.shape #define dimensions  

	### let's create the network matrix
	
	mNet = np.zeros([nRow,nRow])

	#FIXME check of missing elements in the matrix
	if nRow == 0 or nCol == 0:
		print 'null input'
		return None

	for i in range(1,nRow): #loop on samples indexes

		for k in range(i): #loop on previous samples

			L1 = [M[i,j] for j in setCol]
			L2 = [M[k,j] for j in setCol]

			pear = pearsonr(L1,L2)      #output as array

			mNet[i,k] = abs(pear[0])
			mNet[k,i] = abs(pear[0])
	### mNet is now our network matrix

	return mNet

########

def mknetfeatures(M, setCol):  #M is our dear big matrix
		       #setCol is the array of column indexes chosen

	nRow, nCol = M.shape #define dimensions

	### let's create the network matrix
	
	mNet = np.zeros([setCol,setCol])

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

			        mNet[i,k] = abs(pear[0])
			        mNet[k,i] = abs(pear[0])
	### mNet is now our network matrix

	return mNet

########

def mklaplacian (M): #makes a squared  2d-matrix laplacian
	nRow, nCol = M.shape #take dimensions
	# check whether the matrix is an adjacency one
	if not isthisadj(M):
		print 'not an adjacency matrix in input'
		return None
	#checked

	asum = M.sum(axis = 1) #array of the sum of rows (cols?)
	mdiag = np.diag(asum)  #degree matrix
	L = mdiag - M          #laplacian matrix

	return L

########
### historic interest
##
##	for i in range(nRow): #summing rows and printing on diagonal
##		temp = 0
##		for j in range(nCol): #ok, nCol is as swag as nRow
##			temp += M[i,j]
##		M[i,i] = temp
##
##	return M
##
########
### this is not for wheighted graphs
## def 2dhamming(m1, m2): # finds hamming distance beetween 2 adj matrixes
##		 #i.e. how many elements they do not have in common
##	if m1.shape != m2.shape: #checking they've the same shape
##		print 'invalid input: 2d arrays with same shape needed'
##		return None
##	if (not isthisadj(m1)) or (not isthisadj(m2)):
##		print 'invalid input: both 2d arrays must be adjacency matrixes'
##		return None
##	#checked	
##
##	nRow, nCol = m1.shape #take dimensions
##
##	##controlling only half of each matrix
##	dist = 0
##	for i in range(1,nRow):    #loop on all-1 rows
##		for j in range(i): #loop on all-1 columns
##			if m1[i,j] != m2[i,j]:
##				dist += 1
##
##	return dist
##
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
	print mknet(a,tst)

