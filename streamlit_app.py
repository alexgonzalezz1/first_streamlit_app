import streamlit
import pandas 

streamlit.title('My parents New healthy Diner')

streamlit.header('🥣Menú de desayuno')
streamlit.text('🥗Omega 3 y avena con arándanos')
streamlit.text('🐔Batido de col rizada, espinacas y rúcula')
streamlit.text('🥑🍞Huevo duro de gallinas camperas')

streamlit.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include 

# Display the table on the page.

streamlit.header("Fruityvice Fruit Advice!")


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")



# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

