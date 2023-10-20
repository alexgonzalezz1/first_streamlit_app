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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])


streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 

# Display the table on the page.
