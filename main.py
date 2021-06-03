import discord
from decouple import config
from urllib.request import urlopen

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

    if message.content.startswith('!wotd'):
        url = "https://www.merriam-webster.com/word-of-the-day"
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")


        title_index = html.find("<title>")
        start_indext = title_index + len("<title>Word of the Day: ")
        end_indext = html.find(" | Merriam-Webster</title>")
        wordTitle = html[start_indext:end_indext]
        # print(wordTitle)

        pos_index = html.find("\"main-attr\">")
        start_indexpos = pos_index + len("\"main-attr\">")
        end_indexpost = html.find("<!--<span class=\"word")
        end_indexpos = end_indexpost - 20
        pos = html[start_indexpos:end_indexpos]
        posp = ""
        if pos == "verb":
            posp = "v."
        elif pos == "noun":
            posp = "n."
        elif pos == "adjective":
            posp = "adj."
        #        print(pos)


        def_index1 = html.find("<p><strong>1")
        start_indexd1 = def_index1 + len("<p><strong>1 :</strong> ")
        end_indexd1 = html.find(" <strong>:</strong>")
        wordDef1 = html[start_indexd1:end_indexd1]
        # print(wordDef1)

        # print("**" + wordTitle + "** " + "*(" + posp + ")* " + "-" + wordDef1)
        await message.channel.send("**" + wordTitle + "** " + "*(" + posp + ")* " + "-" + wordDef1)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')  

# # If Kevin is typing
# @client.event
# async def on_typing(channel, user):
#     if user != client.user:
#         await channel.send('stfu')


TOKEN = config("TOKEN")
client.run(TOKEN)