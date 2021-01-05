 1 import requests
 2 from bs4 import BeautifulSoup
 3 from csv import writer
 4 
 5 response = requests.get('http://codedemos.com/sampleblog/')
 6 
 7 soup = BeautifulSoup(response.text, 'html.parser')
 8 
 9 posts = soup.find_all(class_='post-preview')
 10 
 11 with open('posts.csv', 'w') as csv_file:
 12 csv_writer = writer(csv_file)
 13 headers = ['Title', 'Link', 'Date']
 14 csv_writer.writerow(headers)
 15 
 16 for post in posts:
 17     title = post.find(class_='post-title').get_text().replace('\n', '')
 18     link = post.find('a')['href']
 19     date = post.select('.post-date')[0].get_text()
 20     csv_writer.writerow([title, link, date])
 21
