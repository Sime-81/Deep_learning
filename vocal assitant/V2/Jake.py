import asyncio
import re
import boto3
import whisper
import pydub.playback
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle

# Variable de reconnaissance vocale
recognizer = sr.Recognizer()
BING_WAKE_WORD = "jack"

def get_wake_word(phrase):
    if BING_WAKE_WORD in phrase.lower():
        return BING_WAKE_WORD
    else:
        return None

def synthesize_speech(text, output_filename):
    polly = boto3.client('polly', region_name='eu-west-3')
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId='Rémi',
        Engine='neural'
    )

    with open(output_filename, "wb") as f:
        f.write(response['AudioStream'].read())

def play_audio(file):
    sound = pydub.AudioSegment.from_file(file, format='mp3')
    pydub.playback.play(sound)

async def main():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print(f"En attente du mot d'activation 'Ok Jake' ...")
            while True:
                audio = recognizer.listen(source)
                try:
                    with open("audio.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                    # Utilisez le modèle "tiny" préchargé
                    model = whisper.load_model("tiny")
                    result = model.transcribe("audio.wav", fp16=False)
                    phrase = result["text"]
                    print(f"Vous avez dit : \n{phrase}")

                    wake_word = get_wake_word(phrase)
                    if wake_word is not None:
                        break
                    else:
                        break
                        print("Vous n'avez pas prononcé le nom d'activation ...")
                except Exception as e:
                    print("Erreur lors de la transcription audio : {0}".format(e))
                    continue

            print("Posez votre question...")
            synthesize_speech('Comment puis-je vous aider ?', 'response.mp3')
            play_audio('response.mp3')
            audio = recognizer.listen(source)

            try:
                with open("audio_prompt.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                model = whisper.load_model("base")
                result = model.transcribe("audio_prompt.wav", fp16=False)
                user_input = result["text"]
                print(f"You said: {user_input}")
            except Exception as e:
                print("Erreur lors de la transcription audio : {0}".format(e))
                continue

        bot = await Chatbot.create()
        response = await bot.ask(prompt=user_input, conversation_style=ConversationStyle.creative)

        # Sélection de la réponse du bot
        bot_response = None
        for message in response["item"]["messages"]:
            if message["author"] == "bot":
                bot_response = message["text"]
                break

        if bot_response:
            # Supprime les balises dans la réponse
            bot_response = re.sub(r'\[.*?\]', '', bot_response)
            print(f"Jake : \n{bot_response}")
            synthesize_speech(bot_response, 'response.mp3')
            play_audio('response.mp3')

        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())