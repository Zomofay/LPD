# Atualizar PATH com as variáveis de ambiente do sistema
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Definir diretório de trabalho
cd "c:\Users\Rhafael\Desktop\Projetos\LPD"

# Executar compressão
& ffmpeg.exe -i assets/tocando.mp4 -vf scale=1280:720 -c:v libx264 -preset medium -crf 28 -c:a aac -b:a 128k assets/tocando_compressed.mp4

# Verificar se deu certo
if ($LASTEXITCODE -eq 0) {
    # Remover arquivo original
    Remove-Item assets/tocando.mp4
    # Renomear arquivo comprimido
    Rename-Item assets/tocando_compressed.mp4 assets/tocando.mp4
    Write-Host "Compressão concluída com sucesso!"
} else {
    Write-Host "Erro na compressão!"
}
