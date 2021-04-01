import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# Use requests to fetch URL
result = requests.get("https://wuzzuf.net/search/jobs/?q=asp.net&a=hpb")

# Save the content of result into src
src = result.content

# Create a soup object to parse content of the page
soup = BeautifulSoup(src, "lxml")
print(soup)

job_titles = soup.find_all("a", {"class":"css-m604qf"})
