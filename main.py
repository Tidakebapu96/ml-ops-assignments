from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline




STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"Starting: {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"Starting: {STAGE_NAME}")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"Completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"
try:
    logger.info(f"Starting: {STAGE_NAME}")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"Completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"Starting: {STAGE_NAME}")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f"Completed: {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
        raise e


