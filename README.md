# Automatic Speech Recognition with Grammar Correction

This project captures live audio using a microphone, transcribes it using [OpenAI's Whisper ASR model](https://github.com/openai/whisper), and corrects grammar mistakes using [LanguageTool](https://github.com/jxmorris12/language-tool-python). It's ideal for speech-to-text transcription with real-time grammar improvement.

---

## 🚀 Features

- Real-time microphone audio recording
- Speech recognition using OpenAI Whisper
- Automatic grammar correction using LanguageTool
- Temporary file handling with cleanup
- Simple and modular Python implementation

## ⚙️ Requirements
- Python 3.8+
- OpenAI Whisper (pip install -U openai-whisper)
- sounddevice
- scipy
- numpy
- language_tool_python
- pyaudio (for AssemblyAI)
- requests (for AssemblyAI)
### Install all dependencies:
```bash
pip install -r requirements.txt
```
## 🖥️ How to Run
Clone the repo
```bash
git clone https://github.com/ShrutiGupta37/Automatic-Speech-Recognition.git
```
Whisper (Offline) ASR
```bash
python ASR_whisper.py
```
- Records 10 seconds of audio
- Transcribes using Whisper
- Corrects grammar using LanguageTool

AssemblyAI (Cloud) ASR
1. Set your AssemblyAI API key in the script
2. Then run:
```bash
python ASR_assemblyAI.py
```
- Uploads audio to AssemblyAI
- Polls transcription status
- Returns and displays the result
## 📊 Comparison
| Feature              | Whisper (Local)          | AssemblyAI (Cloud)      |
| -------------------- | ------------------------ | ----------------------- |
| Deployment           | Offline                  | Cloud-based             |
| Accent Adaptation    | Requires fine-tuning     | Built-in support        |
| Internet Requirement | ❌                        | ✅                       |
| Transcript Accuracy  | High (with large models) | Very High               |
| Grammar Correction   | ✅                        | ❌ (manual post-process) |
| Privacy              | ✅                        | ❌ (data sent to cloud)  |
| Cost                 | Free                     | Paid (Free Tier)        |

## 📈 Future Improvements
- Add live streaming support
- Use Mozilla Common Voice for dialect training
- Build a GUI with Streamlit or Flask
- Integrate noise reduction filters
- NLP-based context correction
