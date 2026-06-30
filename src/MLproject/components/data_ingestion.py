import os 
import sys
import pandas as pd
from src.MLproject.logger import logging
from src.MLproject.exception import CustomException 
from sklearn.model_selection import train_test_split


from dataclasses import dataclass
@dataclass
class DataIngestion:
    def __init__(self):
        self.train_data_path = os.path.join('artifacts', 'train.csv')
        self.test_data_path = os.path.join('artifacts', 'test.csv')
        self.raw_data_path = os.path.join('artifacts', 'raw.csv')

    def initiate_data_ingestion(self):
        logging.info("Reading the CSV file")
        print("Reading the CSV file")
        df = pd.read_csv("StudentsPerformancedataset.csv")
        print("CSV file read successfully")
        os.makedirs("artifacts", exist_ok=True)
        print("Artifacts directory created")
        df.to_csv(self.raw_data_path, index=False)
        logging.info("Data ingestion completed successfully")

    
        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
        train_set.to_csv(self.train_data_path, index=False)
        test_set.to_csv(self.test_data_path, index=False)

        return self.train_data_path, self.test_data_path