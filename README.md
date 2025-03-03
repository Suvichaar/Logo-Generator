# Video Watermarking Tool

This project is a Streamlit-based web application that allows users to upload a video and a logo, apply the logo as a watermark on the video, and download the processed video.

## Features
- Upload video files in `.mp4`, `.avi`, or `.mov` format
- Upload logo images in `.png`, `.jpg`, or `.jpeg` format
- Choose watermark position: `top-left`, `top-right`, `bottom-left`, `bottom-right`, or `center`
- Adjust logo scale factor between 0.05 and 0.5
- Download the processed video with the logo watermark applied

## Prerequisites
- Python 3.x
- FFmpeg installed on your system
- Streamlit library installed

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/video-watermarking-tool.git
   cd video-watermarking-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - For Windows: Download and install from [FFmpeg Website](https://ffmpeg.org/download.html)
   - For Linux/Mac: Install via package manager
   ```bash
   sudo apt-get install ffmpeg   # For Ubuntu/Debian
   brew install ffmpeg          # For macOS
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Upload your video and logo files through the interface.
3. Select the desired logo position and scale factor.
4. Click the **Add Logo** button.
5. Download the processed video once completed.

## Directory Structure
```
├── app.py               # Main Streamlit app file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Dependencies
- streamlit
- ffmpeg
- subprocess

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Author
Kumar Mayank

