"""
Runs the job_hunter program
"""

import pull_indeed as pull_indeed
import waze
import tqdm

def job_hunter():
    CITY = str(input("Search which City, State?:  "))
    CITY = CITY.replace(" ", "+")
    JOB_TITLE = str(input("what job title?:  "))
    JOB_TITLE = JOB_TITLE.replace(" ", "+")
    TO_ADDRESS = str(input("What is your address?:  "))
    df = pull_indeed.scrape_indeed(city=CITY, title=JOB_TITLE)
    return df


if __name__ == "__main__":
    for address in job_hunter()['clean_address']:
        print(waze.calc_route(TO_ADDRESS=TO_ADDRESS,
        FROM_ADDRESS=address))
