import requests
import time
import wave
import pyaudio
import os

API_KEY_ASSEMBLYAI="4621ab9b854c4d4a9285a31e81c1798f"

# AssemblyAI endpoints
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers = {'authorization': API_KEY_ASSEMBLYAI}

# Upload audio file
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data
    response = requests.post(upload_endpoint, headers=headers, data=read_file(filename))
    audio_url = response.json()['upload_url']
    return audio_url

# Submit transcription request
def transcribe(audio_url):
    response = requests.post(transcript_endpoint, json={'audio_url': audio_url}, headers=headers)
    transcript_id = response.json()['id']
    return transcript_id

# Poll for transcription result
def poll(transcript_id):
    polling_endpoint = f"{transcript_endpoint}/{transcript_id}"
    while True:
        response = requests.get(polling_endpoint, headers=headers)
        data = response.json()
        if data['status'] == 'completed':
            return data['text']
        elif data['status'] == 'error':
            return f"Error: {data['error']}"
        time.sleep(5)

# Record audio chunk from microphone
def record_audio_chunk(filename, record_seconds=18):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print(f"Recording {record_seconds} seconds...")
    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Main real-time loop
def transcription():
    try:
        while True:
            temp_filename = "temp_chunk.wav"
            record_audio_chunk(temp_filename, record_seconds=10)

            audio_url = upload(temp_filename)

            print("Requesting transcription")
            transcript_id = transcribe(audio_url)
            result = poll(transcript_id)
            print(f"Transcription: {result}")

            os.remove(temp_filename)
            print("\n")
            print("press ctrl+c to exit...")

    except KeyboardInterrupt:
        print("\nStopped by user.")


transcription()
