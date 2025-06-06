import modulos

class ErroTipo(Exception): pass


while True:
    print("\n--------------------------------------")
    print("Opção 1: Adicionar Itens")
    print("Opção 2: Ver Itens da Mochila")
    print("Opção 3: Ver Peso da Mochila")
    print("Opção 4: Remover Item")
    print("Opção 5: Sair")
    print("--------------------------------------\n")

    try:
        opcao = int(input("Selecione uma opção: "))
        if opcao == 1:
            nome_item = str(input("Nome do item: ")).lower()
            tipo_item = str(input("Tipo do item (Arma, Comida, Poção ...): ")).lower()
            peso_item = int(input("Peso do item: "))
            novo_item = modulos.Item(nome_item, tipo_item, peso_item)
            modulos.mochila.add_items(novo_item)
        elif opcao == 2:
            print(modulos.mochila)
        elif opcao == 3:
            print(modulos.mochila.peso)
        elif opcao == 4:
            item = str(input("\nNome do Item a Remover: "))
            del_item = modulos.mochila.remove_items(item)
        elif opcao == 5:
            break
        else:
            raise ErroTipo
    except ErroTipo:
        print("Selecione uma opção válida") 
    except ValueError:
        print("Digite números inteiros")
