import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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


# we make a function!
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get(url_petition + fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  # we take the json and normalize it
  return fruityvice_normalized

# making this a try sentence!
url_petition = "https://fruityvice.com/api/fruit/"
streamlit.header("Fruityvice Fruit Advice!")
try:
  # We get rid of the default option:
  # fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

 
except URLError as e:
  streamlit.error()
 


# SNOWFLAKE CONECTION:
streamlit.header("The fruit load contains:")

# Snowflake related functions:
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
# add a button to load the fruit:
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data = get_fruit_load_list()
  streamlit.dataframe(my_data)


##########################################
# WE STOP THE EXECUTION HERE 
# streamlit.stop()
##########################################

# ADDING THINGS!!!!!!!
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('from streamlit')")
    return 'Thanks for adding ' + new_fruit

fruit_choice = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(fruit_choice)
  streamlit.text(back_from_function)
  



