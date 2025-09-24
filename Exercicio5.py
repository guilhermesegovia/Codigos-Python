#Exercicio 5
# 1 - Cadastro dos clientes 
# 2 - Acesso ao sistema
# 3 - Reserva de corte
# 4 - Incluir serviços
# 5 - Historico de clientes
# 6 - 
# 7 - Suporte ao cliente


from dataclasses import dataclass

@dataclass
class RegistroCliente:
    nome: str
    email: str
    telefone: str

registros_clientes = []

class ReservaCorte:
    nome: str
    estilo: str
    hora: str
    email: str
    profissional: str

reservas_lista = []

class Servico:
    nome_servico: str
    detalhe: str
    custo: str

lista_servico = []

def adicionar_cliente():
    nome = input ("Qual seu nome? ")
    email = input ("Digite seu email: ")
    telefone = input ("Digite seu telefone Ex:(1399999999): ")
    cliente_adicionado = RegistrodeCliente(nome, email, telefone)
    registros_clientes.append(cliente_adicionado)
    print ("Seu cadastro foi concluido com sucesso!")
    
def verificar_acesso():
    email_login = input ("Qual seu email? ")
    telefone_login = input ("Insira seu telefone Ex:(1399999999): ")
    
    for registro in registro_clientes:
        if registro.email == email_login:
            if registro.telefone == telefone_login:
                print ("Acesso Concedido!")
            else:
                print("Acesso Negado!")
    
def reservar_corte():
    email = input("Qual seu email?")
    nome = input("Qual seu nome?")
    estilo = input("Qual estilo de corte você prefere? ")
    profissional = input("Qual profissional você prefere? ")
    hora = input("Informe o horário desejado: ")
    
    reservar = ReservaCorte(email,nome,estilo,profissional,hora)
    reservas_listas.append(reservar)
    print("Marcado com sucesso!")
    
def incluir_servico():
    nome_servico = input("Informe o serviço desejado")
    detalhe = input ("Descreva o serviço: ")
    custo = input ("Informe o custo do serviço")
    
    servico = Servico(nome_servico,detalhe,custo)
    lista_servico.append(servico)
    print(f"{nome_servico} adicionado com sucesso!")
    
def suporte_cliente():
    duvida = input ("Informe sua duvida: ")
    print("Um Email foi enviado a você! ")
    

def opcoes_menu():
    print("\n---  Barbearia DZ7  ---")
    print("1 - Registro de cliente")
    print("2 - Acesso ao sistema")
    print("3 - Reserva de corte")
    print("4 - Incluir serviço")
    print("5 - Suporte ao cliente")
    print("6 - Encerrar")
    return input("Selecione uma opção: ")

while True:
    selecao = opcoes_menu()
    if selecao == "1":
        adicionar_cliente()
    
    elif selecao == "2":
        verificar_acesso()
    
    elif selecao == "3":
        reservar_corte()
        
    elif selecao == "4":
        incluir_servico()
    
    elif selecao == "5":
        suporte_cliente()
        
    elif selecao == "6":
        print("Fechando Programa... ")
        break
    else:

        print("Opção não reconhecida")

