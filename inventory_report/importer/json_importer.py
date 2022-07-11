from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('json'):
            return Inventory.get_file_json(path_file)
        else:
            raise ValueError('Arquivo inválido')
