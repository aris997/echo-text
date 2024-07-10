FROM python:3.12

USER root

# Update and install ffmpeg (dependencies of openai-whisper)
RUN apt-get update -y

RUN apt-get install -y ffmpeg

WORKDIR /app

COPY . .

# Install requirements by hand

RUN pip3 install fastapi PyYAML Requests uvicorn

RUN pip3 install langchain_cohere

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip3 install openai

RUN pip3 install openai-whisper==20231117

RUN pip install numpy==1.26.4

# RUN pip install -r requirements.txt

CMD ["python", "main.py"]