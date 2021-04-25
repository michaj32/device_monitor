class AbstractReader:
    def __init__(self, config):
        """Standard constructor

        Args:
            config ([dict]): [Must include (str)ID and (list)measures]

        Returns:
            [self]
        """
        pass

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
        return None
    
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
        return None

    @property
    def measurements(self):
        """[measurements getter]

        Returns:
            [dict]: [read measurements]
        """
        return self._measurments

    @measurements.setter
    def measurements(self, value):
        """[measurements setter]

        Args:
            value ([dict]): [read measurements]

        Returns:
            [None]
        """
        return None


class FileReader(AbstractReader):
    def __init__(self, config):
        """Standard constructor

        Args:
            config ([dict]): [Must include (str)ID, (str)Filepath and (list)measures]

        Returns:
            [self]
        """
        pass

    def read(self):
        """[reading from device]

        Returns:
            [dict]: [read measures and its values]
        """
        return self.measurements

    @property
    def file_path(self):
        """[file_path getter]

        Returns:
            [str]: [path to device file]
        """
        return self._filepath

    @file_path.setter
    def file_path(self, value):
        """[file_path setter]

        Args:
            value ([str]): [path to device file]

        Returns:
            [None]
        """
        return None
