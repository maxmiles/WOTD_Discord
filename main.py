import discord
from decouple import config
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import requests

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
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        psoup = soup.prettify()
        ssoup = str(psoup)

        title_temp = str(soup.title)
        title_endex = title_temp.find(" | Merriam")
        title = title_temp[24:title_endex]
        # print(title)

        temp_index = ssoup.find("1 :")
        def_st_index = ssoup[temp_index:].find(">") + temp_index + 1
        def_end_index = ssoup[def_st_index:].find("<") + def_st_index
        def_one = ssoup[def_st_index:def_end_index]
        # print(def_one.lstrip())

        if (ssoup.find("2 :")) != -1:
            two = True
            temp_index = ssoup.find("2 :")
            def_st_index = ssoup[temp_index:].find(">") + temp_index + 1
            def_end_index = ssoup[def_st_index:].find("<") + def_st_index
            def_two = ssoup[def_st_index:def_end_index]
            # print(def_two.lstrip())
        else:
            two = False

        if (ssoup.find("3 :")) != -1:
            three = True
            temp_index = ssoup.find("3 :")
            def_st_index = ssoup[temp_index:].find(">") + temp_index + 1
            def_end_index = ssoup[def_st_index:].find("<") + def_st_index
            def_three = ssoup[def_st_index:def_end_index]
            # print(def_three.lstrip())
        else:
            three = False

        if (ssoup.find("4 :")) != -1:
            four = True
            temp_index = ssoup.find("4 :")
            def_st_index = ssoup[temp_index:].find(">") + temp_index + 1
            def_end_index = ssoup[def_st_index:].find("<") + def_st_index
            def_four = ssoup[def_st_index:def_end_index]
            # print(def_four.lstrip())
        else:
            four = False

        if (ssoup.find("verb")) != -1:
            pos = "(v.)"
        if (ssoup.find("noun")) != -1:
            pos = "(n.)"
        if (ssoup.find("adjective")) != -1:
            pos = "(adj.)"

        # print(pos)

        wotd = "**" + title + "** *" + pos + "* - 1: " + def_one.strip() + "."
        if two:
            wotd += " 2: " + def_two.strip() + "."
        if three:
            wotd += " 3: " + def_three.strip() + "."
        if four:
            wotd += " 4: " + def_four.strip() + "."
        await words.send(wotd)
        await words.send("from Word of the Day!")

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