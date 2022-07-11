from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        'mouse',
        'Logitech',
        '10/01/2020',
        '10/01/2030',
        '123456',
        'Armazenar em ambiente arejado sem contato direto com calor',
    )

    product_result = "O produto mouse fabricado em 10/01/2020"\
        " por Logitech com validade até 10/01/2030 precisa ser armazenado"\
        " Armazenar em ambiente arejado sem contato direto com calor."

    assert repr(product) == product_result
