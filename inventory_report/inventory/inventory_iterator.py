from collections.abc import Iterator


class InventoryIterator(Iterator):

    def __init__(self, report):
        self.position = 0
        self.report = report

    def __next__(self):
        self.position += 1
        if self.position > len(self.report):
            raise StopIteration()
        return self.report[self.position - 1]
