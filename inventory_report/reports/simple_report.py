from datetime import datetime


class SimpleReport:
    @staticmethod
    def search_by_oldest_fabrication(list_products):
        oldest_date = datetime.now().strftime('%Y-%m-%d')
        for product in list_products:
            if product['data_de_fabricacao'] < oldest_date:
                oldest_date = product['data_de_fabricacao']
        return oldest_date

    @staticmethod
    def search_by_nearest_fabrication(list_products):
        nearest_date = datetime.now().strftime('%Y-%m-%d')
        date_list = []
        for product in list_products:
            if product['data_de_validade'] > nearest_date:
                date_list.append(product['data_de_validade'])
        date_list.sort()
        return date_list

    @staticmethod
    def search_by_stock_quantity(list_products):
        list_companies = [product_element['nome_da_empresa']
                          for product_element in list_products]
        return max(list_companies)

    @classmethod
    def generate(cls, all_products):
        old_fabrication = cls.search_by_oldest_fabrication(all_products)
        near_fabrication = cls.search_by_nearest_fabrication(all_products)[0]
        stock_company = cls.search_by_stock_quantity(all_products)
        generate_string = (
            f"Data de fabricação mais antiga: {old_fabrication}\n"
            f"Data de validade mais próxima: {near_fabrication}\n"
            f"Empresa com maior quantidade de "
            f"produtos estocados: {stock_company}\n"
        )
        return generate_string