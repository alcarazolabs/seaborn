import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Cargar Dataset
df = pd.read_excel('decesos12junio2020.xlsx')
#Ordenar distritos de manera descendente por casos
ndf = df.nlargest(31, 'Decesos')
print(ndf)

plt.figure(figsize=(6,6))
plt.title("Reporte COVID-19 Lambayeque 12-Jun-2020")
"""
Colores:
- YlGnBu

"""
sns.heatmap(df[['Decesos']].sort_values(by=['Decesos'],ascending=False),
   vmin=-1, cmap='coolwarm',
    fmt="0.0f",
    annot=True,
    yticklabels=ndf['Distrito'],
    xticklabels=["Número de Decesos/Defunciones"]) 
plt.savefig('heatmap.png', dpi=100, bbox_inches='tight')
