from pydub import AudioSegment
from pydub.effects import speedup

def modulate_emotions(input_path):
    sound = AudioSegment.from_file(input_path)

    emotions = ["happy", "sad", "angry", "funny", "excited"]

    for emotion in emotions:
        modified_sound = sound
        if emotion == "happy":
            modified_sound = sound.speedup(playback_speed=1.5)
        elif emotion == "sad":
            modified_sound = sound.speedup(playback_speed=0.8)
        elif emotion == "angry":
            modified_sound = sound - 10
            modified_sound = modified_sound.speedup(playback_speed=1.2)
        elif emotion == "funny":
            modified_sound = sound + sound._spawn(sound.raw_data * 2)
        elif emotion == "excited":
            modified_sound = sound + 10
            modified_sound = modified_sound.speedup(playback_speed=1.4)

        output_path = f"{emotion}_modulation.wav"
        modified_sound.export(output_path, format="wav")
        print(f"{emotion} emotion saved to {output_path}")



input_file_path = "Recording.wav"

modulate_emotions(input_file_path)

for emotion in ["happy", "sad", "angry", "funny", "excited"]:
    output_file = f"{emotion}_modulation.wav"
    print(f"{emotion} emotion saved to {output_file}")
