

-----

# TPF Engenharia - Agente de IA

Este projeto é uma aplicação web completa que utiliza a **API Gemini do Google** para gerar relatórios detalhados a partir de prompts do usuário. A aplicação tem uma interface amigável construída com **Flask** e é capaz de exportar o conteúdo gerado em três formatos profissionais: Word (**DOCX**), Excel (**XLSX**) e PDF (**PDF**).

## 🚀 Funcionalidades Principais

  * **Interface Web Amigável:** O usuário interage com o Agente de IA através de um frontend simples e intuitivo.
  * **Geração de Relatórios:** Produz conteúdo detalhado sobre diversos tópicos, desde tecnologia até projetos de engenharia.
  * **Exportação em Múltiplos Formatos:** Permite o download do relatório em DOCX, XLSX e PDF com apenas um clique.
  * **Nomeação de Arquivos Inteligente:** Os arquivos de relatório são nomeados dinamicamente com base nas palavras-chave mais relevantes do prompt do usuário, como "relatorio\_computacao\_quantica.docx".

## ⚙️ Tecnologias Utilizadas

  * **Python:** Linguagem de programação principal.
  * **Flask:** Framework web para criar a interface e gerenciar as rotas.
  * **Google Gemini API:** Para a geração de conteúdo de IA.
  * **python-docx:** Para a criação de arquivos `.docx`.
  * **openpyxl:** Para a criação de arquivos `.xlsx`.
  * **reportlab:** Para a criação de arquivos `.pdf`.
  * **python-dotenv:** Para o gerenciamento seguro da chave de API.
  * **re (Regular Expressions):** Para a lógica de nomeação de arquivos.

## ⚙️ Como Instalar e Rodar

Para rodar este projeto, siga os passos abaixo:

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/MorganaSouza/AgenteAI_TPF_Engenharia.git
    ```
2.  **Entre na pasta do projeto:**
    ```sh
    cd AgenteAI_TPF_Engenharia
    ```
3.  **Crie e ative o ambiente virtual:**
    ```sh
    # Cria o ambiente
    python -m venv venv
    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate
    # Ativa o ambiente (Linux/macOS)
    source venv/bin/activate
    ```
4.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Configure a chave de API:**
      * Crie um arquivo chamado `.env` na pasta principal do projeto.
      * Adicione sua chave de API nele, no formato:
        ```ini
        GOOGLE_API_KEY=SUA_CHAVE_AQUI
        ```
6.  **Execute a aplicação:**
    ```sh
    python app.py
    ```
    A aplicação estará disponível em `http://127.0.0.1:5000`.

## ✨ Como Funciona

Ao executar o `app.py`, o servidor Flask é iniciado e a interface web é carregada. O usuário insere um prompt, que é enviado ao servidor. O servidor, por sua vez, interage com a API do Google Gemini, gera o relatório e, em seguida, salva os arquivos `.docx`, `.xlsx` e `.pdf` com um nome dinâmico (ex: `relatorio_tecnologias_inovadoras.docx`).

## 🤝 Como Contribuir

Contribuições são sempre bem-vindas\! Se você tiver sugestões de melhoria, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📜 Licença

Este projeto está sob a licença [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
