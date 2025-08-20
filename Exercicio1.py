#Exercicio1
Sistema de estoque com apenas um produto
1 opção de cadastro de nome do produto
2 opção de retirar produto do estoque (Precisa verificar se tem o produto)
3 opção de adicionar produto no estoque (Precisa adicionar um numero maior que zero)
4 opção de ver a quantidade no estoque
def menu():
    print("\n--- Sistema de Estoque ---")
    print("1- Cadastrar Produto")
    print("2- Retirada do estoque")
    print("3 - Adicionar ao Estoque")
    print("4 - Ver quantidade em Estoque")
    print("0 - Sair")
    return input("Escolha uma opção: ")



#variaveis de controle
produto = None
quantidade = 0
     
while True:
    opcao = menu()
        
    if opcao == "1":
        produto = input("Digite o nome do produto:")
        quantidade = 0
        print(f"produto '{produto}' Cadastrado com sucesso!")
    
    elif opcao == "2":
        if produto is None:
            print("Nenhum Produto Cadastrado ainda!")
        else:
           retirar = int(input("Digite a quantidade a retirar"))
           if retirar <= 0:
                print ("A quantidade deve ser maior que zero!")
           elif retirar > quantidade:
                print ("Quantidade insulficiente no estoque!")
           else:
                quantidade -= retirar
                print (f"Retirado {retirar} Unidade(s) Estoque atual {quantidade}")
                                 
    elif opcao == "3":
        if produto is None:
            print ("Nenhum produto cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade (s). Estoque atual: {quantidade}")
    
    elif opcao == "4":
        if produto is None:
            print("Nenhum produto cadastrado ainda!")
        else:
            print(f"Poduto: {produto} | Quantidade em estoque: {quantidade}")
                                                                 
    elif opcao == "0":
            print("Saindo do sistema... até mais")
            break
    
    else:
        print("Opção Invalida! Tente Novamente")