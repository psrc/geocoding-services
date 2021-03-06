# This script will parse Pierce County Parcel site addresses (Address_Points.dbf). The output is an excel file in 2Working to be
# joined with Address_Points.shp as a reference dataset to create address locators.
# May take 5 mins to run

import os, usaddress
import pandas as pd
import numpy as np
import re
from simpledbf import Dbf5
from collections import Counter

# function to extract piece of parsed address
def extractParsedAddr(parsedAddresses, label):
    v = [item for item in parsedAddresses if label in item] # list tuples containing the label
    if len(v) == 1:
        v2 = map(str, [x[0] for x in v])[0]
        vv = v2
    elif (label == 'AddressNumber') & (len(v) > 1):
        v2 = map(str, [x[0] for x in v])[0]
        vv = v2
    elif (label == 'SubaddressIdentifier') & (len(v) > 1):  
        v2 = map(str, [x[0] for x in v])[0]
        vv = v2
    else:
        v2 = map(str, [x[0] for x in v])
        v3 = ' '.join(v2)
        vv = v3
    return vv

# Dictionary for template and usaddress column names
addrDict = {
        'AddressNumber' : 'HOUSENO',
        'StreetNamePreDirectional': 'PREFIX',
        'StreetName': 'STRNAME',
        'StreetNamePostType': 'STRTYPE',
        'StreetNamePostDirectional': 'SUFFIX', 
        'OccupancyType': 'UNITBLD_TYPE',
        'OccupancyIdentifier': 'UNIT',
        }

addrDict2 = {
        'SubaddressIdentifier' : 'HOUSENO',
        'StreetNamePreDirectional': 'PREFIX',
        'StreetName': 'STRNAME',
        'StreetNamePostType': 'STRTYPE',
        'StreetNamePostDirectional': 'SUFFIX', 
        'OccupancyType': 'UNITBLD_TYPE',
        'OccupancyIdentifier': 'UNIT',
        }

addrDictKey = addrDict.keys() # list all keys (usaddress.LABELS) in AddrDict 
addrDictKey2 = addrDict2.keys() # list all keys (usaddress.LABELS) in AddrDict2 
                           
rootDir = r'J:\Projects\Geocoding\19GEOCODING\Setup'
inDir = r'1Raw\Pierce'
outDir = r'2Working\Pierce'

dbf = Dbf5(os.path.join(rootDir, inDir, 'Address_Points.dbf'))

df = dbf.to_dataframe()

df['HOUSENO'] = np.nan
df = df.reindex(columns = np.append(df.columns.values, ['PREFIX', 'STRNAME', 'STRTYPE', 'SUFFIX', 'UNITBLD_TYPE', 'UNIT', 'SUBAREA']))
df['PREFIX'] = df['PREFIX'].astype(str)
df['STRNAME'] = df['STRNAME'].astype(str)
df['STRTYPE'] = df['STRTYPE'].astype(str)
df['SUFFIX'] = df['SUFFIX'].astype(str)
df['SUBAREA'] = df['SUBAREA'].astype(str)
df['UNIT'] = df['UNIT'].astype(str)
df['UNITBLD_TYPE'] = df['UNITBLD_TYPE'].astype(str)

# use usaddress package to parse address into a tupled list
for i in range(len(df.index)): # loop through each row
    if isinstance(df.ix[df.index[i],'Address'], float): # if ADDRESS is Nan (float)
        continue
    else:
        addr = df.ix[df.index[i], 'Address'] 
        addrParsedOrig = usaddress.parse(addr)
        temp = []
        for a,b in addrParsedOrig :
            if (a,b) not in temp: #to check for the duplicate tuples
               temp.append((a,b))
        addrParsed = temp * 1 #copy temp to d
        addrElements = [a[0] for a in addrParsed] # untupled list
        if 'XXX' in addrElements:
            continue
        else:
            hn = [h[0] for h in addrParsed if 'AddressNumber' in h] # isolate 'AddressNumber'
            pattern = re.compile('[A-Z]|-') # if there are alphabet or dashes detected in the 'AddressNumber'
            pattern4 = re.compile('/') # if there slash in the 'AddressNumber'
            pattern5 = re.compile('[A-Z]')
            if (len(hn) == 0):
                continue
            elif (len(pattern.findall(hn[0])) != 0):
                continue
            else:
                origLabels = [x[1] for x in addrParsed] # list all labels in tuples
                if (('TO', 'StreetName') in addrParsed) | (('TO', 'StreetNamePreDirectional') in addrParsed):
                    counts = Counter(t for t in origLabels) # evaluate # of labels in origLabels
                    if counts['AddressNumber'] >= 2: # evaluate 'AddressNumber' in origLabels
                        pattern3 = re.compile('[A-Z]|-|/')
                        hns = [h for h in addrParsed if 'AddressNumber' in h]
                        hnExclude = [v for v in hns if len(pattern3.findall(v[0])) != 0]
                        exclude = []
                        if len(hnExclude) != 0: # if there's something to exclude                      
                            exclude = exclude + hnExclude
                        else:
                            addNum = [an for an in addrParsed if an[1] == 'AddressNumber'][0]
                            exclude.append(addNum)
                        if ('TO', 'StreetName') in addrParsed:
                            exclude.append(('TO', 'StreetName'))
                        else:
                            exclude.append(('TO', 'StreetNamePreDirectional'))
                        addrParsedChg = [y for y in addrParsed if y not in exclude]
                        labels = [x for x in origLabels if x in addrDictKey]
                        for label in labels:
                            extractValue = extractParsedAddr(addrParsedChg, label) 
                            df.set_value(df.index[i], addrDict[label], extractValue)
                    elif counts['StreetName'] >= 2: # evaluate 'StreetName' in origLabels
                         strnames = [s for s in addrParsed if 'StreetName' in s]
                         exStrnames = [sn for sn in strnames if len(pattern5.findall(sn[0])) == 0]
                         exStrnames.append(('TO', 'StreetName'))
                         addrParsedChg = [y for y in addrParsed if y not in exStrnames]
                         labels = [x for x in origLabels if x in addrDictKey]
                         for label in labels:
                            extractValue = extractParsedAddr(addrParsedChg, label) 
                            df.set_value(df.index[i], addrDict[label], extractValue)
                    else:
                        labels = [x for x in origLabels if x in addrDictKey]
                        for label in labels:
                            extractValue = extractParsedAddr(addrParsed, label) 
                            df.set_value(df.index[i], addrDict[label], extractValue)
                elif (len(pattern4.findall(hn[0])) != 0): # evaulate if there is a '/' in the address number
                    labels = [x for x in origLabels if x in addrDictKey2]
                    for label in labels:
                        extractValue = extractParsedAddr(addrParsed, label) 
                        pattern2 = re.compile('\\d+')
                        if (label == 'SubaddressIdentifier') & (len(pattern2.findall(extractValue)) != 0):
                            extractDigits = pattern2.findall(extractValue)[0]
                            df.set_value(df.index[i], addrDict2[label], extractDigits) # need dict between template col and usaddress col
                        else:    
                            df.set_value(df.index[i], addrDict2[label], extractValue) # need dict between template col and usaddress col
                else:
                    labels = [x for x in origLabels if x in addrDictKey]
                    for label in labels:
                        extractValue = extractParsedAddr(addrParsed, label) 
                        df.set_value(df.index[i], addrDict[label], extractValue) # need dict between template col and usaddress col

# clean individual columns
parsedHeaders = ['HOUSENO', 'PREFIX', 'STRNAME', 'STRTYPE', 'SUFFIX', 'SUBAREA', 'UNITBLD_TYPE', 'UNIT']
for header in parsedHeaders:
    for i in range(len(df.index)):
        p = df.ix[df.index[i], header]
        if p == 'nan':
            df.set_value(df.index[i], header, '')                          
        if (header == 'UNIT') & (p in ['KP N', 'KP S', 'KP', 'FI', 'KI', 'AI']):
            df.set_value(df.index[i], 'SUBAREA', p)
        if (header == 'PREFIX') & (p not in ['N', 'E', 'S', 'W', 'NE', 'NW', 'SE', 'SW', 'NORTH', 'EAST', 'SOUTH', 'WEST']):
            df.set_value(df.index[i], 'PREFIX', '') 
        if (header == 'STRTYPE') & (p == 'KP'):
            df.set_value(df.index[i], 'SUBAREA', p)
            df.set_value(df.index[i], 'STRTYPE', '')
            pattern3 = re.compile('\\sSTCT|\\sAVCT|\\sROAD')
            z = df.ix[df.index[i], 'STRNAME']
            if len(pattern3.findall(z)) != 0:
                newStrtype = re.compile('\s(\w+)').findall(z)[0]
                newStrname = re.compile('(\w+)\s').findall(z)[0]
                df.set_value(df.index[i], 'STRTYPE', newStrtype)
                df.set_value(df.index[i], 'STRNAME', newStrname)
         
dfExport = df[['OBJECTID', 'Address', 'HOUSENO', 'PREFIX', 'STRNAME', 'STRTYPE', 'SUFFIX', 'SUBAREA', 'UNITBLD_TYPE', 'UNIT', 'ZipCode']]                         
dfExport.to_excel(os.path.join(rootDir, outDir, 'AddressPoints_parsed.xlsx'), index = False)                                         
