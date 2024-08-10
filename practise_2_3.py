import xml.etree.ElementTree as ET
import json


class SensorXML:
    def __init__(self, path: str):
        self.path = path

    def get_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = file.read()
        return data

class JSONAdapter:
    def __init__(self, sensor_xml: SensorXML):
        self.sensor_xml = sensor_xml

    def get_data(self):
        xml_data = self.sensor_xml.get_data()
        root = ET.fromstring(xml_data)
        return self.xml_to_json(root)

    @staticmethod
    def xml_to_json(root):
        dict_data = {}
        for element in root:
            dict_data[element.tag] = element.text
        # {"altitude": 1000, "speed": 150}
        return dict_data


sensor_data = SensorXML("sensor.xml")
adapter = JSONAdapter(sensor_data)
json_data = adapter.get_data()
print(json.dumps(json_data, indent=4))
