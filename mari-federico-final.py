# this file was created by Federico Mari on 11/16/2023

'''sources: "freeCodeCamp.org" (greate YT channel with a 1 hour tutorial on web-scraping), "The Nature of Code", 
"How To Automate The Boring Stuff With Python'''

# title: "End Carbon Emissions"

'''Goals: Find an automotive website and screeen scrape its contents using the directions from 'How to Automate the Boring
Stuff With Python'''
# parses HTML or the format in which web pages are written in
from bs4 import BeautifulSoup
# This library launches and controls a web browser, it is able to simulate mouse clicks in this browser
import selenium
# downloads the desired files and pages from the internet
import requests
# opens a web browser to a specifc page on the web
import webbrowser
import time
from tkinter import ttk
from tkinter import *

# user could provide some information to specify the job 
print("S...")
# later use this variable to 
unfamiliar_skill = input('>')
# will filter out/remove the input provided by the user...
print(f"Filtering out: {unfamiliar_skill}")

def find_jobs():
    # get specific info from a we bsite, include website url as string
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Architectural+Design%22&txtKeywords=%22Architectural+Design%22&txtLocation=').text

    # parse the html file with lxml 
    soup = BeautifulSoup(html_text, 'lxml')
    # for this job website accumulate all the jobs (first element of find_all func is the item tags, then the class_ from html)
    # located underneath the 'ul' tag (unordered list with 'li')
    # use find_all() func to list all the jobs in website 
    jobs = soup.find_all('li', class_= "clearfix job-bx wht-shd-bx")
    # apply results for jobs in the code
    for i,job in enumerate(jobs):
        publishing_date = job.find('span', class_= "sim-posted").text.replace(' ', '')
        # define a condition, to know if the jobs were recently posted or not, use the keyword 'few' to search for these recent jobbs
        if 'few' in publishing_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
            job_time = job.find('ul', class_ = "top-jd-dtl clearfix").text.replace(' ')
            key_skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            # first tag or top tag on the website format:
            # travel to header, then to h2 tag, and finally to the a tag(information is stored there w/ link for info)
            # print'href' because it is specified in a tag, this variable contains the link, print it in string datatype
            more_info = job.header.h2.a['href'].replace(' ', '')
            if unfamiliar_skill not in key_skills:
                # creating a file name to display the text values
                # use the 'w' to write within this new file, no longer read
                with open(f'posts/ {i}.txt', 'w') as f:
                    # '\n will break a line within the text file...making it more presentable within the file'
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills Required: {key_skills.strip()} \n")
                    f.write(f"Length of Job: {job_time.strip()} \n")
                    f.write(f"More information: {more_info.strip()}")

                    # provides an extra space for your displaying of information
                    print(f'File Saved: {i}')

# __name__ == '__main__' will 
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting: {time_wait} seconds...")
        time.sleep(time_wait*60)