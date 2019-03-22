# Create Kitsap County address locators
# The new address locators will be created in a separate file folder.

# Import system modules
import os, arcpy

rootDir = r'J:\Projects\Geocoding\19GEOCODING'
inDir = r'Setup\3FinalProducts' 
county = 'Kitsap'

arcpy.env.workspace = os.path.join(rootDir, inDir, county)

# site address based (point file)
AddressLocator_OutputPath = os.path.join(rootDir, "AddressLocators\\19kit_siteaddr")
arcpy.CreateAddressLocator_geocoding(in_address_locator_style="US Address - Single House", 
                                     in_reference_data="siteaddr.shp 'Primary Table'", 
                                     in_field_map="'Point Address ID' FID VISIBLE NONE;'Street ID' <None> VISIBLE NONE;'*House Number' HOUSE_NO VISIBLE NONE;Side <None> VISIBLE NONE;'Full Street Name' <None> VISIBLE NONE;'Prefix Direction' PREFIX VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' STREETNAME VISIBLE NONE;'Suffix Type' STREETTYPE VISIBLE NONE;'Suffix Direction' SUFFIX VISIBLE NONE;'City or Place' CITY VISIBLE NONE;County <None> VISIBLE NONE;State STATE VISIBLE NONE;'State Abbreviation' STATE VISIBLE NONE;'ZIP Code' ZIP_CODE VISIBLE NONE;'Country Code' <None> VISIBLE NONE;'3-Digit Language Code' <None> VISIBLE NONE;'2-Digit Language Code' <None> VISIBLE NONE;'Admin Language Code' <None> VISIBLE NONE;'Block ID' <None> VISIBLE NONE;'Street Rank' <None> VISIBLE NONE;'Display X' '' VISIBLE NONE;'Display Y' <None> VISIBLE NONE;'Min X value for extent' <None> VISIBLE NONE;'Max X value for extent' <None> VISIBLE NONE;'Min Y value for extent' <None> VISIBLE NONE;'Max Y value for extent' <None> VISIBLE NONE;'Additional Field' <None> VISIBLE NONE;'Altname JoinID' <None> VISIBLE NONE;'City Altname JoinID' <None> VISIBLE NONE", 
                                     out_address_locator=AddressLocator_OutputPath, 
                                     config_keyword="", 
                                     enable_suggestions="DISABLED")

# street centerline based
AddressLocator_OutputPath = os.path.join(rootDir, "AddressLocators\\19kit_stcl")
arcpy.CreateAddressLocator_geocoding(in_address_locator_style="US Address - Dual Ranges", 
                                     in_reference_data="stcl.shp 'Primary Table'", 
                                     in_field_map="'Feature ID' FID VISIBLE NONE;'*From Left' FR_ADDR_L VISIBLE NONE;'*To Left' TO_ADDR_L VISIBLE NONE;'*From Right' FR_ADDR_R VISIBLE NONE;'*To Right' TO_ADDR_R VISIBLE NONE;'Left Parity' <None> VISIBLE NONE;'Right Parity' <None> VISIBLE NONE;'Full Street Name' FULL_NAME VISIBLE NONE;'Prefix Direction' PREFIX VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' STREETNAME VISIBLE NONE;'Suffix Type' STREETTYPE VISIBLE NONE;'Suffix Direction' SUFFIX VISIBLE NONE;'Left City or Place' <None> VISIBLE NONE;'Right City or Place' <None> VISIBLE NONE;'Left County' <None> VISIBLE NONE;'Right County' <None> VISIBLE NONE;'Left State' <None> VISIBLE NONE;'Right State' <None> VISIBLE NONE;'Left State Abbreviation' <None> VISIBLE NONE;'Right State Abbreviation' <None> VISIBLE NONE;'Left ZIP Code' ZIP_CODE_L VISIBLE NONE;'Right ZIP Code' ZIP_CODE_R VISIBLE NONE;'Country Code' <None> VISIBLE NONE;'3-Digit Language Code' <None> VISIBLE NONE;'2-Digit Language Code' <None> VISIBLE NONE;'Admin Language Code' <None> VISIBLE NONE;'Left Block ID' <None> VISIBLE NONE;'Right Block ID' <None> VISIBLE NONE;'Left Street ID' <None> VISIBLE NONE;'Right Street ID' <None> VISIBLE NONE;'Street Rank' <None> VISIBLE NONE;'Min X value for extent' <None> VISIBLE NONE;'Max X value for extent' <None> VISIBLE NONE;'Min Y value for extent' <None> VISIBLE NONE;'Max Y value for extent' <None> VISIBLE NONE;'Left Additional Field' <None> VISIBLE NONE;'Right Additional Field' <None> VISIBLE NONE;'Altname JoinID' <None> VISIBLE NONE;'City Altname JoinID' <None> VISIBLE NONE", 
                                     out_address_locator=AddressLocator_OutputPath, 
                                     config_keyword="", 
                                     enable_suggestions="DISABLED")