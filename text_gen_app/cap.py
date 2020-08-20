import streamlit as st
from app_functs import *

#code for streamlit app

st.title('Hello welcome to the A.I. Lyric Generation')

# select genre to create lyrics for
st.sidebar.markdown('### What genre would you like me to use')
genre_opt = st.sidebar.radio(
	'',
	['Pop', 'Rock', 'Rap', 'Country'])

# slider option for user to choose temerature
st.sidebar.markdown('### Wacky Meter')
st.sidebar.markdown('#### Slide bar higher for odder lyrics')
st.sidebar.markdown('#### Slide bar lower for more predictive lyrics')
temp = st.sidebar.slider('temperature', .2, 2.0, .7)

# sets what to do if user chooses pop genre
if genre_opt == 'Pop':

	# format blank space
	st.markdown('')
	st.markdown('')

	# format larger label
	st.markdown('#### Please enter a word or phrase...')
	# ask user for a word
	starting_phrase = st.text_input(
	'')

	#when user inputs phrase, creates song based on it
	if starting_phrase:

			song = pop(starting_phrase.lower(), temp)

			st.markdown(song)

# sets what to do if user chooses rock genre
elif genre_opt == 'Rock':

	# blank space
	st.markdown('')
	st.markdown('')

	# format larger label
	st.markdown('#### Please enter a word or phrase...')
	# ask user for a word or phrase
	starting_phrase = st.text_input(
	'')

	#when user inputs phrase, creates song based on it 
	if starting_phrase:

			song = rock(starting_phrase.lower(), temp)

			st.markdown('')
			st.markdown(song)

# chooses what to do if user chooses rap genre
elif genre_opt == 'Rap':

	# blank space
	st.markdown('')
	st.markdown('')

	# format larger label
	st.markdown('#### Please enter a word or phrase...')
	# ask user for a word or phrase
	starting_phrase = st.text_input(
	'')

	#when user inputs phrase, creates song based on it
	if starting_phrase:

			song = rap(starting_phrase.lower(), temp)

			st.markdown('')
			st.markdown(song)
			
elif genre_opt == 'Country':

	# blank space
	st.markdown('')
	st.markdown('')

	# format larger label
	st.markdown('#### Please enter a word or phrase...')
	# ask user for a word or phrase
	starting_phrase = st.text_input(
	'')

	# when user inputs phrase, creates song based on it
	if starting_phrase:

			song = country(starting_phrase.lower(), temp)

			st.markdown('')
			st.markdown(song)
			
