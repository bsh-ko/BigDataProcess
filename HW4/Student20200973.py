#!/usr/bin/python3

from os import listdir
import sys
import numpy as np
import operator

test = sys.argv[2]
training = sys.argv[1]
testD = listdir(test)
trainingD = listdir(training)

def readFile(fName):
	vector = np.zeros((1, 1024))
	
	with open(fName) as f:
		for i in range(32):
			line = f.readline()

			for j in range(32):
				vector[0, 32*i+j] = int(line[j])
	return vector

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1))-dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def createDataSet(dataset):
	len = len(trainingD)
	group = np.zeros((len, 1024))
	labels = []

	for i in range(len):
		fName = trainingD[i]
		label = int(fName.split('_')[0])
		labels.append(label)
		group[i, :] = readFile(dataset +'/' + fName)

	return group, labels

group, labels = createDataSet(training)


for i in range(1, 21):
	sum=0
	fail=0

	for j in range(len(testD)):
		tData = readFile(test+ '/' +testD[i])
		answer = int(testD[i].split('_')[0])
		expect = classify0(tData, group, labels, k)

		if answer != expect:
			fail += 1
		sum += 1
	result = int((fail / sum) * 100)

	print(result)
