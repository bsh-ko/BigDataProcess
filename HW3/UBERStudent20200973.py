#!/usr/bin/python3

import sys
from datetime import datetime, date

inputFile = sys.argv[1]
outputFile = sys.argv[2]

def Weekday(date):
	wday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return wday[day]

trip = {}
with open(inputFile, "rt") as f:
	for r in f:
		uber = r.split(',')
		uberDate = uber[1].split("/")
		today = Weekday(date(int(uberDate[2]), int(uberDate[0], int(uberDate[1])))

		if t not in trip:
			trip[t] = [int(uber[2]), int(uber[3])]
		else:
			trip[t][0] += int(today[2])
			trip[t][1] += int(today[3])

with open(outputFile, "wt") as f:
	for k, v in trip.items():
		f.write(k +" "+str(v[0]) +str(v[1]) + "\n")
