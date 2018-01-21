#!/bin/bash

#####
#NOTE: THIS CAN BE PUT IN A CRONJOB TO RUN AT 8AM AND AT 5PM - THIS WAY COMMUTE TIMES ARE APPROPRIATE

#Copy this file to the hourly cronjobs

#Scrapes data from indeed
python /home/jj_espinoza_la/itsfriday/1_src/2_python/2_pull_indeed.py

#pushes data to Google Storage For Additional Processing
gsutil cp /home/jj_espinoza_la/itsfriday/2_data/1_raw/scraper_indeed_jobs_raw.csv gs://indeed-scraper
gsutil cp /home/jj_espinoza_la/itsfriday/2_data/2_clean/scraper_indeed_jobs_clean_enhanced.csv gs://indeed-scraper


