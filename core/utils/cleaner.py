from datetime import datetime, date
import re

def formatar_data_br(data_input):
    """
    Recebe uma data (string ou objeto) e retorna no padrão DD/MM/AAAA.
    Ex: 2026-03-15 -> 15/03/2026
    """
    if not data_input or data_input == "A confirmar":
        return "A confirmar"
    
    # Se já for objeto de data, formata direto
    if isinstance(data_input, (date, datetime)):
        return data_input.strftime("%d/%m/%Y")
    
    texto = str(data_input).strip()
    
    try:
        # Tenta YYYY-MM-DD (Padrão ISO)
        dt = datetime.strptime(texto, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    except: pass

    try:
        # Tenta DD/MM/YYYY (Já está no formato, só valida)
        dt = datetime.strptime(texto, "%d/%m/%Y")
        return dt.strftime("%d/%m/%Y")
    except: pass
    
    # Se não conseguir converter, retorna o texto original limpo
    return texto

def limpar_resumo_tecnico(texto):
    """
    Remove cabeçalhos técnicos do resumo (ex: Fonte: pdfplumber).
    """
    if not texto: return "Sem descrição disponível."
    
    linhas = texto.split('\n')
    linhas_limpas = []
    
    for linha in linhas:
        l = linha.strip()
        # Pula linhas que começam com metadados técnicos
        if l.startswith("#") or l.lower().startswith("fonte:") or l.lower().startswith("arquivo:") or l.lower().startswith("url:"):
            continue
        if len(l) > 0:
            linhas_limpas.append(l)
            
    # Junta de volta e pega os primeiros 200 caracteres
    texto_final = " ".join(linhas_limpas)
    return texto_final[:250] + "..." if len(texto_final) > 250 else texto_final