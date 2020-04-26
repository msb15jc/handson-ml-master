"""
Sample input

# file paths
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
# file name do not start with "/", otherwise the os.path.join won't work
FILE_NAME = "housing.tgz"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "housing.tgz"
CSV_FILE_NAME = "housing.csv"

import fetch_online_datasets as fod
fod.fetch_online_datasets(web_url = DOWNLOAD_ROOT, project_path = HOUSING_PATH, file_name = FILE_NAME)
housing = fod.load_raw_data(project_path = HOUSING_PATH, file_name = CSV_FILE_NAME)
"""

import os
import tarfile
from six.moves import urllib
import numpy as np
import pandas as pd

def fetch_online_datasets(web_url, project_path, file_name):
    if not os.path.isdir(project_path):
        os.makedirs(project_path)
    tgz_path = os.path.join(project_path, file_name)
    DOWNLOAD_URL = web_url + tgz_path
    urllib.request.urlretrieve(DOWNLOAD_URL, tgz_path)
    dataset_raw = tarfile.open(tgz_path)
    dataset_raw.extractall(path = project_path)
    dataset_raw.close()

    
    
    
def load_raw_data(project_path, csv_file_name):
    csv_path = os.path.join(project_path, csv_file_name)
    return pd.read_csv(csv_path)