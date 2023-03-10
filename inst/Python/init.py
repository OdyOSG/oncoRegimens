import numpy as np
import pandas as pd
import math as math
import re

def init_Hmat(s1_len,s2_len,g):
	
	H = np.zeros((s2_len+1,s1_len+1), float)
	for row in range(s2_len+1):
		H[row][0] = 0
	
	for col in range(s1_len+1):
		H[0][col] = 0
	
	return H

def init_TRmat(s1,s1_len,s2,s2_len):
	TR = np.zeros((s2_len+1,s1_len+1), float)

	for row in range(1,s2_len+1):
		TR[row][0] = TR[row-1][0] + float(s2[row-1][0])

	return TR

def init_TCmat(s1,s1_len,s2,s2_len):
	TC = np.zeros((s2_len+1,s1_len+1), float)

	for col in range(1,s1_len+1):
		TC[0][col] = TC[0][col-1] + float(s1[col-1][0])

	return TC

def init_traceMat(s1_len,s2_len):

	traceMat = np.zeros((s2_len+1,s1_len+1), float)
	traceMat[0] = 0
	traceMat[:,0] = 0
	traceMat[0][0] = 0

	return traceMat

