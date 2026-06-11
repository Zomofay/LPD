from moviepy.editor import VideoFileClip
import os

# Caminho do vídeo
video_path = "assets/tocando.mp4"
output_path = "assets/tocando_compressed.mp4"

print(f"Comprimindo vídeo: {video_path}")
print("Isso pode levar alguns minutos...")

# Carregar o vídeo
video = VideoFileClip(video_path)

# Reduzir resolução para 720p e bitrate para reduzir tamanho
# Isso mantém qualidade aceitável enquanto reduz drasticamente o tamanho
video_resized = video.resize(height=720)

# Escrever vídeo comprimido
video_resized.write_videofile(
    output_path,
    codec='libx264',
    audio_codec='aac',
    bitrate="2000k",  # 2Mbps - bom balanço entre qualidade e tamanho
    verbose=False,
    logger=None
)

# Obter tamanhos
size_original = os.path.getsize(video_path) / (1024 * 1024)
size_compressed = os.path.getsize(output_path) / (1024 * 1024)
reduction = ((size_original - size_compressed) / size_original) * 100

print(f"\n✅ Compressão concluída!")
print(f"Tamanho original: {size_original:.2f} MB")
print(f"Tamanho comprimido: {size_compressed:.2f} MB")
print(f"Redução: {reduction:.1f}%")

# Substituir arquivo original
os.remove(video_path)
os.rename(output_path, video_path)
print(f"\n✅ Arquivo original substituído com sucesso!")
