import asyncio
import re
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


text = input("Prompt : ")

asyncio.run(generate_IA(text))