import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np
import re 


from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# création logo en haut sidebar
add_logo("https://res.cloudinary.com/wildcodeschool/image/upload/c_fill,h_50/v1/static/irjoy97aq0eol8bf6959")


# ## Import du df_wine mordifié par mes soins
# df_wine = pd.read_csv("C:/Users/vdane/Desktop/projets_power_bi/CHECKPOINT 4/df_wine.csv")


## Titres de la page
st.title('Pour les vins du Domaine des Croix')

st.write("""
# 
""")
st.write("Le modèle utilisé ici est le RandomForestRegressor")
st.caption("avec les paramètres suivants : n_estimators = 1000, max_depth= 15, min_samples_leaf= 1, min_samples_split= 10, random_state=42")

st.write("""
# 
""")

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
# df_wine_ml = df_wine_mml[["country", 'points', 'price', 'variety', 'millesime']]
# # on supprime les lignes avec des valeurs manquantes
# df_wine_ml.dropna(inplace=True)


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


# ## Standardisation des données

# # créer scaler
# scaler = StandardScaler()
# # entrainer scaler sur X_train
# scaler.fit(X_train)
# # transformer données
# X_train_scaled = scaler.transform(X_train)
# X_test_scaled = scaler.transform(X_test)


# mod = RandomForestRegressor(n_estimators = 1000, max_depth= 15, min_samples_leaf= 1, min_samples_split= 10, random_state=42)

# mod.fit(X_train_scaled, y_train)

# ### prediction
# pred_y_train = mod.predict(X_train_scaled)
# pred_y_test = mod.predict(X_test_scaled)

# # ### r2 score
# # r2_score_train = round(r2_score(y_train, pred_y_train), 4)
# # r2_score_test = round(r2_score(y_test, pred_y_test), 4)


# # #### Affichage
# # st.header("")
# # st.write('Modèle choisit : RandomForestRegressor')
# # st.write(f"R2 Score_train : {r2_score_train}")
# # st.write(f"R2 Score_test : {r2_score_test}")


# ## fichier df_croix
# link = "https://github.com/murpi/wilddata/raw/master/domaine_des_croix.csv"
# df_croix = pd.read_csv(link)

# ## création colonne millésime dans le df_croix

# # création fonction qui prenne en compte d'éventuelles années manquantes
# def trouver_année(année_str):
#     année = re.search("19\d{2}|20\d{2}", année_str)
#     if année:
#         return int(année.group())
#     else:
#         return None

# # appliquer à la colonne title
# df_croix["millesime"] = df_croix["title"].apply(trouver_année)



# df_croix_ml = df_croix[["country", 'points', 'price', 'variety', 'millesime']]


# ## Encodage

# # on choisit les colonnes qui seront encodées
# col_a_encoder_croix = df_croix_ml.select_dtypes(exclude='number')
# # on encode les données concernées
# OHencod.transform(col_a_encoder_croix)
# # on les remet dans un DF
# df_encod = pd.DataFrame(OHencod.transform(col_a_encoder_croix),
#                     columns=OHencod.get_feature_names_out(),
#                     index=df_croix_ml.index)
# # on rassemble nos colonnes encodées avec celles qui étaient déjà des colonnes numériques
# df_croix_encod = pd.concat([df_croix_ml[['points', 'price', 'millesime']], df_encod], axis=1)


# ## Définition X et y
# X = df_croix_encod.drop('price', axis=1)
# y = df_croix_ml['price']


# ## Standardisation des données

# # transformer données
# X_scaled = scaler.transform(X)


# # prédiction avec remplissage colonne price
# df_croix_ml['price'] = mod.predict(X_scaled)

# # création df final avec toutes les colonnes remises
# df_croix_avec_prix = pd.concat([df_croix_ml[['price']], df_croix.drop('price', axis=1)], axis=1)


## utilisation directe du df_croix_avec_prix exporté en csv sur github (pour éviter à chaque fois le rechargement de la page)
link = "https://raw.githubusercontent.com/VirginieData/vin_domaine_des_croix/main/df_croix_avec_prix.csv"
df_croix_avec_prix = pd.read_csv(link)

# choix de l'utilisateur
titre_wine = st.selectbox(
    'Selectionnez le vin à afficher',
    list(df_croix_avec_prix['title'])
)

## fonction qui va permettre d'afficher à partir du titre du vin 
## sa description, son cépage et le prix conseillé
def affichage_final(titre) :
    i = df_croix_avec_prix[df_croix_avec_prix["title"] == titre ].index
    st.write(f"Cépage : {df_croix_avec_prix['variety'].iloc[i].values[0]}")
    st.write(df_croix_avec_prix['description'].iloc[i].values[0])
    st.write(f"Note : {df_croix_avec_prix['points'].iloc[i].values[0]}")
    st.write(f"Prix conseillé : {round(df_croix_avec_prix['price'].iloc[i].values[0])} $")


affichage_final(titre_wine)
