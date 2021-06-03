import discord
import os
from decouple import config
import dotenv

client = discord.Client()

# Alert when ready 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    print(f'{client.user} has connected to Discord!')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

print(os.getenv("TOKEN"))
print(load_dotenv(verbose=True))
# client.run(os.environ.get("TOKEN"))