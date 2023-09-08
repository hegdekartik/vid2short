import os
import whisper
from whisper.utils import get_writer
import yt_dlp as youtube_dl

from download_ytvid_as_mp3 import *

# Extracting audio(.mp3) from the youtube link

video_url = 'https://www.youtube.com/watch?v=NHopJHSlVo4'
audio_extract_folder = 'audio files/'
audio_file_path = download_ytvid_as_mp3(video_url,audio_extract_folder)
    

# Audio file transcription
model = whisper.load_model("base")
audio = audio_file_path
result = model.transcribe(audio)

# Saving the transcribed files
output_transcribed_dir_srt = "./transcribed srt files"
output_transcribed_dir_txt = "./transcribed text files"

output_transcribed_path = output_transcribed_dir_txt + '/' + audio_file_path.split('.mp3')[0] + '.txt'

# Save as a TXT file without any line breaks
with open(output_transcribed_path, "w", encoding="utf-8") as txt:
    txt.write(result["text"])


# Save as an SRT file
srt_writer = get_writer("srt", output_transcribed_dir_srt)
srt_writer(result, audio)


# Save as a VTT file
#vtt_writer = get_writer("vtt", output_directory)
#vtt_writer(result, audio)




