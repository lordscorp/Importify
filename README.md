# Importify

Este é um projeto Python simples que importa um arquivo CSV e cria uma playlist no Spotify.

## 🚀 Começando

Estas instruções permitirão que você obtenha uma cópia do projeto em funcionamento na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

O que você precisa para instalar o software e como instalá-lo:

- Python 3.6 ou superior
- Biblioteca Spotipy para Python

### 🔧 Instalação

1. Clone este repositório para a sua máquina local.
2. Instale as dependências necessárias com o comando `pip install -r requirements.txt`.
3. Renomeie o arquivo `.env_example` para `.env`.
4. Substitua `SPOTIPY_CLIENT_ID` e `SPOTIPY_CLIENT_SECRET` no arquivo `.env` com suas credenciais do Spotify Developer Dashboard.
5. Crie um arquivo `my_lib.csv` com uma faixa por linha, contendo o nome da música e o artista.

## 🎈 Uso

Execute o script Python principal para criar a playlist no Spotify com as faixas do arquivo `my_lib.csv`. Por padrão, o nome da playlist é "Favoritas". Se você quiser alterar isso, modifique diretamente o trecho de criação da playlist no script.
