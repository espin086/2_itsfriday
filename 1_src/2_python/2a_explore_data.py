#!/usr/bin/python
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
	print 'description: exploratory analysis'
	print 'created: 2017-12-13'
	print ''
	print 'commands:                 descriptions:'
	print '__________________________________________________'
	print ''
	print '--h                                      help menu'
	print '--TopCompaniesInNetwork                  # per company'
	print '--SearchEmails ["company"][posiiton]     find emails'
	print '__________________________________________________'
	print ''

if sys.argv[1] == "--TopCompaniesInNetwork":
	df = pd.read_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/1_raw/Connections.csv')
	my_tab = pd.crosstab(index=df["Company"],  columns="count")
	my_tab = my_tab.sort_values(by = 'count', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
	print(my_tab.head)   

if sys.argv[1] == "--SearchEmails":
	df = pd.read_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/1_raw/Connections.csv')
	df_filtered = df[df.Company == sys.argv[2]]
	df_filtered = df_filtered[df_filtered['Position'].str.contains(sys.argv[3])]
	print(df_filtered)

    
