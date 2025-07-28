from moviepy.editor import ImageClip, concatenate_videoclips, TextClip, CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def create_video(image_path, audio_path, output_path, text=""):
    # تحميل الصورة
    img_clip = ImageClip(image_path, duration=10)  # مدة الفيديو 10 ثوانٍ

    # تحميل الصوت
    audio_clip = AudioFileClip(audio_path)
    img_clip = img_clip.set_audio(audio_clip)

    # إضافة نص (اختياري)
    if text:
        txt_clip = TextClip(text, fontsize=70, color='white', size=img_clip.size)
        txt_clip = txt_clip.set_duration(10).set_position('center')
        final_clip = CompositeVideoClip([img_clip, txt_clip])
    else:
        final_clip = img_clip

    # حفظ الفيديو
    final_clip.write_videofile(output_path, codec="libx264", fps=24)
    final_clip.close()

# مثال الاستخدام
create_video("assets/images/sample.jpg", "assets/audio/output.mp3", "assets/videos/output_video.mp4", text="مرحبًا بكم!")
