import pandas as pd
import json
import requests
import numpy as np

def clean_data(df : pd.DataFrame) -> pd.DataFrame:
    # Cleaning
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df['GLA (Above Grade)']=df['GLA (Above Grade)'].str.replace(',','').astype(float)    
    df['Building_Value_Float']=df['FY24 Bldg Val'].str.replace('$','').str.replace(',','').astype(float)
    df['Land_Value_Float']=df['FY24 Land Val'].str.replace('$','').str.replace(',','').astype(float)
    df['Total_Value_Float']=df['FY24 Total Val'].str.replace('$','').str.replace(',','').astype(float)
    df['ELA']=df['ELA'].str.replace(',','').astype(float)

    # Calcs
    df['$/AGSF']=df['Building_Value_Float']/df['GLA (Above Grade)']
    df['$/Acre']=df['Land_Value_Float']/df['Acres']
    df['BGSF']=df['ELA']-df['GLA (Above Grade)']
    return df

def ingest(url):
    # Load the JSON data from the URL
    data = requests.get(url).json()

    # Initialize an empty list to store the dictionaries
    dicts = []

    # Initialize a counter for the parcelid
    parcelid = 1

    # Iterate over the list of strings
    for item in data:
        # Check if the item is a string
        if isinstance(item, str):
            # Split the string into the address and the property details
            address, details = item.split(': ', 1)
            
            # Convert the property details from a string to a dictionary
            details_dict = json.loads(details)
        else:
            # If the item is not a string, assign it a 'parcelid' and increment the parcelid
            address = f'parcelid_{parcelid}'
            details_dict = {}
            parcelid += 1
        
        # Combine the address and the property details into a single dictionary
        combined_dict = {'Address': address, **details_dict}
        
        # Append this dictionary to the list
        dicts.append(combined_dict)

    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(dicts)

    # Clean the data
    df_clean = clean_data(df)
    # Return the DataFrame
    return df_clean