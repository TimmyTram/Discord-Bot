import discord
from dotenv import load_dotenv
import os
from utils.printer import bcolors as bc
from llm_client import get_llm_response

class llmClient(discord.Client):
    
    async def on_ready(self):
        bc.color_print(bc.OKGREEN, f'Logged on as {self.user}!')

    async def on_message(self, message):
        
        at_mention = f'<@{self.user.id}>'
        context_id = str(message.channel)

        # do not let the bot respond to itself
        if message.author.id == self.user.id:
            return 

        # Only respond if the user @s the bot
        if message.content.startswith(at_mention):
            truncated_msg = str(message.content).replace(at_mention, '').strip()
            formatted_msg = f"{message.author}: {truncated_msg}"
            bc.color_print(bc.OKBLUE, formatted_msg)
            response = await get_llm_response(formatted_msg, context_id)
            bc.color_print(bc.OKGREEN, f'{self.user}: {response}')
            await message.reply(response, mention_author=True)




load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = llmClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))