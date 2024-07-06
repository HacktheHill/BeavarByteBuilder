from tkinter import *
import os
import json

class ScanFolders:
    def scanFolders(self, sensor_options):
        directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\..\\drivers\\mcus\\')
        print('Directory:', directory_path)
        folders = [f.name for f in os.scandir(directory_path) if f.is_dir()] # non recursive
        print('folders', folders)
        for name in folders:
            f = open(directory_path + name + '\\' + name + '-config.json')
            print('f', f)
            data = json.load(f)
            sensor_options[name] = []
            for i in data['sensors']:
                sensor_options[name].append(i)
        f.close()