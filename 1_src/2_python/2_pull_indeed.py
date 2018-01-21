
# coding: utf-8

# In[52]:


import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import WazeRouteCalculator
import datetime


# ## Pulling Job Data

# In[53]:


project_path = "/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/"
#project_path = "/home/jj_espinoza_la/itsfriday/"

now = datetime.datetime.now()
now.year
now.month
now.day
date = str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute)
date


# In[104]:


max_results_per_city = 100
max_commute = 45
#city_set = ['Los+Angeles']
city_set = ['Los+Angeles', 'Los+Angeles+County', 'Long+Beach', 'Downey', 'Commerce']
#title_set = ['data+scientist']
title_set = ['data+scientist', 'senior+data+scientist', 'director+data+science', 'director+analytics', 'vice+president+analytics', 'vice+president+data+science']
columns = ['city', 'job_title', 'company_name', 'location', 'summary', 'salary']
sample_df = pd.DataFrame(columns = columns)


# In[55]:


#scraping code:
for title in title_set:
    for city in city_set:
        for start in range(0, max_results_per_city, 10):
            page = requests.get('http://www.indeed.com/jobs?q='+ str(title) +'+%2420%2C000&l=' + str(city) + '&start=' + str(start))
            time.sleep(1)  #ensuring at least 1 second between page grabs
            soup = BeautifulSoup(page.text, 'lxml')
            for div in soup.find_all(name='div', attrs={'class':'row'}): 
                #specifying row num for index of job posting in dataframe
                num = (len(sample_df) + 1) 
                #creating an empty list to hold the data for each posting
                job_post = [] 
                #append city name
                job_post.append(city) 
                #grabbing job title
                for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
                    job_post.append(a['title']) 
                #grabbing company name
                company = div.find_all(name='span', attrs={'class':'company'}) 
                if len(company) > 0: 
                    for b in company:
                        job_post.append(b.text.strip()) 
                else: 
                    sec_try = div.find_all(name='span', attrs={'class':'result-link-source'})
                    for span in sec_try:
                        job_post.append(span.text) 
                #grabbing location name
                c = div.findAll('span', attrs={'class': 'location'}) 
                for span in c: 
                    job_post.append(span.text) 
                #grabbing summary text
                d = div.findAll('span', attrs={'class': 'summary'}) 
                for span in d:
                    job_post.append(span.text.strip()) 
                #grabbing salary
                try:
                    job_post.append(div.find('nobr').text) 
                except:
                    try:
                        div_two = div.find(name='div', attrs={'class':'sjcl'}) 
                        div_three = div_two.find('div') 
                        job_post.append(div_three.text.strip())
                    except:
                        job_post.append('Nothing_found') 
                #appending list of job post info to dataframe at index num
                sample_df.loc[num] = job_post




# In[63]:


del sample_df['city']


# In[79]:


sample_df['job_title'] = sample_df['job_title'].str.lower()
sample_df['company_name'] = sample_df['company_name'].str.lower()
sample_df['location'] = sample_df['location'].str.lower()
sample_df['summary'] = sample_df['summary'].str.lower()
sample_df = sample_df.drop_duplicates(subset=['job_title', 'company_name'], keep = False)


# ### Saving Raw Data

# In[80]:


sample_df.to_csv(project_path + "2_data/1_raw/scraper_indeed_jobs_raw.csv", encoding='utf-8')
sample_df


# ## Dropping unwanted job titles
# 

# In[87]:


#Try this
sample_df = sample_df[(sample_df["job_title"] != "account") & 
                       (~sample_df["job_title"].str.contains('engineer')) &
                      (~sample_df["job_title"].str.contains('research')) &
                     (~sample_df["job_title"].str.contains('manager')) &
                      (~sample_df["job_title"].str.contains('developer')) & 
                        (~sample_df["job_title"].str.contains('vice president of sales')) & 
                        (~sample_df["job_title"].str.contains('communications')) & 
                    (~sample_df["job_title"].str.contains('client')) & 
                     (~sample_df["job_title"].str.contains('analyst'))]






sample_df


# ## Dropping Unwanted Cities

# In[93]:


sample_df = sample_df[ (~sample_df["location"].str.contains('woodland hills')) &
                      (~sample_df["location"].str.contains('santa monica')) &
                      (~sample_df["location"].str.contains('culver city')) &
                      (~sample_df["location"].str.contains('burbank')) &
                      (~sample_df["location"].str.contains('hollywood')) &
                      (~sample_df["location"].str.contains('westwood')) &
                      (~sample_df["location"].str.contains('universal city')) &
                      (~sample_df["location"].str.contains('beverly hills')) &
                      (~sample_df["location"].str.contains('playa vista')) &
                      (~sample_df["location"].str.contains('valencia')) &
                      (~sample_df["location"].str.contains('encino')) &
                      (~sample_df["location"].str.contains('venice'))
                     ]



sample_df


# ## Dropping Companies

# In[97]:


sample_df = sample_df[ (~sample_df["company_name"].str.contains('ucla Extension')) &
                      (~sample_df["company_name"].str.contains('usc')) &
                      (~sample_df["company_name"].str.contains('health')) &
                      (~sample_df["company_name"].str.contains('riot games')) &
                      (~sample_df["company_name"].str.contains('los angeles county')) &
                      (~sample_df["company_name"].str.contains('lieberman research worldwide')) &
                      (~sample_df["company_name"].str.contains('hospital')) &
                      (~sample_df["company_name"].str.contains('medicine')) &
                       (~sample_df["company_name"].str.contains('university')) &
                      (~sample_df["company_name"].str.contains('first 5 la'))
                      
                     ]



health


sample_df


# In[98]:


sample_df.to_csv(project_path + "2_data/2_clean/scraper_indeed_jobs_clean.csv", encoding='utf-8')


# ### Saving Clean Data

# ## Calculating Distance

# In[99]:


sample_df["clean_address"] = sample_df["company_name"] + ' ' + sample_df["location"]


# In[100]:


commutes = []

for address in sample_df["clean_address"]:
    from_address = "10757 Longworth Ave Santa Fe Springs CA 90670"
    region = 'US'
    try:
        to_address = address
        route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region )
        commutes.append(route.calc_route_info(real_time=False))
    except:
        commutes.append((0,0))
    
    
        
    
        


# In[108]:


df = pd.DataFrame(commutes) 
df.columns = ['commute', 'distance_km']
df.index = range(1,len(df)+1)
sample_df = sample_df.join(df, lsuffix='_caller', rsuffix='_other')
sample_df


# ### Filtering Based on Distance

# In[109]:


sample_df.to_csv(project_path + "2_data/2_clean/scraper_indeed_jobs_clean_enhanced.csv", encoding='utf-8')


# In[ ]:




