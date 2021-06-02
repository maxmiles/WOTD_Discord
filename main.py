import discord
import os

client = discord.Client()

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

client.run(os.getenv('ODQ5NTU5MjMwNDE5MzA0NDY5.YLc7sA.TmPEeMf6MgsiCFzbRDDmm6kqnho'))