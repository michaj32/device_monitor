import json
from pathlib import Path


class AbstractReader:
    def __init__(self, config):
        """Standard constructor

        Args:
            config ([dict]): [Must include (str)ID and (list)measures]

        Returns:
            [self]
        """
        self._id = None
        self._measures = None
        self._measurements = None
        self.id = config.get('ID')
        self.measures = config.get('measures')

    def read(self):
        """[Interface method for reading from device. Should be overwritten]

        Returns:
            [dict]: [read measures and its values]
        """
        return self.measurements

    @property
    def id(self):
        """[device ID getter]

        Returns:
            [str]: [description]
        """
        return self._id

    @id.setter
    def id(self, value):
        """[device id setter]

        Args:
            value ([str]): [device ID]

        Returns:
            [None]
        """
        if isinstance(value, str):
            self._id = value
        else:
            raise ValueError("Device ID should be of type str")

    @property
    def measures(self):
        """[measures getter]

        Returns:
            [list]: [keywords for read measures]
        """
        return self._measures

    @measures.setter
    def measures(self, value):
        """[measures setter]

        Args:
            value ([list]): [keywords for read measures]

        Returns:
            [None]
        """
        if isinstance(value, list):
            if len(value) == 0:
                raise ValueError(f"Measures cannot be of length 0")
            self._measures = value
        else:
            raise ValueError(
                f"Measures should be of type list not {type(value)}")

    @property
    def measurements(self):
        """[measurements getter]

        Returns:
            [dict]: [read measurements]
        """
        return self._measurements

    @measurements.setter
    def measurements(self, value):
        """[measurements setter]

        Args:
            value ([dict]): [read measurements]

        Returns:
            [None]
        """
        if isinstance(value, dict):

            for key in self.measures:
                if key not in value:
                    raise ValueError(
                        f"Couldn't read value {key} from device {self.id}")

            for key in list(value.keys()):
                if key not in self.measures:
                    value.pop(key, None)

            self._measurements = value


class FileReader(AbstractReader):
    def __init__(self, config):
        """Standard constructor

        Args:
            config ([dict]): [Must include (str)ID, (str)Filepath and (list)measures]

        Returns:
            [self]
        """
        super().__init__(config)
        self._file_path = None
        self.file_path = config.get('file_path')

    def read(self):
        """[reading from device]

        Returns:
            [dict]: [read measures and its values]
        """
        with open(self.file_path, 'r') as file:
            self.measurements = json.load(file)
        return self.measurements

    @property
    def file_path(self):
        """[file_path getter]

        Returns:
            [str]: [path to device file]
        """
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        """[file_path setter]

        Args:
            value ([str]): [path to device file]

        Returns:
            [None]
        """
        if isinstance(value, str):
            if Path(value).is_file():
                self._file_path = value
            else:
                raise FileNotFoundError(
                    f"File {value} does not exist. Cannot create device {self.id}.")
        else:
            raise ValueError(
                f"file_path should be of type str, {type(value)} given.")


def create_reader(config):
    if config['type'] == "file":
        return FileReader(config)
