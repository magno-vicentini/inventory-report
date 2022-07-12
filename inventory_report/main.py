import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")
    path_file = sys.argv[1]
    type_report = sys.argv[2]

    if sys.argv[1].endswith('csv'):
        report = InventoryRefactor(CsvImporter)
        print(report.import_data(path_file, type_report), end="")
    elif sys.argv[1].endswith('json'):
        report = InventoryRefactor(JsonImporter)
        print(report.import_data(path_file, type_report), end="")
    else:
        report = InventoryRefactor(XmlImporter)
        print(report.import_data(path_file, type_report), end="")
