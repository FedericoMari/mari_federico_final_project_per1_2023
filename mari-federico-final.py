# this file was created by Federico Mari on 11/16/2023

'''sources: "freeCodeCamp.org" (greate YT channel with a 1 hour tutorial on web-scraping), "The Nature of Code", 
"How To Automate The Boring Stuff With Python'''

# title: "Architectural Jobs Right For You"

'''1st Goal: Find a job-listing website and screeen scrape its contents (jobs, companies, more info, possibly contract time and location, will have to see) 
using the directions from 'How to Automate the Boring Stuff With Python' and my youtube video source code
    2nd Goal: Display the contents of the screen scraper within a separate terminal, not default vscode... (tkinter?)
'''
# parses HTML or the format in which web pages are written in
from bs4 import BeautifulSoup
# downloads the desired files and pages from the internet
import requests
import os 
import time
from os import *

# define the output file for the text products:
# file = "jobs_list.txt"

#user could provide some information to specify the job 
print("Specify the skills you are unfamiliar with...")
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
    # provide a for loop to validate whether jobs exist in the job_list from above^
    for index, job in enumerate(jobs):
        publishing_date = job.find('span', class_= "sim-posted").span.text
        # define a condition, to know if the jobs were recently posted or not, use the keyword 'few' to search for these recent jobbs
        if 'few' in publishing_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
            # job_time = job.find().replace(' ', '')
            # job_location = job.find('span', class_ = '')
            key_skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            # first tag or top tag on the website format:
            # travel to header, then to h2 tag, and finally to the a tag(information is stored there w/ link for info)
            # print'href' because it is specified in a tag, this variable contains the link, print it in string datatype
            more_info = job.header.h2.a['href'].replace(' ', '')
            # conditional statement to discern whether the skill you do not know is not in the required job skills for each company
            if unfamiliar_skill not in key_skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    # creating a file name to display the text values
                    # use the 'w' to write within this new file, no longer read
                    # '\n will break a line within the text file...making it more presentable within the file'
                    # could use f.write in front to write on a separate file
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Skills Required: {key_skills.strip()}")
                    # print(f"Location: {job_location.strip()} \n")
                    # print(f"Length of Job: {job_time.strip()} \n")
                    f.write(f"More information: {more_info}")
                    # adds separations between each data display for the job info:
                    print(f'File Saved: {index}')

# __name__ == '__main__' will check whether the current script is being run in the program, then calls the main() func to execute the code
if __name__ == '__main__':
    while True:
        # call back main functions 
        find_jobs()
        time_wait = 10
        print(f"Waiting: {time_wait} minutes...")
        time.sleep(time_wait*60)