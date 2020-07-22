"""
Runs the job_hunter program
"""
import pandas as pd
import pull_indeed as pull_indeed
import waze
from tqdm import tqdm

def job_hunter():
    CITY = str(input("Search which City, State?:  "))
    CITY = CITY.replace(" ", "+")
    JOB_TITLE = str(input("what job title?:  "))
    JOB_TITLE = JOB_TITLE.replace(" ", "+")

    df = pull_indeed.scrape_indeed(city=CITY, title=JOB_TITLE)
    return df


if __name__ == "__main__":
    TO_ADDRESS = str(input("What is your address?:  "))
    JOB_HUNTER = job_hunter()
    print(JOB_HUNTER)
    COMMUTES = []

    for address in tqdm(JOB_HUNTER['clean_address']):

        COMMUTES.append(waze.calc_route(TO_ADDRESS=TO_ADDRESS,
        FROM_ADDRESS=address))

    commutes = pd.DataFrame(COMMUTES, columns=['waze'])
    results = pd.concat([JOB_HUNTER, commutes], axis=1, sort=False)
    results.to_csv("results/results.csv", encoding='utf-8')
