import streamlit as st
import subprocess
import os

def add_logo_to_video(video_path, logo_path, output_path, position="bottom-left", scale_factor=0.08):
    positions = {
        "top-left": "10:10",
        "top-right": "W-w-10:10",
        "bottom-left": "10:H-h-10",
        "bottom-right": "W-w-10:H-h-10",
        "center": "(W-w)/2:(H-h)/2"
    }
    
    command = [
        "ffmpeg",
        "-i", video_path,
        "-i", logo_path,
        "-filter_complex", f"[1:v]scale=iw*{scale_factor}:-1[logo];[0:v][logo]overlay={positions.get(position, '10:H-h-10')}",
        "-c:a", "copy",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        return f"Logo added successfully! Saved as {output_path}"
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

st.title("Video Watermarking Tool")
st.write("Upload a video and logo to add watermark")

video_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"])
logo_file = st.file_uploader("Upload Logo", type=["png", "jpg", "jpeg"])
position = st.selectbox("Select Logo Position", ["top-left", "top-right", "bottom-left", "bottom-right", "center"])
scale = st.slider("Logo Scale Factor", min_value=0.05, max_value=0.5, value=0.08, step=0.01)

if st.button("Add Logo"):
    if video_file and logo_file:
        video_path = video_file.name
        logo_path = logo_file.name
        output_path = f"output_{video_path}"
        
        # Save uploaded files
        with open(video_path, "wb") as f:
            f.write(video_file.read())
        with open(logo_path, "wb") as f:
            f.write(logo_file.read())
        
        result = add_logo_to_video(video_path, logo_path, output_path, position, scale)
        st.success(result)
        
        if os.path.exists(output_path):
            with open(output_path, "rb") as f:
                st.download_button("Download Video", f, file_name=output_path)

    else:
        st.error("Please upload both video and logo files.")
