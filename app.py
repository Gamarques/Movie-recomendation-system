import pickle 
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7036a5d62c096f4eca7581c5dd19db4e&&language=en-US".format(movie_id)

    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original" + poster_path


    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.header("Movie Recommendation System Using Machine Learning")
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Select a movie or type the tittle to get a recommendation',
    movie_list
)

def get_movie_id(movie_name):
    movie_row = movies.loc[movies['title'] == movie_name]
    return movie_row.iloc[0]['movie_id']

if st.button('Show_recomendation'):
   movieId = get_movie_id(selected_movie)
   poster= fetch_poster(movieId)
   st.image(poster)