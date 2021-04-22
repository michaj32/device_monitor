class DeviceMonitor:

    def __init__(self, config=None):
        """Standard constructor

        Args:
            config ([dict], optional): [Dictionary providing information about devices. For every device it should have its ID and information about accessing device, For more information lookup AbstractReader and its derivatives]. Defaults to None.

        Returns:
            [None]
        """
        return None

    def start(self, time_interval=1):
        """[summary]

        Args:
            time_interval (int, optional): [Time interval in seconds between internal updates of devices' statuses]. Defaults to 1.

        Returns:
            [None]:
        """
        return None

    def stop(self):
        """[Stop monitoring devices]

        Returns:
            [None]
        """
        return None

    def get_statuses(self):
        """[Retrieve status for every connected device]

        Returns:
            [dict]: [Status for every connected device]
        """
        return self.status

    def _update(self, interval):
        """[Threaded method periodically updating statuses]

        Args:
            interval ([int]): [interval between updates]

        Returns:
            [None]:
        """
        return None

    @property
    def status(self):
        """[status getter]

        Returns:
            [dict]: [retrive private status of devices]
        """
        return self._status

    @status.setter
    def status(self, value):
        """[status setter]

        Args:
            value ([dict]): [status for each device]

        Returns:
            [None]
        """
        return None

    @property
    def devices(self):
        """[devices getter]

        Returns:
            [list]: [List of AbstractReader derivative instances]
        """
        return self._devices

    @devices.setter
    def devices(self, value):
        """[devices setter
            Appends list of AbstractReader derivative instances]

        Args:
            value ([AbstractReader derivative eg. FileReader]): [Instance of device Reader]

        Returns:
            [None]
        """
        return None
