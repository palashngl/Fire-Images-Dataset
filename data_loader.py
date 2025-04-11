import os
import pandas as pd
import rarfile
from zipfile import ZipFile

def extract_rar(rar_path, extract_to='./extracted_data'):
    """Extracts a .rar file to a specified directory"""
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with rarfile.RarFile(rar_path) as rf:
        rf.extractall(path=extract_to)
    print(f"Extracted to {extract_to}")

def load_sensor_data(sensor_csv_path):
    """Loads sensor CSV data"""
    return pd.read_csv(sensor_csv_path)

# Example usage
# extract_rar('Fire_Image_Sensor_Data.rar')
# df = load_sensor_data('./extracted_data/sensors/Raw_data.csv')
