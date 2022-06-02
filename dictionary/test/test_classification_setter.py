import unittest
import shutil
from pathlib import Path
from dictionary.main.classification_setter import ClassificationSetter


class ClassificationSetterTestCase(unittest.TestCase):
    def test_classification_setter(self):
        directory = 'test'
        engine_settings = 'engine_settings_classification.json'
        custom_value_gen = 'custom_value_gen_classification.py'
        try:
            Path(directory).mkdir(parents=True)
            setter = ClassificationSetter(directory, engine_settings, custom_value_gen)
            setter.execute()
            self.assertTrue(Path.exists(Path(directory, engine_settings)))
            self.assertTrue(Path.exists(Path(directory, custom_value_gen)))
            self.assertTrue(Path.exists(Path(directory, 'custom_value_list')))
        finally:
            shutil.rmtree(Path(directory))


if __name__ == '__main__':
    unittest.main()
