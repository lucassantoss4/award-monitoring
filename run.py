from app import create_app
from core.pipeline.pipeline_manager import Pipeline
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import logging

# Configura logs para aparecerem no terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Scheduler")

app = create_app()

def job_scanner_automatico():
    """
    Esta função roda sozinha nos horários agendados.
    """
    logger.info("⏰ [AUTO] Iniciando Rotina de Extração Agendada...")
    try:
        pipe = Pipeline()
        pipe.run_full_scan()
        logger.info("✅ [AUTO] Rotina finalizada com sucesso.")
    except Exception as e:
        logger.error(f"❌ [AUTO] Erro na rotina agendada: {e}")

if __name__ == "__main__":
    # 1. Cria o Agendador
    scheduler = BackgroundScheduler()
    
    # 2. Configura o Horário
    # Opção A: Rodar todo dia às 08:00 da manhã
    # scheduler.add_job(func=job_scanner_automatico, trigger="cron", hour=8, minute=0)
    
    # Opção B: Rodar a cada 4 horas (Ideal para monitoramento contínuo)
    scheduler.add_job(func=job_scanner_automatico, trigger="interval", hours=4)
    
    # 3. Inicia o Agendador
    scheduler.start()
    logger.info("🕒 Agendador iniciado! O robô rodará automaticamente a cada 4 horas.")

    # Garante que o agendador pare se o site for desligado
    atexit.register(lambda: scheduler.shutdown())

    # 4. Roda o Site
    # use_reloader=False é IMPORTANTE para não duplicar o agendador
    app.run(debug=True, use_reloader=False)