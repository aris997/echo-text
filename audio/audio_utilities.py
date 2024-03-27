from globals import *

def generate_path_file(file_id: str) -> str:
    url = API_TELEGRAM.get('get_path')
    response = requests.get(url, params = {"file_id": file_id})
    file_path = response.json()["result"]["file_path"]
    return file_path


def download_voice_file(file_path: str, saving_path = AUDIO_PATH_FOLDER, file_format: str = ".ogg"):
    url = API_TELEGRAM.get('download') + file_path
    response = requests.get(url)
    file_name = datetime.now().strftime("voice_%Y%m%d_%H%M%S") + file_format
    destination = os.path.join(saving_path, file_name)
    with open(destination, 'wb') as file:
        file.write(response.content)
    return destination

def speech_to_text_whisper(file_path: str, language_transcription = 'en') -> str:
    result = MODEL.transcribe(
        file_path, 
        fp16 = False,
        temperature = 0.0, 
        language = language_transcription,
        # patience = None,
        )

    LOG.info(f"speech_to_text_whisper -> testo trascritto: {result['text']}")
    return result['text']