#!/usr/bin/python

import pandas as pd

#How to use arguments in a Python Script
import sys

if sys.argv[1] == "--h":
	print ''
	print '***************************************'
	print '************** help menu **************'
	print '***************************************'
	print ''
	print 'author: JJ Espinoza'
	print 'description: pulls and analyzes data for job hunt'
	print 'created: 2017-12-13'
	print ''
	print 'commands:                 descriptions:'
	print '_______________________________________'
	print ''
	print '--h                           help menu'
	print '--emailCompany ["company"]    saves email lists'
	print '_______________________________________'
	print ''


if sys.argv[1] == "--emailCompany":
	print(pandas.read_csv("/Users/jje/Documents/00__mytools/2_itsfriday/"))