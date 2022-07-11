from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('csv'):
            return Inventory.get_file_csv(path_file)
        else:
            raise ValueError('Arquivo inválido')
