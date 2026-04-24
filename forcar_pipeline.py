import sys
import os
import json
from pathlib import Path

# Adiciona o diretório atual ao path para encontrar o módulo 'core'
basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, basedir)

from core.config.settings import settings
from core.pipeline.pipeline_manager import Pipeline

def forcar_execucao():
    print("\n==================================================")
    print("🚀 FORÇANDO EXECUÇÃO DO PIPELINE (MODO DEBUG)")
    print("==================================================\n")

    # 1. Verifica caminhos
    print(f"📂 Diretório Base: {basedir}")
    print(f"📂 Pasta PDFs Entrada: {settings.INPUT_PDFS}")
    print(f"📂 Arquivo JSON Saída: {settings.OUTPUT_JSON / 'monitoramento_consolidado.json'}\n")

    # 2. Inicializa Pipeline
    print("1️⃣  Inicializando Pipeline...")
    try:
        pipe = Pipeline()
        print("   ✅ Pipeline instanciado com sucesso.")
    except Exception as e:
        print(f"   ❌ ERRO FATAL AO INICIAR CLASSE PIPELINE: {e}")
        import traceback
        traceback.print_exc()
        return

    # 3. Executa
    print("\n2️⃣  Rodando scan completo (Aguarde)...")
    try:
        # Chama o método que varre os PDFs
        pipe.run_full_scan()
        print("   ✅ Método run_full_scan() finalizado.")
    except Exception as e:
        print(f"   ❌ ERRO DURANTE A EXECUÇÃO: {e}")
        import traceback
        traceback.print_exc()
        return

    # 4. Verifica Resultado
    print("\n3️⃣  Verificando o arquivo JSON gerado...")
    arquivo_json = settings.OUTPUT_JSON / "monitoramento_consolidado.json"
    
    if not arquivo_json.exists():
        print(f"   ❌ O ARQUIVO NÃO FOI CRIADO NO DISCO!")
    else:
        try:
            with open(arquivo_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
            
            print(f"   ✅ Arquivo lido com sucesso.")
            print(f"   📊 Total de itens encontrados: {len(dados)}")
            
            if len(dados) == 0:
                print("   ⚠️ AVISO: O arquivo existe mas está VAZIO [].")
                print("      Verifique se o Parser está rejeitando os PDFs.")
            else:
                print("\n   🔎 Itens no JSON:")
                for item in dados:
                    print(f"      - [{item.get('status')}] {item.get('titulo')} (Fim: {item.get('data_inscricao_fim')})")

        except Exception as e:
            print(f"   ❌ Erro ao ler o JSON gerado: {e}")

    print("\n==================================================")
    print("FIM DO TESTE")
    print("==================================================")

if __name__ == "__main__":
    forcar_execucao()