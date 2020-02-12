# This script will download shapefiles from King County

import os
import geopandas as gpd

rootDir = r'J:\Projects\Geocoding\20GEOCODING\Setup'

outDir = r'1Raw\King'

urls = {'address' : 'https://opendata.arcgis.com/datasets/56809ab507814d3a80c2c58616e999b5_642.geojson',
        'parcel': 'https://opendata.arcgis.com/datasets/c7a17b7ad3ec44b7ae64796dca691d72_1722.geojson',
        'st_address': 'https://opendata.arcgis.com/datasets/122d3117fcd043489e395296ef563a97_108.geojson'}

for k, v in urls.items():
    print(k)
    df = gpd.read_file(v)
    print('Writing ' + k + ' to file')
    df.to_file(os.path.join(rootDir, outDir, k + '.shp'))

