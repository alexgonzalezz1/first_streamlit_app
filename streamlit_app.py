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

streamlit.header("the fruit list conatains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * pc_rivery_db.public.from fruit_load_list")
    return my_cur.fetchall()

# ...
if streamlit.button('Get fruit load list'):
    try:
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        my_data_rows = get_fruit_load_list()
        streamlit.dataframe(my_data_rows)
    except Exception as e:
        streamlit.error("Error connecting to Snowflake or retrieving data.")
        streamlit.error(str(e))


def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
     return "Thansk for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Add a Fruit to the List'):
        my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
        back_from_function = insert_row_snowflake(add_my_fruit)
        streamlit.text(back_from_function)

if streamlit.button('Add fruit to Snowflake'):
    try:
        my_cur = my_cnx.cursor()
        streamlit.success(f"Successfully added {fruit_choice} to Snowflake!")
    except Exception as e:
        streamlit.error("Error adding data to Snowflake.")
        streamlit.error(str(e))



