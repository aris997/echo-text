from globals import *
from audio import stt
from actions import generate_response

app = FastAPI()

@app.get("/")
async def health(request: Request):
    response={"status":"ok"}
    logger.debug(f"GET request {response = }")
    return response

@app.post("/webhook")
async def messager(request: Request):

    payload = await request.json()
    chat_id = payload.get("message", {}).get("chat", {}).get("id", 0)
    print(payload, "="*100)
    message_type = [key for key in payload.get("message", {}).keys() if key not in UNUSEFUL_KEYS]
    logger.debug(f"{message_type = }")

    if "text" in message_type:
        # tutto tuo ennio
        user_message = payload.get("message", {}).get("text", "")
        logger.debug(user_message)
        bot_message = user_message
        bot_message = generate_response.answer(user_message)
        # chiamata a clode

    elif "voice" in message_type and False:
        logger.debug(f"is audio message")
        audio_transcription = stt.via_whisper(
            payload.get("message", {}).get("voice", {}).get("file_id", ""),
            language_transcription = "it")
        bot_message = audio_transcription

    else:
        with open(os.path.join(TEMP_PATH, f"""{message_type[0]}_{utils.now()}.json"""), 'w') as file_path:
            logger.debug(f"{message_type}")
            json.dump(payload, file_path, indent = 4, sort_keys = True)
        bot_message = "something went wrong. Let me die.\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    
    message = {
        "chat_id" : chat_id,
        "text" : bot_message
        }
    response = requests.post(TELEGRAM_SEND_MESSAGE, json = message)
    logger.debug(response)
    return response.json()



if __name__ == "__main__":
        import uvicorn 

        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)