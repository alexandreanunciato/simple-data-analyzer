def carregar_dados():
    """Carrega uma lista de números informada pelo usuário."""
    print("Digite os números separados por vírgula (ex: 10,20,30):")
    entrada = input("> ")

    try:
        dados = [float(item.strip()) for item in entrada.split(",")]
        return dados
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números.")
        return []


def calcular_media(dados):
    """Retorna a média dos números."""
    if not dados:
        return None
    return sum(dados) / len(dados)


def encontrar_maior(dados):
    """Retorna o maior valor da lista."""
    return max(dados) if dados else None


def encontrar_menor(dados):
    """Retorna o menor valor da lista."""
    return min(dados) if dados else None


def exibir_relatorio(dados):
    """Mostra os resultados formatados."""
    print("\n📊 RELATÓRIO DE ANÁLISE")
    print("------------------------")

    if not dados:
        print("Nenhum dado para analisar.")
        return

    print(f"Quantidade de valores: {len(dados)}")
    print(f"Média: {calcular_media(dados):.2f}")
    print(f"Maior valor: {encontrar_maior(dados)}")
    print(f"Menor valor: {encontrar_menor(dados)}")


def main():
    print("=== Analisador de Dados Simples ===")
    dados = carregar_dados()
    exibir_relatorio(dados)


if __name__ == "__main__":
    main()
