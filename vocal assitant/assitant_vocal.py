import openai
import pyttsx3
import speech_recognition as sr 
import time

#mise en place des clef OpenAI API
openai.api_key = "..."

# Initialisation du module vocal
engine = pyttsx3.init()

def tatt(filenam):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filenam) as source:
        audio = recognizer.record(source)
    try : 
        return recognizer.recognize_google(audio, language="fr-FR")
    except :
        print('Skipping unknown error')

def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Dite 'Jake' pour commencer à enregistrer votre requête ...")
        with sr.Microphone() as source :
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try :
                transcription = recognizer.recognize_google(audio, language="fr-FR")
                if transcription.lower() == "jake":
                    filename = "input.wav"
                    speak_text("Jake vous écoute quel est votre question ?")
                    print("Posez votre question ...")
                    with sr.Microphone() as source :
                        recognizer = sr.Recognizer()
                        source.pausetreshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f :
                            f.write(audio.get_wav_data())
                    
                    # Retranscription de la requête
                    text = tatt(filename)
                    if text :
                        print(f"Vous venez de dire: \n{text}")

                        #génération de la réponce
                        if text == 'est-ce que tu me comprends':
                            speak_text("Oui mais je ne suis pas encore relier à une IA")

                        elif text == 'au revoir Jake' :
                            speak_text("Au revoir au plaisir de vous entendre à nouveau monsieur")
                            print("Merci d'avoire utiliser le programme")
                            break

                        response = generate_response(text)
                        print(f"Réponse de Génius : \n{response}")
                        # Initiation Vocale de la réponse
                        speak_text(response)
            except Exception as e:
                print(f"An error occured: {e}")


if __name__ == "__main__":
    main()