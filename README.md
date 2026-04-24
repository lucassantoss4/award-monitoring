# Sistema de Monitoramento de Oportunidades de Inovação

Um robô inteligente que monitora e consolida premiações e eventos de tecnologia e inovação, fornecendo uma visão unificada e organizada das oportunidades disponíveis.

## 🚀 Funcionalidades Principais

### Monitoramento de Premiações
- **Extração automática** de PDFs e sites de premiações
- **Análise semântica** para identificar oportunidades relevantes
- **Formatação inteligente** de datas e resumos técnicos
- **Status em tempo real** (Aberto/Encerrado)

### Monitoramento de Eventos
- **Web scraping** avançado de sites de eventos de tecnologia
- **Validação de schema** para garantir qualidade dos dados
- **Consolidação** de eventos de múltiplas fontes
- **Datas no padrão ISO** (YYYY-MM-DD) para melhor organização

### Dashboard Web
- **Interface intuitiva** para visualização das oportunidades
- **Timeline organizada** por meses e status
- **Filtros e buscas** para encontrar oportunidades específicas
- **Logos e branding** automatizados para cada premiação/evento

### Notificações
- **Alertas por email** quando novas oportunidades são identificadas
- **Integração com Outlook** para notificações corporativas
- **Resumos diários** das oportunidades disponíveis

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.10+** - Linguagem principal
- **Flask** - Framework web para o dashboard
- **Playwright** - Automação de navegador para web scraping
- **Crawl4AI** - Extração inteligente de conteúdo web
- **Docling** - Leitura e processamento de PDFs

### Processamento de Dados
- **Pandas** - Manipulação e análise de dados
- **OpenPyXL** - Leitura de arquivos Excel
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

### Automação Windows
- **PyWin32** - Integração com Outlook para notificações

## 📦 Instalação

### Requisitos Prévios
- Python 3.10 ou superior
- Microsoft Outlook (para notificações)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/award-monitoring.git
   cd award-monitoring
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instale o Playwright:**
   ```bash
   playwright install
   ```

5. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto com as configurações necessárias (veja `core/config/.env` para referência).

## 🏃‍♂️ Execução

### Modo Web (Dashboard)
```bash
python run.py
```
Acesse o dashboard em: `http://localhost:5000`

### Modo Pipeline (Robô)
```bash
python debug_robo.py
```
Executa o pipeline completo de monitoramento.

### Forçar Pipeline
```bash
python forcar_pipeline.py
```
Força a execução do pipeline mesmo quando já processado.

## 📁 Estrutura do Projeto

```
award-monitoring/
├── app/                    # Aplicação Flask
│   ├── __init__.py        # Inicialização da aplicação
│   ├── routes.py          # Rotas do dashboard
│   ├── static/            # Arquivos estáticos (CSS, JS, imagens)
│   └── templates/         # Templates HTML
├── core/                  # Lógica de negócios
│   ├── config/            # Configurações e settings
│   ├── extractors/        # Extratores de dados
│   │   ├── pdf.py         # Extração de PDFs
│   │   ├── web.py         # Web scraping
│   │   ├── json_parser.py # Processamento JSON
│   │   └── events.py      # Extração de eventos
│   ├── parsers/           # Processadores de dados
│   │   ├── heuristicas_editais.py  # Análise semântica
│   │   ├── schema_validator.py     # Validação de schemas
│   │   └── normalizador.py         # Normalização de dados
│   ├── pipeline/          # Pipeline de processamento
│   │   ├── pipeline_manager.py     # Gerenciador principal
│   │   ├── etapas.py               # Etapas do pipeline
│   │   └── scheduler.py            # Agendamento
│   ├── notifications/     # Sistema de notificações
│   │   └── email_service.py        # Integração com Outlook
│   └── utils/             # Utilitários
│       ├── cleaner.py     # Limpeza de dados
│       ├── dates.py       # Manipulação de datas
│       ├── files.py       # Operações com arquivos
│       ├── json_schema.py # Schemas JSON
│       └── logger.py      # Sistema de logging
├── data/                  # Dados de entrada e saída
│   ├── entrada_pdfs/      # PDFs de premiações
│   ├── entrada_json/      # JSONs processados
│   ├── entrada_scraped/   # Dados raspados
│   ├── curadoria/         # Dados curados manualmente
│   ├── saida_json/        # Resultados consolidados
│   ├── eventos/           # Eventos processados
│   └── logs/              # Logs do sistema
├── debug_robo.py          # Script de debug do robô
├── forcar_pipeline.py     # Script para forçar pipeline
├── run.py                 # Script principal de execução
└── requirements.txt       # Dependências do projeto
```

## 🔧 Configuração

### Sites Monitorados
Configure os sites de premiações no arquivo `core/config/sites.py`:

```python
SITES_MONITORADOS = {
    "nome_do_site": "https://url-do-site.com",
    # Adicione mais sites conforme necessário
}
```

### Eventos Monitorados
Configure os sites de eventos no arquivo `core/config/sites_eventos.py`:

```python
SITES_EVENTOS = {
    "nome_do_evento": "https://url-do-evento.com",
    # Adicione mais eventos conforme necessário
}
```

### Curadoria Manual
Para ajustes manuais de premiações ou eventos, edite os arquivos:
- `data/curadoria/descricoes.json` - Para premiações
- `data/curadoria/eventos_curadoria.json` - Para eventos

## 📊 Como Funciona

### Pipeline de Premiações
1. **Extração**: Lê PDFs e faz web scraping de sites
2. **Análise**: Processa o conteúdo com IA para identificar oportunidades
3. **Normalização**: Formata datas, resumos e metadados
4. **Consolidação**: Une todos os dados em um único JSON
5. **Notificação**: Envia alertas por email

### Pipeline de Eventos
1. **Scraping**: Extrai eventos de sites de tecnologia
2. **Validação**: Verifica o schema dos dados
3. **Curadoria**: Aplica ajustes manuais configurados
4. **Consolidação**: Gera JSON organizado por data
5. **Notificação**: Envia alertas sobre novos eventos

## 🎯 Uso do Dashboard

### Visualização de Oportunidades
- **Lista de Premiações**: Todas as premiações disponíveis
- **Lista de Eventos**: Eventos de tecnologia organizados
- **Timeline**: Visão cronológica unificada

### Filtros e Busca
- **Busca por título**: Encontre oportunidades específicas
- **Filtros por status**: Separe oportunidades abertas/encerradas
- **Organização por data**: Veja o que está por vir

## 🤖 Inteligência Artificial

O sistema utiliza IA para:
- **Análise semântica** de documentos PDF
- **Identificação automática** de oportunidades relevantes
- **Extração inteligente** de informações de sites
- **Classificação** de oportunidades por relevância

## 📧 Notificações

### Configuração de Email
Configure as credenciais do Outlook no arquivo `.env`:

```env
OUTLOOK_EMAIL=seu-email@empresa.com
OUTLOOK_PASSWORD=sua-senha
```

### Tipos de Notificações
- **Novas oportunidades**: Quando novas premiações são identificadas
- **Eventos próximos**: Alertas sobre eventos que se aproximam
- **Resumos diários**: Panorama das oportunidades disponíveis

## 🔒 Segurança

- **Variáveis de ambiente**: Credenciais armazenadas de forma segura
- **Validação de schemas**: Garantia da integridade dos dados
- **Logging controlado**: Registros de atividades para auditoria

## 🚀 Deploy

### Produção
Para deploy em produção, recomenda-se:

1. **Configurar variáveis de ambiente** no servidor
2. **Instalar dependências** em ambiente virtual
3. **Configurar serviço** (systemd, supervisor, etc.)
4. **Configurar proxy reverso** (nginx, apache)
5. **Configurar SSL/TLS** para HTTPS

### Docker (Futuro)
Planejamos adicionar suporte Docker para facilitar o deploy em containers.

## 🤝 Contribuição

### Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch para sua feature: `git checkout -b feature/nome-da-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona nova feature'`
4. Push para a branch: `git push origin feature/nome-da-feature`
5. Abra um Pull Request

### Diretrizes de Código
- Siga o padrão de codificação já estabelecido
- Adicione comentários para funcionalidades complexas
- Mantenha a consistência nas naming conventions
- Teste suas alterações antes de submeter

## 📋 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- Comunidade Open Source
- Contribuidores
- Comunidade open source

## 📞 Suporte

Para suporte técnico ou dúvidas sobre o projeto:

- **Email**: [seu-email@empresa.com](mailto:seu-email@empresa.com)
- **Issues**: [GitHub Issues](https://github.com/seu-usuario/award-monitoring/issues)

---

**Desenvolvido com ❤️ pela comunidade**