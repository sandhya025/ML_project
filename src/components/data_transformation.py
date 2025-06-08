import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")
    cluster_model_file_path = os.path.join('artifacts', "kmeans_model.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This function is responsible for data transformation.
        """
        try:
            # Define numerical and categorical columns
            numerical_columns = ['Transaction ID', 'Age', 'Quantity', 'Price per Unit', 'Total Amount']
            categorical_columns = ['Customer ID', 'Gender', 'Product Category']

            # Numerical pipeline
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),  # Handle missing values
                    ("scaler", StandardScaler())  # Scale numerical data
                ]
            )

            # Categorical pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),  # Handle missing values
                    ("one_hot_encoder", OneHotEncoder()),  # Encode categorical data
                    ("scaler", StandardScaler(with_mean=False))  # Scale encoded data
                ]
            )

            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            # Combine pipelines into a ColumnTransformer
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_data_path: str, test_data_path: str) -> pd.DataFrame:
        """
        This function applies preprocessing and clustering to customer data.
        """
        try:
            train_df= pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            logging.info("Data loaded successfully")
            logging.info("Initiating preprocessing")
            preprocessor = self.get_data_transformer_object()    
            target_column = 'Total Amount'
            # Separate features and target variable 

            return customer_data

        except Exception as e:
            raise CustomException(e, sys)