import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import whisper
import tempfile
import os
import language_tool_python
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='whisper')
tool = language_tool_python.LanguageTool('en-US')

duration = 10 
samplerate = 16000 
model_size = "base" 

# Load Whisper model
model = whisper.load_model(model_size)

def transcribe():
    print("Press Ctrl+C to stop...")

    try:
        while True:
            print("\nRecording",duration,"seconds...")
            audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
            sd.wait()

            # Save to a temporary WAV file
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
                wavfile.write(tmpfile.name, samplerate, audio)
                temp_filename = tmpfile.name

            # Transcribe 
            print("Transcribing...")
            result = model.transcribe(temp_filename)
            corrected_transcript = grammar_correction(result['text'])
            print("Transcription:", corrected_transcript)
            print("Press Ctrl+C to stop...")


            # deleting temp file
            os.remove(temp_filename)

    except KeyboardInterrupt:
        print("\nStopped by user.")


def grammar_correction(text):
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return corrected


transcribe()
