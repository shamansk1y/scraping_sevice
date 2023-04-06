import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('work', 'dou', 'djinni')

headers =[
    {'User-Agent': 'Mozilla/5.0 Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4',
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5'
           },
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
     'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5'
     },
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
     'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5'
     },
]


def work(url):
    jobs = []
    errors = []
    domain = 'https://www.work.ua/'
    url = 'https://www.work.ua/jobs-kyiv-python/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='pjax-job-list')
        if main_div:
            div_list = main_div.find_all('div', attrs={'class': 'job-link'})
            for div in div_list:
                title = div.find('h2')
                href = title.a['href']
                content = div.p.text
                company = 'No name'
                logo = div.find('img')
                if logo:
                    company = logo['alt']
                jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})
    return jobs, errors

def rabota(url):
    pass
    # jobs = []
    # errors = []
    # domain = 'https://rabota.ua/'
    # resp = requests.get(url, headers=headers)
    # if resp.status_code == 200:
    #     soup = BS(resp.content, 'html.parser')
    #     table = soup.find('table', id='pjax-job-list')
    #     if table:
    #         div_list = table.find_all('div', attrs={'class': 'job-link'})
    #         for div in div_list:
    #             title = div.find('h2')
    #             href = title.a['href']
    #             content = div.p.text
    #             company = 'No name'
    #             logo = div.find('img')
    #             if logo:
    #                 company = logo['alt']
    #             jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company})
    #     else:
    #         errors.append({'url': url, 'title': 'Table does not exists'})
    # else:
    #     errors.append({'url': url, 'title': 'Page do not response'})
    # return jobs, errors


def dou(url):
    jobs = []
    errors = []
    # domain = 'https://jobs.dou.ua/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', id='vacancyListId')
        if main_div:
            li_list = main_div.find_all('li', attrs={'class': 'l-vacancy'})
            for li in li_list:
                title = li.find('div', attrs={'class': 'title'})
                href = title.a['href']
                cont = li.find('div', attrs={'class': 'sh-info'})
                content = cont.text
                company = 'No name'
                a = title.find('a', )
                logo = li.find('img', attrs={'class': 'company'})
                if a:
                    company = a.text
                if logo:
                    company = logo['alt']
                jobs.append({'title': title.text, 'url': href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})
    return jobs, errors


def djinni(url):
    jobs = []
    errors = []
    domain = 'https://djinni.co/'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_ul = soup.find('ul', attrs={'class': 'list-jobs'})
        if main_ul:
            li_list = main_ul.find_all('li', attrs={'class': 'list-jobs__item'})
            for li in li_list:
                title = li.find('div', attrs={'class': 'list-jobs__title'})
                href = title.a['href']
                cont = li.find('div', attrs={'class': 'list-jobs__description'})
                content = cont.text
                company = 'No name'
                comp = li.find('div', attrs={'class': 'list-jobs__details__info'})
                if comp:
                    company = comp.text
                jobs.append({'title': title.text, 'url': domain + href, 'description': content, 'company': company})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})
    return jobs, errors



if __name__=='__main__':
    url = 'https://djinni.co/jobs/?primary_keyword=Python&region=UKR'
    jobs, errors = djinni(url)
    h = codecs.open('../work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()