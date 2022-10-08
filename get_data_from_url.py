""" Use wget to read a .csv file into a pandas data frame. """
import os

# Directory of the raw data files
DATA_DIR = '/content/data/'

# Download the dataset
!wget -nc https://raw.githubusercontent.com/https-deeplearning-ai/MLEP-public/main/course2/week4-ungraded-lab/data/jena_climate_2009_2016.csv -P {DATA_DIR}

# Assign data path to a variable for easy reference
INPUT_FILE = os.path.join(DATA_DIR, 'jena_climate_2009_2016.csv')

import pandas as pd

# Put dataset in a dataframe
df = pd.read_csv(INPUT_FILE, header=0, index_col=0)

# Preview the last few rows
df.tail()
