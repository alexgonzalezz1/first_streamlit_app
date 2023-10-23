import streamlit
import pandas 
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My parents New healthy Diner')

streamlit.header('🥣Menú de desayuno')
streamlit.text('🥗Omega 3 y avena con arándanos')
streamlit.text('🐔Batido de col rizada, espinacas y rúcula')
streamlit.text('🥑🍞Huevo duro de gallinas camperas')

streamlit.header('🍌🥭 Prepara tu propio batido de frutas 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# Let's put a pick list here so they can pick the fruit they want to include

# Display the table on the page.

streamlit.header("Fruityvice Fruit Advice!")

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
    fruit_choice = streamlit.text_input('¿Sobre qué fruta le gustaría obtener información?', 'Kiwi')
    if not fruit_choice:
        streamlit.write('El usuario ingresó ', fruit_choice)
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.stop()

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.text(my_data_row)

streamlit.stop()

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('¿Qué fruta le gustaría añadir?', 'Kiwi')
streamlit.write('El usuario ingresó ', fruit_choice)
streamlit.write('Thanks for adding', fruit_choice)
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_cnx.commit()
