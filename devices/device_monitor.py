import threading as th
from time import sleep
from devices.device_reader import create_reader, AbstractReader


class DeviceMonitor:

    def __init__(self, config=None):
        """Standard constructor

        Args:
            config ([dict], optional): [Dictionary providing information about devices. For every device it should have its ID and information about accessing device, For more information lookup AbstractReader and its derivatives]. Defaults to None.

        Returns:
            [self]
        """
        self.lock = th.Lock()
        self._status = None
        self._devices = []
        self.stopping_event = th.Event()
        for device in config['devices']:
            self.devices = create_reader(device)

    def start(self, time_interval=1):
        """[summary]

        Args:
            time_interval (int, optional): [Time interval in seconds between internal updates of devices' statuses]. Defaults to 1.

        Returns:
            [None]:
        """
        self.thread = th.Thread(target=self._update,
                                name="DeviceMonitor", args=[time_interval])
        self.thread.start()

    def stop(self):
        """[Stop monitoring devices]

        Returns:
            [None]
        """
        self.stopping_event.set()
        self.thread.join()

    def get_statuses(self):
        """[Retrieve status for every connected device]

        Returns:
            [dict]: [Status for every connected device]
        """
        with self.lock:
            return self.status

    def _update(self, interval):
        """[Threaded method periodically updating statuses]

        Args:
            interval ([int]): [interval between updates]

        Returns:
            [None]:
        """
        while not self.stopping_event.isSet():
            temp_dict = {}
            for device in self.devices:
                temp_dict[device.id] = device.read()
                with self.lock:
                    self.status = temp_dict
            sleep(interval)

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
        if isinstance(value, dict):
            self._status = value

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
        if isinstance(value, AbstractReader):
            self._devices.append(value)

