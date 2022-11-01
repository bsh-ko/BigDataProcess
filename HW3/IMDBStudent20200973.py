#!/usr/bin/python3

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

AllG = {}
with open(inputFile, "rt") as f:
	genre = []
	for r in f:
		r = r.replace("\n", "")
		movie = r.split("::")
		genre = movie[2].split("|")

		for g in genre:
			if g in AllG:
				AllG[g] += 1
			else:
				AllG[g] = 1

with open(outputFile, "wt") as f:
	for g in AllG:
		f.write("{} {}\n".format(g, AllG[g])) 
