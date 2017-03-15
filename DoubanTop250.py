import requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient as mc

douban_url='http://movie.douban.com/top250'

def download_page(url):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'}
    data=requests.get(url, headers=headers).content
    return data

def parse_html(html):
    """ save parsed html information to dict and return"""
    data={}
    soup=bs(html)
    movie_list_soup=soup.find('ol', attrs={'class': 'grid_view'})
    for movie_li in movie_list_soup.find_all('li'):
        detail=movie_li.find('div', attrs={'class':'hd'})
        movie_name=detail.find('span',attrs={'class': 'title'}).getText()
        detail_pic=movie_li.find('div', attrs={'class':'pic'})
        movie_pic=detail_pic.find('a').img['src']
        data[movie_name]=str(movie_pic)
    return data

def download_img(img_dict):
    """ download a dictionary of images """
    i=0.0
    for key, value in img_dict.iteritems():
        i+=1.0
        perc=i/float(len(img_dict))*100
        with open('temp_img/'+key+'.jpg', 'wb') as file:
            file.write(requests.get(value).content)
        print '%.2f%% completed' % perc

def save(data):
    data['_id']=data['']


def main():
    html=download_page(douban_url)
    data=parse_html(html)
    download_img(data)

if __name__=="__main__":
    main()
