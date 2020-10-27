################################ 
# Data Prep classes
#
# Loads, cleans, and formats data
# Returns a preprocessing layer to handle
# raw data
#
# by Thomas Kidd, 2020
#

import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

class InputData:
    
    #### Data loading

    def __init__(self, csv):
        self.__data = pd.read_csv(csv) # We only want outsiders to be able to access features and labels
        self.features = pd.DataFrame()
        self.labels = pd.DataFrame()
        return
    
    def info(self):
        print(self.__data.info())
        return

    #### Data cleanup

    # Extract labels (and features) from dataset
    def split_labels_and_features(self, labelKeys):
        if self.labels.empty:
            for key in labelKeys:
                if key in self.__data:
                    self.labels[key] = self.__data.pop(key)
        
        self.features = self.__data

        return
    
    # Remove useless columns
    def remove_columns(self, columns):
        for col in columns:
            if col in self.features:
                self.data.pop(col)

        return

    # Replace nan in certain columns
    # In some cases, NaN is not a missing value but a valid option
    def fill_nan(self, columns, fillers):
        for col, filler in columns, fillers:
            if col in self.features:
                self.features[col].fillna(filler, inplace=True)

        return

    # Attempt to impute values
    def impute_values(self):
        return

    # Drop useless rows
    def remove_rows(self):
        return

    #### Build Preprocessing layer

    # Returns a preprocessing layer based on the input data
    def create_preprocessing_layer(self):
        return
