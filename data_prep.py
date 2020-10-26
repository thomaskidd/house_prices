################################ 
# Data Prep classes
#
# Loads, cleans, and formats data
# Returns a preprocessing layer to handle
# raw data
#
# by Thomas Kidd, 2020
#

class InputData:

    def __init__(self):
        return

    #### Data loading
    
    def load_from_csv(self, csv):
        return

    #### Data cleanup

    # Remove useless columns
    def remove_columns(self):
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
