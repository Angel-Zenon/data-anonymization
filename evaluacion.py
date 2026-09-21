import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data_anonima.csv')

# 1. Rango de edad que más compra en Farmacia
farmacia_edad = df[df['Categoria_Producto'] == 'Farmacia'].groupby('Fecha_Nacimiento')['Monto_Compra'].sum()

# 2. Género que compra más en Cuidado Personal
cuidado_sexo = df[df['Categoria_Producto'] == 'Cuidado Personal'].groupby('sexo')['Monto_Compra'].sum()
cuidado_sexo.index = ['Femenino' if s == 'f' else 'Masculino' for s in cuidado_sexo.index]

# 3. CP donde más gastan en Equipamiento
equip_cp = df[df['Categoria_Producto'] == 'Equipamiento'].groupby('Codigo_Postal')['Monto_Compra'].sum().sort_values(ascending=False)

# 4. Rango de edad que genera más ventas
ventas_edad = df.groupby('Fecha_Nacimiento')['Monto_Compra'].sum()

# 5. Categoría que genera más ventas
ventas_cat = df.groupby('Categoria_Producto')['Monto_Compra'].sum().sort_values(ascending=False)

# Graficar las 5 preguntas en un dashboard
fig, axs = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Fase de Toma de Decisiones - Respuestas Gráficas', fontsize=14, fontweight='bold')

# 1. Farmacia por Edad
axs[0, 0].bar(farmacia_edad.index, farmacia_edad.values, color='#2a9d8f')
axs[0, 0].set_title('1. Ventas en Farmacia por Edad')
axs[0, 0].set_ylabel('Monto ($)')

# 2. Cuidado Personal por Género
axs[0, 1].bar(cuidado_sexo.index, cuidado_sexo.values, color=['#e76f51', '#457b9d'])
axs[0, 1].set_title('2. Cuidado Personal por Género')
axs[0, 1].set_ylabel('Monto ($)')

# 3. Equipamiento por CP
axs[0, 2].bar(equip_cp.index, equip_cp.values, color='#e9c46a')
axs[0, 2].set_title('3. Equipamiento por CP')
axs[0, 2].set_ylabel('Monto ($)')
axs[0, 2].tick_params(axis='x', rotation=30)

# 4. Rango de edad con más ventas
axs[1, 0].bar(ventas_edad.index, ventas_edad.values, color='#264653')
axs[1, 0].set_title('4. Ventas Totales por Rango de Edad')
axs[1, 0].set_ylabel('Monto ($)')

# 5. Categoría con más ventas
axs[1, 1].pie(ventas_cat.values, labels=ventas_cat.index, autopct='%1.1f%%', colors=['#457b9d', '#e9c46a', '#e76f51'], startangle=140)
axs[1, 1].set_title('5. Ventas por Categoría')

# Desactivar eje sobrante
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()