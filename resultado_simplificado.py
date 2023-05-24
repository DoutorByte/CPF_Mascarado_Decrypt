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

    combinations = {}
    for idx, comb in enumerate(product(additional_digits, repeat=num_asterisks)):
        temp_number = number
        temp_control_digits = control_digits
        for digit in comb:
            if '*' in temp_number:
                temp_number = temp_number.replace('*', digit, 1)
            else:
                temp_control_digits = temp_control_digits.replace('*', digit, 1)
        temp_cpf = temp_number + temp_control_digits
        if is_valid_cpf(temp_cpf):
            combinations[idx] = temp_cpf

    return combinations

number = '196109338' #informe aqui o cpf mascarado (SEM OS DIGITOS DE VERIFICAÇÃO)
control_digits = '**' #se possuir o dígito verificador do cpf, informe aqui. caso contrario deixe ** ou ainda 3*
additional_digits = '0123456789' #estes são os digitos usando para preencher as lacunas, não altere!

combinations = generate_combinations(number, additional_digits, control_digits)
counter = 0  # Inicializa o contador como 0
for combination_list in combinations.values():
    cpf_number = combination_list.replace('-', '')  # Remove o traço do número de CPF
    print(cpf_number)
    counter += 1  # Incrementa o contador

print("Quantidade de resultados encontrados:", counter)
