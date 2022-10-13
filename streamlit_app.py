import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 🥗 🍞Dosa 2 & Idly 2')
streamlit.text('🥭Mango, 🍇Grapes, 🫐Blueberry & Blackberry Smoothies')
streamlit.text('🥛Milk, Curd, 🧈Butter')
streamlit.text('🥚Boiled-Eggs, Bread Omlette')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
