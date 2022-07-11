import csv
import json
import xml.etree.ElementTree as ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def get_file_csv(path_file):
        with open(path_file) as csv_file:
            file_data = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            list_result = [data_element for data_element in file_data]
            return list_result

    @staticmethod
    def get_file_json(path_file):
        with open(path_file) as json_file:
            file_data = json.load(json_file)
            return file_data

    @staticmethod
    def get_file_xml(path_file):
        with open(path_file) as xml_file:
            element = ElementTree.parse(xml_file)
            root = element.getroot()
            data = []
            for child in root:
                item = {}
                for element_child in child:
                    item[element_child.tag] = element_child.text
                data.append(item)
            return data

    @classmethod
    def import_data(cls, path_file, type_report):
        if path_file.endswith('csv'):
            data_converted = cls.get_file_csv(path_file)
        elif path_file.endswith('json'):
            data_converted = cls.get_file_json(path_file)
        else:
            data_converted = cls.get_file_xml(path_file)

        if type_report == 'simples':
            return SimpleReport.generate(data_converted)
        elif type_report == 'completo':
            return CompleteReport.generate(data_converted)
