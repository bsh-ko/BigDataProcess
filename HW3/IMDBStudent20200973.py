#!/usr/bin/python3

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

AllG = {}
with open(inputFile, "rt") as f:
	for r in f:
		movie = r.split("::")
		genre = movie[2].split("|")

		for g in genre:
			if g not in AllG:
				AllG[g] = 1
			else:
				AllG[g] += 1

with open(outputFile, "wt") as f:
	for k, v in AllG.items():
		f.write(k + " " + str(v) + "\n") 
