import os
import requests

def save_video(video_urls: list, directory: str = "./temp") :
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    video_paths = []
    for video_id, video_url in enumerate(video_urls):
        video_path = f"{directory}/{video_id+1}.mp4"
        with open(video_path, "wb") as f:
            f.write(requests.get(video_url).content)
        video_paths.append(video_path)
    
    return video_paths