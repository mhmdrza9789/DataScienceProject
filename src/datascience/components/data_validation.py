import os
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    
    def validation_all_columns(self) -> bool: # خروجی باید bool باشد
        try:
            validation_status = True # فرض اول بر درست بودن است
            data = pd.read_csv(self.config.unzip_data_dir, encoding='utf-8')
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break # به محض دیدن اولین ستون اشتباه، متوقف شو
                
                # ثبت نتیجه نهایی در فایل
            with open(self.config.STATUS_FILE, 'w', encoding='utf-8') as f:
                f.write(f"Validation status: {validation_status}")
                
            return validation_status
        except Exception as e:
            raise e