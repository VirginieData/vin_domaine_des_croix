# vin_domaine_des_croix

CHECKPOINT 4 - DATA -  WILD CODE SCHOOL
mars 2023


Etude de marché sur le vin

Le client, le Domaine des Croix, cherche à définir le prix de ses bouteilles de vin pour le marché américain. Il a récupéré un jeu de données de 130k bouteilles de vin, avec les cépages, les pays et région de production, les millésimes (c'est-à-dire les années de production), ainsi que des notes ("points") et descriptifs d'oenologues (les spécialistes du vin), et le prix en dollars de toutes ces bouteilles sur le marché américain.

L'objectif sera de faire une présentation de l'analyse du marché, et du prix que tu conseilles de fixer pour les vins du client. Le client n'est pas data analyst, mais souhaiterait comprendre la démarche. Il faudra donc s'attacher à expliquer comment les prix ont été fixés, sans rentrer dans un trop grand niveau technique, autrement dit : vulgariser.

données utilisées : 

* Dataset des 130k vins : https://github.com/murpi/wilddata/raw/master/wine.zip 
* Dataset des 14 vins du Domaine des Croix : https://github.com/murpi/wilddata/raw/master/domaine_des_croix.csv 


LES ÉTAPES POUR LA PRÉPARATION DES DONNÉES

dans un notebook python : 
* création colonne ‘millesime’ contenant l’année du vin
* suppression colonne ‘taster_twitter_handle’
* suppression des lignes dont le pays est représenté avec moins de 50 unités dans le df
* suppression des lignes dont la variété est représentée avec moins de 30 unités


dans power BI : 
* suppression de quelques lignes aberrantes trouvées à partir de country (4 lignes)
* changement type des données des colonnes numériques
* suppression des erreurs
* changement type donnée colonnes country et province en donnée géographique


ANALYSE DES DONNÉES 

5 slides (power bi)

* Les données de l’étude - portrait
* Note par pays et pour les 20 premiers cépages
* Focus sur le pinot noir
* Focus sur le Chardonnay
* Focus sur ces deux cépages en France


MACHINE LEARNING

(google collab)

* Choix de 3 modèles de régression pour voir quel est le plus pertinent : Linear Regression, KNeighborsRegressor, RandomForestRegressor.
* Objectif : prédire le prix

Step by step : 
* utilisation des colonnes millésime et note
* ajout des colonnes pays et cépages en limitant au 10 plus présents dans le df
* ajout de la colonne taster_name (non retenu)
* ajout de la colonne province (non retenu)
* Prédiction des prix des bouteilles de vin du Domaine des Croix 


MISE EN FORME SUR STREAMLIT

5 pages

* Accueil
* Contexte avec quelques éléments sur le domaine des Croix et sur la vente aux Etats Unis
* Analyse des données : lien vers le rapport Power BI (captures d’écran pour le moment)
* Machine Learning : possibilités de tests de 3 modèles sur notre df en faisant bouger quelques hyperparamètres 
* Prix des bouteilles : l’utilisateur choisit un vin, cela affiche son cépage, sa description, sa note et le prix conseillé (prédit par le modèle)
*Modèle retenu : RandomForestRegressor(n_estimators = 1000, max_depth= 15, min_samples_leaf= 1, min_samples_split= 10, random_state=42)*
