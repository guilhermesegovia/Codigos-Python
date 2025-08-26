#Exercicio1.2
#Sistema de bilheteria de eventos com apenas um evento
#1 opção de cadastro de nome do evento
#2 opção de retirar ingresso do estoque (Precisa verificar se tem o ingresso)
#3 opção de adicionar ingresso no estoque (Precisa adicionar um numero maior que zero)
#4 opção de ver a quantidade no estoque

def menu():
    print("\n--- sistema do evento ---")
    print("1- Cadastrar evento ")
    print("2- Comprar ingresso ")
    print("3 - Repor ingresso ")
    print("4 - Ver quantidade de ingresso ")
    print("0 - Sair")
    return input("Escolha uma opção: ")



#variaveis de controle
evento = None
quantidade = 0
     
while True:
    opcao = menu()
        
    if opcao == "1":
        evento = input("Digite o nome do evento: ")
        quantidade = 0
        print(f" Evento '{evento}' Cadastrado com sucesso!")
    
    elif opcao == "2":
        if evento is None:
            print("Nenhum evento Cadastrado ainda!")
        else:
           retirar = int(input("Digite a quantidade a retirar: "))
           if retirar <= 0:
                print ("A quantidade deve ser maior que zero!")
           elif retirar > quantidade:
                print ("Quantidade insulficiente no estoque!")
           else:
                quantidade -= retirar
                print (f"Retirado {retirar} Unidade(s) Estoque atual {quantidade}")
                                 
    elif opcao == "3":
        if evento is None:
            print ("Nenhum evento cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade a adicionar: "))
            if adicionar <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade (s). Estoque atual: {quantidade}")
    
    elif opcao == "4":
        if evento is None:
            print("Nenhum evento cadastrado ainda!")
        else:
            print(f"Evento: {evento} | Quantidade em estoque: {quantidade}")
                                                                 
    elif opcao == "0":
            print("Saindo do sistema... até mais")
            break
    
    else:

        print("Opção Invalida! Tente Novamente")