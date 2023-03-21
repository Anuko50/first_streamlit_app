import streamlit
import pandas as pd

# First steps: adding text and that kind of stuff

streamlit.title('My Parents new healthy dinner')
streamlit.header('Breakfast Menu:')
streamlit.text('Omega & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Breakfast Favourites!! ')
streamlit.text('🥣 Omega & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Secondly: importing pandas and reading a text file

url_fruit_macros = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_fruit_list = pd.read_csv(url_fruit_macros)
streamlit.dataframe(my_fruit_list)
