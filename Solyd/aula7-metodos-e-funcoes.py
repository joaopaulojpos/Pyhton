def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

if tem_sete_itens([1, 2, 3, 4, 5, 6, 7]):
    print('realmente tem sete itens')
