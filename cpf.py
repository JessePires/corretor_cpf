def verifica_caractere_dez(cpf):

    aux = 0

    for i in range(1, 10):
        aux += i * cpf[i-1]

    return (aux % 11) % 10


def verifica_caractere_onze(cpf):

    aux = 0

    for i in range(2, 11):
        aux += ((i-1) * cpf[i-1])

    return (aux % 11) % 10


def verifica_cpf(cpf):

    flag = 0

    if len(cpf) == 9:
        cpf += [0, 0]

    n10 = verifica_caractere_dez(cpf)
    if cpf[9] != n10:

        cpf[9] = n10
        flag = 1

    n11 = verifica_caractere_onze(cpf)
    if cpf[10] != n11:
        cpf[10] = n11
        flag = 1

    return flag


def valida_estado(estado):

    flag = 0
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

    for i in estados:   
        if estado == i:
            flag = 1
    
    if flag == 1:
        return True
    
    else:
        return False


def retorna_digito_estado(estado):

    digitos = {"DF" : 1, "GO" : 1, "MT" : 1, "TO" : 1, "PA" : 2, "AM" : 2, "AC" : 2, "AP" : 2, "RO" : 2, "RR" : 2, "CE" : 3, "MA" : 3, "PI" : 3, "PE" : 4, "RN" : 4, "PB" : 4, "AL" : 4, "BA" : 5, "SE" : 5, "MG" : 6, "RJ" : 7, "ES" : 7, "SP" : 8, "PR" : 9, "SC" : 9, "RS" : 0}

    return digitos[estado]


def obtem_estado():

    print("Lista com as siglas dos estados: ")
    print("Acre -> AC")
    print("Alagoas -> AL")
    print("Amapá -> AP")
    print("Amazonas -> AM")
    print("Bahia -> BA")
    print("Ceará -> CE")
    print("Distrito Federal -> DF")
    print("Espírito Santo -> ES")   
    print("Goiás -> GO")
    print("Maranhão -> MA")
    print("Mato Grosso -> MT")
    print("Mato Grosso do Sul -> MS")
    print("Minas Gerais -> MG")
    print("Pará -> PA")
    print("Paraíba -> PB")
    print("Paraná -> PR")
    print("Pernambuco -> PE")
    print("Piauí -> PI")
    print("Rio de Janeiro -> RJ")
    print("Rio Grande do Norte -> RN")
    print("Rio Grande do Sul -> RS")
    print("Rondônia -> RO")
    print("Roraima -> RR")
    print("Santa Catarina -> SC")
    print("São Paulo -> SP")
    print("Sergipe -> SE")
    print("Tocantins -> TO")
    estado = input("Digite o seu estado de origem: ").upper()

    return estado


def verifica_caractere_nove(cpf, estado):

    flag = 0
    digito = retorna_digito_estado(estado)

    if digito != cpf[8]:
        cpf[8] = digito
        flag = 1

    return flag


def main():

    estado = ""
    cpf = []
    teste = input("Digite seu CPF: ")
    
    while valida_estado(estado) == False:
        estado = obtem_estado()

    while len(teste) < 9:
        print("O CPF deve ter 9 dígitos!\n")
        teste = input("Digite seu CPF: ")
    
    print("\n")
    
    for i in range(len(teste)):
        aux = ""
        aux += teste[i]
        cpf.append(int(aux))

    verifica_nono_digito = verifica_caractere_nove(cpf, estado)

    if verifica_nono_digito == 1:
        print("Foi detectado um erro no nono dígito do CPF. Ele não está de acordo com o Estado de origem informado!")
        print("O CPF informado com o nono dígito corrigido é o seguinte: ")

        for i in cpf:
            print(i, end = "")
    
    print("\n")

    verify = verifica_cpf(cpf)

    if verify == 0:
        print("CPF correto!\n")
    
    elif verify == 1:
        print("Erro encontrado nos dígitos de verificação!\n")
        
    for i in range(len(cpf)):

        if(i == 2 or i == 5):
            print(cpf[i], end = "")
            print(".", end = "")
        
        elif(i == 9):
            print("-", end = "")
            print(cpf[i], end = "")

        else:
            print(cpf[i], end = "")

    print("\n")

main()