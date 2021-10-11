import json
import requests
import dateutil.parser
import plotly.express as px
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

def main():
    contents = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson').json()
    earthquakes = contents["features"]
    magnitudes, lats, longs, places, times = [],[],[],[],[]
    for earthquake in earthquakes:
        magnitudes.append(earthquake['properties']['mag'])
        longs.append(earthquake['geometry']['coordinates'][0])
        lats.append(earthquake['geometry']['coordinates'][1])
        places.append(earthquake['properties']['place'])

    eqData = [{
        'type': 'scattergeo',
        'lon': longs,
        'lat': lats,
        'text': places,
        'marker':{
            'size': [5*mag for mag in magnitudes],
            'color': magnitudes,
            'colorscale': 'Rainbow',
            'reversescale': False,
            'colorbar': {
                'title': 'Magnitude'
            }
        },
      }]

    figure_layout = Layout(title = "Global Earthquakes (Last 30 Days) Updated Every Minute")
    fig = {
        'data':eqData,
        'layout': figure_layout
    }

    offline.plot(fig, filename = 'globalQuakes30Days.html')

if __name__ == '__main__':
    main()