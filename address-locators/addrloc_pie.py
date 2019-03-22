# Create Pierce County address locators
# The new address locators will be created in a separate file folder.

# Import system modules
import os, arcpy

rootDir = r'J:\Projects\Geocoding\19GEOCODING'
inDir = r'Setup\3FinalProducts' 
county = 'Pierce'

arcpy.env.workspace = os.path.join(rootDir, inDir, county)

# site address based (point file)
AddressLocator_OutputPath = os.path.join(rootDir, "AddressLocators\\19pie_siteaddr")
arcpy.CreateAddressLocator_geocoding(in_address_locator_style="US Address - Single House", 
                                     in_reference_data="siteaddr.shp 'Primary Table'", 
                                     in_field_map="'Point Address ID' FID VISIBLE NONE;'Street ID' <None> VISIBLE NONE;'*House Number' HOUSENO VISIBLE NONE;Side <None> VISIBLE NONE;'Full Street Name' <None> VISIBLE NONE;'Prefix Direction' PREFIX VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' STRNAME VISIBLE NONE;'Suffix Type' STRTYPE VISIBLE NONE;'Suffix Direction' SUFFIX VISIBLE NONE;'City or Place' CITY VISIBLE NONE;County <None> VISIBLE NONE;State <None> VISIBLE NONE;'State Abbreviation' <None> VISIBLE NONE;'ZIP Code' ZipCode VISIBLE NONE;'Country Code' <None> VISIBLE NONE;'3-Digit Language Code' <None> VISIBLE NONE;'2-Digit Language Code' <None> VISIBLE NONE;'Admin Language Code' <None> VISIBLE NONE;'Block ID' <None> VISIBLE NONE;'Street Rank' <None> VISIBLE NONE;'Display X' <None>  VISIBLE NONE;'Display Y' <None> VISIBLE NONE;'Min X value for extent' <None> VISIBLE NONE;'Max X value for extent' <None> VISIBLE NONE;'Min Y value for extent' <None> VISIBLE NONE;'Max Y value for extent' <None> VISIBLE NONE;'Additional Field' <None> VISIBLE NONE;'Altname JoinID' <None> VISIBLE NONE;'City Altname JoinID' <None> VISIBLE NONE", 
                                     out_address_locator=AddressLocator_OutputPath, 
                                     config_keyword="", 
                                     enable_suggestions="DISABLED")

# street centerline based
AddressLocator_OutputPath = os.path.join(rootDir, "AddressLocators\\19pie_stcl")
arcpy.CreateAddressLocator_geocoding(in_address_locator_style="US Address - Dual Ranges", 
                                     in_reference_data="stcl.shp 'Primary Table'", 
                                     in_field_map="'Feature ID' FID VISIBLE NONE;'*From Left' LFROM VISIBLE NONE;'*To Left' LTO VISIBLE NONE;'*From Right' RFROM VISIBLE NONE;'*To Right' RTO VISIBLE NONE;'Left Parity' <None> VISIBLE NONE;'Right Parity' <None> VISIBLE NONE;'Full Street Name' FULLNAME VISIBLE NONE;'Prefix Direction' PREDIR VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' NAME VISIBLE NONE;'Suffix Type' TYPE VISIBLE NONE;'Suffix Direction' SUFDIR VISIBLE NONE;'Left City or Place' <None> VISIBLE NONE;'Right City or Place' <None> VISIBLE NONE;'Left County' <None> VISIBLE NONE;'Right County' <None> VISIBLE NONE;'Left State' <None> VISIBLE NONE;'Right State' <None> VISIBLE NONE;'Left State Abbreviation' <None> VISIBLE NONE;'Right State Abbreviation' <None> VISIBLE NONE;'Left ZIP Code' LZIP VISIBLE NONE;'Right ZIP Code' RZIP VISIBLE NONE;'Country Code' <None> VISIBLE NONE;'3-Digit Language Code' <None> VISIBLE NONE;'2-Digit Language Code' <None> VISIBLE NONE;'Admin Language Code' <None> VISIBLE NONE;'Left Block ID' <None> VISIBLE NONE;'Right Block ID' <None> VISIBLE NONE;'Left Street ID' <None> VISIBLE NONE;'Right Street ID' <None> VISIBLE NONE;'Street Rank' <None> VISIBLE NONE;'Min X value for extent' <None> VISIBLE NONE;'Max X value for extent' <None> VISIBLE NONE;'Min Y value for extent' <None> VISIBLE NONE;'Max Y value for extent' <None> VISIBLE NONE;'Left Additional Field' <None> VISIBLE NONE;'Right Additional Field' <None> VISIBLE NONE;'Altname JoinID' <None> VISIBLE NONE;'City Altname JoinID' <None> VISIBLE NONE", 
                                     out_address_locator=AddressLocator_OutputPath, 
                                     config_keyword="", 
                                     enable_suggestions="DISABLED")

