import pandas as pd
#How to use arguments in a Python Script
import sys
if sys.argv[1] == "--h":
	print ''
	print '*****************************************************'
	print '       ************** help menu **************'
	print '*****************************************************'
	print ''
	print 'author: JJ Espinoza'
	print 'description: data acquring and cleaning'
	print 'created: 2017-12-13'
	print ''
	print 'commands:                 descriptions:'
	print '__________________________________________________'
	print ''
	print '--h                             help menu'
	print '--TopEndorsers                  identify top endorsers'
	print '__________________________________________________'
	print ''

if sys.argv[1] == "--TopEndorsers":
	print('Top Endorsers:')
	print '__________________________________________________'
	df = pd.read_csv('/Users/jje/Documents/00__mytools/2_itsfriday/2_data/1_raw/Endorsements.csv')
	print(df)
	

