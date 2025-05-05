# Furia Chatbot

O **Furia Chatbot** é uma aplicação de chatbot baseada na API do ChatGPT da Azure. O objetivo é oferecer aos fãs da FURIA um assistente interativo, respondendo perguntas sobre a organização e oferecendo funcionalidades adicionais através de botões, como **Sobre**, **Loja**, **Times** etc...

Este repositório contém o código-fonte da aplicação que utiliza **Flask** para carregar a API do ChatGPT e oferece uma interface de fácil uso para os fãs da FURIA. A aplicação está implantada no **Vercel** para acesso via web.

## Deploy no Vercel

A aplicação está disponível online via Vercel. Para acessar, use o seguinte link:

https://furia-tech-test.vercel.app

## Funcionalidades

* **Respostas automatizadas** com base nas perguntas dos usuários.
* **Botões interativos** com opções como:

  * **Sobre**: Informações sobre a FURIA.
  * **Notícias**: Últimas atualizações e novidades sobre a FURIA.
  * **Loja**: Acesso à loja oficial da FURIA.
  * **Equipes**: Detalhes sobre as equipes e jogadores da FURIA.
  * **Instagram**: Link para o perfil oficial no Instagram.
  * **Twitter**: Link para o perfil oficial no Twitter.

* **Botões de erros**:
  * **Abrir reclamação**: Permite que o usuário registre uma reclamação diretamente no repositório para relatar o erro.
  * **Recarregue a página**: Sugere ao usuário atualizar a página para corrigir possíveis erros temporários (não possui link).

* Suporte para até **três botões** por vez com links relacionados ao prompt enviado.

## Tecnologias Utilizadas

* **Flask**: Framework web para a construção da API e backend em Python.
* **ChatGPT API (Azure)**: Integração com a API do ChatGPT para fornecer respostas inteligentes.
* **Vercel**: Plataforma de deploy para rodar a aplicação na nuvem.
* **HTML / CSS / JS**: Utilizados para criar e estilizar a interface do usuário, garantindo uma experiência visual agradável e interativa.


## Pré-requisitos

Antes de rodar a aplicação localmente, você precisará de:

* `Python 3.12.4` instalado (Testado)
* Conta no Azure com acesso à **API do ChatGPT** versão gpt-4o-mini (2024-12-01-preview)
* `pip` para instalar dependências

## Instalação Local

Siga os passos abaixo para rodar a aplicação localmente em sua máquina:

### 1. Clonar o repositório

```bash
git clone https://github.com/GTazz/Furia-chatBot.git
cd Furia-chatBot
```

### 2. Criar um ambiente virtual e instalar dependências

Para evitar conflitos de dependências, é recomendado criar um ambiente virtual com o script de setup fornecido:

```bash
python setup_env.py
source env/bin/activate   # Para Linux/Mac
env\Scripts\activate      # Para Windows
```

### 3. Configurar a API do ChatGPT

Você precisa configurar sua chave de API e Endpoint da Azure. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
CHATGPT_API_KEY=<Sua_Chave_Aqui>
OPENAI_ENDPOINT=<Seu_End_Point>
```

Substitua `<Sua_Chave_Aqui>` pela chave da API obtida no portal da Azure.

Substitua `<Seu_End_Point>` pelo Endpoint obtido no portal da Azure.

### 4. Rodar a aplicação localmente

Com tudo configurado, você pode rodar o servidor Flask localmente:

```bash
python run.py
```

A aplicação estará disponível em `http://127.0.0.1:5000/` por padrão.

## Parte mais relevante da estrutura do Projeto

```
Furia-chatBot/
│
├── run.py                 # Arquivo principal da aplicação Flask
├── requirements.txt       # Dependências do projeto
├── .env                   # Configuração da chave da API e Endpoint (não subir para o GitHub)
└── app/                   # Arquivos que compões a aplicação

```

## Licença

Este projeto está licenciado sobre a seguinte licença: [LICENSE](LICENSE.md)

## Contato

Caso tenha alguma dúvida ou sugestão, entre em contato pelo meu [LinkedIn](https://www.linkedin.com/in/gabriel-tazz) ou [GitHub](https://github.com/GTazz).
