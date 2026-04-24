from core.extractors.web import WebExtractor
from core.parsers.heuristicas_eventos import AnalisadorEventos
import logging

# Configura log simples para ver no terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DebugTool")

def testar_site_especifico():
    url_alvo = "https://www.congressodeinovacao.com.br/"
    nome_evento = "Congresso de Inovacao"

    print(f"\n--- 🕵️ INVESTIGANDO: {nome_evento} ---")
    print(f"URL: {url_alvo}\n")

    # 1. Tenta Extrair o Texto
    extractor = WebExtractor()
    texto_bruto = extractor.extract_text(url_alvo)

    print(f"--- 1. RESULTADO DA EXTRAÇÃO (Primeiros 500 caracteres) ---")
    if not texto_bruto:
        print("❌ ERRO CRÍTICO: O extrator retornou vazio. O site bloqueou ou requer JavaScript.")
        return
    else:
        print(texto_bruto[:500]) # Mostra o começo do texto
        print("...\n(Resto do texto oculto)\n")

    # 2. Tenta Entender os Dados (Parser)
    print(f"--- 2. TENTATIVA DE INTERPRETAÇÃO (IA/Heurística) ---")
    parser = AnalisadorEventos()
    dados = parser.processar(texto_bruto, nome_evento, url_alvo)

    print("📊 DADOS IDENTIFICADOS:")
    print(f"Nome: {dados.get('nome')}")
    print(f"Data Bruta Encontrada: {dados.get('data_inicio')} (Status: {dados.get('data_status')})")
    print(f"Local: {dados.get('localizacao')}")
    print(f"Custo: {dados.get('custo')}")

if __name__ == "__main__":
    testar_site_especifico()