"""
teste Configuration of all relevant parameters to use in the project and data format validation
"""

import os
from pathlib import Path
from typing import List, Dict
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

class DataSchema(BaseModel):
    """
    Schema for raw data and model data
    """
    quanti_variables: List[str]
    quali_variables: List[str]
    model_variables: List[str]

class Config(BaseModel):
    """Master config object."""

    data_config: DataSchema
    ml_config: ModelConfig

class RawDataSchema(BaseModel):
    """
    Data Model Input schema
    """
    tenure: int
    MonthlyCharges : int
    TotalCharges : float
    OnlineSecurity: str
    TechSupport : str

class MultipleDataSchema(BaseModel):
    '''Master model validation object'''
    inputs_raw: List[RawDataSchema]

def create_and_validate_config(cfg_path = CONFIG_FILE_PATH) -> Config:
    """Run validation on config values."""

    parsed_config = None
    try:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
    except:
        raise OSError(f"Did not find config file at path: {cfg_path}")

    
    _config = Config(
        data_config=DataSchema(**parsed_config.data),
        ml_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()

if __name__ == '__main__':
    print(create_and_validate_config())
