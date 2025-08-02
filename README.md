# ⚡ Electricity Fraud Prediction

Ce projet utilise des techniques de machine learning pour détecter les cas potentiels de fraude dans la consommation d'électricité à partir de données de compteurs.

## 📂 Contenu du projet

- `notebooks/` : notebooks Jupyter d’exploration, de traitement des données et de modélisation.
- `data/` : (fichiers zippés) contient les données brutes et transformées.
- `models/` : modèles entraînés enregistrés.
- `src/` : scripts Python pour le nettoyage, l’ingénierie des features et la prédiction.
- `requirements.txt` : dépendances Python du projet.

## 🧪 Modèles utilisés

- **Random Forest**
- **XGBoost**
- **LightGBM**
- **Logistic Regression**

## 📊 Variables importantes

Les données contiennent des variables telles que :

- `customer_id`
- `meter_reading`
- `timestamp`
- `location`
- `fraud_flag`
- etc.

Un prétraitement rigoureux est appliqué : gestion des valeurs manquantes, détection des valeurs aberrantes, encodage des variables catégorielles, normalisation.

## 🎯 Objectif

> Prédire si un client présente un comportement suspect lié à la fraude à l’électricité, à partir de données de consommation passées.

## 🚀 Utilisation

### Installation

```bash
git clone https://github.com/FranckKD/electricity-fraud-prediction.git
cd electricity-fraud-prediction
pip install -r requirements.txt
```