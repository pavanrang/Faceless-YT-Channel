import os
import soundfile
import re
from llm import *
from links import *
from video import *
from vtt_to_srt.vtt_to_srt import ConvertFile

# Define the topic for the video
topic = "Traveling to Korea"

# Generate the script for the video based on the topic
text = script.generate_video_script(topic)
print("Script written!")

# Get search terms based on the topic and generated text, `n` specifies the number of terms
n = 2
search_terms = tags.get_search_terms(topic, n, text)
search_term = eval(search_terms)

# Search for stock videos using the search terms
video_links = links.search_for_stock_videos(search_term)
print("Research done!")

# Save the found video links to the specified directory
video_paths = save.save_video(video_links, "./videos")

# Clean up the generated text for text-to-speech conversion
a = re.sub(r"\s+", " ", text)
a = a[1:-1]

# Generate the audio file and subtitle file from the text
audio_file, subtitle_file = tts.text_to_speech(a)
print("Dubbing Done!")

# Get information about the audio file to determine its duration
info = soundfile.info(audio_file)
duration = info.duration

# Combine the video clips to match the duration of the audio
cvp = merge.combine_videos(video_paths, duration)
print("Initial edit Done!")

# Convert the subtitle file from VTT to SRT format
convert_file = ConvertFile("output.vtt", "utf-8")
convert_file.convert()

# Generate the final edited video with the combined video, audio, and subtitles
final_edit.generate_video(cvp, audio_file, 'output.srt')
print("Final Edit Done!!")
