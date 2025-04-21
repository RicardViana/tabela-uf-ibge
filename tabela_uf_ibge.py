import requests
from lxml import html
import pandas as pd

# URL da página
url = "https://www.ibge.gov.br/explica/codigos-dos-municipios.php"

# Requisição
resposta = requests.get(url)
resposta.encoding = 'utf-8'  # Garante que acentos não quebrem

# Parse HTML
arvore = html.fromstring(resposta.content)

# Extrai os dados da tabela de UFs
ufs = arvore.xpath('//table[1]/tbody/tr/td[1]/a/text()')
codigos = arvore.xpath('//table[1]/tbody/tr/td[2]/a/text()')

# Monta o DataFrame
codigo_uf = pd.DataFrame({
    'Código': codigos,
    'UF': ufs
})

# Mapeamento de Código para Sigla e Região
mapa_uf = {
    '11': {'Sigla': 'RO', 'Região': 'Norte'},
    '12': {'Sigla': 'AC', 'Região': 'Norte'},
    '13': {'Sigla': 'AM', 'Região': 'Norte'},
    '14': {'Sigla': 'RR', 'Região': 'Norte'},
    '15': {'Sigla': 'PA', 'Região': 'Norte'},
    '16': {'Sigla': 'AP', 'Região': 'Norte'},
    '17': {'Sigla': 'TO', 'Região': 'Norte'},
    '21': {'Sigla': 'MA', 'Região': 'Nordeste'},
    '22': {'Sigla': 'PI', 'Região': 'Nordeste'},
    '23': {'Sigla': 'CE', 'Região': 'Nordeste'},
    '24': {'Sigla': 'RN', 'Região': 'Nordeste'},
    '25': {'Sigla': 'PB', 'Região': 'Nordeste'},
    '26': {'Sigla': 'PE', 'Região': 'Nordeste'},
    '27': {'Sigla': 'AL', 'Região': 'Nordeste'},
    '28': {'Sigla': 'SE', 'Região': 'Nordeste'},
    '29': {'Sigla': 'BA', 'Região': 'Nordeste'},
    '31': {'Sigla': 'MG', 'Região': 'Sudeste'},
    '32': {'Sigla': 'ES', 'Região': 'Sudeste'},
    '33': {'Sigla': 'RJ', 'Região': 'Sudeste'},
    '35': {'Sigla': 'SP', 'Região': 'Sudeste'},
    '41': {'Sigla': 'PR', 'Região': 'Sul'},
    '42': {'Sigla': 'SC', 'Região': 'Sul'},
    '43': {'Sigla': 'RS', 'Região': 'Sul'},
    '50': {'Sigla': 'MS', 'Região': 'Centro-Oeste'},
    '51': {'Sigla': 'MT', 'Região': 'Centro-Oeste'},
    '52': {'Sigla': 'GO', 'Região': 'Centro-Oeste'},
    '53': {'Sigla': 'DF', 'Região': 'Centro-Oeste'}
}

# Adiciona as colunas com base no mapeamento
codigo_uf['Sigla'] = codigo_uf['Código'].map(lambda x: mapa_uf.get(x, {}).get('Sigla'))
codigo_uf['Região'] = codigo_uf['Código'].map(lambda x: mapa_uf.get(x, {}).get('Região'))

# Exibe o DataFrame
print(codigo_uf.head())

# Salva o DataFrame em um arquivo CSV
codigo_uf.to_csv('codigo_uf.csv', index=False, encoding='utf-8')