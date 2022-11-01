#!/usr/bin/python3

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

G = {}
with open(inputFile, "rt") as f:
	for r in f:
		movie = r.split("::")
		genre = movie[2].split("|")

		for g in genre:
			if g not in G:
				G[g] = 1
			else:
				G[g] += 1

with open(outputFile, "wt") as f:
	for r in G:
		f.write("{} {}\n".format(g, G[g]))
