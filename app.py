import streamlit as st
import pickle

mov_info = pickle.load(open('movies.pkl',"rb"))
mov_list = mov_info['title'].values
similarity = pickle.load(open('similarity.pkl',"rb"))

def recommender(movie):
    index = mov_info[mov_info['title'] == movie].index[0]
    
    sim_list = sorted(list(enumerate(similarity[index])),reverse=True,key= lambda x:x[1])[1:6]
    
    rec_movies = []
    for i in sim_list:
        rec_movies.append(mov_info.loc[i[0]].title)
    
    return rec_movies

st.title("Movie Recommender System")  

selected_movie = st.selectbox("Select Movie",mov_list)

if st.button("Recommend"):

    for i in recommender(selected_movie):
        st.write(i)
