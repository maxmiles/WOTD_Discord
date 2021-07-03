import discord
from decouple import config
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import requests
from PyDictionary import PyDictionary

url = "https://www.merriam-webster.com/word-of-the-day/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
psoup = soup.prettify()
ssoup = str(psoup)
stsoup = ""
snsoup = ""

def falsetter():
    global one_a
    one_a = False
    global one_b
    one_b = False
    global one_c
    one_c = False

def href_check(temp_index):
    if ssoup[temp_index:(temp_index + 100)].find("href") != -1:
        return True
    else:
        return False

def final_indexer(temp_index):
    global def_st_index
    global def_end_index
    if href_check(temp_index):
        temp_index = ssoup[temp_index:(temp_index + 100)].find("href") + temp_index
    def_st_index = ssoup[temp_index:].find(">") + temp_index + 1
    def_end_index = ssoup[def_st_index:].find("<") + def_st_index
    return ssoup[def_st_index:def_end_index]

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
        one_a = False
        title_temp = str(soup.title)
        title_endex = title_temp.find(" | Merriam")
        title = title_temp[24:title_endex]
        # print(title)

        if (ssoup.find("1 :")) != -1 or (ssoup.find("1 a :")) != -1:
            if (ssoup.find("1 a :")) != -1:
                one_a = True
                temp_index = ssoup.find("1 a :")
                def_one = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                one_a = False
                temp_index = ssoup.find("1 :")
                def_one = final_indexer(temp_index)
                # print(def_one.lstrip())
            if one_a:
                one_b = True
                temp_index = ssoup[def_end_index:].find("  b") + def_end_index
                def_one_b = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                one_b = False
            if (ssoup[temp_index:(temp_index + 500)].find("c :")) != -1:
                one_c = True
                temp_index += ssoup[temp_index:(temp_index + 500)].find("c :")
                def_one_c = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                one_c = False
        else:
            falsetter()
            temp_index = ssoup.find("wotd-definition") - 200
            if ssoup[temp_index:(temp_index + 100)].find("<a") != -1:
                temp_index = ssoup[temp_index:].find("<a") + temp_index + 1
                def_one = final_indexer(temp_index)
            else:
                temp_index = ssoup[temp_index:].find(":") + temp_index + 1
                def_one = final_indexer(temp_index)

            # print(def_one.lstrip())

        if (ssoup.find("2 :")) != -1 or (ssoup.find("2 a")) != -1:
            two = True
            if (ssoup.find("2 a :")) != -1:
                two_a = True
                temp_index = ssoup.find("2 a :")
                def_two = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                two_a = False
                temp_index = ssoup.find("2 :")
                def_two = final_indexer(temp_index)
                # print(def_one.lstrip())
            if two_a:
                two_b = True
                temp_index = ssoup[def_end_index:].find("  b") + def_end_index
                def_two_b = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                two_b = False
            if (ssoup[temp_index:(temp_index + 500)].find("c :")) != -1:
                two_c = True
                temp_index += ssoup[temp_index:(temp_index + 500)].find("c :")
                def_two_c = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                two_c = False
        else:
            two = False

        if (ssoup.find("3 :")) != -1 or (ssoup.find("3 a")) != -1:
            three = True
            if (ssoup[temp_index:].find("a :")) != -1:
                three_a = True
                temp_index = ssoup.find("3 a :")
                def_three = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                three_a = False
                temp_index = ssoup.find("3 :")
                def_three = final_indexer(temp_index)
                # print(def_one.lstrip())
            if three_a:
                three_b = True
                temp_index = ssoup[def_end_index:].find("  b") + def_end_index
                def_three_b = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                three_b = False
            if (ssoup[temp_index:(temp_index + 500)].find("c :")) != -1:
                three_c = True
                temp_index += ssoup[temp_index:(temp_index + 500)].find("c :")
                def_three_c = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                three_c = False
        else:
            three = False

        if (ssoup.find("4 :")) != -1 or (ssoup.find("4 a")) != -1:
            four = True
            if (ssoup.find("4 a :")) != -1:
                four_a = True
                temp_index = ssoup.find("4 a :")
                def_four = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                four_a = False
                temp_index = ssoup.find("4 :")
                def_four = final_indexer(temp_index)
                # print(def_one.lstrip())
            if four_a:
                four_b = True
                temp_index = ssoup[def_end_index:].find("  b") + def_end_index
                def_four_b = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                four_b = False
            if (ssoup[temp_index:(temp_index + 500)].find("c :")) != -1:
                four_c = True
                temp_index += ssoup[temp_index:(temp_index + 500)].find("c :")
                def_four_c = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                four_c = False
        else:
            four = False

        if (ssoup.find("5 :")) != -1 or (ssoup.find("5 a")) != -1:
            five = True
            if (ssoup.find("5 a :")) != -1:
                five_a = True
                temp_index = ssoup.find("5 a :")
                def_five = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                five_a = False
                temp_index = ssoup.find("5 :")
                def_five = final_indexer(temp_index)
                # print(def_one.lstrip())
            if five_a:
                five_b = True
                temp_index = ssoup[def_end_index:].find("  b") + def_end_index
                def_five_b = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                five_b = False
            if (ssoup[temp_index:(temp_index + 500)].find("c :")) != -1:
                five_c = True
                temp_index += ssoup[temp_index:(temp_index + 500)].find("c :")
                def_five_c = final_indexer(temp_index)
                # print(def_one.lstrip())
            else:
                five_c = False
        else:
            five = False

        if (ssoup[:50000].find("verb")) != -1:
            pos = "(v.)"
        if (ssoup[:50000].find("noun")) != -1:
            pos = "(n.)"
        if (ssoup[:50000].find("adjective")) != -1:
            pos = "(adj.)"

        # print(pos)
        if one_a:
            wotd = "**" + title + "** *" + pos + "* - 1a: " + def_one.strip() + "."
            if one_b:
                wotd += " 1b: " + def_one_b.strip() + "."
            if one_c:
                wotd += " 1c: " + def_one_c.strip() + "."
        else:
            wotd = "**" + title + "** *" + pos + "* - 1: " + def_one.strip() + "."
        if two:
            if two_a:
                wotd += " 2a: " + def_two.strip() + "."
                if two_b:
                    wotd += " 2b: " + def_two_b.strip() + "."
                if two_c:
                    wotd += " 2c: " + def_two_c.strip() + "."
            else:
                wotd += " 2: " + def_two.strip() + "."
        if three:
            if three_a:
                wotd += " 3a: " + def_three.strip() + "."
                if three_b:
                    wotd += " 3b: " + def_three_b.strip() + "."
                if three_c:
                    wotd += " 3c: " + def_three_c.strip() + "."
            else:
                wotd += " 3: " + def_three.strip() + "."
        if four:
            if four_a:
                wotd += " 4a: " + def_four.strip() + "."
                if four_b:
                    wotd += " 4b: " + def_four_b.strip() + "."
                if four_c:
                    wotd += " 4c: " + def_four_c.strip() + "."
            else:
                wotd += " 4: " + def_four.strip() + "."
        if five:
            if five_a:
                wotd += " 5a: " + def_five.strip() + "."
                if five_b:
                    wotd += " 5b: " + def_five_b.strip() + "."
                if five_c:
                    wotd += " 5c: " + def_five_c.strip() + "."
            else:
                wotd += " 5: " + def_five.strip() + "."
        await words.send(wotd)
        await words.send("from Word of the Day!")
    if message.content.startswith('!define'):
        word = message.content[8:]
        dictionary = PyDictionary(word)
        word_dict = dictionary.meaning(word)
        output = "**" + word.title() + "** - "
        for key in word_dict:
            if key == "Verb":
                pos = "*(v.):*"
            if key == "Noun":
                pos = "*(n.):*"
            if key == "Adjective":
                pos = "*(adj.):*"
            if key == "Adverb":
                pos = "*(adv.):*"
            output += pos
            word_list = word_dict[key]
            for i in word_dict[key]:
                if i == word_list[-1]:
                    output += " " + i + ". "
                else:
                    output += " " + i + " :"
        await words.send(output)
        await words.send("from Defined " + word.title() + ".")


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

    #if message.content.startswith('hello'):
     #   await message.channel.send('heyyyyy ;)')  

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