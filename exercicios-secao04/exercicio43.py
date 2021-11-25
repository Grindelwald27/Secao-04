valor = 500
valor_desconto = valor - (valor * 10) / 100
print('O valor a vista fica R$%.2d' % valor_desconto)
valor_parcela = valor / 3
print('O valor parcelado fica R$%.2f' % valor_parcela)
comissao_vend_a_vista = (valor_desconto * 5) / 100
print('A comissão da venda a vista é R$%.2f' % comissao_vend_a_vista)
comissao_vend_parc = (valor * 5) / 100
print('A comissão da venda parcelada é R$%.2f' % comissao_vend_parc)
