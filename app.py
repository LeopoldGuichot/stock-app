import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

# Liste des entreprises
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Google": "GOOGL",
    "Meta": "META",
    "Nvidia": "NVDA",
    "Netflix": "NFLX"
}

# Titre de l'application
st.title("Application de suivi des valorisations boursières")

# Sélection de l'entreprise
company_name = st.selectbox("Sélectionnez une entreprise", list(companies.keys()))

# Récupérer le symbole de l'entreprise sélectionnée
company_symbol = companies[company_name]

# Télécharger les données de l'entreprise via yfinance
stock_data = yf.Ticker(company_symbol)
stock_info = stock_data.info

# Afficher la capitalisation boursière
st.subheader(f"Capitalisation boursière de {company_name}:")
market_cap = stock_info.get("marketCap", "Information non disponible")
st.write(f"{market_cap:,} $")

# Récupérer les données historiques pour le graphique
hist = stock_data.history(period="1y")  # Données sur un an

# Créer le graphique avec Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'], mode='lines', name='Prix de clôture'))

# Mise à jour des labels du graphique
fig.update_layout(
    title=f"Évolution de la valorisation boursière de {company_name} (sur un an)",
    xaxis_title="Date",
    yaxis_title="Prix de clôture ($)",
    template="plotly_dark"
)

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)

