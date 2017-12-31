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
	print '--h                                        help menu'
	print '--TopCompaniesInNetwork                    # per company'
	print '--SearchContacts ["company"]["posiiton"]   find emails'
	print '--MostInbox                                contacts by inbox freq'
	print '--TopEndorsers                             Names of people with top endorsements'
	print '__________________________________________________'
	print ''

if sys.argv[1] == "--TopCompaniesInNetwork":
	df = pd.read_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/1_raw/Connections.csv')
	my_tab = pd.crosstab(index=df["Company"],  columns="count")
	my_tab = my_tab.sort_values(by = 'count', axis=0, ascending=False, inplace=False, kind='quicksort', na_position='last')
	print(my_tab.head) 
	my_tab.to_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/2_clean/TopCompaniesInNetwork.csv')  

if sys.argv[1] == "--MostInbox":
	print("MostInbox")
	df = pd.read_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/1_raw/Messages.csv')
	df = df[df.Direction == "INCOMING"]
	count = df['From'].value_counts()
	print(count)
	count.to_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/2_clean/MostInbox.csv')

if sys.argv[1] == "--SearchContacts":
	df = pd.read_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/1_raw/Connections.csv')
	company = sys.argv[2]
	position = sys.argv[3]
	df_filtered = df[df.Company == company]
	df_filtered = df_filtered[df_filtered['Position'].str.contains(position)]
	print(company + '-' + position)
	df_filtered.to_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/2_clean/' + company +  '-' + position + '.csv')
	# print(df_filtered)

#Do this manually for now
# if sys.argv[1] == "--TopEndorsers":
# 	df = pd.read_csv('/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/2_data/1_raw/Endorsements.csv', sep='\t')
# 	print(df)


