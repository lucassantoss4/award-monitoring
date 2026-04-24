from core.config.sites_eventos import SITES_EVENTOS
from core.extractors.web import WebExtractor
from core.parsers.heuristicas_eventos import AnalisadorEventos
from core.utils.logger import get_logger

logger = get_logger("EventScraper")

class EventScraper:
    def __init__(self):
        self.web = WebExtractor()      # Ferramenta
        self.parser = AnalisadorEventos() # Cérebro (já com Validator)

    def run(self):
        logger.info(f"📅 Iniciando Scan de {len(SITES_EVENTOS)} Eventos...")
        eventos_processados = []

        for nome_evento, url in SITES_EVENTOS.items():
            # [IMPORTANTE] Modelo padrão compatível com o NOVO SCHEMA
            # Se o site der erro (503/403), usamos isso para não quebrar o site.
            dados = {
                "nome": nome_evento,
                "data_inicio": None,          # Era 'data'
                "data_status": "a_confirmar",
                "localizacao": {              # Era 'local' e 'regiao' soltos
                    "cidade": "Verificar Site",
                    "estado": "N/A",
                    "formato": "presencial"
                },
                "categoria": "Tecnologia",
                "areas_foco": ["Tecnologia"],
                "ia_foco_principal": False,
                "custo": "a_confirmar",
                "publico_alvo": "misto",
                "link": url
            }

            try:
                # 1. Usa a ferramenta Web
                raw_text = self.web.extract_text(url)
                
                if raw_text and len(raw_text) > 100:
                    # 2. Usa o Cérebro (que chama o Validator interno)
                    extraido = self.parser.processar(raw_text, nome_evento, url)
                    
                    # Atualiza os dados padrão com o que a IA achou
                    # Como o Validator já retorna a estrutura certa, podemos usar update
                    dados.update(extraido)
                    logger.info(f"   ✅ Processado: {nome_evento}")
                else:
                    logger.warning(f"   ⚠️ Site ilegível: {nome_evento} (Mantendo dados básicos)")
            
            except Exception as e:
                logger.error(f"   ❌ Erro em {nome_evento}: {e}")
            
            eventos_processados.append(dados)

        return eventos_processados