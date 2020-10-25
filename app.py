import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

chart_height = 300
##plotting the pie chart
labels = ['2015','2016','2017']
values = [4500, 2500, 1053]
pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
pie.update_layout(
    annotations=[dict(text='hapiness', x=0.5, y=0.5, font_size=10, showarrow=False)],
    height= chart_height,
    paper_bgcolor='#000000',
    plot_bgcolor='#000000'
)


#plotting the geographical map
us_cities = pd.read_csv("data/us-cities-top-1k.csv")

maps = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=1, height=chart_height)
maps.update_layout(
    paper_bgcolor='#000000',
    plot_bgcolor='#000000',
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
maps.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

## ploting the scatter chart
dff = px.data.gapminder()

happy_scatter = px.scatter(dff.query("year==2007"), x="gdpPercap", y="lifeExp",
	         size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)


happy_scatter.update_layout(
    paper_bgcolor='#000000',
    plot_bgcolor='#000000',
    height=chart_height
)

## plotting the table
tab = go.Figure(data=[go.Table(
    header=dict(values=list(us_cities.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[us_cities.City, us_cities.State, us_cities.Population, us_cities.lat, us_cities.lon],
               fill_color='lavender',
               align='left'))
])
tab.update_layout(
    paper_bgcolor='#000000',
    plot_bgcolor='#000000',
    height=chart_height
)
## plotting the bar
data = px.data.gapminder()
data_canada = data[data.country == 'Canada']
bar = px.bar(data_canada, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=chart_height)
bar.update_layout(
    paper_bgcolor='#000000',
    plot_bgcolor='#000000',
    height=chart_height
)

### second map

df = pd.read_csv('data/2014_world_gdp_with_codes.csv')

map2 = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP<br>Billions US$',
))

map2.update_layout(
    title_text='2014 Global GDP',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
        showarrow = False
    )], 
    height= chart_height,
    paper_bgcolor='#000000',
    plot_bgcolor='#000000'
)



colors = {
    'background':'#000000',
    'text': '#FFFFFF'
}

items = [
    dbc.DropdownMenuItem("Item 1"),
    dbc.DropdownMenuItem("Item 2"),
    dbc.DropdownMenuItem("Item 3"),
]

app.layout =  html.Div(style={'backgroundColor': colors['background']}, children=[
    dbc.Row(dbc.Col(
        html.H4(
            children='WHAT MAKES THE WORLD HAPPY',
            style={
                'textAlign': 'left',
                'color': colors['text'],
                'marginBottom':'20px',
                }
                ),
                )
            ),
    dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='filters',
                                style={
                                    'textAlign': 'left',
                                    'color': colors['text']
                                    }
                                    ),
                            dbc.DropdownMenu(items, 
                                    label="year", 
                                    color="success", 
                                    className="m-1", bs_size="sm"),
                            dbc.DropdownMenu(items, 
                                    label="country", 
                                    color="success", 
                                    className="m-1", bs_size="sm"),
                            dbc.DropdownMenu(items, 
                                    label="continent", 
                                    color="success", 
                                    className="m-1", bs_size="sm"),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ), 
                width="2"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='hapiness',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='generocity',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='corruption',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='freedom',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='GDP',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='social',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1"),

                dbc.Col(
                    html.Div(
                        children=[
                            html.P(
                                children='health',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                            html.H5(
                                children='0.75',
                                style={
                                    'textAlign': 'center',
                                    'color': colors['text']
                                    }
                                    ),
                                ],
                        style={
                            'background': '#000000'
                            }
                        ),
                width="1")
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                dcc.Graph(figure=pie)
                ,width="4"
            ),
            dbc.Col(
                dcc.Graph(figure=happy_scatter)
                ,width="4"
            ),
            dbc.Col(
                dcc.Graph(figure=maps)
                ,width="4"
            )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(figure=tab)
                    ,width="6"
                ),
                 dbc.Col(
                    dcc.Graph(figure=bar)
                    ,width="6"
                )
            ]
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)