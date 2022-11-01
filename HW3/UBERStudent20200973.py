#!/usr/bin/python3

import sys
from datetime import datetime, date

inputFile = sys.argv[1]
outputFile = sys.argv[2]

Weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

trip = {}
with open(inputFile, "rt") as f:
	for r in f:
		row = r.replace("\n", "")
		uber = r.split(',')
		uberDate = uber[1].split("/")
		today = Weekday[uberDate.weekday()]

		if t not in trip:
			trip[t] = [int(uber[2]), int(uber[3])]
		else:
			trip[t][0] += int(today[2])
			trip[t][1] += int(today[3])

with open(outputFile, "wt") as f:
	for key, value in trip.items():
		f.write(key +" "+str(value[0]) +str(value[1]) + "\n")
