import asyncio
import re
import emoji
from EdgeGPT import Chatbot, ConversationStyle

async def generate_IA(prompt):
    bot = await Chatbot.create()
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative)


    # Sélection de la réponse du bot
    bot_response = None
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            bot_response = message["text"]


    if bot_response:
       # Supprime les balises dans la réponse
        bot_response = re.sub(r'\[.*?\]', '', bot_response)
        bot_response = re.sub(r'Bing', 'Jake', bot_response)
        print(f"JAKE : {bot_response}")


    await bot.close()

    sauv = int(input("\nVoulez-vous sauvegardé la réponse :\n1) Oui\n2) Non\nVotre réponse : "))

    if sauv == 1 :
        titre = input("Donné un nom au Sujet : ")

        titre = re.sub(r' ', '_', titre)

        sauvegarde(titre, bot_response)
    else :
        print("Merci d'avoir utilisé Jake")

def supprimer_emoji(chaine):
    chaine_texte = emoji.demojize(chaine)
    
    return chaine_texte


def sauvegarde(Titre, Jake):
    Jake = supprimer_emoji(Jake)

    with open(f"./Sauvegarde/{Titre}.txt", "w", encoding='UTF-8') as f :
        f.write(Jake)

    print(f"Votre fichier à été sauvegardés: {Titre}.txt")


text = input("Prompt : ")

asyncio.run(generate_IA(text))
