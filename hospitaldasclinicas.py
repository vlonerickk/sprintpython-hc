# Sistema de Gerenciamento Médico para o Hospital das Clínicas
# Autor: Richard F. RM: 566127, Maicon Douglas RM: 561279, Pedro Henrique RM: 563062.
# Data: Início 16/05/25 - Término 20/05/25

pacientes = []
medicos = []
consultas = []
laudos = []

def exibir_menu_principal():
    print("\n=== SISTEMA MÉDICO ===")
    print("1. Cadastrar Paciente")
    print("2. Listar Pacientes")
    print("3. Cadastrar Médico")
    print("4. Listar Médicos")
    print("5. Agendar Consulta")
    print("6. Listar Consultas")
    print("7. Registrar Laudo")
    print("8. Visualizar Laudos")
    print("9. Consultas por Paciente")
    print("0. Sair do Sistema")
    print("======================")

def validar_opcao_menu(opcoes_validas):
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao in opcoes_validas:
                return opcao
            print(f"Opção inválida! Digite um número entre {min(opcoes_validas)} e {max(opcoes_validas)}.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

def validar_data_hora():
    while True:
        data = input("Data da consulta (DD/MM/AAAA): ")
        hora = input("Hora da consulta (HH:MM): ")
        
        try:
            dia, mes, ano = map(int, data.split('/'))
            hora, minuto = map(int, hora.split(':'))
            
            if (1 <= dia <= 31) and (1 <= mes <= 12) and (ano >= 2023):
                if (0 <= hora < 24) and (0 <= minuto < 60):
                    return f"{data} {hora}"
            
            print("Data ou hora inválida!")
        except:
            print("Formato incorreto! Use DD/MM/AAAA para data e HH:MM para hora.")

def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")
    
    nome = input("Nome completo: ").strip()
    while len(nome.split()) < 2:
        print("Digite o nome completo!")
        nome = input("Nome completo: ").strip()
    
    while True:
        cpf = input("CPF (apenas números): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            if not any(paciente['cpf'] == cpf for paciente in pacientes):
                break
            print("CPF já cadastrado!")
        else:
            print("CPF inválido! Deve conter 11 dígitos numéricos.")
    
    while True:
        nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        try:
            dia, mes, ano = map(int, nascimento.split('/'))
            if (1 <= dia <= 31) and (1 <= mes <= 12) and (1900 <= ano <= 2023):
                break
            print("Data inválida!")
        except:
            print("Formato incorreto! Use DD/MM/AAAA.")
    
    while True:
        telefone = input("Telefone (com DDD): ").strip()
        if telefone.isdigit() and len(telefone) >= 10:
            break
        print("Telefone inválido! Digite apenas números com DDD.")
    
    paciente = {
        'nome': nome,
        'cpf': cpf,
        'nascimento': nascimento,
        'telefone': telefone,
        'historico': []
    }
    
    pacientes.append(paciente)
    print("\nPaciente cadastrado com sucesso!")
    return paciente

def listar_pacientes():
    print("\n--- LISTA DE PACIENTES ---")
    
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    
    for i, paciente in enumerate(pacientes, 1):
        print(f"{i}. {paciente['nome']} | CPF: {paciente['cpf']} | Nasc: {paciente['nascimento']} | Tel: {paciente['telefone']}")

def cadastrar_medico():
    print("\n--- CADASTRO DE MÉDICO ---")
    
    nome = input("Nome completo: ").strip()
    while len(nome.split()) < 2:
        print("Digite o nome completo!")
        nome = input("Nome completo: ").strip()
    
    while True:
        crm = input("CRM (com UF): ").strip()
        if len(crm.split()) >= 2 and crm[-2:] in ["SP", "RJ", "MG", "RS", "PR", "SC", "BA", "DF"]:
            break
        print("CRM inválido! Inclua a UF (ex: 12345/SP)")
    
    especialidade = input("Especialidade médica: ").strip()
    while not especialidade:
        print("Especialidade não pode ser vazia!")
        especialidade = input("Especialidade médica: ").strip()
    
    medico = {
        'nome': nome,
        'crm': crm,
        'especialidade': especialidade
    }
    
    medicos.append(medico)
    print("\nMédico cadastrado com sucesso!")
    return medico

def listar_medicos():
    print("\n--- LISTA DE MÉDICOS ---")
    
    if not medicos:
        print("Nenhum médico cadastrado.")
        return
    
    for i, medico in enumerate(medicos, 1):
        print(f"{i}. Dr. {medico['nome']} | CRM: {medico['crm']} | Especialidade: {medico['especialidade']}")

def agendar_consulta():
    print("\n--- AGENDAMENTO DE CONSULTA ---")
    
    if not pacientes:
        print("Nenhum paciente cadastrado. Cadastre um paciente primeiro.")
        return
    
    if not medicos:
        print("Nenhum médico cadastrado. Cadastre um médico primeiro.")
        return
    
    listar_pacientes()
    while True:
        try:
            paciente_idx = int(input("Digite o número do paciente: ")) - 1
            if 0 <= paciente_idx < len(pacientes):
                break
            print(f"Digite um número entre 1 e {len(pacientes)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    
    listar_medicos()
    while True:
        try:
            medico_idx = int(input("Digite o número do médico: ")) - 1
            if 0 <= medico_idx < len(medicos):
                break
            print(f"Digite um número entre 1 e {len(medicos)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    
    data_hora = validar_data_hora()
    
    for consulta in consultas:
        if consulta['medico']['crm'] == medicos[medico_idx]['crm'] and consulta['data_hora'] == data_hora:
            print("Médico já possui consulta agendada neste horário!")
            return
    
    motivo = input("Motivo da consulta: ").strip()
    while not motivo:
        print("Motivo não pode ser vazio!")
        motivo = input("Motivo da consulta: ").strip()
    
    consulta = {
        'paciente': pacientes[paciente_idx],
        'medico': medicos[medico_idx],
        'data_hora': data_hora,
        'motivo': motivo,
        'realizada': False,
        'laudo': None
    }
    
    consultas.append(consulta)
    pacientes[paciente_idx]['historico'].append(f"Consulta agendada para {data_hora} com Dr. {medicos[medico_idx]['nome']}")
    print("\nConsulta agendada com sucesso!")
    return consulta

def listar_consultas():
    print("\n--- LISTA DE CONSULTAS ---")
    
    if not consultas:
        print("Nenhuma consulta agendada.")
        return
    
    for i, consulta in enumerate(consultas, 1):
        status = "Realizada" if consulta['realizada'] else "Agendada"
        print(f"\nConsulta {i}:")
        print(f"Paciente: {consulta['paciente']['nome']}")
        print(f"Médico: Dr. {consulta['medico']['nome']} ({consulta['medico']['especialidade']})")
        print(f"Data/Hora: {consulta['data_hora']}")
        print(f"Motivo: {consulta['motivo']}")
        print(f"Status: {status}")
        if consulta['laudo']:
            print(f"Laudo registrado: Sim")

def registrar_laudo():
    print("\n--- REGISTRO DE LAUDO ---")
    
    consultas_pendentes = [c for c in consultas if not c['realizada']]
    
    if not consultas_pendentes:
        print("Nenhuma consulta pendente para laudar.")
        return
    
    print("\nConsultas pendentes:")
    for i, consulta in enumerate(consultas_pendentes, 1):
        print(f"{i}. {consulta['paciente']['nome']} com Dr. {consulta['medico']['nome']} em {consulta['data_hora']}")
    
    while True:
        try:
            consulta_idx = int(input("Digite o número da consulta: ")) - 1
            if 0 <= consulta_idx < len(consultas_pendentes):
                break
            print(f"Digite um número entre 1 e {len(consultas_pendentes)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    
    diagnostico = input("Diagnóstico: ").strip()
    while not diagnostico:
        print("Diagnóstico não pode ser vazio!")
        diagnostico = input("Diagnóstico: ").strip()
    
    prescricao = input("Prescrição médica: ").strip()
    while not prescricao:
        print("Prescrição não pode ser vazia!")
        prescricao = input("Prescrição médica: ").strip()
    
    laudo = {
        'consulta': consultas_pendentes[consulta_idx],
        'diagnostico': diagnostico,
        'prescricao': prescricao,
        'data_emissao': datatime.now  
    }
    
    laudos.append(laudo)
    consulta_ref = consultas_pendentes[consulta_idx]
    consulta_ref['realizada'] = True
    consulta_ref['laudo'] = laudo
    
    paciente = consulta_ref['paciente']
    paciente['historico'].append(f"Consulta realizada em {consulta_ref['data_hora']} - Diagnóstico: {diagnostico}")
    
    print("\nLaudo registrado com sucesso!")
    return laudo

def visualizar_laudos():
    print("\n--- LAUDOS MÉDICOS ---")
    
    if not laudos:
        print("Nenhum laudo registrado.")
        return
    
    for i, laudo in enumerate(laudos, 1):
        consulta = laudo['consulta']
        print(f"\nLaudo {i}:")
        print(f"Paciente: {consulta['paciente']['nome']}")
        print(f"Médico: Dr. {consulta['medico']['nome']}")
        print(f"Data da consulta: {consulta['data_hora']}")
        print(f"Diagnóstico: {laudo['diagnostico']}")
        print(f"Prescrição: {laudo['prescricao']}")
        print(f"Data de emissão: {laudo['data_emissao']}")

def consultas_por_paciente():
    print("\n--- CONSULTAS POR PACIENTE ---")
    
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    
    listar_pacientes()
    while True:
        try:
            paciente_idx = int(input("Digite o número do paciente: ")) - 1
            if 0 <= paciente_idx < len(pacientes):
                break
            print(f"Digite um número entre 1 e {len(pacientes)}")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    
    paciente = pacientes[paciente_idx]
    consultas_paciente = [c for c in consultas if c['paciente']['cpf'] == paciente['cpf']]
    
    print(f"\nConsultas do paciente {paciente['nome']}:")
    if not consultas_paciente:
        print("Nenhuma consulta registrada.")
        return
    
    for i, consulta in enumerate(consultas_paciente, 1):
        status = "Realizada" if consulta['realizada'] else "Agendada"
        print(f"\nConsulta {i}:")
        print(f"Médico: Dr. {consulta['medico']['nome']} ({consulta['medico']['especialidade']})")
        print(f"Data/Hora: {consulta['data_hora']}")
        print(f"Motivo: {consulta['motivo']}")
        print(f"Status: {status}")
        if consulta['laudo']:
            print(f"Diagnóstico: {consulta['laudo']['diagnostico']}")

def main():
    print("Bem-vindo ao Sistema de Gerenciamento Médico!")
    
    while True:
        exibir_menu_principal()
        opcao = validar_opcao_menu(range(10))  # 0 a 9
        
        if opcao == 1:
            cadastrar_paciente()
        elif opcao == 2:
            listar_pacientes()
        elif opcao == 3:
            cadastrar_medico()
        elif opcao == 4:
            listar_medicos()
        elif opcao == 5:
            agendar_consulta()
        elif opcao == 6:
            listar_consultas()
        elif opcao == 7:
            registrar_laudo()
        elif opcao == 8:
            visualizar_laudos()
        elif opcao == 9:
            consultas_por_paciente()
        elif opcao == 0:
            print("\nObrigado por usar o Sistema Médico. Até logo!")
            break
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()