# **Rifadenomes**

Este é um aplicativo Flask que implementa um formulário de registro, permitindo que usuários se cadastrem com nomes específicos em um banco de dados SQLite. Ele suporta o registro, a desinscrição e exibe uma lista de registrantes.

---

## **Recursos**
- Interface web para registro de nomes.
- Suporte para validação de nomes pré-definidos.
- Banco de dados persistente usando SQLite.
- API para visualizar registrantes em formato JSON.
- Arquitetura pronta para implantação em Railway ou servidores similares.

---

## **Requisitos**
- Python 3.10 ou superior.
- Pacotes listados no arquivo `requirements.txt`.

---

## **Configuração e Execução Local**

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o aplicativo**:
   ```bash
   flask run
   ```
   Acesse o aplicativo em [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Estrutura do Projeto**
```
.
├── app.py                # Código principal do aplicativo Flask
├── requirements.txt      # Dependências do projeto
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── templates/            # Arquivos HTML para renderização
└── tmp/                  # Diretório para o banco de dados SQLite
```

---

## **Endereços Principais**

- **Página inicial**: `http://127.0.0.1:5000/`
  - Exibe os nomes disponíveis e a interface para registro.

- **Lista de Registrantes**: `http://127.0.0.1:5000/registrants`
  - Exibe os registrantes registrados.

- **Admin API (JSON)**: `http://127.0.0.1:5000/admin/registrants`
  - Retorna a lista de registrantes no formato JSON.

---

## **Validação de Nomes**
Os nomes permitidos são validados com base em uma lista fixa definida no arquivo `app.py`. Caso o nome não esteja na lista, o registro será rejeitado.

---

## **Persistência do Banco de Dados**
Este aplicativo utiliza SQLite como banco de dados. O arquivo `rifadenomes.db` é armazenado no diretório `/app/tmp`, configurado para persistir em volumes ao ser implantado no Railway.

---

## **Implantação no Railway**
1. Configure um volume persistente montado em `/app/tmp`.
2. Certifique-se de que o arquivo `rifadenomes.db` está sendo armazenado neste diretório.
3. Configure o aplicativo para iniciar com Gunicorn:
   - Crie um arquivo `Procfile`:
     ```
     web: gunicorn app:app
     ```
4. Faça o push para o GitHub e conecte o repositório ao Railway.

---

## **Contribuição**
Sinta-se à vontade para abrir issues e pull requests para melhorias ou novos recursos.
