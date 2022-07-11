from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(1, 'mouse', 'Logitech', '10/01/2020', '10/01/2030','123456', 'Armazenar em ambiente arejado sem contato direto com calor')

    assert product.id == 1
    assert product.nome_do_produto == 'mouse'
    assert product.nome_da_empresa == 'Logitech'
    assert product.data_de_fabricacao == '10/01/2020'
    assert product.data_de_validade == '10/01/2030'
    assert product.numero_de_serie == '123456'
    assert product.instrucoes_de_armazenamento == 'Armazenar em ambiente arejado sem contato direto com calor'

