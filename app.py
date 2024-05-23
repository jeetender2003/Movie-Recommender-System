import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id) :
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MjczODU4NTljY2VkMWMxOWJkOGY2M2U4MDZiYWNiOCIsInN1YiI6IjY2NGRmOTlmYmVmM2M4YmFkYmZkMWE3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pyNcDnqkGf4nlwcr9buuBGKtfXcyyMarfudCcqx5r5g"
    }

    response = requests.get(url, headers=headers)

    print(response.json)
    data = response.json()
    return "https://image.tmdb.org/t/p/w780/" + data['poster_path']


def recommend(movie) :
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list :
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_movies_poster.append(fetch_poster(movie_id))

    print(recommended_movies)
    print(recommended_movies_poster)
    return recommended_movies,recommended_movies_poster

movies = pd.read_pickle(open('movies.pkl','rb'))
similarity = pd.read_pickle(open('similarity.pkl','rb'))


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'])


if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


