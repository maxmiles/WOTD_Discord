import discord
from decouple import config

client = discord.Client()

# Alert when ready 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
# Default hello message response
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!word'):
        await message.channel.send('!word')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')  

# # If Kevin is typing
# @client.event
# async def on_typing(channel, user):
#     if user != client.user:
#         await channel.send('stfu')


TOKEN = config("TOKEN")
client.run(TOKEN)