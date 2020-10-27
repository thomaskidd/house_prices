################################ 
# Main file for housing prices ML model
#
# by Thomas Kidd, 2020
#

#### Imports and System Setup

# Suppress TF warnings
import os
import logging
# TF debug message level
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
logging.getLogger('tensorflow').setLevel(logging.FATAL)

# TF
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

# Helper libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# Custom libraries
from data_prep import InputData

#### Load and Clean Data

train = InputData("data/train.csv")
train.split_labels_and_features(["SalePrice"])

# Print feature and label data
print(train.features.head())
print(train.labels.head())

#### Build and Test Models

#### Compute Predictions
