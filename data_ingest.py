import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


#Ayush Singh End-to-End project on Data Ingestion using zipfile package

with zipfile.ZipFile('./data/archive.zip','r') as zip_ref:
    zip_ref.extractall("extracted_data")

#create a list of all the items in extracted_data path:
extracted_files =  os.listdir('extracted_data')


#join the parent directory path with the csv file to form a new path to the csv file ie extracted_data/file.csv
for i in extracted_files:
    csv_data_path = os.path.join('extracted_data',i)



print(csv_data_path)#before \
csv_data_path = csv_data_path.replace("\\","/")
print(csv_data_path)#after /


#using the new modified csv path we read it into a pandas dataframe
df = pd.read_csv(csv_data_path)
print(df)