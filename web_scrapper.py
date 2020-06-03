#!/usr/bin/env python
# coding: utf-8

# In[16]:


from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in soup.find_all('article'):

#print(soup.prettify())

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div',class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe',class_='youtube-player')['src']
        print(vid_src)

        vid_id = vid_src.split('/')[4]
        print(vid_id)
        vid_id = vid_id.split('?')[0]
        print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'
        
    except Exception as e:
        yt_link = None
    
    print(yt_link)
    
    print()
    
    csv_writer.writerow([headline,summary,yt_link])
    
csv_file.close()


# In[ ]:




