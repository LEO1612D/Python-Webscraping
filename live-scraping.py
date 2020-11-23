from bs4 import BeautifulSoup
import requests

job_title = input('Please enter job title').split()


html_text = requests.get('https://in.linkedin.com/jobs/search?keywords='+job_title[0]+'+%20+'+job_title[1]+'+&location=Vadodara%2C%20Gujarat%2C%20India&geoId=106728703&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0').text

soup = BeautifulSoup(html_text,'lxml')

job_cards = soup.findAll('div',class_='job-result-card__contents')

for data in job_cards:
    print(f'Job Of {data.h3.text} \n In {data.h4.text}  {data.div.time.text} \n')
    