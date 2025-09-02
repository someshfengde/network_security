from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

## Config of data  ingestion config
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact 

import os
import sys
import numpy as np
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        pass
    def export_collection_as_dataframe(self):
        """
        Read data from local CSV file
        """
        try:
            # Read data from local CSV file
            local_csv_path = self.data_ingestion_config.local_csv_path
            logging.info(f"Reading data from local CSV file: {local_csv_path}")
            
            if not os.path.exists(local_csv_path):
                raise FileNotFoundError(f"CSV file not found at: {local_csv_path}")
            
            df = pd.read_csv(local_csv_path)
            logging.info(f"Successfully loaded data with shape: {df.shape}")
            
            # Replace "na" strings with actual NaN values
            df.replace({"na": np.nan}, inplace=True)
            
            return df
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def export_data_into_feature_store(self, dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train test split on the dataframe")
            logging.info("Exited split_data_as_train_test method")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Exporting train and test file path")
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )
            logging.info(f"Exported train and test file path")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, 
                                                        test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)