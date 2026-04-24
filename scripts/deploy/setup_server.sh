#!/bin/bash

# --- CONFIGURAÇÕES ---
APP_NAME="award-monitoring"
APP_DIR="/var/www/$APP_NAME"
REPO_URL="SUA_URL_DO_GIT_AQUI" # Usuário deve preencher

echo "🚀 Iniciando configuração do servidor para $APP_NAME..."

# 1. Atualizar Sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar Dependências do Sistema
sudo apt install -y python3-pip python3-venv nginx git curl

# 3. Criar diretório da aplicação
sudo mkdir -p $APP_DIR
sudo chown $USER:$USER $APP_DIR

# 4. Criar Ambiente Virtual
if [ ! -d "$APP_DIR/venv" ]; then
    python3 -m venv $APP_DIR/venv
    echo "✅ Ambiente virtual criado."
fi

# 5. Configurar Firewall (UFW)
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw --force enable

echo "--------------------------------------------------"
echo "✅ Servidor preparado!"
echo "Próximos passos:"
echo "1. Clone o repositório em $APP_DIR"
echo "2. Configure o arquivo .env em $APP_DIR/.env"
echo "3. Execute o script de deploy: ./scripts/deploy/deploy.sh"
echo "--------------------------------------------------"
