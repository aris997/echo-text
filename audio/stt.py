from globals import *

# This function should stay somewhere else, is needed in a lot of features
def generate_path_file(file_id: str) -> str:
    url = TELEGRAM_GET_PATH
    response = requests.get(url, params = {"file_id": file_id})
    file_path = response.json()["result"]["file_path"]
    return file_path

# this is the same as before
def download_voice_file(file_path: str, saving_path = AUDIO_PATH_FOLDER, file_format: str = ".ogg"):
    url = TELEGRAM_DOWNLOAD + file_path
    response = requests.get(url)
    file_name = utils.now() + file_format
    destination = os.path.join(utils.create_folder(saving_path), file_name)
    # TODO: control how many files are in the folder and delete oldests 
    with open(destination, 'wb') as file:
        file.write(response.content)
    return destination

def speech_to_text_whisper(file_path: str, language_transcription = 'en') -> str:
    print(file_path)
    result = MODEL.transcribe(
        file_path, 
        fp16 = False,
        temperature = 0.0, 
        language = language_transcription,
        # patience = None,
        )

    logger.info(f"speech_to_text_whisper -> testo trascritto: {result['text']}")
    return result['text']

def via_whisper(file_id: str, language_transcription = "en", saving_path = AUDIO_PATH_FOLDER, file_format = ".ogg"):
    logger.debug("whisper started...")
    url = TELEGRAM_GET_PATH
    response = requests.get(url, params = {"file_id": file_id})
    file_path = response.json()["result"]["file_path"]
    url = TELEGRAM_DOWNLOAD + file_path
    response = requests.get(url)

    file_name = "voice_" + utils.now() + file_format
    destination = os.path.join(utils.create_folder(saving_path), file_name)
    with open(destination, 'wb') as file:
        file.write(response.content)

    logger.debug(destination)
    result = MODEL.transcribe(
        # fr"C:\Users\RIVAR\Documents\github\echo-text\{file_path}", 
        destination,
        fp16 = False,
        temperature = 0.0, 
        language = language_transcription,
        # patience = None,
        )

    logger.info(f"speech_to_text_whisper -> testo trascritto: {result['text']}")
    return result['text']