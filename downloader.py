import yt_dlp
import os

# === Settings ===
output_folder = r"F:\mini-rag\downloads"  # Replace with your desired output folder
playlist_url = "https://www.youtube.com/playlist?list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj"  # Replace with your playlist URL

# Ensure folder exists
os.makedirs(output_folder, exist_ok=True)

# === yt-dlp options ===
ydl_opts = {
    "ffmpeg_location": r"C:/ffmpeg/ffmpeg-2025-09-25-git-9970dc32bf-essentials_build/bin",
    "format": "bestvideo+bestaudio/best",   # Best available quality
    "merge_output_format": "mp4",           # Always output mp4
    "outtmpl": output_folder + "/%(playlist_index)02d - %(title).80s.%(ext)s",
    "progress_hooks": [
        lambda d: print(f"\n✅ Finished: {d['filename']}") if d["status"] == "finished" else None
    ],
    "retries": 10,
    "fragment_retries": 10,
}

# === Run downloader ===
if __name__ == "__main__":
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
