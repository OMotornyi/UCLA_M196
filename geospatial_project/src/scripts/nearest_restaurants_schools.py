import numpy as np
import pandas as pd
import googlemaps
from os import getcwd, listdir
from getpass import getpass

# Getting Coordinates of Schools
coord_path = getcwd() + "/geospatial_project/data/csv"
coord_df = pd.read_csv(f"{coord_path}/{listdir(coord_path)[0]}")

coordinates = list(zip(coord_df['latitude'].tolist(), coord_df['longitude'].tolist()))

# Establishing Google Maps Client with API Key
gmaps = googlemaps.Client(key=getpass("Type in your API key: "))

# Search Restaurants Within a 10 Meter Radius from Each School
