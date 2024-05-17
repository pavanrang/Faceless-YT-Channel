from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def generate_video(combined_video_path, tts_path, subtitles_path, output_file_name: str = "main_output.mp4"):
    generator = lambda txt: TextClip(txt, font=fr"MoneyPrinter\fonts\bold_font.ttf", fontsize=100, color="#FFFF00",
    stroke_color="black", stroke_width=5)

    # Burn the subtitles into the video
    subtitles = SubtitlesClip(subtitles_path, generator)
    result = CompositeVideoClip([
        VideoFileClip(combined_video_path),
        subtitles.set_pos(("center", "center"))
    ])

    # Add the audio
    audio = AudioFileClip(tts_path)
    result = result.set_audio(audio)

    result.write_videofile("output.mp4", threads=3)

    return output_file_name

# generate_video("result.mp4" ,"output.mp3", "output.srt" )