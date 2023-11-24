import pandas as pd
import plotly.express as px

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Graficar la distribución de notas con un boxplot
fig = px.box(df, x='materia', y='nota', points="all", title='Distribución de Notas',
             labels={'nota': 'Nota', 'materia': 'Materia'})
fig.update_layout(showlegend=False)

# Mostrar la gráfica
fig.show()

# Graficar la distribución de aprobados con un pie chart
aprobados = df['aprobado'].value_counts()

fig_pie = px.pie(aprobados, values=aprobados.values, names=aprobados.index, title='Distribución de Aprobados',
                 labels={'label': 'Aprobado'})
fig_pie.update_traces(textinfo='percent+label')

# Mostrar la gráfica
fig_pie.show()
