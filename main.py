import pickle

import pandas as pd
import streamlit as st
import requests
import bz2
import pickle
import _pickle as cPickle

def fetch_poster(mv_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c2665c794d9e9995cae79259213f9852&language=en-US'.format(mv_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

  recommended_movies = []
  recommended_movies_posters = []
  for i in movies_list:
      mv_id = movies.iloc[i[0]].id
      recommended_movies.append(movies.iloc[i[0]].title)
      recommended_movies_posters.append(fetch_poster(mv_id))
  return recommended_movies,recommended_movies_posters


def recommend_for(userId, title):
    index_of_movies = pd.Series(movies.index, index=movies['title']).drop_duplicates()
    index_map = movie_id.set_index('id')
    index = index_of_movies[title]
    tmdbId = movie_id.loc[title]['id']

    # content based
    sim_scores = list(enumerate(similarity[int(index)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:100]
    movie_indices = [i[0] for i in sim_scores]

    mv = movies.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'id']]
    mv = mv[mv['id'].isin(movie_id['id'])]
    print(mv)
    # CF
    mv['est'] = mv['id'].apply(lambda x: svd.predict(userId, index_map.loc[x]['movieId']).est)
    mv = mv.sort_values('est', ascending=False)

    return mv.head(10)


def popular():
    pop = movies.sort_values('popularity', ascending=False)
    return pop[['title','popularity']].head(10)

svd =  pickle.load(open('svd.pkl','rb'))

movie_id = pickle.load(open('moviesid.pkl','rb'))

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)


def decompress_pickle(file):
 data = bz2.BZ2File(file, 'rb')
 data = cPickle.load(data)
 return data

#similarity = pickle.load(open('similarity.pkl','rb'))
similarity = decompress_pickle('Similarity.pbz2')
#similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender')

userId = st.number_input('User Id', min_value=None, max_value=None, value=0, step=1)

selected_movie_name = st.selectbox(
     'Search',
     movies['title'].values)



if st.button('Recommend'):


     popularmvs = popular()
     ppmv = popularmvs.title
     pmv = ppmv.to_dict()
     pms = []
     posterset = []
     for pm in pmv.values():
         mv_id = movie_id.loc[pm]['id']
         pms.append(pm)
         posterset.append(fetch_poster(mv_id))
     names2 = pms
     posters2 = posterset
     st.header('POPULAR MOVIES')
     #for l in pms:
         #st.write(l)
     col1, col2, col3, col4, col5 = st.columns(5)
     y = 0
     for clm in st.columns(5):
         with clm:
             st.text(names2[y])
             st.image(posters2[y])
             y = y + 1

     for clm in st.columns(5):
         with clm:
             st.text(names2[y])
             st.image(posters2[y])
             y = y + 1


     names,posters= recommend(selected_movie_name)
     st.header('CONTENT BASED')
     col1, col2, col3, col4, col5= st.columns(5)
     v=0
     for c in st.columns(5):
            with c:
                st.text(names[v])
                st.image(posters[v])
                v=v+1

     for c in st.columns(5):
            with c:
                st.text(names[v])
                st.image(posters[v])
                v=v+1

     #names1= recommend_for(userId,selected_movie_name)
     recos = recommend_for(userId,selected_movie_name)
     #recs = recos['title'].todict()
     recs = recos.title
     recomdns = recs.to_dict()
     cfrecs = []
     posters = []
     for cfr in recomdns.values():
         cfrecs.append(cfr)
         mv_id = movie_id.loc[cfr]['id']
         posters.append(fetch_poster(mv_id))
     names1 = cfrecs
     posters1 = posters
     var = len(posters1)

     st.header('COLLABORATIVE FILTERING')
     #for k in cfrecs:
       #  st.write(k)
    # st.write(cfrecs)
    # st.write(recomdns.values())
     #st.write(recos.values)
     #for j in recos:
        #st.write(j)
     col1, col2, col3, col4, col5 = st.columns(5)
     z = 0
     for co in st.columns(5):
         with co:
             st.text(names1[z])
             st.image(posters1[z])
             z = z + 1

     for co in st.columns(5):
         with co:
             st.text(names1[z])
             st.image(posters1[z])
             z = z + 1
             if (z == var):
                 break







