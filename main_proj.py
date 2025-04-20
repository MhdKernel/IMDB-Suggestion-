# ----  imports  ----

import csv
import nltk
import numpy 
import math

# ---- -------  ----

# ---- stop words list ----

stopwords = nltk.corpus.stopwords.words('english')
stopwords_2 = ['!' , '(' ,')' , '-' , '[' , ']' , '{' , '}' , ';' , "'" , '"' , "," , '<' , '>' , '.' , '/' , '?' , '@' , '#' , '%' , '^' , '&' , '*' , '_' , '~' , '$']

# ---- ---- ----- --- ----

# ---- dicts ----

sim_movies = {}
c_data = {}

# ---- ---- ----

# ---- files ----

with open('data.csv' , 'r') as datas:
    csv_reader = csv.reader(datas)
    d_data = dict(csv_reader)

# ---- ---- ----

# ---- functions ----

def cleaning(dirty_data , clean_data): #removing stop words
    for data in dirty_data:
        movie_description = dirty_data[data]
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
        clean_data[data] = movie_description_li

def main_def(words , clean_data): # main function
    tf_idf_lists = []
    for word in words:
        idf = tf_idf(word , c_data , 0 , 0) # calculate idf
        tf_idf_list = []
        for data in clean_data:
            num = c_data[data]
            tf = tf_idf(word , 0 , num , 1) # calculate tf 
            tf_idf_list.append(tf*idf)
        tf_idf_lists.append(tf_idf_list)
    return numpy.transpose(numpy.array(tf_idf_lists))

def tf_idf(words , clean_data  , nums , id): 
    if id == 0: # calculate idf
        counter = 0
        for movie_des in clean_data:
            movie_des = clean_data[movie_des]
            if words in movie_des:
                counter += 1
        return math.log10((250/counter))+1
    
    elif id == 1: #calculate tf
        count = nums.count(words)
        count_2 = len(nums)
        return count/count_2

def similarity(numpy_d , s_movie):
    for index_movie , movie in enumerate(numpy_d):
        second_part = numpy.linalg.norm(numpy_d[-1]) * numpy.linalg.norm(movie) # calculate cosine similarity
        similarity_percent = numpy.dot(numpy_d[-1] , movie) / second_part
        c_data_list = list(c_data)[index_movie]
        s_movie[c_data_list] = similarity_percent
        movie_sorted_by_sim = sorted(sim_movies.items(), key=get_value, reverse=True)
        similar_movie_dict = dict(movie_sorted_by_sim)
    
    print('if you copy plot from site the first one is your movie name')
    print('You can also watch this movies : ')
    for movie in list(similar_movie_dict.keys())[1:7]:
        print(f'{movie} : {similar_movie_dict[movie]}')
        
def get_value(item):
    return item[1]

# ----  --------  -----

 
cleaning(d_data ,c_data) #clean datas

user_movie = input('Enter Your Movie summery : ')
user_movie_dict = {'user_movie' : user_movie}
cleaning(user_movie_dict , c_data) #add user entry to dict

set_of_words = set() # remove sim
for summary in c_data.values():
    set_of_words.update(summary)
final_list = sorted(set_of_words)

numpy_datas = main_def(final_list , c_data)
similarity(numpy_datas , sim_movies)