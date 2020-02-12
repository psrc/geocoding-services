# This script extracts downloaded shapefiles in 1Raw directory and re-projects them into the 2Working directory
import os, zipfile, geopandas, shutil, re

def unzipfiles (shpDir, filenames):
    for afile in filenames:
        path_to_zip_file = os.path.join(shpDir, afile + '.zip')
        #print "Unzipping " + afile
        print("Unzipping " + afile)
        zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
        zip_ref.extractall(shpDir)
        zip_ref.close()
    #print "Unzipping Complete"
    print("Unzipping Complete")

def reproject_shps (shpDir, outDir, infilenames, outfilenames):
    # replace the “.prj” file with one that has the projection that was converted the points to 
    # do the conversion to your projection--the error may be writing out the prj file, not the conversion itself
    corrPrjFile = r'J:\Projects\Geocoding\Scripts\projections\102748.prj' # An ESRI projection format for NAD83/Washington North 4601 Ft
    for i in range(len(infilenames)):
        #print "Converting " + infilenames[i]
        print("Converting " + infilenames[i])
        ashp = geopandas.read_file(os.path.join(shpDir, infilenames[i]))
        # ESRI:102748 proj4 format
        pshp = ashp.to_crs('+proj=lcc +lat_1=47.5 +lat_2=48.73333333333333 +lat_0=47 +lon_0=-120.8333333333333 +x_0=500000.0000000002 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs')
        pshp.to_file(driver = 'ESRI Shapefile', filename = os.path.join(outDir, infilenames[i]))
        shutil.copyfile(corrPrjFile, os.path.join(outDir, outfilenames[i] + '.prj'))
    
county = 'Pierce'
rootDir = r'J:\Projects\Geocoding\20GEOCODING\Setup'
shpDir = os.path.join(rootDir, '1Raw', county)
outDir = os.path.join(rootDir, '2Working', county)

files = ['Address_Points', 'Tax_Parcels', 'Roads']
unzipfiles(shpDir, files)

allfiles = os.listdir(shpDir)
shps = [s for s in allfiles if re.match(r'.+\.shp', s)] 
reproject_shps(shpDir, outDir, shps, files)
