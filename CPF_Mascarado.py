#Nome do arquivo: CPF_Mascarado.py
#Descrição: Este código gera todas as combinações possíveis de números de CPF a partir de um número parcialmente conhecido e dígitos adicionais. As combinações geradas são verificadas para garantir que sejam números de CPF válidos e são separadas em listas diferentes de acordo com o nono dígito da cadeia de 9 dígitos iniciais.
#Descrição detalhada: Este código define duas funções principais: `is_valid_cpf` e `generate_combinations`. A função `is_valid_cpf` verifica se um número de CPF é válido usando a regra de validação dos dígitos verificadores do CPF. A função `generate_combinations` gera todas as combinações possíveis de números de CPF a partir de um número parcialmente conhecido (representado por um número de 9 dígitos com lacunas representadas por `*`) e dígitos adicionais. A função também aceita dígitos de controle conhecidos ou desconhecidos (representados por `*`) e gera combinações para preencher as lacunas nos dígitos de controle também. As combinações geradas são verificadas usando a função `is_valid_cpf` e apenas as combinações que são números de CPF válidos são incluídas na lista de combinações geradas. Por fim, a função separa as combinações geradas em listas diferentes de acordo com o nono dígito da cadeia de 9 dígitos iniciais e retorna um dicionário com as listas separadas e suas respectivas descrições.
#Autor: Doutor Byte
#Website: https://www.doutorbyte.com
#Data: 25/04/2023
#Instruções de uso: Apenas altere abaixo, nos locais informados. Não informe caracteres de pontuação ( ponto ou hifen).

from itertools import product

def is_valid_cpf(cpf: str) -> bool:
    cpf_digits = [int(d) for d in cpf if d.isdigit()]
    if len(cpf_digits) != 11:
        return False
    first_sum = sum((a * b for a, b in zip(range(10, 1, -1), cpf_digits)))
    first_digit = (first_sum * 10 % 11) % 10
    second_sum = sum((a * b for a, b in zip(range(11, 1, -1), cpf_digits)))
    second_digit = (second_sum * 10 % 11) % 10
    return first_digit == cpf_digits[9] and second_digit == cpf_digits[10]

def generate_combinations(number: str, additional_digits: str, control_digits: str) -> dict:
    num_asterisks = number.count('*') + control_digits.count('*')
    descriptions = {
        '0': 'Rio Grande do Sul',
        '1': 'Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins',
        '2': 'Amazonas, Pará, Roraima, Amapá, Acre e Rondônia',
        '3': 'Ceará, Maranhão e Piauí',
        '4': 'Paraíba, Pernambuco, Alagoas e Rio Grande do Norte',
        '5': 'Bahia e Sergipe',
        '6': 'Minas Gerais',
        '7': 'Rio de Janeiro e Espírito Santo',
        '8': 'São Paulo',
        '9': 'Paraná e Santa Catarina'
    }
    combinations = {
        description: [] for description in descriptions.values()
    }
    counts = {
        description: 0 for description in descriptions.values()
    }
    for comb in product(additional_digits, repeat=num_asterisks):
        temp_number = number
        temp_control_digits = control_digits
        for digit in comb:
            if '*' in temp_number:
                temp_number = temp_number.replace('*', digit, 1)
            else:
                temp_control_digits = temp_control_digits.replace('*', digit, 1)
        temp_number += '-' + temp_control_digits
        if is_valid_cpf(temp_number):
            ninth_digit = temp_number[8]
            description = descriptions[ninth_digit]
            combinations[description].append(temp_number)
            counts[description] += 1
    print('\nTabela de contagem de CPFs por localidade:')
    print('Localidade e Quantidade')
    for description, count in counts.items():
        print(f'{description} = {count} CPFs')
    return combinations

number = '***79627*' #informe aqui o cpf mascarado (SEM OS DIGITOS DE VERIFICAÇÃO)
control_digits = '4*' #se possuir o dígito verificador do cpf, informe aqui. caso contrario deixe ** ou ainda 3*
additional_digits = '0123456789' #estes são os digitos usando para preencher as lacunas, não altere!

combinations = generate_combinations(number, additional_digits, control_digits)
for description, combination_list in combinations.items():
    print(f'CPFs de {description}:')
    print(combination_list)
