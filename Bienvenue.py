import streamlit as st
#from streamlit_extras.let_it_rain import rain
#from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Checkpoint 4 - Virginie DANET - Wild Code School",
    page_icon="👋",
)

st.title("Bienvenue à bord")
# st.sidebar.success("Select a page above.")

# création logo en haut sidebar
#add_logo("https://res.cloudinary.com/wildcodeschool/image/upload/c_fill,h_50/v1/static/irjoy97aq0eol8bf6959")

# création animation verres de vins
rain(
   emoji="🍷",
   font_size=54,
   falling_speed=5,
    animation_length="infinite",)

# Page d'accueil avec logo Domaine de Croix
st.image("https://wineguildeducation.org/wp-content/uploads/2020/03/domaine-de-croix.jpg")














