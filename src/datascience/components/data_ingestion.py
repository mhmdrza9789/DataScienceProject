import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with folowing info : \n{headers}")
        else:
            logger.info(f"file already exist")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)




# class DataIngestion:
#     def __init__(self, config: DataIngestionConfig):
#         self.config = config

#     # متد اصلی: بر اساس نوع منبع، متد مناسب را صدا می‌زند
#     def download(self):
#         source_type = self.config.source_type  # مثلا "url" یا "kaggle" یا "mongodb"
#         logger.info(f"Starting data ingestion from source type: {source_type}")

#         if source_type == "url":
#             self._download_from_url()
#         elif source_type == "kaggle":
#             self._download_from_kaggle()
#         elif source_type == "mongodb":
#             self._download_from_mongodb()
#         else:
#             raise ValueError(f"Unsupported source_type: {source_type}")

#     # ---------------- URL / GitHub ----------------
#     def _download_from_url(self):
#         local_path = self.config.local_data_file

#         if not os.path.exists(local_path):
#             source_url = self.config.source_config.source_url
#             filename, headers = request.urlretrieve(
#                 url=source_url,
#                 filename=local_path
#             )
#             logger.info(f"{filename} downloaded with headers: \n{headers}")
#         else:
#             logger.info(f"File already exists at {local_path}")

#     # ---------------- Kaggle ----------------
#     def _download_from_kaggle(self):
#         # فعلا فقط اسکلت - بعدا اگر خواستی دیتاست واقعی را اضافه می‌کنیم
#         source_cfg = self.config.source_config
#         dataset_id = source_cfg.dataset_id
        
#         logger.info(f"Downloading Kaggle dataset: {dataset_id}")
        
#         # api = KaggleApi()
#         # api.authenticate()
#         #
#         # api.dataset_download_files(
#         #     dataset=dataset_id,
#         #     path=str(self.config.root_dir),
#         #     unzip=True
#         # )
#         #
#         # اگر دیتاست zip نبود، می‌تونی خودت روی فایل کار کنی.

#         logger.info("Kaggle download logic not implemented yet (skeleton only).")

#     # ---------------- MongoDB ----------------
#     def _download_from_mongodb(self):
#         source_cfg = self.config.source_config
        
#         logger.info("Starting MongoDB data export (skeleton).")
        
#         # uri = source_cfg.uri
#         # db_name = source_cfg.database
#         # collection_name = source_cfg.collection
#         #
#         # client = pymongo.MongoClient(uri)
#         # collection = client[db_name][collection_name]
#         #
#         # docs = list(collection.find())
#         # df = pd.DataFrame(docs)
#         # df.to_csv(self.config.local_data_file, index=False)
#         #
#         # logger.info(f"MongoDB data exported to {self.config.local_data_file}")

#         logger.info("MongoDB download logic not implemented yet (skeleton only).")

#     # ---------------- Extract ZIP ----------------
#     def extract_zip_file(self):
#         unzip_path = self.config.unzip_dir
#         os.makedirs(unzip_path, exist_ok=True)

#         with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
#             zip_ref.extractall(unzip_path)

#         logger.info(f"Files extracted to: {unzip_path}")
