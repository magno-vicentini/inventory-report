from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(all_products):
        value_simple_report = SimpleReport.generate(all_products)
        list_companies = [product_element['nome_da_empresa']
                          for product_element in all_products]
        dict_companies = {}

        for element in list_companies:
            if element in dict_companies:
                dict_companies[element] += 1
            else:
                dict_companies[element] = 1

        string_companies = ""
        for key, value in dict_companies.items():
            string_companies += f"- {key}: {value}\n"
            
        return (
            f"{value_simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{string_companies}"
        )