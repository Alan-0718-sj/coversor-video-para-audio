# Conversor de Vídeo para Áudio com Moviepy

Este script Python simples utiliza a biblioteca Moviepy para converter um arquivo de vídeo em um arquivo de áudio MP3.

## Pré-requisitos

*   **Python:** Certifique-se de ter o Python instalado em seu sistema (versão 3.6 ou superior recomendada).
*   **Moviepy:** Instale a biblioteca Moviepy utilizando o pip:

    ```bash
    pip install moviepy
    ```

    **Observação:** A Moviepy depende de outras bibliotecas como `imageio`, `numpy` e `tqdm`.  O `pip` instalará essas dependências automaticamente, mas se você tiver problemas, verifique se elas estão corretamente instaladas.  Em alguns sistemas, pode ser necessário instalar o `imageio-ffmpeg` separadamente:

    ```bash
    pip install imageio_ffmpeg
    ```

## Uso

1.  **Baixe o script:** Salve o código Python fornecido em um arquivo, por exemplo, `video_to_audio.py`.

2.  **Coloque o arquivo de vídeo:** Certifique-se de que o arquivo de vídeo que você deseja converter (neste caso, 'O LIVRO DOS SALMOS CAPÍTULO 61 VERSÍCULO 1 AO 8.mp4') esteja no mesmo diretório que o script `video_to_audio.py`. Se não estiver, você precisará alterar o caminho do arquivo no script.

3.  **Execute o script:** Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o script e execute-o com o comando:

    ```bash
    python video_to_audio.py
    ```

4.  **Verifique o resultado:** Após a execução bem-sucedida, um arquivo de áudio chamado 'livro_salmos_C61_V_1_8.mp3' será criado no mesmo diretório.

## Explicação do Código

*   **`import moviepy.editor`:** Importa a biblioteca Moviepy para edição de vídeo.
*   **`import os`:** Importa o módulo `os` para interagir com o sistema operacional.
*   **`clear()`:**  Função para limpar o terminal/console. Usa `cls` no Windows e `clear` em outros sistemas (Linux, macOS).
*   **`title()`:** Função para exibir um título formatado no terminal.
*   **`video = moviepy.editor.VideoFileClip('O LIVRO DOS SALMOS  CAPÍTULO 61 VERSÍCULO 1 AO 8.mp4')`:** Carrega o arquivo de vídeo especificado.  **Importante:** Certifique-se de que o nome do arquivo corresponda exatamente ao nome do seu arquivo de vídeo.
*   **`audio = video.audio`:** Extrai a faixa de áudio do vídeo.
*   **`audio.write_audiofile('livro_salmos_C61_V_1_8.mp3')`:** Salva a faixa de áudio extraída em um arquivo MP3 com o nome especificado.

## Requisitos

- Python 3.x
- [MoviePy](https://zulko.github.io/moviepy/)  
- [FFmpeg](https://ffmpeg.org/) (necessário para o MoviePy funcionar corretamente)

## Instalação

1. **Clone o repositório (ou baixe o arquivo):**

   ```bash
   git clone https://github.com/Alan-0718-sj/coversor-video-para-audio.git
   cd seurepositorio

## Observações

*   **Nome do arquivo de vídeo:** Adapte o nome do arquivo de vídeo em `VideoFileClip()` para o nome do vídeo que você deseja converter.
*   **Nome do arquivo de áudio:** Você pode alterar o nome do arquivo de áudio de saída em `write_audiofile()`.
*   **Erros:** Se você encontrar erros, verifique se Moviepy e suas dependências estão instaladas corretamente.  Mensagens de erro no terminal podem fornecer pistas sobre o que está errado.
*   **Desempenho:** A conversão pode demorar dependendo do tamanho do arquivo de vídeo e da capacidade do seu computador.
*   **Caminhos:** Para evitar erros, o ideal é colocar o script e o arquivo de vídeo no mesmo diretório, ou especificar o caminho completo para o arquivo de vídeo.

## Licença

Este código é fornecido sem garantia. Você é livre para usar, modificar e distribuir como achar melhor.
