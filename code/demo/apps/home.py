
import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
from annotated_text import annotated_text

from functions import make_a_fragrance

st.set_page_config(
        page_title="Fragrance maker!",
        initial_sidebar_state='expanded')
st.beta_container()
# def app():
st.title('Home page')
@st.cache
def load_data():
    demo_df = pd.read_csv('../../../data/data_subsets/demo/demo_df.csv')
    return demo_df

st.title("Let's make a fragrance and predict the customer rating!")

st.image('../../../figures/vibe_setters/cropped_flowers_melons_@_positivity on @fruitassembly IG.png')
st.text('Image source: @_positivity on @fruitassembly IG')

# Read in the pickle file of the fitted model
with open('../../../models/logreg.pkl', 'rb') as pickle_in:
    logreg_from_pkl = pickle.load(pickle_in)

top_notes_demo_orig_and_sani = {'top_0_amalfi_lemon': 'Amalfi lemon',
                                'top_0_pink_grapefruit': 'Pink grapefruit',
                                'top_1_watermelon': 'Watermelon',
                                'top_1_mint': 'Mint',
                                'top_1_earl_grey_tea': 'Earl grey tea',
                                'top_1_champagne': 'Champagne',
                                'top_1_creme_brulee': 'Creme brulee',
                                'top_1_pepper': 'Pepper',
                                'top_1_nutmeg': 'Nutmeg',
                                'top_1_teak_wood': 'Teakwood',
                                'top_1_pine_needles': 'Pine needles',
                                'top_1_mountain_air': 'Mountain air'}

# Set feature space (original names)
top_notes_demo = ['top_0_amalfi_lemon',  'top_0_pink_grapefruit', 'top_1_watermelon',
                  'top_1_mint', 'top_1_earl_grey_tea', 'top_1_champagne', 'top_1_creme_brulee',
                  'top_1_pepper', 'top_1_nutmeg', 'top_1_teak_wood', 'top_1_pine_needles', 'top_1_mountain_air']


# Set radio buttons for feature input (one top note only)
top_note_selection = st.radio(label = 'Select a top note',
                  options = ['Amalfi lemon', 'Pink grapefruit', 'Watermelon', 'Mint',
       'Earl grey tea', 'Champagne', 'Crème brûlée', 'Pepper', 'Nutmeg',
       'Teakwood', 'Pine needles', 'Mountain air'])

### accessing original vs. sanitized top_note name
# option = st.selectbox("selectbox 2", list(options.items()), 0 , format_func=lambda o: o[1])
# option[0]

# st.write(top_note_selection)
st.subheader('Your fragrance is below!')
st.write("If you don't care for this one, just click another radio button above and the middle and base notes will generate randomly.")

# ref: https://github.com/tvst/st-annotated-text

# st.title(
#     annotated_text(
#     (make_a_fragrance(top_note_selection)[0], "(top note)", "#97f0e3"),
#     (make_a_fragrance(top_note_selection)[1], "(middle note)", "#fd7c6e"),
#     (make_a_fragrance(top_note_selection)[2], "(base note)", "#ace5ee")
    
#     ))

# Read in the pickle file of the fitted model
with open('../../../data/data_subsets/demo/synth_df.pkl', 'rb') as pickle_in:
    synth_df_from_pkl = pickle.load(pickle_in)


# Predict the rating 
predicted_rating = logreg_from_pkl.predict(synth_df_from_pkl)

st.subheader(f'Your fragrance will likely get an average rating of {predicted_rating[0]}')

# Get user text, save it
st.write('If you were offered a sample of this fragrance, would you wear it?')

user_text = st.text_input('Wear the sample offered?', 
              value = "Yes I'd totally try this!")


page = st.sidebar.selectbox(
    'Page',
    ('About', 'Explore', 'Make a fragrance', 'Predict customer rating')
)
if page == 'About':
    st.subheader('About this project')
    st.write('This is an ongoing project initiated as a capstone project for my General Assembly Data Science Intensive coursework.')
elif page == 'EDA':
    st.subheader('Explore the data')
elif page == 'Make a fragrance':
    st.subheader('Make a fragrance')
    st.subheader('What scent family would you like for your fragrance?')
    st.write("Top notes form customers' initial impression of a fragrance. That's what you will select today.")
    st.write("FYI, middle notes and base notes form the body of a fragrance and slowly unfold once the top notes evaporate. Due to data constraints, these notes will be randomly assigned out of the existing feature space (fragrances already on the market).")
elif page == 'Predict customer rating':
    st.subheader('Predict customer rating for your fragrance!')