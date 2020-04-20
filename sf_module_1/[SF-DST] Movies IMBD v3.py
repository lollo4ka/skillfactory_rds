#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import itertools as itr
from collections import Counter
#print(os.listdir("../input"))


# In[4]:


data = pd.read_csv('/Users/alina/Code/skillfactory/data.csv')


# # Предобработка датасета

# In[5]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете
data['profit'] = data.revenue - data.budget


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[6]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
answer_ls.append(4)
data[data.budget == data.budget.max()]


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[974]:


answer_ls.append(2)
data.runtime.max()
data[data.runtime == data.runtime.max()]


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[975]:


answer_ls.append(3)
data[data.runtime == data.runtime.min()]


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[976]:


answer_ls.append(2)
data.runtime.mean()


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[977]:


answer_ls.append(1)
data.runtime.median()


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[978]:


answer_ls.append(5)
data['profit'] = data.revenue - data.budget
data[data.profit == data.profit.max()]


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[979]:


answer_ls.append(2)
data[data.profit == data.profit.min()]


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[980]:


answer_ls.append(1)

len(data[data.profit > 0])


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[981]:


answer_ls.append(4)
s = data[(data.release_year == 2008)]
s.profit == s.profit.max()
s.loc[600]


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[982]:


answer_ls.append(5)
year = data[(data.release_year >= 2012)&(data.release_year <= 2014)]
print(year.profit.min())
data['profit'].sort_values(ascending=True).head(10)
data.loc[1246]


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[984]:


answer_ls.append(3)


# In[983]:


pd.DataFrame(data.genres.str.split('|').to_list()).stack().value_counts()


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[985]:


answer_ls.append(3)


# In[962]:


profit = data[data.profit > 0]

pd.DataFrame(profit.genres.str.split('|').to_list()).stack().value_counts()


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[986]:


answer_ls.append(3)


# In[959]:


pd.DataFrame(data.director.str.split('|').to_list()).stack().value_counts()


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[987]:


answer_ls.append(4)


# In[198]:


profit = data[data.profit > 0]

flat_list = []
for sublist in profit.director.str.split('|'):
    for item in sublist:
        flat_list.append(item)

import collections
c = collections.Counter()
for director in flat_list:
    c[director] += 1
    
print(c.most_common(5))


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[988]:


answer_ls.append(5)


# In[958]:


grouped_df = data.groupby(['director'])['profit'].sum().sort_values(ascending=False)
display(grouped_df)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[989]:


answer_ls.append(1)


# In[956]:


pd.DataFrame(data.cast.str.split('|').to_list(), index=data.profit).stack().reset_index()[[0, 'profit']].groupby([0])['profit'].sum().sort_values(ascending=False)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[990]:


answer_ls.append(3)
new_data = data[data.release_year == 2012]
pd.DataFrame(new_data.cast.str.split('|').to_list(), index=new_data.profit).stack().reset_index()[[0, 'profit']].groupby([0])['profit'].sum().sort_values()


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[991]:


answer_ls.append(3)


# In[326]:


new_data = data[data.budget > data.budget.mean()]
high_budget_films = pd.DataFrame(new_data.cast.str.split('|').to_list()).stack()
high_budget_films.value_counts()


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[992]:


answer_ls.append(2)


# In[339]:


cage_films_ = pd.DataFrame(data.cast.str.split('|').to_list(), index=data.genres).stack().reset_index()[[0, 'genres']]
cage_films = cage_films_[cage_films_[0] == 'Nicolas Cage']
genre_cage_films = pd.DataFrame(cage_films.genres.str.split('|').to_list()).stack()
genre_cage_films.value_counts()


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[993]:


answer_ls.append(1)


# In[344]:


studio_films_ = pd.DataFrame(data.production_companies.str.split('|').to_list()).stack()
studio_films_.value_counts()


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[994]:


answer_ls.append(4)


# In[345]:


new_data = data[data.release_year == 2015]
studio_films_ = pd.DataFrame(new_data.production_companies.str.split('|').to_list()).stack()
studio_films_.value_counts()


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[995]:


answer_ls.append(2)


# In[448]:


production_split = pd.DataFrame(data.genres.str.split('|').to_list(), index=data.imdb_id)
reset_production = production_split.stack().reset_index()[[0, 'imdb_id']]
comedy_films = reset_production[reset_production[0] == 'Comedy']
comedy = comedy_films.merge(data, on='imdb_id', how='left')
comedy_split_production = pd.DataFrame(comedy.production_companies.str.split('|').to_list(), index=comedy.profit).stack().reset_index()[[0, 'profit']].groupby([0])['profit'].sum().sort_values()
comedy_split_production


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[996]:


answer_ls.append(3)


# In[358]:


new_data = data[data.release_year == 2012]

production_split = pd.DataFrame(new_data.production_companies.str.split('|').to_list(), index=new_data.profit)
reset_production = production_split.stack().reset_index()[[0, 'profit']]
max_profit_production = reset_production.groupby([0])['profit'].sum().sort_values(ascending=False)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[997]:


answer_ls.append(1)


# In[955]:


paramount_films_ = pd.DataFrame(data.production_companies.str.split('|').to_list(), index=data.original_title).stack().reset_index()[[0, 'original_title']]
paramount_films = paramount_films_[paramount_films_[0] == 'Paramount Pictures']
paramount = paramount_films.merge(data, on='original_title', how='left')
display(paramount[paramount.profit == paramount.profit.min()])


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[998]:


answer_ls.append(5)


# In[401]:


grouped_df = data.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(grouped_df)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[999]:


answer_ls.append(1)


# In[414]:


warner_bros_ = pd.DataFrame(data.production_companies.str.split('|').to_list(), index=data.original_title).stack().reset_index()[[0, 'original_title']]
warner_bros = warner_bros_[warner_bros_[0] == 'Warner Bros.']
warner_bros_film = warner_bros.merge(data, on='original_title', how='left')
grouped_df = warner_bros_film.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(grouped_df)


# In[569]:


warner_bros_ = pd.DataFrame(data.production_companies.str.split('|').to_list(), index=data.original_title).stack().reset_index()[[0, 'original_title']]
warner_bros_pic = warner_bros_[warner_bros_[0] == 'Warner Bros. Pictures']
warner_bros_all = warner_bros_[(warner_bros_[0] == 'Warner Bros. Pictures') | (warner_bros_[0] == 'Warner Bros.') ]
warner_bros_film = warner_bros_all.merge(data, on='original_title', how='left')
grouped_df = warner_bros_film.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(grouped_df)


# In[564]:


data[data['production_companies'].str.contains('Warner Bros')].groupby(['release_year'])[['profit']].sum().sort_values(['profit'],ascending=False)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[1000]:


answer_ls.append(4)


# In[1001]:


month = pd.DataFrame(data.release_date.str.split('/').to_list())
month[0].value_counts()


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[1002]:


answer_ls.append(2)


# In[1003]:


month = pd.DataFrame(data.release_date.str.split('/').to_list())
month_counts = month[0].value_counts()
month_counts['8'] + month_counts['7'] + month_counts['6']


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[1004]:


answer_ls.append(5)


# In[1005]:


month = pd.DataFrame(data.release_date.str.split('/').to_list(), index = data.original_title)
winter_month = month[(month[0] == "1") | (month[0] == "2") | (month[0] == "12") ]
winter_data = winter_month.merge(data, on='original_title', how='left')
winter_count = pd.DataFrame(winter_data.director.str.split('|').to_list()).stack().value_counts()
winter_count


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[1006]:


answer_ls.append(2)


# In[7]:


month = pd.DataFrame(data.release_date.str.split('/').to_list(), index = data.original_title)
new_month = month.merge(data, on='original_title', how='left')
grouped_df = new_month.groupby([0])['profit'].sum().sort_values(ascending=False)
grouped_df


# In[10]:


pivot = new_month.pivot_table(values=['profit'],
index=[0],
columns=[2],
aggfunc='sum',
margins=True)
pivot
#df = pivot.sort_values(['All'], ascending = False)
#df

df = pivot.reindex(pivot['profit'].sort_values(by='All', ascending=False).index)
df


# In[1017]:


new_month


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[1008]:


answer_ls.append(5)


# In[954]:


production = pd.DataFrame(data.production_companies.str.split('|').to_list(), index=data.original_title).stack().reset_index()[[0, 'original_title']]
production.columns = ['production', 'original_title']
production['name_len'] = production.original_title.str.len()
production.groupby(['production'])['name_len'].mean().sort_values(ascending=False)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[1009]:


answer_ls.append(5)


# In[953]:


production['len_words'] = production['original_title'].str.split().apply(len)
production.groupby(['production'])['len_words'].mean().sort_values(ascending=False)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[1010]:


answer_ls.append(3)


# In[685]:


data["new_title"] = map(lambda x:x.lower(), data.original_title )

ndata = data["new_title"].str.split()
films_words = set()

for row in ndata:
    for word in row:
        films_words.add(word)
        
len(films_words)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[1011]:


answer_ls.append(1)


# In[703]:


data[data.vote_average > data.vote_average.quantile(q=0.99)].sort_values(by=['vote_average'], ascending=False)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[1012]:


answer_ls.append(5)


# In[951]:


act3 = act.apply(lambda x: list(itr.combinations(x,2)), axis=1)
act3_frame = act3.reset_index()
act3_new_frame = pd.DataFrame(act3_frame[0].to_list(), index=act3_frame.imdb_id).stack().reset_index([0, 'imdb_id'])
act3_new_frame.columns = ['imdb_id', 'cast']
act3_new_frame.cast.value_counts()


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[1013]:


answer_ls.append(4)


# In[944]:


director_ = pd.DataFrame(data.director.str.split('|').to_list(), index = data.imdb_id).stack().reset_index([0,'imdb_id'])
director = director_.merge(data, on='imdb_id', how='left')

a = pd.DataFrame(director.groupby([0])['profit'].count()).reset_index()
a.columns = ['director', 'all_films']

profit = director[director.profit > 0]
b = pd.DataFrame(profit.groupby([0])['profit'].count()).reset_index()
b.columns = ['director', 'profit_films']

all_profit = a.merge(b, on='director', how='outer')
all_profit['result'] = (all_profit['profit_films'] / all_profit['all_films']) * 100
all_profit[all_profit.result == all_profit.result.max()]

df = all_profit.sort_values(['result', 'profit_films'], ascending = False)
df.head(10)


# # Submission

# In[1014]:


len(answer_ls)


# In[1015]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


# In[ ]:




