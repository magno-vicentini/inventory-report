from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path_file, type_report="simples"):
        report_class = SimpleReport
        if type_report == "completo":
            report_class = CompleteReport
        self.data += self.importer.import_data(path_file)
        return report_class.generate(self.data)
