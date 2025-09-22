
from plotly import express as px
from plotly import graph_objects as go
from dash import Dash, dcc, html

# this is how to create a dash app
data = px.data.iris()

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Iris Data Visualization'),
    dcc.Graph(
        id='example-graph',
        figure=px.scatter(data, x='sepal_width', y='sepal_length', color='species')
    )
])

if __name__ == '__main__':
    app.run(debug=True)
