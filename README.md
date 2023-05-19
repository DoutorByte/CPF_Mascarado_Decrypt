# Descrição
Este código gera todas as combinações possíveis para números de CPF a partir de um número parcialmente conhecido e dígitos verificadores(que podem ou não ser conhecidos também). As combinações geradas são verificadas para garantir que sejam números de CPF válidos e são separadas em listas diferentes de acordo com o estado(UF) ou região de origem.<br>

<br>

# Detalhamento 
Este código define duas funções principais: `is_valid_cpf` e `generate_combinations`. A função `is_valid_cpf` verifica se um número de CPF é válido usando a regra de validação dos dígitos verificadores do CPF. A função `generate_combinations` gera todas as combinações possíveis de números de CPF a partir de um número parcialmente conhecido (representado por um número de 9 dígitos com lacunas representadas por `*`) e dígitos adicionais. A função também aceita dígitos de controle conhecidos ou desconhecidos (representados por `*`) e gera combinações para preencher as lacunas nos dígitos de controle também. As combinações geradas são verificadas usando a função `is_valid_cpf` e apenas as combinações que são números de CPF válidos são incluídas na lista de combinações geradas. Por fim, a função separa as combinações geradas em listas diferentes de acordo com o nono dígito da cadeia de 9 dígitos iniciais e retorna um dicionário com as listas separadas e suas respectivas descrições.

# Instruções de uso

Apenas altere abaixo, nos locais informados. Não informe caracteres de pontuação ( ponto ou hifen).

exemplo:

number = '***402628'<br>
control_digits = '**'

ou

number = '**1402628'<br>
control_digits = '10'

ou

number = '**140262*'<br>
control_digits = '10'

# Exemplo de saída

CPFs de Rio Grande do Sul:<br>
['151402620-10', '341402620-10']

CPFs de Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins:<br>
['881402621-10']

CPFs de Amazonas, Pará, Roraima, Amapá, Acre e Rondônia:<br>
['401402622-10']

CPFs de Ceará, Maranhão e Piauí:<br>
['031402623-10', '221402623-10']

CPFs de Paraíba, Pernambuco, Alagoas e Rio Grande do Norte:<br>
['761402624-10', '951402624-10']

CPFs de Bahia e Sergipe:<br>
['391402625-10', '581402625-10']

CPFs de Minas Gerais:<br>
['101402626-10']

CPFs de Rio de Janeiro e Espírito Santo:<br>
['641402627-10', '831402627-10']

CPFs de São Paulo:<br>
['271402628-10', '461402628-10']

CPFs de Paraná e Santa Catarina:<br>
['091402629-10']

# Atenção
ZERO é número e ele faz parte do cadastro de CPF de algumas pessoas e ele não pode ser omitido mesmo quando iniciado por Zero.

Este script gera toda a faixa de números de CPF disponíveis. Entretanto e obviamente alguns números são inexistentes na base de dados oficial por não terem sido ainda atribuido a uma pessoa fisica ou ainda se o numero de CPF foi dado baixa no sistema da Receita Federal.

# Curiosidade
O primeiro CPF (Cadastro de Pessoas Físicas) foi emitido em 1972, para o economista João Paulo dos Reis Velloso, que foi o primeiro presidente do Instituto Brasileiro de Planejamento Tributário (IBPT). Seu número de CPF era o 0000.001.923-00. Estranhamente este numero são segue a lógica atual para os numero de CPF.

# TODO 
~filtrar mais ainda o resultado final  exibindo apenas os CPFs ativos e o nome da pessoa física~<br>
Dispobilização pública cancelada devido ao risco de uso indevido. Será criado outro repositório privado com o codigo que obtem nome e situação cadastral dos CPFs.<br>
Posso antecipar que a ferramenta consegue capturar nomes de cpfs gerados por este script mas depois de um determinado número de consultas em sequencia, o script é barrado pelo cloudflare. Estou tentando identificar depois de quanto tempo a consulta pode ser retomada para que o script entre em pausa ao detectar o limitador e retome a atidade após o cloudflare não barrar mais.

# SCRIPT PARA FINS DIDÁTICOS, USE COM RESPONSABILIDADE.


