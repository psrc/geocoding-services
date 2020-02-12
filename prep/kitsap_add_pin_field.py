# This script will join Kitsap files to append PIN and copy into 2Working

# read from 1Raw
import os
import pandas as pd
from simpledbf import Dbf5
import geopandas as gpd

rootDir = r'J:\Projects\Geocoding\20GEOCODING\Setup'

inDir = r'1Raw\Kitsap'
outDir = r'2Working\Kitsap'

# join main.dbf with parcel shape to append 14 digit ACCT_NO as PIN (primarily for permit database purposes)
dbf = Dbf5(os.path.join(rootDir, inDir, 'main.dbf'))
df = dbf.to_dataframe()

shp = gpd.read_file(os.path.join(rootDir, inDir, 'parcels.shp'))
df = df[['RP_ACCT_ID', 'ACCT_NO']]

shpJoin = shp.merge(df, on = 'RP_ACCT_ID', how = 'left')
shpJoin['ACCT_NO'] = shpJoin['ACCT_NO'].replace('-', '', regex=True)
shpJoin.rename(columns = {'ACCT_NO' : 'PIN'}, inplace=True)

shpJoin.to_file(os.path.join(rootDir, outDir, 'parcels.shp'))



