
# coding: utf-8

# In[10]:


import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import WazeRouteCalculator
import datetime


# ## Pulling Job Data

# In[11]:


#project_path = "/Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/"
project_path = "/home/jj_espinoza_la/itsfriday/"

now = datetime.datetime.now()
now.year
now.month
now.day
date = str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour) + str(now.minute)
date


# In[17]:


max_results_per_city = 10
city_set = ['Los+Angeles']
#city_set = ['Los+Angeles', 'Los+Angeles+County', 'Long+Beach', 'Downey', 'Commerce']
title_set = ['data+scientist']
#title_set = ['data+scientist', 'senior+data+scientist', 'director+data+science', 'director+analytics', 'vice+president+analytics', 'vice+president+data+science']
columns = ['city', 'job_title', 'company_name', 'location', 'summary', 'salary']
sample_df = pd.DataFrame(columns = columns)


# In[18]:


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




# In[19]:


del sample_df['city']


# In[20]:


sample_df = sample_df.drop_duplicates()


# In[21]:


sample_df


# ## Calculating Distance

# In[22]:


sample_df["clean_address"] = sample_df["company_name"] + ' ' + sample_df["location"]


# In[23]:


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
    
    
        
    
        


# In[25]:


df = pd.DataFrame(commutes) 
df.columns = ['commute', 'distance_km']
df.index = range(1,len(df)+1)
sample_df = sample_df.join(df, lsuffix='_caller', rsuffix='_other')
sample_df


# In[66]:


sample_df.to_csv(project_path + "2_data/1_raw/scraper_indeed_jobs_" + date + ".csv", encoding='utf-8')


# In[ ]:




