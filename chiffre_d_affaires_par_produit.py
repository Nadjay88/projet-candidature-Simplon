import pandas as pd
import plotly.express as px

df = pd.read_csv('ventes.csv')
df['chiffre_affaires'] = df['prix'] * df['qte']

par_produit = df.groupby('produit').agg(chiffre_affaires=('chiffre_affaires', 'sum')).reset_index()

fig = px.bar(par_produit, x='produit', y='chiffre_affaires', title="Chiffre d'affaires par produit", color='produit', text='chiffre_affaires')
fig.update_traces(textposition='outside')
fig.write_html('chiffre-d-affaires-par-produit.html')
print("chiffre-d-affaires-par-produit.html généré avec succès !")
