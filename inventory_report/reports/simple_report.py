from datetime import date
from collections import Counter


class SimpleReport():
    @classmethod
    def generate(cls, all_products):
        oldest_date = ''
        today_date = str(date.today())
        list_expiration_date = []
        list_company_name = []
        list_manufacturing_date = []

        for product in all_products:
            # populo as listas primeiro
            list_manufacturing_date.append(product['data_de_fabricacao'])

            if product['data_de_validade'] > today_date:
                list_expiration_date.append(product['data_de_validade'])

            list_company_name.append(product['nome_da_empresa'])

        # com elas cheias, guardo na variavel
        oldest_date = min(list_manufacturing_date)

        closest_expiration_date = min(list_expiration_date)

        c = Counter(list_company_name)
        most_repeated_name = c.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {most_repeated_name}"
        )
