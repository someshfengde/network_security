import os
import sys
import numpy as np
import pandas as pd


"""
Data Ingestion related constants start with DATA_INGESTION
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABSE_NAME: str = "NS"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "NetworkData"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
# Local CSV file path for data ingestion
DATA_INGESTION_LOCAL_CSV_PATH: str = "NetworkData/data.csv"


"""
Defining the common constant variables for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "data.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Defining the common constant variables for training pipeline for data validation
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_reprot"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "reprot.yaml"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")


"""
Data Transformation constants
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# KNN imputer class to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform"
}

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'


# Model trainer
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
MODEL_FILE_NAME = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD = 0.05


SAVED_MODEL_DIR = os.path.join("saved_models")