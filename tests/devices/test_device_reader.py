import pytest
import json
from devices.device_reader import FileReader

@pytest.fixture
def config():
    config = {
            "ID": 1,
            "file_path": "assets/1.json",
            "measures": ["current", "voltage"]
        }

class TestDeviceReader:
    
    def test_initialize_input_values(self, config):
        reader = FileReader(config = config)
        assert reader.id == config['id']
        assert reader.file_path == config['file_path']
        assert reader.measures == config['measures']

    def test_normal_read_from_file(self, config):
        reader = FileReader(config = config)
        with open(config['file_path', 'r']) as file:
            file_read = json.load(file)
        for key in file_read.keys():
            if key not in config['measures']:
                file_read.pop(key, None)
        assert file_read == reader.read()

    def test_wrong_file_path(self, config):
        config['file_path'] = ""
        with pytest.raises(FileNotFoundError):
            reader = FileReader(config = config)
        config['file_path'] = None
        with pytest.raises(ValueError):
            reader = FileReader(config = config)
    def test_empty_measures(self, config):
        config['measures'] = []
        with pytest.raises(ValueError):
            reader = FileReader(config = config)

    def test_no_id(self, config):
        config.pop('ID', None)
        with pytest.raises(ValueError):
            reader = FileReader(config = config)
