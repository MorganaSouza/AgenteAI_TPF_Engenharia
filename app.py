from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Importa as funções do seu script principal
from main import gerar_resposta, extrair_topicos, salvar_docx, salvar_xlsx, salvar_pdf

app = Flask(__name__)

# Configuração da API do Gemini
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("A variável de ambiente GOOGLE_API_KEY não foi definida.")
genai.configure(api_key=API_KEY)

# Rota principal para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o prompt e gerar a resposta
@app.route('/gerar', methods=['POST'])
def gerar():
    prompt = request.form['prompt']
    
    # Gera a resposta com o Gemini (texto bruto)
    resposta_bruta = gerar_resposta(prompt)
    
    # Extrai os tópicos para salvar nos arquivos
    topicos_processados = extrair_topicos(resposta_bruta)

    # --- Lógica de nomeação atualizada e mais robusta ---
    # Lista de "stop words" em português
    stop_words = ["o", "a", "os", "as", "um", "uma", "uns", "umas", "de", "do", "da", "dos", "das", "para", "em", "no", "na", "nos", "nas", "com", "por", "sobre", "que", "e", "se", "ou"]
    
    # Filtra as palavras do prompt para remover "stop words" e palavras curtas
    palavras_chave = [
        palavra.lower() 
        for palavra in re.split(r'\W+', prompt) 
        if palavra.lower() not in stop_words and len(palavra) > 2
    ]

    # Junta as primeiras 3 palavras-chave para criar o nome base
    if palavras_chave:
        nome_base = "relatorio_" + "_".join(palavras_chave[:3])
    else:
        nome_base = "relatorio_gerado"
    # --- Fim da nova lógica ---
    
    # Salva os arquivos com os tópicos processados
    salvar_docx(topicos_processados, nome_base=nome_base)
    salvar_xlsx(topicos_processados, nome_base=nome_base)
    salvar_pdf(topicos_processados, nome_base=nome_base)
    
    # Renderiza a mesma página, mas com a resposta da IA e o nome base do arquivo
    return render_template('index.html', resposta=resposta_bruta, nome_base=nome_base)

# --- Nova Rota para um novo chat ---
@app.route('/novo_chat')
def novo_chat():
    return redirect(url_for('index'))

# --- Novas Rotas de Download ---
@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except FileNotFoundError:
        return "Arquivo não encontrado.", 404

if __name__ == '__main__':
    app.run(debug=True)