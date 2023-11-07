# Import necessary libraries
import streamlit as st
import subprocess
import xarray as xr
import pandas as pd
import glob
import matplotlib.pyplot as plt

# Function to download data from S3
def download_s3_data(start_hour, end_hour, interval, date, init_condition):
    for hour in range(start_hour, end_hour + 1, interval):
        fhour = f"{hour:03d}"
        s3_file_path = f"s3://noaa-gefs-pds/gefs.{date}/{init_condition}/atmos/pgrb2ap5/gec00.t00z.pgrb2a.0p50.f{fhour}"
        local_file_path = f"./gec00.t00z.pgrb2a.0p50.f{fhour}"
        aws_cli_command = [
            "aws", "s3", "--no-sign-request", "cp",
            s3_file_path,
            local_file_path
        ]
        result = subprocess.run(aws_cli_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f"Error copying f{fhour}: {result.stderr.decode('utf-8')}")
        else:
            print(f"Successfully copied f{fhour}")

# Streamlit interface
st.title('GEFS Data Downloader and Analyzer')

# User input for date
date = st.date_input("Select the Date")

# User input for region
region_lon = st.slider('Select longitude range', -180, 180, (-98, -97))
region_lat = st.slider('Select latitude range', -90, 90, (30.5, 30))

# Button to start the download and analysis
if st.button('Start Download and Analysis'):
    start_hour = 6
    end_hour = 384
    interval = 6
    init_condition = "00"
    date_str = date.strftime("%Y%m%d")
    
    # Download data
    download_s3_data(start_hour, end_hour, interval, date_str, init_condition)
    
    # Now we assume that the files are downloaded and converted to .nc format
    
    # Temperature Analysis
    pattern = 'gec00.t00z.pgrb2a.0p50.f*.nc'
    file_list = glob.glob(pattern)
    file_list.sort()
    
    # Assuming the conversion to .nc has been completed as in the original code
    # and that all the other required steps have been performed
    
    # Process the temperature data
    # ... (process the temperature data as in the original code)
    
    # Precipitation Analysis
    # ... (process the precipitation data as in the original code)

# The analysis results will be shown after the user clicks the button
# and the data processing is complete. Place the analysis and plotting code here.
