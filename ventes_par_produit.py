import pandas as pd
import plotly.express as px

df = pd.read_csv('ventes.csv')
df['chiffre_affaires'] = df['prix'] * df['qte']

par_produit = df.groupby('produit').agg(quantite=('qte', 'sum')).reset_index()

fig = px.bar(par_produit, x='produit', y='quantite', title='Ventes par produit', color='produit', text='quantite')
fig.update_traces(textposition='outside')
fig.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')
