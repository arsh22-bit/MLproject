from src.MLproject.logger import logging
from src.MLproject.exception import CustomException
from src.MLproject.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("Starting the ML project application...")
    
    
    obj = DataIngestion()    
    train_data_path, test_data_path = obj.initiate_data_ingestion()