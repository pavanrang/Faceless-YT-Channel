from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.all import crop

def combine_videos(video_paths, max_duration):
    combined_video_path = "result.mp4"
    clips = []
    for video_path in video_paths:
        clip = VideoFileClip(video_path)
        clip = clip.without_audio()       
        clip = clip.subclip(0, max_duration / len(video_path))
        clip = clip.set_fps(30)

        # Not all videos are same size,
        # so we need to resize them
        clip = crop(clip, width=1080, height=1920, \
                    x_center=clip.w / 2, \
                        y_center=clip.h / 2)
        clip = clip.resize((1080, 1920))

        clips.append(clip)

    final_clip = concatenate_videoclips(clips)
    final_clip = final_clip.set_fps(30)
    final_clip.write_videofile(combined_video_path, threads=3)

    return combined_video_path

