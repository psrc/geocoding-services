# This script will take projected shapefiles and add two new columns: X_COORD and Y_COORD

import os
import geopandas as gpd

rootDir = r'J:\Projects\Geocoding\20GEOCODING\Setup'

inDir = r'2Working'
outDir = r'3FinalProducts'

data_dict = {'Pierce' : {'files' : [('Address_Points.shp', 'siteaddr.shp'), ('Tax_Parcels.shp', 'prcl.shp')]},
             'Kitsap' : {'files': [('siteaddr.shp', 'siteaddr_test.shp'), ('parcels.shp', 'prcl.shp')]},
             'Snohomish' : {'files': [('parcels.shp', 'prcl.shp')]},
             'King' : {'files': [('address.shp', 'siteaddr.shp'), ('parcel.shp', 'prcl.shp')]}
             }

for k, v in data_dict.items():
    for file_names in v['files']:
        print(file_names)
        df = gpd.read_file(os.path.join(rootDir, inDir, k, file_names[0]))
        print(file_names[0])
        shpType = df.geom_type.unique()
        print(shpType)
        #if len(shpType) == 1:
        if (shpType[0] == 'Point'):
            df['X_COORD'] = df.geometry.x
            df['Y_COORD'] = df.geometry.y
        else:
            df['X_COORD'] = df.centroid.x
            df['Y_COORD'] = df.centroid.y
        df.to_file(os.path.join(rootDir, outDir, k, file_names[1]))
        #else:
            #print('Inspect shapefile, contains none or multi-geometry')