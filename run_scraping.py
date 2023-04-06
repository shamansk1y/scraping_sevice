import codecs

from scraping.parsers import *
from scraping.models import Vacancy, City, Language


parsers = (
    (work, 'https://www.work.ua/jobs-kyiv-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?category=Python'),
    (djinni, 'https://djinni.co/jobs/?primary_keyword=Python&region=UKR')
)

city = City.objects.filter(slug='kiev')

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()