import streamlit
import pandas as pd
import requests

# First steps: adding text and that kind of stuff

streamlit.title('My Parents New Healthy Dinner')
# streamlit.header('Breakfast Menu:')
# streamlit.text('Omega & Blueberry Oatmeal')
# streamlit.text('Kale, Spinach & Rocket Smoothie')
# streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Breakfast Favourites!! ')
streamlit.text('🥣 Omega & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Secondly: importing pandas and reading a text file

url_fruit_macros = "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
my_fruit_list = pd.read_csv(url_fruit_macros)
my_fruit_list = my_fruit_list.set_index('Fruit')    # put the fruit column as index to have a cleaner view

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

# Display the table on the page.
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#now we make querys with the python package request
url_petition = "https://fruityvice.com/api/fruit/"
# We NO LONGER HARDCORE THIS:
# fruityvice_response = requests.get(url_petition + "Kiwi")
fruityvice_response = requests.get(url_petition + fruit_choice)

# we take the json and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# we put the output as a dataframe table
streamlit.dataframe(fruityvice_normalized)


