from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def check_installation():
    try:
        # Cek versi yt-dlp
        ytdlp_version = subprocess.check_output(["yt-dlp", "--version"]).decode().strip()

        # Cek versi ffmpeg
        ffmpeg_version = subprocess.check_output(["ffmpeg", "-version"]).decode().split('\n')[0]

        return jsonify({
            "yt-dlp": f"Terinstal (Versi: {ytdlp_version})",
            "ffmpeg": f"Terinstal (Versi: {ffmpeg_version})"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
