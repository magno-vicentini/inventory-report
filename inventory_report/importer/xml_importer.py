from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('xml'):
            return Inventory.get_file_xml(path_file)
        else:
            raise ValueError('Arquivo inválido')
