@echo off
chcp 65001 > nul
echo ========================================================
echo      AWARD MONITORING DASHBOARD (FLASK SERVER)
echo ========================================================
echo.

:: 1. Navegar até a pasta do script
cd /d "%~dp0"

:: 2. Verificar/Ativar o Ambiente Virtual (opcional, se usar venv local)
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
) else (
    echo [AVISO] Ambiente virtual .venv não encontrado. Usando Python global...
)

:: Instalar dependências se necessário (opcional, mas ajuda a evitar erros)
:: pip install -r requirements.txt

:: 3. Iniciar o Servidor Web
echo.
echo [INFO] Iniciando servidor em http://127.0.0.1:5000 ...
echo [INFO] Para parar, feche esta janela.
echo.

:: Abre o navegador automaticamente
start http://127.0.0.1:5000

:: Roda o Flask
python run.py