import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self) ->bool:
        try:
            varlidation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    varlidation_status = False

                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {varlidation_status}")

                else:
                    varlidation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status: {varlidation_status}")

            return varlidation_status
        
        except Exception as e:
            raise e