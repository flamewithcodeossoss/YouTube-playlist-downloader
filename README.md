# 🎬 YouTube Playlist Downloader

A robust Python script to download entire YouTube playlists in **best quality** and save them as `.mp4` files. Built with `yt-dlp` for reliable and fast downloads.

## ✨ Features

- 📥 **Download entire playlists** with a single command
- 🎯 **Best quality** video and audio combination
- 📁 **Automatic folder creation** with fallback options
- 🔄 **Retry mechanism** for failed downloads
- 📊 **Progress tracking** with completion notifications
- 🛡️ **Error handling** with user-friendly messages
- 🎬 **MP4 output format** for universal compatibility

## 📋 Prerequisites

- Python 3.7 or higher
- Windows, macOS, or Linux
- Internet connection
- (Optional) FFmpeg for enhanced video processing

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Your Settings

Edit `downloader.py` and update:
- **Playlist URL**: Replace with your YouTube playlist link
- **Output folder**: (Optional) Change if you want a specific location

### 3. Run the Downloader

```bash
python downloader.py
```

## ⚙️ Configuration

### Playlist URL
Replace the default playlist URL in `downloader.py`:
```python
playlist_url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

### Output Location
The script automatically creates a `YouTubeDownloads` folder in your current directory. If there are permission issues, it falls back to your Downloads folder.

### Advanced Options
You can modify the download options in `ydl_opts`:
- **Quality**: Change `format` setting
- **Retries**: Adjust `retries` and `fragment_retries`
- **Output template**: Customize file naming with `outtmpl`

## 🛠️ FFmpeg Installation (Optional)

FFmpeg enhances video processing but is not required. To install:

### Windows
1. Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract to `C:\ffmpeg\`
3. Add to PATH:
   - Win+R → `sysdm.cpl` → Enter
   - Advanced tab → Environment Variables
   - Add to PATH: `C:\ffmpeg\bin`

### macOS
```bash
brew install ffmpeg
```

### Linux
```bash
sudo apt install ffmpeg  # Ubuntu/Debian
sudo yum install ffmpeg  # CentOS/RHEL
```

## 📁 Output Structure

Downloaded videos are saved with this naming pattern:
```
YouTubeDownloads/
├── 01 - Video Title 1.mp4
├── 02 - Video Title 2.mp4
├── 03 - Video Title 3.mp4
└── ...
```

## 🐛 Troubleshooting

### Permission Denied
- The script automatically tries alternative locations
- Check that you have write permissions in the target folder
- Run as administrator if necessary

### Download Failures
- Check your internet connection
- Verify the playlist URL is correct and public
- Ensure YouTube is accessible in your region

### FFmpeg Issues
- The script works without FFmpeg but quality may be limited
- Install FFmpeg for best results
- Check the ffmpeg path in the script if manually installed

### Slow Downloads
- Try different times of day
- Check if your ISP throttles YouTube
- Consider using a VPN if geo-restricted

## 🔧 Customization Examples

### Download Single Video
```python
playlist_url = "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Change Quality
```python
"format": "worst"  # For smaller files
"format": "best[height<=720]"  # For 720p max
```

### Custom Output Template
```python
"outtmpl": output_folder + "/%(uploader)s - %(title)s.%(ext)s"
```

## 📚 Learn More

- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [YouTube Playlist Format](https://support.google.com/youtube/answer/7544833)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this downloader!

## ⚖️ Legal Notice

This tool is for educational purposes. Respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.bash
python downloader.py
