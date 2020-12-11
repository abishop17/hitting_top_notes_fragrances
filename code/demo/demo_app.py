# ref: https://github.com/upraneelnihar/streamlit-multiapps

# from multiapp import MultiApp
# from apps import home, explore

import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Let's make a fragrance!",
    # page_icon=":-)",
    layout="wide",
    initial_sidebar_state="expanded")

@st.cache
def load_data():
    df = pd.read_csv('data/austen_poe.csv')
    return df

# st.title('Fragrance')


# app = MultiApp()

# # Applications
# app.add_app("Home", home.app)
# app.add_app("Explore", explore.app)

# # The main app
# app.run()

# # import streamlit as st
# # from multiapp import MultiApp
# # from apps import home, data_stats # import your app modules here

# # app = MultiApp()

# # # Add all your application here
# # app.add_app("Home", home.app)
# # app.add_app("Data Stats", data_stats.app)

# # # The main app
# # app.run()