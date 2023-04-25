# Descrição
Este código gera todas as combinações possíveis de números de CPF a partir de um número parcialmente conhecido e dígitos adicionais. As combinações geradas são verificadas para garantir que sejam números de CPF válidos e são separadas em listas diferentes de acordo com o nono dígito da cadeia de 9 dígitos iniciais.


# Detalhamento 
Este código define duas funções principais: `is_valid_cpf` e `generate_combinations`. A função `is_valid_cpf` verifica se um número de CPF é válido usando a regra de validação dos dígitos verificadores do CPF. A função `generate_combinations` gera todas as combinações possíveis de números de CPF a partir de um número parcialmente conhecido (representado por um número de 9 dígitos com lacunas representadas por `*`) e dígitos adicionais. A função também aceita dígitos de controle conhecidos ou desconhecidos (representados por `*`) e gera combinações para preencher as lacunas nos dígitos de controle também. As combinações geradas são verificadas usando a função `is_valid_cpf` e apenas as combinações que são números de CPF válidos são incluídas na lista de combinações geradas. Por fim, a função separa as combinações geradas em listas diferentes de acordo com o nono dígito da cadeia de 9 dígitos iniciais e retorna um dicionário com as listas separadas e suas respectivas descrições.

# Instruções de uso

Apenas altere abaixo, nos locais informados. Não informe caracteres de pontuação ( ponto ou hifen).

exemplo:

number = '***402628'

control_digits = '**'

ou

number = '**1402628'

control_digits = '10'

ou

number = '**140262*'

control_digits = '10'

# Exemplo de saída

CPFs de Rio Grande do Sul:

['151402620-10', '341402620-10']

CPFs de Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins:

['881402621-10']

CPFs de Amazonas, Pará, Roraima, Amapá, Acre e Rondônia:

['401402622-10']

CPFs de Ceará, Maranhão e Piauí:

['031402623-10', '221402623-10']

CPFs de Paraíba, Pernambuco, Alagoas e Rio Grande do Norte:

['761402624-10', '951402624-10']

CPFs de Bahia e Sergipe:

['391402625-10', '581402625-10']

CPFs de Minas Gerais:

['101402626-10']

CPFs de Rio de Janeiro e Espírito Santo:

['641402627-10', '831402627-10']

CPFs de São Paulo:

['271402628-10', '461402628-10']

CPFs de Paraná e Santa Catarina:

['091402629-10']

# Atenção
ZERO é número e ele faz parte do cadastro de CPF de algumas pessoas e ele não pode ser omitido mesmo quando iniciado por Zero.
