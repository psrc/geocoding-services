# Create Snohomish County address locators
# The new address locator will be created in a separate file folder.

# Import system modules
import os, arcpy

rootDir = r'J:\Projects\Geocoding\19GEOCODING'
inDir = r'Setup\3FinalProducts' 
county = 'Snohomish'

arcpy.env.workspace = os.path.join(rootDir, inDir, county)
AddressLocator_OutputPath = os.path.join(rootDir, "AddressLocators\\19sno_prcl")

# parcel based
arcpy.CreateAddressLocator_geocoding(in_address_locator_style = "US Address - Single House", 
                                     in_reference_data = "prcl.shp 'Primary Table'", 
                                     in_field_map = "'Point Address ID' FID VISIBLE NONE;'Street ID' <None> VISIBLE NONE;'*House Number' SITUSHOUSE VISIBLE NONE;Side <None> VISIBLE NONE;'Full Street Name' <None> VISIBLE NONE;'Prefix Direction' SITUSPREFX VISIBLE NONE;'Prefix Type' <None> VISIBLE NONE;'*Street Name' SITUSSTRT VISIBLE NONE;'Suffix Type' SITUSTTYP VISIBLE NONE;'Suffix Direction' SITUSPOSTD VISIBLE NONE;'City or Place' <None> VISIBLE NONE;County <None> VISIBLE NONE;State <None> VISIBLE NONE;'State Abbreviation' <None> VISIBLE NONE;'ZIP Code' SITUSZIP VISIBLE NONE;'Country Code' <None> VISIBLE NONE;'3-Digit Language Code' <None> VISIBLE NONE;'2-Digit Language Code' <None> VISIBLE NONE;'Admin Language Code' <None> VISIBLE NONE;'Block ID' <None> VISIBLE NONE;'Street Rank' <None> VISIBLE NONE;'Display X' X_COORD VISIBLE NONE;'Display Y' Y_COORD VISIBLE NONE;'Min X value for extent' <None> VISIBLE NONE;'Max X value for extent' <None> VISIBLE NONE;'Min Y value for extent' <None> VISIBLE NONE;'Max Y value for extent' <None> VISIBLE NONE;'Additional Field' <None> VISIBLE NONE;'Altname JoinID' <None> VISIBLE NONE;'City Altname JoinID' <None> VISIBLE NONE", 
                                     out_address_locator = AddressLocator_OutputPath, 
                                     config_keyword = "", 
                                     enable_suggestions= "DISABLED")