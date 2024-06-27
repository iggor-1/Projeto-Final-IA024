import re
import requests
from bs4 import BeautifulSoup

#url = "https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l11033.htm"
#lei_atual = 'Lei_11033'

#url = "https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm"
#lei_atual = 'Lei_5172'

#url = "https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/L11051.htm"
#lei_atual = 'Lei_11051'

#url = "https://www.planalto.gov.br/ccivil_03/leis/l8981.htm"
#lei_atual = 'Lei_8981'

url = "https://www.planalto.gov.br/ccivil_03/leis/l8383.htm"
lei_atual = 'Lei_8383'

# Faz a solicitação HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Define a codificação correta
    response.encoding = 'ISO-8859-1'

    # Remove quebras de linha, tabulações e outros caracteres de espaçamento do texto bruto
    conteudo_limpo = re.sub(r'\s+', ' ', response.text)
    
    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(conteudo_limpo, 'html.parser')
    
    # Encontra todos os parágrafos
    paragrafos = soup.find_all('p')

    # Lista para armazenar os textos dos parágrafos válidos
    lista_textos = []

    for paragrafo in paragrafos:
        # Verifica se o parágrafo contém uma tag <strike>
        has_strike = paragrafo.find('strike') is not None

        # Verifica se o parágrafo contém uma tag com text-decoration: line-through
        has_line_through = any(
            'text-decoration:line-through' in tag.get('style', '') for tag in paragrafo.find_all(True)
        )

        if not has_strike and not has_line_through:
            # Extrai o texto do parágrafo e adiciona à lista
            texto = paragrafo.get_text(separator='', strip=True)
            #texto = texto.replace('\n', '').replace('\t', '')
            lista_textos.append(texto)
    
    # Opcional: Imprimir cada parágrafo
    for idx, texto in enumerate(lista_textos, 1):
        print(f"Parágrafo {idx}: {texto}")
        
    # Salva a lista de parágrafos em um arquivo para processamento posterior
    with open(lei_atual, 'w', encoding='utf-8') as f:
        for texto in lista_textos:
            f.write(texto + '\n')
        
else:
    print(f"Erro ao acessar a página: {response.status_code}")
