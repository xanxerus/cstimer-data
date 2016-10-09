#!/usr/bin/env python
# coding: utf-8
import json
import sys

def parse(file='cstimer.txt', dest='/home/jbelpois/Desktop'):
	contents = json.load(open(file, 'r'))
	contents = {i:json.loads(contents[i]) for i in contents if i != 'properties'}

	for session in contents:
		with open('%s/%s%s.csv' % (dest, file[:-4], session), 'w') as out:
			print out.name
			for i in contents[session]:
				if isinstance(i, list):
					out.write("%.3f\n" % (i[0][1]*1e-3))

if len(sys.argv) <= 1:
	parse('cstimer2016-08-09-yellow.txt')
else:
	for f in sys.argv[1:]:
		parse(f)
