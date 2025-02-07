import whisper

# Charger le modèle Whisper
model = whisper.load_model("large")

# Transcrire directement le fichier audio
result = model.transcribe("Conférence-vulnérabilité.wav", language="fr")
print(result["text"])

with open("text.txt", "w", encoding='utf-8') as fc :
    fc.write(result['text'])
