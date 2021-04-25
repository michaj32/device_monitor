import json
import threading as th
from time import sleep
from random import randrange
from devices.device_monitor import DeviceMonitor

def main():
    config = {
        "devices": [{
            "type": "file",
            "ID": "1",
            "file_path": "assets/1.json",
            "measures": ["current", "voltage"]
        }, {
            "type": "file",
            "ID": "2",
            "file_path": "assets/2.json",
            "measures": ["current", "voltage"]
        }]
    }
    monitor = DeviceMonitor(config)
    monitor.start()
    sleep(1)
    event = th.Event()
    thread = th.Thread(target=change_periodically_at_random, name = "ScriptDeviceMonitor", args=[config, event])
    thread.start()
    i = 0
    while i<2000:
        status = monitor.get_statuses()
        print("DeviceMonitor current status:", status)
        i+=1
        sleep(1)
    event.set()
    thread.join()
    monitor.stop()
    

def change_periodically_at_random(config, event):
    while not event.isSet():
        for device in config['devices']:
            with open(device["file_path"], 'r') as file:
                file_status = json.load(file)
            for key in file_status.keys():
                if isinstance(file_status[key], (int, float)):
                    file_status[key] += randrange(-50, 50)
            with open(device["file_path"], 'w') as file:
                json.dump(file_status, file)
        sleep(1)
if __name__ == "__main__":
    main()