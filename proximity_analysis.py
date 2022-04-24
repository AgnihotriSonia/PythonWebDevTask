
import math
import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPolygon
import folium
from folium import Choropleth, Marker
from folium.plugins import HeatMap, MarkerCluster
from shapely import wkt
import geojson
import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine 

#Database connection

connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "asteria")
cursor = connection.cursor()

#create_table_query = '''CREATE TABLE input_data_set(sr_no  float NOT NULL ,lat  float NOT NULL ,long  float NOT NULL);'''

#cursor.execute(create_table_query)
#connection.commit()

#with open(r"D:\\Asteria\\postgis_inputs.csv", 'r') as f:
    #next(f)
    #cursor.copy_from(f, 'input_data_set', sep=',', columns=('sr_no', 'lat', 'long'))

#connection.commit()
#connection.close()
 
db_connection_url = "postgresql://postgres:postgres@127.0.0.1:5433/asteria"
con = create_engine(db_connection_url)  
sql = "SELECT geom, lat,long FROM input_data_set"
point_gdf = gpd.GeoDataFrame.from_postgis(sql, con) 

#point_df = pd.read_csv(r"D:\\Asteria\\postgis_inputs.csv")
#point_gdf = gpd.GeoDataFrame(point_df, geometry=gpd.points_from_xy(point_df.Longitude, point_df.Latitude,crs='epsg:4326'))
point_gdf.head()

request_df = pd.read_csv(r"D:\\Asteria\\request_inputs.csv")
request_gdf = gpd.GeoDataFrame(request_df, geometry=gpd.points_from_xy(request_df.Longitude, request_df.Latitude,crs='epsg:4326'))
request_gdf.head()

print(point_gdf.crs)
print(request_gdf.crs)
request_gdf_UTM = request_gdf.to_crs(32643)
print(request_gdf_UTM.crs)

buffer = request_gdf_UTM .geometry.buffer(10)
buffer.head()

# Turn group of polygons into single multipolygon
my_union = buffer.geometry.unary_union
print('Type:', type(my_union))

# Show the MultiPolygon object
my_union

# Proximity
#for i in point_df.index:
#my_union.contains(point_df.iloc[0].geometry)
class proximity_analysis():
    def prox(a):
        out = my_union.contains(point_gdf.iloc[a].geom)
        return out

    
