import json
import shutil
from pathlib import Path


class ClassificationSetter:
    def __init__(self, directory, engine_settings, custom_value_gen):
        self._directory = directory
        self._engine_settings = engine_settings
        self._custom_value_gen = custom_value_gen

    def execute(self):
        try:
            self._create_engine_settings()
            custom_value_gen_path = Path(__file__).parent.absolute().joinpath('copy_classification'
                                                                              '/custom_value_gen_template')
            custom_value_list_path = Path(__file__).parent.absolute().joinpath('copy_classification/custom_value_list')
            shutil.copy(custom_value_gen_path, Path(self._directory, self._custom_value_gen))
            shutil.copytree(custom_value_list_path, Path(self._directory,
                                                         'copy_classification/custom_value_list'))
        except OSError as e:
            print(e)

    def _create_engine_settings(self):
        engine_settings = {
            'disable_cert_validation': True,
            'max_combinations': 512,
            'custom_value_generators': str(Path(self._directory, self._custom_value_gen))
        }
        file = open(Path(self._directory, self._engine_settings), "w")
        json.dump(engine_settings, file, indent=4)
        file.close()
