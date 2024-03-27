from globals import *
from audio import audio_utilities

app = FastAPI()

@app.get("/")
async def health(request: Request):
    response={"status":"ok"}
    LOG.debug(f"GET request {response = }")
    return response

@app.post("/webhook")
async def messager(request: Request):

    payload = await request.json()
    chat_id = payload.get("message", {}).get("chat", {}).get("id", 0)
    message_type = [key for key in payload.get("message", {}).keys() if key not in UNUSEFUL_KEYS]
    LOG.debug(f"{message_type = }")

    if "text" in message_type:
        user_message = payload.get("message", {}).get("text", "")
        LOG.debug(user_message)
        bot_message = user_message

    elif "voice" in message_type:
        LOG.debug(f"is audio message")
        audio_transcription = audio_utilities.speech_to_text_whisper(
            audio_utilities.download_voice_file(
                audio_utilities.generate_path_file(
                    payload.get("message", {}).get("voice", {}).get("file_id", "")
                )
            ),
            language_transcription = "it"
        )
        bot_message = audio_transcription

    else:
        with open(
            os.path.join(
                "samples", 
                "temp", 
                f"""{message_type[0]}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json"""), 
                'w') as file_path:
            LOG.debug(message_type, file_path)
            json.dump(payload, file_path, indent = 4, sort_keys = True)
        bot_message = "something went wrong. Let me die.\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    
    message = {
        "chat_id" : chat_id,
        "text" : bot_message
        }
    response = requests.post(API_TELEGRAM["send_message"], json = message)
    return response.json()



if __name__ == "__main__":
    pass