import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


job_title = []
company_name = []
location = []
job_skills = []
links =[]
job_req = []

page_num =0


while True:
    # Use requests to fetch URL
    result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=asp.net&start={page_num}")

    # Save the content of result into src
    src = result.content

    # Create a soup object to parse content of the page
    soup = BeautifulSoup(src, "lxml")
    page_limit = int(soup.find("strong").text)
    if(page_num > page_limit // 15):
        break

    job_titles = soup.find_all("h2", {"class": "css-m604qf"})
    company_names = soup.find_all("a",{"class": "css-17s97q8"})
    locations = soup.find_all("span", {"class":"css-5wys0k"})
    jobs_skills = soup.find_all("div",{"class":"css-y4udm8"})

    # extract needed info to lists
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find("a").attrs['href'])
        company_name.append(company_names[i].text)
        location.append(locations[i].text)
        job_skills.append(jobs_skills[i].text)
    page_num +=1


for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    resp = soup.find( "div", {"class":"css-1uobp1k"}).ul
    req = ""
    for li in resp.find_all("li"):
        req += li.text+","
    req = req[:-2]
    job_req.append(req)
file_list = [job_title, company_name, location, job_skills,job_req]
exported = zip_longest(*file_list)
with open("F:\Projects\WebScraping\Wuzzuf.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title", "company name","location","skills","Job Requirements"])
    wr.writerows(exported)

