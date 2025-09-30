import dash
from dash import html, dcc
import plotly.express as px

app = dash.Dash(__name__)

# Sample data
df = px.data.iris()
# print(df.info())

app.layout = html.Div([
    dcc.Dropdown(
        id='species-dropdown',
        options=[{'label': species, 'value': species} for species in df['species'].unique()],
        value=[df['species'].unique()[0]],
        multi=True
    ),
    dcc.RadioItems(
        id='sepal-radio',
        options=[
            {'label': 'Sepal Width', 'value': 'sepal_width'},
            {'label': 'Sepal Length', 'value': 'sepal_length'}
        ],
        value='sepal_width'
    ),
    dcc.RadioItems(
        id='petal-radio',
        options=[
            {'label': 'Petal Width', 'value': 'petal_width'},
            {'label': 'Petal Length', 'value': 'petal_length'}
        ],
        value='petal_width'
    ),
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    )
])

@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('species-dropdown', 'value'),
     dash.dependencies.Input('sepal-radio', 'value'),
     dash.dependencies.Input('petal-radio', 'value')]
)
def update_scatter_plot(selected_species):
    filtered_df = df[df['species'] == selected_species]
    return px.scatter(filtered_df, x='sepal_width', y='sepal_length', color='species')

if __name__ == '__main__':
    app.run(debug=True)