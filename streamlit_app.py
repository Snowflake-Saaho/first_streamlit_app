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
streamlit.dataframe(my_fruit_list)
