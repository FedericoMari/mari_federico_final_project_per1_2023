# this file was created by Federico Mari on 11/16/2023

''' sources: "freeCodeCamp.org" (greate YT channel with a 1 hour tutorial on web-scraping and will be my base-code), "The Nature of Code", 
"How To Automate The Boring Stuff With Python (for general practicality and usage)" '''

# title: "Architectural Jobs Right For You"

''' Goal: Find a job-listing website and screeen scrape its contents (jobs, companies, more info, possibly contract time and location, will have to see) 
using the directions from 'How to Automate the Boring Stuff With Python' and my youtube video source code
'''
# import all libraries: 

# most essential library for screen scraping
from bs4 import BeautifulSoup
# downloads the desired files and pages from the internet link
import requests
from os import path 
import time

#user could provide some information to specify the job 
print("Specify the skills you are unfamiliar with...")
# define unfamiliar skill variable and filter the key string word out from the parsed code
unfamiliar_skill = input('>')
# will filter out/remove the input provided by the user...
print(f"Filtering out: {unfamiliar_skill}")

def find_jobs():
    # get specific info from a we bsite, include website url as string using the requests library
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Architectural+Design%22&txtKeywords=%22Architectural+Design%22&txtLocation=').text

    '''parse the html file (format in which pages are written in) with lxml, will edit the 'parse tree' (hierarchy of elements within the code and relationship between them) 
    of a python function and make it executable in the code'''
    soup = BeautifulSoup(html_text, 'lxml')
    # for this job website accumulate all the jobs (first element of find_all func is the item tags, then the class_ from html)
    # located underneath the 'ul' tag (unordered list with 'li')
    # use find_all() func to list all the jobs in website 
    jobs = soup.find_all('li', class_= "clearfix job-bx wht-shd-bx")
    # apply results for jobs in the code
    for job in jobs:
        publishing_date = job.find('span', class_= "sim-posted").span.text
        # define a condition, to know if the jobs were recently posted or not, use the keyword 'few' to search for these recent jobs
        if 'few' in publishing_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
            key_skills = job.find('span', class_ = "srp-skills").text.replace(' ', '')
            # first tag or top tag on the website format:
            # travel to header, then to h2 tag, and finally to the a tag(information is stored there w/ link for info)
            # print'href' because it is specified in a tag, this variable contains the link, print it in string datatype
            more_info = job.header.h2.a['href'].replace(' ', '')
            if unfamiliar_skill not in key_skills:
                    # '\n will break a line within the text file...making it more presentable within the file'
                    # could use f.write in front to write on a separate file
                    print(f"Company Name: {company_name.strip()} \n")
                    print(f"Skills Required: {key_skills.strip()}")
                    print(f"More information: {more_info.strip()}")

                    # provides an extra space for your displaying of information in between each info for the company
                    print('')

# __name__ == '__main__' will check whether the current script is being run in the program, then calls the main() func to execute the code
if __name__ == '__main__':
    while True:
        # call back main functions
        find_jobs()
        time_wait = 10
        print("You may now consider your options...")
        print(f"Waiting: {time_wait} minutes...")
        time.sleep(time_wait*60)