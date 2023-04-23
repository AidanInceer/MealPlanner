from dataclasses import dataclass

import yaml
from yaml import SafeLoader


@dataclass
class Config:
    @staticmethod
    def create_config():
        with open(r"./config/config.yaml") as f:
            config = yaml.load(f, Loader=SafeLoader)
        return config
