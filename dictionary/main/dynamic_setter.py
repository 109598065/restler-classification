import json
import shutil
from pathlib import Path


class DynamicSetter:
    def __init__(self, directory, engine_settings, custom_value_gen):
        self._directory = directory
        self._engine_settings = engine_settings
        self._custom_value_gen = custom_value_gen

    def execute(self):
        try:
            self._create_engine_settings()
            # shutil.copy('copy_classification/custom_value_gen_template', Path(self._directory, self._custom_value_gen))
        except OSError as e:
            print(e)

    def _create_engine_settings(self):
        engine_settings = {
            'disable_cert_validation': True,
            'max_combinations': 20,
            'custom_value_generators': str(Path(self._directory, self._custom_value_gen))
        }
        file = open(Path(self._directory, self._engine_settings), "w")
        json.dump(engine_settings, file, indent=4)
        file.close()
