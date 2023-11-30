import pandas as pd
import plotly.express as px

# pip install -U kaleido
salary = pd.read_csv('salaries.csv', sep = '\t')

fig = px.parallel_categories(dogs, dimensions = ['sex','age','size'],
                            labels = {'age':'Age', 'sex':'Sex', 'size':'Size'},
                            title = 'Characteristics of Adoptable Dogs',
                            )
fig.show()