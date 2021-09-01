"""
Esse script tem como objetivo facilitar as configurações dos equipamentos de rede.

Criado com a utilização em paralelo ao Packet Tracer - Software disponibilizado pela CISCO.

Realizado em: 08/08/2021
Realizado por: Jacqueline Rodrigues
"""

# gatpass permite o adicionamento de informações, sem que sejam vistas. Ideal para colocação de senhas.
import getpass

# configuração inicial para Switches. Adicionamento em variáveis e apresentado juntamente com as devidas configurações.
def sw_configuracao_inicial():
    # solicitação das devidas informações para configuração.
    nome_equipamento = input("Informe o nome do equipamento: ")
    end_interface = input("Informe o endereço da interface da vlan 1: ")
    mask_interface = input("Informe a máscara da interface: ")
    dominio = input("Informe o domínio para o acesso remoto via ssh: ")
    nome_usario = input("Informe o nome do usuário para acesso remoto: ")
    senha_ssh = getpass.getpass("Informe a senha para acesso remoto via ssh: ")
    senha_console = getpass.getpass("Informe a senha de acesso console: ")
    senha_enable = getpass.getpass("Informe a senha de acesso ao modo privilegiado (enable): ")

    print("\n\n")
    
    # apresentação das configurações.
    print("------Configurações iniciais para Switches-------")
    print("configure terminal")  # entrando em modo de global
    print(f"hostname {nome_equipamento}")   # alterando nome do equipamento (importante para identificação e ponto de presença)
    print(f"interface vlan 1") # entrando na interface virtual 1 (interface destinada para acesso remoto ao equipamento)
    print(f"ip address {end_interface} {mask_interface}")  # adcionamento dos endereços de rede com IP e Máscara
    print("no shutdown")  # subindo a interface virtual
    print("exit") # saindo da configuração de interface
    print(f"ip domain-name {dominio}") # criando domínio para fornecer acesso remoto via SSH (criptografado) ao equipamento
    print("crypto key generate rsa") # escolha do tamanho da chave
    print("ip ssh time-out 60") # tempo permitido para tentar o acesso remoto
    print("ip ssh authentication-retries 2") # quantidade de tentativas ao acesso remoto
    print(f"username {nome_usario} priv 15 secret {senha_ssh}") # relacionamento o usuário e sua senha de acesso remoto (escolher senhas com frases longas)
    print("line vty 0 4") # entrando ao acesso remoto via TELNET (sem criptografia - texto puro)
    print("login local") # informação de acesso local
    print("transport input ssh")   # transformando o acesso TELNET (texto puro) para o acesso SSH (criptografado)
    print("exit") # saindo da configuração de linha
    print("line console 0") # entrando na configuração de linha console (acesso ao equipamento via console ou acesso direto)
    print(f"password {senha_console}")  # senha de acesso ao console (escolher senhas com frases longas)
    print("login") # adicionando senha
    print("exit") # saindo do acesso console
    print(f"enable secret {senha_enable}")   # adicionando senha de acesso enable, ao modo EXEC privilegiado (escolher senhas com frases longas)
    print("service password-encryption")  # encriptografando senhas dentro do próprio equipamento (forcendo maior segurança)
    print("end") # saindo do modo de configuração global
    print("copy running-config startup-config")   # salva as configurações


# configuração inicial para Roteadores. Adicionamento em variáveis e apresentado juntamente com as devidas configurações.
def router_configuracao_inicial():
    nome_equipamento = input("Informe o nome do equipamento: ")
    nome_interface = input("Informe o nome da interface: ")
    num_interface = input("informe o número da interface: ")
    end_interface = input("Informe o endereço de gateway: ")
    mask_interface = input("Informe a máscara da interface: ")
    dominio = input("Informe o domínio para o acesso remoto via ssh: ")
    nome_usario = input("Informe o nome do usuário para acesso remoto: ")
    senha_ssh = getpass.getpass("Informe a senha para acesso remoto via ssh: ")
    senha_console = getpass.getpass("Informe a senha de acesso console: ")
    senha_enable = getpass.getpass("Informe a senha de acesso ao modo privilegiado (enable): ")

    print("\n\n")
    
    # apresentação das configurações.
    print("------Configurações iniciais para Roteadores-------")
    print("configure terminal") # entrando em modo de global
    print(f"hostname {nome_equipamento}") # alterando nome do equipamento (importante para identificação e ponto de presença)
    print(f"interface {nome_interface} {num_interface}") # adicionando o nome da interface a ser acessada mais o número dessa interface
    print(f"ip address {end_interface} {mask_interface}")  # adicionamento endereços de rede - IP e Máscara para roteamento interno (chamado de gateway)
    print("no shutdown") # subindo a interface definida
    print("exit") # saindo do como de configuração da interface
    print(f"ip domain-name {dominio}") # criando domínio para fornecer acesso remoto via SSH (criptografado) ao equipamento
    print("crypto key generate rsa") # escolha do tamanho da chave
    print("ip ssh time-out 60") # tempo permitido para tentar o acesso remoto
    print("ip ssh authentication-retries 2") # quantidade de tentativas ao acesso remoto
    print(f"username {nome_usario} priv 15 secret {senha_ssh}") # relacionamento o usuário e sua senha de acesso remoto (escolher senhas com frases longas)
    print("line vty 0 4") # entrando ao acesso remoto via TELNET (sem criptografia - texto puro)
    print("login local") # informação de acesso local
    print("transport input ssh")   # transformando o acesso TELNET (texto puro) para o acesso SSH (criptografado)
    print("exit") #  saindo da configuração de linha
    print("line console 0") # entrando na configuração de linha console (acesso ao equipamento via console ou acesso direto)
    print(f"password {senha_console}")  # senha de acesso ao console (escolher senhas com frases longas)
    print("login") # adicionando senha
    print("exit") # saindo do acesso console
    print(f"enable secret {senha_enable}")   # adicionando senha de acesso enable, ao modo EXEC privilegiado (escolher senhas com frases longas)
    print("service password-encryption") # encriptografando senhas dentro do próprio equipamento (forcendo maior segurança)
    print("end") # saindo do modo de configuração global
    print("copy running-config startup-config")  # salva as configurações


# configuração de interfaces seriais para Roteadores. Adicionamento em variáveis e apresentado juntamente com as devidas configurações.
def router_interface_serial():
    num_serial = input("Informe o número da interface serial: ")
    gateway = input("Informe o gateway: ")
    mask = input("Informe a máscara de rede: ")

    print("\n\n")
    
    # apresentação das configurações.
    print("------Configurações de interfaces seriais para Roteadores-------")
    print("config t")  # entrando em modo de configuração global
    print(f"interface serial {num_serial}") # entrando na interface serial e adicionamento o número da interface escolhida
    print(f"ip address {gateway} {mask}") # adicionamento endereçamento de rede com IP e Máscara
    print("clock rate 64000") # informa a frequência do relógio (velocidade que o roteador processará as informações)
    print("bandwidth 64000") # informa a largura da banda
    print("no shutdown") # subindo interface serial
    print("end") # saindo do modo de configuração global
    print("copy running-config startup-config") # salvando configurações

# configuração de roteamento interno (utilizando OSPF) para Roteadores. Adicionamento em variáveis e apresentado juntamente com as devidas configurações.
def router_ospf():
    loopback = int(input("Informe o número da loopback: "))
    router_id = input("Informe o router-id: ")
    num_ospf = int(input("Informe o número do OSPF: "))
    rede_ospf = input("Informe a rede do OSPF: ")
    mask_ospf = input("Informe a máscara do OSPF: ")
    num_area = int(input("Informe a área do OSPF: "))

    print("\n\n")
    
    # apresentação das configurações de roteamento interno.
    print("------Configurações do OSPF (roteamento interno) para Roteadores-------")
    print("config t") # entrando do modo de configuração global
    print(f"interface loopback{loopback}") # adicionando interface loopback (interface lógica que rompe com todos os problemas físicos das interfaces físicas)
    print(f"ip address {router_id} 255.255.255.255") # adicionamento do router-id (identificação do OSPF de 32bits - não é um endereço IPv4)
    print("exit") # saindo da configuração da interface loopback
    print(f"router ospf {num_ospf}") # entrando no OSPF e adicionando o número do OSPF
    print(f"network {rede_ospf} {mask_ospf} area {num_area}") # adicionando a rede que queira se conectar, com máscara coringa e área (começar sempre coma área backbone, ou seja, área 0)
    print("end") # saindo da configuração do roteamento interno
    print("copy running-config startup-config") # salvando as configurações

# configuração de roteamento interno (iBGP) e externo (eBGP) para Roteadores. Adicionamento em variáveis e apresentado juntamente com as devidas configurações.
def router_bgp():
    print("Para o iBGP, informe\n")
    seu_as = input("Informe o seu AS: ")
    gw_vizinho = input("Informe o gateway do vizinho: ")
    rotas_internas = input("Informe a rota interna: ")

    print("\n")

    print("Para o eBGP, informe \n")
    seu_as = input("Informe o seu AS: ")
    as_vizinho = input("Informe o AS do vizinho: ")
    gw_vizinho = input("Informe o gateway do vizinho: ")
    rotas_internas = input("Informe a rota interna: ")

    print("\n\n")

    # apresentação das configurações de roteamento interno (iBGP).
    # OBS: importante utilizar iBGP com o OSPF. O OSPF apresenta os caminhos existentes ao iBGP
    # Sobre o iBGP: todo mundo se conecta com todo mundo dentro da mesma rede com o seu próprio AS (sistema autônomo)
    print("------iBGP-------")
    print("config t") # entrando no como de configuração global
    print(f"router bgp {seu_as}") # entrando na configuração do bgp interno (iBGP) e adicionando o seu AS
    print(f"neighbor {gw_vizinho} remote-as {seu_as}") # adicionado o vizinho inteiro que queira conectar mais o seu AS (iBGP todo mundo conecta com todo mundo, internamente)
    print(f"network {rotas_internas}") # publica as redes que queira internas
    print("end") # saindo da configuração do roteamento interno
    print("copy running-config startup-config") # salvando as configurações

    print("\n\n")

    # apresentação das configurações de roteamento externo (eBGP).
    # OBS: importante utilizar iBGP adicione filtros de entrada e saída. Aqui, é apenas uma configuração simples
    # Sobre o eBGP: todo mundo se conecta com todo mundo fora da rede interna, conexões com AS (sistema autônomo) diferentes
    print("------eBGP-------")
    print("config t") # entrando no como de configuração global
    print(f"router bgp {seu_as}") # entrando na configuração do bgp externo (eBGP) e adicionando o seu AS
    print(f"neighbor {gw_vizinho} remote-as {as_vizinho}")  # adicionado o vizinho externo que queira conectar mais o AS dele
    print(f"network {rotas_internas}") # publica as redes que queira a saída externa
    print("end") # saindo da configuração do roteamento interno
    print("copy running-config startup-config") # salvando as configurações

# apresentação das escolhas
print("Bem-vindo(a) as configurações automáticas\nEscolha o equipamento que queira configurar:")
print("1- Switch\n2- Roteador\n")
acesso = int(input("Faça a sua escolha: "))

print()

if acesso == 1:
    print("Possuimos, até o momento, configurações iniciais para o switch")
    sw_configuracao_inicial()
elif acesso == 2:
    print("O que deseja configurar?\n")
    print("1- Configurações iniciais\n2- Interface Serial\n3- OSPF\n4- iBGP e eBGP")
    escolha = int(input("Escolha: "))

    print()

    if escolha == 1:
        router_configuracao_inicial()
    elif escolha == 2:
        router_interface_serial()
    elif escolha == 3:
        router_ospf()
    elif escolha == 4:
        router_bgp()
else:
    print("Não encontrado\nAbortando...")
