# Streamlit Stock App

Cette application Streamlit permet de sélectionner une entreprise américaine parmi une liste et d'afficher sa capitalisation boursière en temps réel, récupérée via l'API Yahoo Finance (yfinance).

## Fonctionnalités

- Sélectionner une entreprise parmi Apple, Microsoft, Amazon, Tesla, Google, Meta, Nvidia, et Netflix.
- Afficher la capitalisation boursière de l'entreprise sélectionnée en temps réel.

## Prérequis

Avant de pouvoir exécuter cette application, assurez-vous d'avoir installé les éléments suivants :

- Python 3.8
- Les bibliothèques Python nécessaires (voir [Installation](#installation)).

## Installation

1. Clonez ce dépôt GitHub sur votre machine locale :

   ```bash
   git clone https://github.com/ton-utilisateur/streamlit-stock-app.git
   cd streamlit-stock-app
   
## Utilisation 

1. Creer la Docker image
   
   ```bash
   docker build -t streamlit-app .
   
2. Run le Docker container
   
  ```bash
   docker run -p 8501:8501 streamlit-app

3. Se rendre à l'adresse suivante http://localhost:8501 pour utiliser k'application


