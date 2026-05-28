from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger

STAGE_NAME="model trainer stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()


