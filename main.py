import streamlit as st
from utils import *

st.title('Movies recommender')
st.write('Welcome to my movies recommender app! Take a look of the movies catalog that I have:')
st.write(df.title)
title = st.text_input('Type a movie that you have enjoyed from the list and I will recommend you some similar', 'The Lion King')
lkcr=content_recommender(title)
st.write(lkcr)
ind = st.text_input('Type the index of one of the suggested movies to see the movie description','892')
if ind:
	st.write('Here you have the description of the movie that you have choosen:')
	st.write(df.loc[lkcr.index].overview.loc[int(ind)])