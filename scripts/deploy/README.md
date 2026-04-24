# Guia de Deploy - Award Monitoring

Este guia descreve como colocar a aplicação em produção em um servidor Linux (Ubuntu/Debian).

## 1. Segurança Inicial (SSH)

1. **Chaves SSH:** Sempre use chaves em vez de senhas.
   - Gere no seu PC: `ssh-keygen -t ed25519`
   - Copie para o servidor: `ssh-copy-id usuario@ip-servidor`
2. **Desativar Senhas:** No servidor, edite `/etc/ssh/sshd_config`:
   - `PasswordAuthentication no`
   - `PermitRootLogin no`

## 2. Configuração do Servidor

Execute o script de setup inicial:
```bash
chmod +x scripts/deploy/setup_server.sh
./scripts/deploy/setup_server.sh
```

## 3. Configuração do Serviço (Systemd)

Crie o arquivo de serviço: `sudo nano /etc/systemd/system/award-monitoring.service`

```ini
[Unit]
Description=Gunicorn instance to serve Award Monitoring
After=network.target

[Service]
User=seu_usuario
Group=www-data
WorkingDirectory=/var/www/award-monitoring
Environment="PATH=/var/www/award-monitoring/venv/bin"
# Carrega as variáveis do .env
ExecStart=/var/www/award-monitoring/venv/bin/gunicorn \
    --config scripts/deploy/gunicorn.conf.py \
    run:app

[Install]
WantedBy=multi-user.target
```

Ative o serviço:
```bash
sudo systemctl start award-monitoring
sudo systemctl enable award-monitoring
```

## 4. Variáveis de Ambiente (.env)

Crie um arquivo `.env` em `/var/www/award-monitoring/.env` com as seguintes chaves:

```env
SECRET_KEY="uma-chave-longa-e-segura"
API_KEY="chave-para-power-automate"
EMAIL_DESTINATARIOS="seu-email@exemplo.com"
POWER_AUTOMATE_WEBHOOK_URL="https://..."
```

## 5. Automação com Power Automate

A aplicação expõe um JSON simplificado para automação em:
**URL:** `http://seu-ip/api/v1/automation/data`
**Header:** `X-API-KEY: sua-chave-aqui`

Use este endpoint para criar alertas personalizados no Power Automate.
