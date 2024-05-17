import os
import soundfile
import re
from llm import script 
from llm import tags
from links import links
from links import save
from video import tts
from video import merge
from video import final_edit

topic = "Traveling to korea"
text = script.generate_video_script(topic)
n=2
# print(text)
print("Script written!")

search_terms = tags.get_search_terms(topic, n, text)
# print(search_terms)
search_term = eval(search_terms)

video_links = links.search_for_stock_videos(search_term)
# print(video_links)
print("Research done!")

video_paths = save.save_video(video_links, "./videos")
# print(video_paths)

a = re.sub(r"\s+", " ", text)
a=a[1:-1]
audio_file, subtitle_file = tts.text_to_speech(a)
print("Dubbing Done!")
info = soundfile.info(audio_file)
duration = info.duration

cvp = merge.combine_videos(video_paths,duration)

print("Intial edit Done!")

final_edit.generate_video(cvp, audio_file, 'output.srt')

print("Final Edit Done!!")