from flask import Flask
import subprocess

app = Flask(__name__)

# Perintah instalasi ffmpeg
def install_ffmpeg():
    try:
        subprocess.run(["apt-get", "update"], check=True)
        subprocess.run(["apt-get", "install", "-y", "ffmpeg"], check=True)
        return "ffmpeg berhasil di install"
    except subprocess.CalledProcessError as e:
        return f"Gagal menginstal ffmpeg: {e}"

@app.route('/')
def home():
    return install_ffmpeg()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
