from bs4 import BeautifulSoup
import csv
import lxml
import requests
import time
import re

def write_csv(data):
    with open('mash.csv', 'a')as f:
        writer = csv.writer(f)
        writer.writerow([data['title'], data['price'], data['image'], data['description'], data['date']])



def find_mashina(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    mashinas = soup.find_all('div', class_ = 'list-item list-label')
    
    for mashina in mashinas:
        name_m = mashina.find('h2', class_ = 'name').text.replace(' ', '').replace('\n', '')
        price_m = mashina.find('strong').text
        image_tag = mashina.find('img', class_ = 'lazy-image')
        if image_tag== None:
             image_tag= 'no image'
        else:
             image_tag = image_tag.get('data-src')
        description = re.sub(r'\s+', ' ',mashina.find('div', class_ = 'block info-wrapper item-info-wrapper').text).strip()
        published_date = mashina.find('span', class_ = 'date').text.replace(' ', '')
        dict_ = {'title': name_m, 'price': price_m, 'description':description,'image': image_tag, 'date': published_date}
        write_csv(dict_)
        


def main():
     for i in range(1,5):
          url = f'https://www.mashina.kg/search/all/?page={i}'
          find_mashina(url)


if __name__ == '__main__':
    main()

#Помогите пожалуйста 