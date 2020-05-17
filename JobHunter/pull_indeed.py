"""
Pulls data from Indeed for job hunting

"""

import time
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


def scrape_indeed(city, title, max_results_per_city=100):
    """
    Indeed Job scraper, multipages are scraped
    """
    columns = ['city', 'job_title', 'company_name', 'location']
    all_listings = []
    for start in tqdm(range(0, max_results_per_city, 10)):
        page = requests.get('http://www.indeed.com/jobs?q=' + str(title) +
                            '+%2420%2C000&l=' + str(city) + '&start=' + str(start))
        time.sleep(1)  # ensuring at least 1 second between page grabs
        soup = BeautifulSoup(page.text, 'lxml')
        for div in soup.find_all(name='div', attrs={'class': 'row'}):

            # creating an empty list to hold the data for each posting
            job_post = []
            # append city name
            job_post.append(city)

            # grabbing job title
            for a in div.find_all(name='a', attrs={'data-tn-element': 'jobTitle'}):
                job_post.append(a['title'])

            # grabbing company name
            company = div.find_all(name='span', attrs={
                                    'class': 'company'})
            if company:
                for b in company:
                    job_post.append(b.text.strip())
            else:
                sec_try = div.find_all(name='span', attrs={
                                        'class': 'result-link-source'})
                for span in sec_try:
                    job_post.append(span.text)
            # grabbing location name
            c = div.findAll('span', attrs={'class': 'location'})
            for span in c:
                job_post.append(span.text)
            all_listings.append(job_post)

    df = pd.DataFrame(all_listings)
    df.columns = columns
    df["clean_address"] = df["company_name"] + \
    ' ' + df["location"]

    del df['city']
    del df['company_name']
    del df['location']

    df = df.sort_values(by='clean_address')
    return df.drop_duplicates()




if __name__ == "__main__":
    CITY = str(raw_input("What city?:  "))
    CITY = CITY.replace(" ", "+")
    JOB_TITLE = str(raw_input("what job title?:  "))
    JOB_TITLE = JOB_TITLE.replace(" ", "+")
    print(scrape_indeed(city=CITY, title=JOB_TITLE))
