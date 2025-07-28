from gtts import gTTS
import os

def create_audio(text, output_path, lang="ar"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)

# مثال الاستخدام
create_audio("مرحبًا، هذا فيديو تم إنشاؤه تلقائيًا!", "assets/audio/output.mp3")
