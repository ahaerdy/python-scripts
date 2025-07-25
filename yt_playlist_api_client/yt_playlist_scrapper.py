# -*- coding: utf-8 -*-

import os
import shutil
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Obter largura do terminal (colunas)
largura = shutil.get_terminal_size(fallback=(80, 20)).columns

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def imprimir_resposta_playlist(youtube, response):
    print("🔍 Resultado da Playlist:")
    print(f"Total de vídeos retornados: {len(response.get('items', []))}")
    print("=" * largura)

    for idx, item in enumerate(response.get('items', []), start=1):
        kind = item.get('kind', 'N/A')
        etag = item.get('etag', 'N/A')
        playlist_item_id = item.get('id', 'N/A')
        content = item.get('contentDetails', {})

        video_id = content.get('videoId', 'N/A')
        publicado_em = content.get('videoPublishedAt', 'N/A')
        link = f"https://www.youtube.com/watch?v={video_id}" if video_id != 'N/A' else 'N/A'

        # Segunda requisição: buscar snippet (título) e estatísticas
        video_response = youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        ).execute()

        
        if not video_response["items"]:
            titulo = "Vídeo não encontrado ou privado"
            views = "N/A"
        else:
            video_data = video_response["items"][0]
            titulo = video_data["snippet"]["title"]
            views = video_data["statistics"].get("viewCount", "0")

        print(f"📹 Vídeo {idx}:")
        print(f"  • Título: {titulo}")
        print(f"  • Tipo do item: {kind}")
        print(f"  • ETag: {etag}")
        print(f"  • ID do item na playlist: {playlist_item_id}")
        print(f"  • ID do vídeo: {video_id}")
        print(f"  • Publicado em: {publicado_em}")
        print(f"  • Link: {link}")
        print(f"  • Visualizações: {views}")
        print("-" * largura)

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secrets.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # executar
    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=25,
        playlistId="PLpdAy0tYrnKyjl4SSIkt0l6DFzMVmtfLd"
    )
    response = request.execute()

    print("\nDicionário Python contendo os dados dos vídeos da playlist:\n")
    print('-' * largura)
    print(f"{response}")
    print('-' * largura)
    print("\nInformações em formato legível:\n")

    # Agora passa o cliente youtube e a resposta para a função:
    imprimir_resposta_playlist(youtube, response)

if __name__ == "__main__":
    main()
