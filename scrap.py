#################### WEB SCRAPING WITH PYTHON ##########################
import requests
from bs4 import BeautifulSoup
import time
from email.message import EmailMessage
import ssl
import smtplib
text = 'Enter the skill to search>>'
# allow the user to search the type of job they dont have the experience
unknown = 'Enter the skill to filter from the list>>'
def get_jobs():
# create a valriable url to store the website urls to scrip
     url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={text}&txtLocation='
#calling the request to the get the url to scrap and store the value in variable Get_url
     get_url = requests.get(url).content
     soup = BeautifulSoup(get_url, 'html.parser')
     jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
     for index,job in enumerate(jobs):
        add_index = index + 1
        publish_date = job.find('span', class_="sim-posted").span.text
        if 'days' in publish_date:
            company_name = job.find('h3', class_="joblist-comp-name").text
            more_info = job.header.h2.a['href']
            skill = job.find('span', class_="srp-skills").text.replace(' ', '')
            if unknown not in skill:
                email_sender = 'your google'
                email_password = 'your app password'
                # create the receiver variable to for the receiver account
                email_receiver = 'replace with the receiver email account'
                # create the message and the subject to be sent to the receiver 
                subject = 'New python job on timesjobs.com that may interest you'
                body='########## Python Developer job alert by PythonDev ############\n\n' \
                f'COMPANY NAME:{company_name.strip()}\n' \
                f'SKILLS:{skill.strip()} \n' \
                f'PUBLISH DATE:{publish_date}\n' \
                f'LINK DETAILS:{more_info}' 
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['subject'] = subject
                em.set_content(body)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender,email_receiver, em.as_string())
if __name__ == '__main__':
    while True:
        get_jobs()
        Time_out = 60
        print(f'wait {Time_out} minutes for another one to load...')
        time.sleep(Time_out * Time_out)