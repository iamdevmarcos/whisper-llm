# TalkingLLM

TalkingLLM is a project that integrates voice recognition, transcription, and audio generation with an OpenAI language model. It uses the Whisper model for audio transcription and ChatOpenAI for interacting with a language model. The system also includes functionality for audio recording, text processing, and generated audio playback.

## Features

- **Recording and Transcription**: Records audio, saves it as a WAV file, and transcribes it using the Whisper model.
- **Processing and Response**: Uses a language model to process the transcribed text and generate responses.
- **Audio Playback**: Converts responses to audio and plays it using `sounddevice`.
- **User Interface**: Starts and stops recording using a keyboard shortcut.

## Dependencies

Ensure you have Python 3.8 or higher installed. You can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### `requirements.txt` File

The project uses the following dependencies:

```
aiohttp==3.9.5
aiosignal==1.3.1
annotated-types==0.6.0
anyio==4.3.0
attrs==23.2.0
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
dataclasses-json==0.6.4
distro==1.9.0
filelock==3.13.4
frozenlist==1.4.1
fsspec==2024.3.1
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
idna==3.7
Jinja2==3.1.3
jsonpatch==1.33
jsonpointer==2.4
langchain==0.1.16
langchain-community==0.0.33
langchain-core==0.1.43
langchain-experimental==0.0.57
langchain-openai==0.1.3
langchain-text-splitters==0.0.1
langsmith==0.1.48
llvmlite==0.42.0
MarkupSafe==2.1.5
marshmallow==3.21.1
more-itertools==10.2.0
mpmath==1.3.0
multidict==6.0.5
mypy-extensions==1.0.0
networkx==3.3
numba==0.59.1
numpy==1.26.4
openai==1.20.0
openai-whisper @ git+https://github.com/openai/whisper.git@ba3f3cd54b0e5b8ce1ab3de13e32122d0d5f98ab
orjson==3.10.1
packaging==23.2
pandas==2.2.2
playsound==1.3.0
pycparser==2.22
pydantic==2.7.0
pydantic_core==2.18.1
pynput==1.7.6
pyobjc-core==10.2
pyobjc-framework-ApplicationServices==10.2
pyobjc-framework-Cocoa==10.2
pyobjc-framework-CoreText==10.2
pyobjc-framework-Quartz==10.2
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.1
PyYAML==6.0.1
regex==2024.4.16
requests==2.31.0
setuptools==69.5.1
six==1.16.0
sniffio==1.3.1
sounddevice==0.4.6
soundfile==0.12.1
SQLAlchemy==2.0.29
sympy==1.12
tabulate==0.9.0
tenacity==8.2.3
tiktoken==0.6.0
torch==2.2.2
tqdm==4.66.2
typing-inspect==0.9.0
typing_extensions==4.11.0
tzdata==2024.1
urllib3==2.2.1
wheel==0.43.0
yarl==1.9.4
```

## Setup

1. **Create a `.env` File**: This file should contain necessary environment variables such as your OpenAI API key.

2. **Prepare the Data File**: Place the `df_rent.csv` file in the same directory as the script.

## Usage

1. **Run the Script**:

   ```bash
   python talking_llm.py
   ```

2. **Record Audio**: Press the defined keyboard shortcut (`<cmd>`) to start and stop recording. The audio will be saved and processed automatically.
