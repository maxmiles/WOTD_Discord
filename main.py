import discord
from decouple import config
from urllib.request import urlopen
import time

client = discord.Client()

# Alert when ready 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
# Retrieve and print WOTD to #words channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words = client.get_channel(844741075386105906)

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
        posp = part_of_speech(pos)

        def_index1 = html.find("<p><strong>1")
        start_indexd1 = def_index1 + len("<p><strong>1 :</strong> ")
        html_temp = html[start_indexd1:]
        end_indexd1 = html_temp.find("</p>")
        wordDef1 = html_temp[:end_indexd1]
        # check for second definition
        if html.find("<p><strong>2 :</strong>")  != -1:
            def_index2 = html.find("<p><strong>2 :</strong>")
            start_indexd2 = def_index2 + len("<p><strong>2 :</strong> ")
            html2 = html[start_indexd2:]
            end_indexd2 = html2.find("</p>")
            wordDef2 = html2[:end_indexd2]
            await words.send("**" + wordTitle + "** " + "*(" + posp + ")* " + "- " + wordDef1 + "; " + wordDef2) 
        else:
            await words.send("**" + wordTitle + "** " + "*(" + posp + ")* " + "- " + wordDef1)

    # if message.content.startswith('!define'):
    #     word = message.content[6:]
    #     html = urlopen("https://www.merriam-webster.com/dictionary/" + word).read().decode("utf-8")

    #     start_index = html.find("<a class=\"important-blue-link\" href=\"/dictionary/")
    #     start_index += len("<a class=\"important-blue-link\" href=\"/dictionary/")
    #     end_index = html.find("</a></span>            </div>")
    #     pos = html[start_index:end_index]
    #     pos = pos.split("\">")[0]
    #     pos = part_of_speech(pos)

    #     print(pos)

    #     def_index1 = html.find("<p><strong>1")
    #     start_indexd1 = def_index1 + len("<p><strong>1 :</strong> ")
    #     end_indexd1 = html.find(" <strong>:</strong>")
    #     definition = html[start_indexd1:end_indexd1]

    #     print(definition)

    #     await words.send("**" + word.title() + "** " + "*(" + pos + ")* " + "-" + definition)

    if message.content.startswith('hello'):
        await message.channel.send('heyyyyy ;)')  

# If Kevin is typing
@client.event
async def on_typing(channel, user, when):
    if user.id == 451512040083947530:
        time.sleep(0.5)
        await channel.send('stfu')

def part_of_speech(pos):
    if pos == "verb":
        return "v."
    elif pos == "noun":
        return "n."
    elif pos == "adjective":
        return "adj."

TOKEN = config("TOKEN")
client.run(TOKEN)