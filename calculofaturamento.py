import json

def calcular_faturamento():
    """Calcula o menor e o maior valor de faturamento, e conta os dias com faturamento acima da média."""
    # Lê os dados do arquivo JSON
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    # Extrai os valores de faturamento
    faturamentos = [item['faturamento'] for item in dados['dias'] if item['faturamento'] > 0]

    if not faturamentos:
        print("Não há dados de faturamento disponíveis.")
        return

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Calcula a média mensal de faturamento
    media_mensal = sum(faturamentos) / len(faturamentos)

    # Conta o número de dias com faturamento acima da média
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

    # Exibe os resultados
    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

# Chama a função para calcular e exibir os resultados
calcular_faturamento()
