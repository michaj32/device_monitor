from _pytest.nodes import File
import pytest
import json
from time import sleep
import threading as th
from devices.device_monitor import DeviceMonitor

@pytest.fixture
def config():
    config = {
        "devices":[{
            "type": "file",
            "ID": 1,
            "file_path": "assets/1.json",
            "measures": ["current", "voltage"]
        },{
            "type": "file",
            "ID": 2,
            "file_path": "assets/2.json",
            "measures": ["current", "voltage"]
        }]
    }
    return config


class TestDeviceMonitor:
    
    def test_get_statuses_normal(self, config):
        monitor = DeviceMonitor(config = config)
        monitor.start()
        statuses = monitor.get_statuses()
        assert isinstance(statuses, dict)
        for device in config["devices"]:
            assert device["ID"] in statuses.keys()
        monitor.stop()

    def test_init_no_devices(self):
        with pytest.raises(Exception):
            monitor = DeviceMonitor(config = {})
        
    def test_thread_created(self, config):
        thread_names = [thread.name for thread in th.enumerate()]
        monitor = DeviceMonitor(config = config)
        monitor.start()
        assert "DeviceMonitor" in thread_names
        monitor.stop()
        assert "DeviceMonitor" not in thread_names

    def test_status_changed(self, config):
        monitor = DeviceMonitor(config = config)
        monitor.start()
        previous_status = monitor.get_statuses()
        for key, device in config.items():
            with open(device["file_path"], 'w') as file:
                file_status = json.load(file)
                for key in file_status.keys():
                    file_status['key']+=1
                json.dump(file_status, file)
        sleep(1)
        current_statuses = monitor.get_statuses()
        for id in current_statuses.keys():
            prev_device = previous_status[id]
            cur_device = current_statuses[id]
            for measure in prev_device.keys():
                assert cur_device[measure] == prev_device[measure]+1
        monitor.stop()
                
                