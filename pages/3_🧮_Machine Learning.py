## Imports

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
#from streamlit_extras.app_logo import add_logo

# création logo en haut sidebar
#add_logo("https://res.cloudinary.com/wildcodeschool/image/upload/c_fill,h_50/v1/static/irjoy97aq0eol8bf6959")


st.title('Prédire le prix du vin')

st.write("""
# Explorons différents modèles pour choisir le plus adapté
""")
st.caption("C'est un peu long... mais ça fonctionne au bout d'un moment")

modele_name = st.sidebar.selectbox(
     'Selectionnez un modèle',
     ('KNN', 'Random Forest')
 )

#############################################################################
# ## Préparation du df utilisé pour le ML

# # Sélection des 10 pays les plus représentés
# top_10_countries = df_wine['country'].value_counts().index[:10]
# # Création d'un masque booléen pour sélectionner les lignes correspondantes
# mask = df_wine["country"].isin(top_10_countries)
# # Sélection des lignes correspondantes
# df_wine_country = df_wine[mask]

# # Sélection des 10 cépages les plus représentés
# top_10_variety = df_wine_country['variety'].value_counts().index[:10]
# # Création d'un masque booléen pour sélectionner les lignes correspondantes
# mask = df_wine_country['variety'].isin(top_10_variety)
# # Sélection des lignes correspondantes
# df_wine_mml = df_wine_country[mask]

# #réduction aux colonnes concernées
# df_wine_ml = df_wine_mml[["country", "province", 'points', 'price', 'variety', 'millesime', 'taster_name']]
# # on supprime les lignes avec des valeurs manquantes
# df_wine_ml.dropna(inplace=True)
####################################################################################
# ## Import du df_wine modifié par mes soins
# df_wine_ml = pd.read_csv("https://raw.githubusercontent.com/VirginieData/vin_domaine_des_croix/main/df_wine_ml.csv")

# ## Encodage

# # on choisit les colonnes qui seront encodées
# col_a_encoder = df_wine_ml.select_dtypes(exclude='number')
# # on encode les données concernées
# OHencod = OneHotEncoder(sparse=False, drop="if_binary")
# OHencod.fit(col_a_encoder)
# OHencod.transform(col_a_encoder)
# # on les remet dans un DF
# df_encod = pd.DataFrame(OHencod.transform(col_a_encoder),
#                     columns=OHencod.get_feature_names_out(),
#                     index=df_wine_ml.index)
# # on rassemble nos colonnes encodées avec celles qui étaient déjà des colonnes numériques
# DF_wine_encod = pd.concat([df_wine_ml[['points', 'price', 'millesime']], df_encod], axis=1)


# ## Définition X et y
# X = DF_wine_encod.drop('price', axis=1)
# y = df_wine_ml['price']

# ## Train test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)


## Standardisation des données

# # créer scaler
# scaler = StandardScaler()
# # entrainer scaler sur X_train
# scaler.fit(X_train)
# # transformer données
# X_train_scaled = scaler.transform(X_train)
# X_test_scaled = scaler.transform(X_test)



# ## Fonction paramètres des différents modèles
# def add_parameter_ui(mod_name):
#     params = dict()
#     if  modele_name == 'KNN':
#         K = st.sidebar.slider('K', 1, 20)
#         params['K'] = K
#     else:
#         max_depth = st.sidebar.slider('max_depth', 2, 20)
#         params['max_depth'] = max_depth
#         n_estimators = st.sidebar.slider('n_estimators', 50, 500)
#         params['n_estimators'] = n_estimators
#     return params

# params = add_parameter_ui(modele_name)


# ## fonction qui définie le modèle avec ses paramètres
# def get_modele(mod_name, params):
#     mod = None
#     if mod_name == 'KNN':
#         mod = KNeighborsRegressor(n_neighbors=params['K'])
#     else:
#         mod = RandomForestRegressor(n_estimators=params['n_estimators'], 
#             max_depth=params['max_depth'], random_state=42)
#     return mod

# mod = get_modele(modele_name, params)

# mod.fit(X_train_scaled, y_train)

# ### prediction
# pred_y_train = mod.predict(X_train_scaled)
# pred_y_test = mod.predict(X_test_scaled)

# ### r2 score
# r2_score_train = round(r2_score(y_train, pred_y_train), 2)
# r2_score_test = round(r2_score(y_test, pred_y_test), 2)

# ### calcul rmse
# rmse_train = mean_squared_error(y_train, pred_y_train)
# rmse_train = round(rmse_train**0.5 , 2)
# mse_test = mean_squared_error(y_test, pred_y_test)
# rmse_test = round(mse_test**0.5 , 2)


# ### Affichage
# st.header("")
# st.write('Taille du dataset après modifications :', X.shape)
# st.write(f'Modèle choisit = {modele_name}')
# st.write(f"R2 Score_train : {r2_score_train}")
# st.write(f"R2 Score_test : {r2_score_test}")
# st.write(f"rmse_train : {rmse_train}")
# st.write(f"rmse_test : {rmse_test}")

