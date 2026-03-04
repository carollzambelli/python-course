"""
teste Configuration of all relevant parameters to use in the project and data format validation
"""

from pathlib import Path
from typing import List
from pydantic import BaseModel
from strictyaml import load

PACKAGE_ROOT = Path().resolve()
ASSETS_PATH =  PACKAGE_ROOT / "assets"
CONFIG_FILE_PATH = ASSETS_PATH / "config.yml"

class ModelConfig(BaseModel):
    """
    All configuration relevant to model application
    """
    trained_model_file: str
    preprocess_model_file : str

class DataConfig(BaseModel):
    """
    All configuration relevant to data
    variables manipulation
    """

    quali_variables: List[str]
    quanti_variables: List[str]

class Config(BaseModel):
    """Master config object."""

    data_config: DataConfig
    ml_config: ModelConfig

class ModelDataSchema(BaseModel):
    """
    Data Model Input schema
    """
    tenure: int
    MonthlyCharges : int
    TotalCharges : float
    OnlineSecurity_No : str
    OnlineSecurity_No_internet_service : str
    OnlineSecurity_Yes : str
    TechSupport_No : str
    TechSupport_No_internet_service : str
    TechSupport_Yes : str

class MultipleDataSchema(BaseModel):
    inputs: List[ModelDataSchema]

def create_and_validate_config(cfg_path = CONFIG_FILE_PATH) -> Config:
    """Run validation on config values."""

    parsed_config = None
    try:
        with open(CONFIG_FILE_PATH, "r") as conf_file:
            parsed_config = load(conf_file.read())
    except:
        raise OSError(f"Did not find config file at path: {CONFIG_FILE_PATH}")

    
    _config = Config(
        data_config=DataConfig(**parsed_config.data),
        ml_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()


if __name__ == '__main__':
    print(PACKAGE_ROOT, ASSETS_PATH, CONFIG_FILE_PATH) 
    print(config)