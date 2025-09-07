# Relatório de Inteligência Artificial

Este projeto utiliza a API Gemini do Google para gerar um relatório detalhado sobre Inteligência Artificial. O relatório é estruturado em tópicos e exportado em três formatos diferentes: Word (DOCX), Excel (XLSX) e PDF.

## 🚀 Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Google Gemini API:** Para a geração de conteúdo.
* **python-docx:** Para a criação de arquivos `.docx`.
* **openpyxl:** Para a criação de arquivos `.xlsx`.
* **reportlab:** Para a criação de arquivos `.pdf`.
* **python-dotenv:** Para o gerenciamento seguro da chave de API.

## ⚙️ Como Instalar e Rodar

Para rodar este projeto, siga os passos abaixo:

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/MorganaSouza/AgenteAI_TPF_Engenharia.git](https://github.com/MorganaSouza/AgenteAI_TPF_Engenharia.git)
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
6.  **Execute o script:**
    ```sh
    python main.py
    ```

## ✨ Como Funciona

O script `main.py` se conecta à API do Google Gemini, solicitando uma explicação detalhada sobre o que é Inteligência Artificial. Em seguida, ele processa a resposta e cria os seguintes arquivos na pasta do projeto:

* `relatorio_ia.docx`
* `relatorio_ia.xlsx`
* `relatorio_ia.pdf`

## 🤝 Como Contribuir

Contribuições são sempre bem-vindas! Se você tiver sugestões de melhoria, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## 📜 Licença

Este projeto está sob a licença [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
