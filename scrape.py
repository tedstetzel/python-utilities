import csv
import requests
from BeautifulSoup import BeautifulSoup

#test comment

pages = ['https://symphonycommerce.com/page1' 'https://symphonycommerce.com/page2']

ids = ['800374','800108']

i = 0 

while i < len(pages):

	url = pages[i]
	id = ids [i]
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('div', attrs={'id': 'FeedingGuidelines'})
	i = i + 1

	# open a csv file with append, so old data will not be erased
	with open('index_1.csv', 'a') as csv_file:  
		writer = csv.writer(csv_file)
		writer.writerow([url,table])
	
    