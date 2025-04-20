import requests
from bs4 import BeautifulSoup
import csv
import nltk

stopwords = nltk.corpus.stopwords.words('english')
stopwords_2 = ['!' , '(' ,')' , '-' , '[' , ']' , '{' , '}' , ';' , "'" , '"' , "," , '<' , '>' , '.' , '/' , '?' , '@' , '#' , '%' , '^' , '&' , '*' , '_' , '~']

# print(stopwords)

header = {'user_agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
respone = requests.get('https://m.imdb.com/chart/top/',headers=header)
soup = BeautifulSoup(respone.content , 'html.parser')
movies_link = []
print(respone)
for movies in soup.find_all('a'):
    try:
        if 'ipc-title-link-wrapper' in movies['class']:
            movies_link.append(movies['href'])
    except:
        pass
    
for i in range(8):
    if movies_link[-1] == '/title/tt1954470/?ref_=chttp_t_250':
        break
    movies_link.pop(-1)

# for n in movies_link:
#     print(n)

csv_file = open('data.csv' , 'w' , encoding= ' utf-8' , newline='')
csv_writer = csv.writer(csv_file)

counter = 1
for movie_link in movies_link:
    movie_link = 'https://m.imdb.com' + movie_link
    respone = requests.get(movie_link , headers=header)
    soup = BeautifulSoup(respone.content , 'html.parser')
    movie_name = soup.find('span' , {'class' : "hero__primary-text"}).text
    movie_description = soup.find('span' , {'class' : 'sc-7193fc79-1 jgFQCx'}).text 
    for stopword_2 in stopwords_2:
        if stopword_2 in movie_description:
            movie_description = movie_description.replace(stopword_2 , '')
    
    movie_description = movie_description.lower()
    movie_description_li = movie_description.split(' ')
    counter_2 = 0
    while True:
        if counter_2 == len(movie_description_li) - 1:
            if movie_description_li[counter_2] in stopwords:
                movie_description_li.remove(movie_description_li[counter_2])
                break
            else:
                break
        else:
            if movie_description_li[counter_2] in stopwords:
                movie_description_li.remove(movie_description_li[counter_2])
            else:
                counter_2 += 1
    movie_description = ' '.join(movie_description_li) 
    
    print(f'{counter} : {movie_name} => {movie_description}')
    csv_writer.writerow([movie_name , movie_description])
    counter += 1

