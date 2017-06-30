#!/usr/bin/env python

import yoda
import sys

def main(arg):
	infile = arg
	outfile = arg[:-5] + '_scatter.yoda'
	aos = yoda.read(infile)
    
	scatter = []
	hs = [h for h in aos.values()]
	for h in hs:
		s = h.mkScatter()
		scatter.append(s)

	yoda.write(scatter, outfile)
	sys.exit(0)

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print('Enter an input file!')
		sys.exit(1)
	else:
	#Enables shell wildcard use
	for arg in sys.argv[1:]:
		main(arg)
