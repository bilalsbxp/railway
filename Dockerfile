FROM python:3.12-slim

# Instalasi yt-dlp dan ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install yt-dlp flask

# Salin file ke dalam container
WORKDIR /app
COPY . .

# Jalankan aplikasi
CMD ["python", "app.py"]
