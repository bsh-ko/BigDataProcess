#!/usr/bin/python3

import sys
from datetime import datetime, date

inputFile = sys.argv[1]
outputFile = sys.argv[2]

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
u_dic1 = dict()
u_dic2 = dict()

with open(inputFile, "rt") as f:
	for row in f:
		uber = row.split(",")
		uber[-1] = uber[-1].split("\n")[0]
		uberDate = uber[1].split("/")
		uber[1] = days[date(int(day[2]), int(day[0]), int(day[1])).weekday()]

		str = uber[0] + "," + uber[1]
		if key not in u_dic1:
			u_dic1[key] = int(uber[2])	
			u_dic2[key] = int(uber[3])	

		else:
			u_dic1[key] += int(uber[2])	
			u_dic2[key] += int(uber[3])	

string = u_dic1.keys()

with open(outputFile, "wt") as f:
	for k in string:
		f.write(k +" "+str(u_dic1[key]) + "," + str(u_dic2[key]) + "\n")
