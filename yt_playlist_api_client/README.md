# Automação em Python com YouTube Data API v3

<p align="center">
  <img src="https://img.shields.io/badge/Status-concluído-brightgreen" />

  <img src="https://img.shields.io/badge/Linguagem-Python-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/API-Google%20YouTube-red" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/Plataforma-Terminal-lightgrey" />
</p>


Este projeto em Python tem como objetivo **coletar informações detalhadas dos vídeos de uma playlist do YouTube**, utilizando a [YouTube Data API v3](https://developers.google.com/youtube/v3). Ele é voltado para **automação de tarefas de análise de conteúdo** e pode ser facilmente adaptado para projetos de monitoramento de canais, relatórios de engajamento, ou extração de dados.

## 🔍 O que este script faz

- Realiza a autenticação OAuth2 com a conta Google do usuário
- Coleta os vídeos de uma playlist específica do YouTube
- Para cada vídeo, obtém:
  - Título
  - Data de publicação
  - Link direto
  - Número de visualizações
- Apresenta os dados em formato legível no terminal (ver arquivo [saida.txt](https://github.com/ahaerdy/python-scripts/blob/main/youtube_scrapper/saida.txt))

---

## 📁 Estrutura do Projeto

```
yt_playlist_api_client.py  # Script principal
saida.txt                  # Arquivo de saída (formatos de dicionário Python e textual)
secrets.json               # Credenciais OAuth2 geradas no Google Cloud Console (não disponibilizado)
README.md                  # Documentação explicativa
```

---

## Entendendo o Código

### Função `main()`

Responsável por coordenar o fluxo principal da aplicação:

1. **Configuração de ambiente**:
   ```python
   os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
   ```
   Permite que a autenticação OAuth2 funcione em localhost sem HTTPS.

2. **Autenticação via OAuth2**:
   ```python
   flow = InstalledAppFlow.from_client_secrets_file(...)
   credentials = flow.run_local_server(port=0)
   ```
   Isso abre uma janela no navegador para autenticar com a conta Google do usuário.

3. **Inicialização do cliente da API do YouTube**:
   ```python
   youtube = googleapiclient.discovery.build(...)
   ```

4. **Requisição dos vídeos da playlist**:
   ```python
   youtube.playlistItems().list(...).execute()
   ```

5. **Impressão dos dados formatados**:
   ```python
   imprimir_resposta_playlist(youtube, response)
   ```

---

## 🔧 Requisição principal (request)

```python
request = youtube.playlistItems().list(
    part="contentDetails",
    maxResults=25,
    playlistId="PLpdAy0tYrnKyjl4SSIkt0l6DFzMVmtfLd"
)
response = request.execute()
```

- A requisição pede os detalhes básicos de até 25 vídeos da playlist.
- O resultado vem em forma de **dicionário Python**.

### Exemplo real de resposta recebida (`response`):
```python
{
  'kind': 'youtube#playlistItemListResponse',
  'etag': 'Q96Z63zqpSC08XFtB-QLLWgAh_c',
  'items': [
    {
      'kind': 'youtube#playlistItem',
      'etag': '6OtmbGMF8SOcLB4n30-4uLLCz24',
      'id': 'UExwZE...',
      'contentDetails': {
        'videoId': 'NRFZFXT1JvM',
        'videoPublishedAt': '2025-01-07T20:00:10Z'
      }
    },
    ...
  ],
  'pageInfo': {
    'totalResults': 10,
    'resultsPerPage': 25
  }
}
```

---

## 📄 Estrutura da Resposta da API `playlistItems().list()`

### Campos principais:

| Campo                        | Significado                                                                 |
|-----------------------------|------------------------------------------------------------------------------|
| `kind`                      | Tipo geral da resposta da API (`playlistItemListResponse`)                  |
| `etag`                      | Identificador de cache da resposta                                          |
| `items`                     | Lista de itens da playlist (vídeos)                                         |
| `items[].id`                | ID interno do item na playlist                                              |
| `items[].contentDetails.videoId` | ID do vídeo propriamente dito (pode ser usado para buscar título, views etc.) |
| `items[].contentDetails.videoPublishedAt` | Data de publicação original do vídeo                                 |
| `pageInfo.totalResults`     | Total de vídeos retornados (nesta chamada)                                  |
| `pageInfo.resultsPerPage`   | Máximo de vídeos por página (nesta chamada)                                 |

Cada item representa um vídeo da playlist, mas para obter mais dados (como título e estatísticas), fazemos uma segunda requisição para `videos().list()`.

---

## 🔁 Requisição complementar: título e visualizações

```python
video_response = youtube.videos().list(
    part="snippet,statistics",
    id=video_id
).execute()
```

- **`snippet.title`** → título do vídeo
- **`statistics.viewCount`** → número de visualizações

---

## ✅ Requisitos

- Python 3.7+
- Bibliotecas:
  - `google-auth-oauthlib`
  - `google-api-python-client`

Instale com:

```bash
pip install --upgrade google-auth google-auth-oauthlib google-api-python-client
```

---

## 🔐 Como gerar o `secrets.json`

1. Vá ao [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto
3. Ative a API "YouTube Data API v3"
4. Crie uma credencial OAuth para aplicativo de área de trabalho
5. Baixe o JSON e renomeie para `secrets.json`

---

## 🧑‍💻 Autor

Este projeto faz parte do meu acervo pessoal de scripts Python. Ele demonstra a capacidade de trabalhar com APIs REST, autenticação OAuth2 e processamento de dados estruturados com clareza e legibilidade.

---

## 📜 Licença

MIT License