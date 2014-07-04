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
	setsamples = np.loadtxt('samples.txt')
	setfeatures = np.loadtxt('features.txt')
	setlabels = np.loadtxt('labels.txt')
	
	if len(setsamples), len(setfeatures) == mdata.shape and len(setsamples) == len(setlabels):

		nlabels = len(set(setlabels))	# how many different labels there are
		mlabels = np.zeros(nlabels)	# 1d-array of 2d-arrays (one for each label)
		mwhere = np.zeros(nlabels)	# 1d-array of 2d-arrays (one for each set of position of the labels in the big dear matrix
		ok = len(set(setlabels)) - 1	# for the condition of the while loop
		while ok >= 0:
			setaux = np.zeros(len(setfeatures))
			k = 0
			for i in np.where(setlabels == np.array(list(set(setlabels)))[ok])	#this is a very strange 2d-array with the positions of the ok-th different element of setlabels in setlabels itself
				maux = np.matrix(np.zeros(len(np.where(setlabels == np.array(list(set(setlabels)))[ok])) * len(setfeatures)).reshape(len(np.where(setlabels == np.array(list(set(setlabels)))[ok]))), len(setfeatures)) # dimensions are the right ones, trust me
				j = 0
				for t in setfeatures:
					setaux[j] = mdata[i, t]
					j += 1
				maux[k,:] = setaux
				k += 1
			#FIXME  ora fai la matrice di tutte le mauxes!
			ok -= 1

		'''
		msani = np.zeros((len(dovesani) * len(setfeatures))
		msani = msani.reshape(len(dovesani), len(setfeatures))
			# zeroed matrix of healthies well-shaped
		mmalati = np.zeros(len(dovemalati) * len(setfeatures))
		mmalati = mmalati.reshape(len(dovemalati), len(setfeatures))
			# zeroed matrix of unhealthies well-shaped
		'''

		r = 0
		for i in dovesani: # fills in the matrix already created in rows
			c = 0
			for j in setfeatures: # and in the columns
				msani[r, c] = mdata[i, j]
				c += 1	#goes on with columns
			r += 1	#goes on with rows
		# healthies matrix done

		r = 0
		for i in dovemalati: # fills in the matrix already created in rows
			c = 0
			for j in setfeatures: # and in the columns
				msani[r, c] = mdata[i, j]
				c += 1	#goes on with columns
			r += 1	#goes on with rows
		# unhealthies matrix done

		adjnetsani = mknetfeatures(msani,setCol) # uses features, not samples!
		adjnetmalati = mknetfeatures(mmalati,setCol)
		hamming, ipsen, him = df.him(adjnetsani, adjnetmalati)

	else:
		print 'invalid input: data non coherent'

	return (him, adjnetsani, adjnetmalati)

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

	# check of missing elements in the matrix
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
