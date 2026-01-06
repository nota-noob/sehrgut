import os, random, discord, asyncio, io, requests, subprocess, time, math, unicodedata, ast, pdfplumber, datetime, aiohttp, termios, typing, deepl, wolframalpha, pathlib, textwrap, json, subprocess, selenium, spacy
import seaborn as sns
import numpy as np
# import matplotlib.pyplot as plt
import google.generativeai as genai

from os.path import exists
from ctypes.wintypes import RGB
from timeit import default_timer
from discord.ext.commands import CommandNotFound, cooldown, BucketType
from discord.ext import commands
from discord.ext.commands.errors import BadArgument
from discord.message import Message
from dotenv import load_dotenv
from groq import Groq
from openai import OpenAI
from g4f.client import Client
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from subprocess import getoutput
from sparknlp.base import *
from sparknlp.annotator import *
from sparknlp.pretrained import PretrainedPipeline
from pyspark.sql import SparkSession
from bs4 import BeautifulSoup
from matplotlib import font_manager
from pathlib import Path

if __name__ == "__main__":
    from dictcc import Dict
    dictcc = Dict()

else:
    from dictcc.dictionaries import Dictionary
    dict_path = Path.home() / ".dict.cc"
    dictcc = Dictionary(path=dict_path,reversed=False)

from simpleeval import simple_eval as calc
from traceback import print_exc
from PIL import Image
from io import BytesIO
from google_translate_py import Translator as t
from discord import app_commands
from IPython.display import display, Markdown
# from spellchecker import SpellChecker

# spellchecker = SpellChecker()
translator = deepl.Translator("57d95539-5eec-dc5c-285f-d2b0c376688f:fx")
calculator = wolframalpha.Client('9E39KJ-J79G69HQYK')
nlp = spacy.load("de_core_news_sm")
import de_core_news_sm
nlp = de_core_news_sm.load()

# spark = sparknlp.start(aarch64=True)
# pipeline = PretrainedPipeline("analyze_sentiment", lang="de")

load_dotenv()
ballgame = ":tennis: noob's ball game"
helpmenu = ":robot: sehr gut's help menu"
maincolor = discord.Color(0xACF3A3)
rpscolor = discord.Color(0xADD8E6)
wrongcolor = discord.Color(0xE09593)
footer = "sehr gut • aka noob's companion"

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-8b')

# OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
# model = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key=OPENROUTER_API_KEY,
# )
# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY"),  # This is the default and can be omitted
# )


TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents = discord.Intents.all()



bot = discord.Client(command_prefix='nub.', help_command=None, intents=intents)
tree = discord.app_commands.CommandTree(bot)

def getpath():
    # try:
    #     path = "/Users/ethantsai/Library/Mobile Documents/com~apple~CloudDocs/Desktop/bot_py/"
    #     with open(path+"testme.txt","r") as g:
    #         g.close()
    # except:
    #     try:
    #         path = "/Users/2happ/Desktop/bot_py/"
    #     except:
    #         path = "/home/opc/"

    return "/home/opc/bot_py/"

async def getcookies():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = "/usr/bin/firefox"
    service = Service(executable_path ="/home/opc/bot_py/.venv/WebDriverManager/gecko/v0.35.0/geckodriver-v0.35.0-linux64/geckodriver")
    driver = webdriver.Firefox(options=options,service=service)
    driver.get("https://quillbot.com/de/rechtschreibprufung")
    driver.implicitly_wait(2)
    while driver.get_cookies() == []:
        await asyncio.sleep(1)
        print("...")
    while "connect.sid" not in str(driver.get_cookies()):
        await asyncio.sleep(1)
        print(len(driver.get_cookies()))


    connectsid = driver.get_cookie("connect.sid")['value']
    print(connectsid)

    # while len(cookies) < len(required_cookies):
    #     cookies = driver.get_cookie("connect.sid")
    #     if cookies != []:
    #         print(cookies)
    #         break
    #     else:
    #         await asyncio.sleep(1)
    #         print(".")
        # try:
        #     if cookies[-1]['name'] == 'connect.sid':
        #         connectsid = cookies[-1]['value']
        #         break
        #     else:
        #         print(cookies)
        #         break
        # except:
        #     print(".")
        #cookie_names = [cookie['name'] for cookie in cookies]
        # driver.implicitly_wait(1)
    driver.close()
    print(f"returned cookies!! (connectsid = {connectsid})")
    with open(getpath()+"cookie.txt", "r+") as g:
        g.seek(0)
        g.write(connectsid)
        g.truncate()
        g.close()
    return connectsid

def curlcmd(sid, payload):
    return f"""'https://quillbot.com/api/utils/grammar-check' \
    -H 'accept: application/json, text/plain, */*' \
    -H 'accept-language: en-US,en;q=0.9' \
    -H 'baggage: sentry-environment=prod,sentry-release=v16.33.0,sentry-public_key=5743ef12f4887fc460c7968ebb2de54d,sentry-trace_id=3897f22a72e04f2cbda27b0646aeaa9c' \
    -H 'content-type: application/json' \
    -H 'cookie: abIDV2=139; _sp_ses.48cd=*; premium=false; qdid=3655179942588509497; connect.sid={sid}; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+07+2025+10%3A23%3A39+GMT-0800+(Pacific+Standard+Time)&version=202211.1.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fquillbot.com%2Fde%2Frechtschreibprufung&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1; AMP_MKTG_6e403e775d=JTdCJTdE; qbDeviceId=6ac67c7d-8c84-48dd-bcaa-bcbcb5596e73; cl_val=19; _gcl_au=1.1.460040276.1738952620; _ga=GA1.1.231832225.1738952620; FPID=FPID2.2.7hzEc56KhQ8HJBQe5FtjfJMPPiTsKVXwUb1EKTdETiE%3D.1738952620; FPLC=vv4T8LedNJn077VBY9z81ZxmXdah5VTaK7xqjwYeXd97v7dE2COLJ%2Byz307W0rLnR5KVsUQYSwUH%2F%2Br8yHTZUU6kLqW2bF7fLzdSa%2BKzDxItS527FUAYQzC0BeNV5Q%3D%3D; FPAU=1.1.460040276.1738952620; _fbp=fb.1.1738952620052.1236009902; _uetsid=a7db0580e58011ef82bb9f46eb598546; _uetvid=a7db21b0e58011ef9d05fb6086cccea5; _ga_D39F2PYGLM=GS1.1.1738952619.1.0.1738952640.0.0.1338778729; AMP_6e403e775d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI2YWM2N2M3ZC04Yzg0LTQ4ZGQtYmNhYS1iY2JjYjU1OTZlNzMlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzM4OTUyNjE5MzE5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczODk1MjY0MDY2NyUyQyUyMmxhc3RFdmVudElkJTIyJTNBOSU3RA==; _sp_id.48cd=ca0787d5-a660-4c68-8c48-a257d8e57e07.1738952617.1.1738952642..0ed2253d-4499-478d-a536-c4f77390d28e..c1bf08ba-3143-4306-98db-bcef91ab1921.1738952618251.3' \
    -H 'origin: https://quillbot.com' \
    -H 'platform-type: webapp' \
    -H 'platform-version;' \
    -H 'priority: u=1, i' \
    -H 'qb-dialect: de-de' \
    -H 'qb-product: GRAMMAR_CHECKER' \
    -H 'referer: https://quillbot.com/de/rechtschreibprufung' \
    -H 'sec-ch-ua: "Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "macOS"' \
    -H 'sec-fetch-dest: empty' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sentry-trace: 3897f22a72e04f2cbda27b0646aeaa9c-858356f81d15b87a' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36' \
    -H 'useridtoken: empty-token' \
    -H 'webapp-version: 16.33.0' \
    -H 'x-device-language: en-US' \
    -H 'x-website-origin: https://quillbot.com' \
    -H 'x-website-url: https://quillbot.com/de/rechtschreibprufung' \
    --data-raw '{payload}'"""

async def quillbot(content):
    with open(getpath()+"cookie.txt", "r+") as f:
        connectsid = f.read()
        f.close()
    payload = json.dumps({
        "language":"DE",
        "text":[{
            "text":content,
            "type":"GENERIC",
            "isLast":True
    }]})
    result = subprocess.run(f"/usr/local/bin/curl_ff98 -k {curlcmd(connectsid,payload)}", capture_output=True,text=True,shell=True)
    if "SESSION_FAILED" in result.stdout:
        connectsid = await getcookies()
        result = subprocess.run(f"/usr/local/bin/curl_ff98 -k {curlcmd(connectsid,payload)}", capture_output=True,text=True,shell=True)
        print(result.stdout)
    # print(result.stdout)
    return(result.stdout)
    
def isfloat(num):
    try:
        float(num)
        return(True)
    except:
        return(False)
    
        


def storeanswer(ans, txt, id):
    userid = str(id)
    with open(getpath()+"answers.txt", "r+") as file:
        answers = ast.literal_eval(file.read())
        answers[userid] = ans
        file.seek(0)
        file.write(str(answers))
        file.truncate()
        return

def filt(content):
    return content.replace(",","").replace(".","").replace("?","").replace("!","")

def articles(content):
    expanded = [
        "zu der" if a == "zur" else
        "zu dem" if a == "zum" else
        "in das" if a == "ins" else
        "in dem" if a == "im" else
        "an das" if a == "ans" else
        "an dem" if a == "am" else
        "auf das" if a == "aufs" else
        "von dem" if a == "vom" else
        "bei dem" if a == "beim" else
        "über das" if a == "übers" else
        "unter das" if a == "unters" else
        "hinter das" if a == "hinters" else
        "vor das" if a == "vors" else
        a for a in content.split()
    ]
    return " ".join(expanded)

async def finderrors(msg):
    pronouns = 0
    correctmessage = msg.lower()
    response = json.loads(await quillbot(correctmessage))
    done = []
    errors = response["data"]["sentences"][0]["contentToReplace"]
    print(response["data"])
    corrected = response["data"]['sentences'][0]['fixed']
    for error in errors:
        realerror = error["explainers"][0]
        if error["explainers"][0]["source_word"].lower().replace("ä","a").replace("ö","o").replace("ü","u").replace("ß","ss") == error["explainers"][0]["target_word"].lower().replace("ä","a").replace("ö","o").replace("ü","u").replace("ß","ss"):
            continue
        # print(error)
        print(error["explainers"][0]["error_type_id"], error["explainers"][0]["source_word"], error["explainers"][0]["target_word"])
        if realerror["error_type_id"] in ["REPLACEMENT_ADJECTIVE_FORM","REPLACEMENT_DETERMINER_FORM","REPLACEMENT_ADPOSITION","REPLACEMENT_NOUN_FORM"]:
            done += [(realerror["source_word"],realerror["target_word"])]
            if realerror["error_type_id"] in ["REPLACEMENT_NOUN_FORM","REPLACEMENT_VERB_FORM"]:
                if realerror["error_type_id"] == "REPLACEMENT_NOUN_FORM":
                    pronouns += 1
    print(done)
    return (done, corrected, pronouns)

def countconjs(msg, pronouns):
    filteredmsg = articles(filt(msg.lower()))
    doc = nlp(filteredmsg)
    analysis = [(w.text, w.pos_) for w in doc]
    print(analysis)
    conjugations = pronouns
    print(pronouns)
    for word in analysis:
        if word[1] in ['DET','ADJ']:
            conjugations += 1
    return(conjugations)

def conjtest(msg):
    # filteredmsg = articles(filt(msg.lower()))
    # doc = nlp(filteredmsg)
    doc = nlp(msg)
    analysis = [(w.text, w.pos_) for w in doc]
    testnouns = []
    testadjectives = []
    testadp = []
    for i in range(len(analysis)):
        if analysis[i][1] == ['DET']:
            if i > 0 and analysis[i-1][1] == ['ADP']:
                testadp.append(analysis[i-1][0])
            else:
                testadp.append("")

            if analysis[i+1][1] == ['ADJ']:
                temp = []
                for j in range(i+1, len(analysis)):
                    if analysis[j][1] == ['ADJ']:
                        temp.append(analysis[j][0])
                    else:
                        testadjectives.append(temp)
                        testnouns.append(analysis[j][0])
                        break
                    
            elif analysis[i+1][1] == ['NOUN']:
                testadjectives.append([])
                testnouns.append(analysis[i][0])

    return(str(testnouns) + "\n" + str(testadjectives) + "\n" + str(analysis) + "\n" + str(testadp))

def getartikel(noun):
    result = translator.translate(noun, from_language="de", to_language="en")
    return ["der" if result[0][0].split()[1][1] == "m" else "die" if result[0][0].split()[1][1] == "f" else "das" if result[0][0].split()[1][1] == "n" else "tot" for a in result[0][0].split()[1][1]][0]

def returngrammatiklb(id):
    with open("grammatik.txt", "r+") as f:
        f.seek(0)
        grammatiklb = ast.literal_eval(f.read())
        if id not in grammatiklb:
            grammatiklb[id] = [[],0,0,0,0,0,0]

        allmsgs = grammatiklb[id][0]
        totalcorrect = grammatiklb[id][1]
        totalconjugations = grammatiklb[id][2]
        lastcorrect = grammatiklb[id][3]
        lastconjugations = grammatiklb[id][4]
        previousfinalscore = grammatiklb[id][5]
        finalscore = grammatiklb[id][6]
    return [allmsgs,totalcorrect,totalconjugations,lastcorrect,lastconjugations,previousfinalscore,finalscore]

def storegrammatiklb(id, userlb):
    with open("grammatik.txt", "r+") as f:
        f.seek(0)
        lb = ast.literal_eval(f.read())
        f.seek(0)
        lb[id] = userlb
        f.write(str(lb))
        f.truncate()

def checksimilarity(msg, id):
    # allmsgs,totalcorrect,totalconjugations,lastcorrect,lastconjugations,previousfinalscore,finalscore = returngrammatiklb(id)
    id = int(id)
    with open("/home/opc/bot_py/msgs.txt", "r+") as f:
        allmsgs = ast.literal_eval(f.read())
        if id not in allmsgs.keys():
            allmsgs[id] = []

    # allmsgs = allmsgs[id]

    filteredmsg = articles(filt(msg.lower()))
    if allmsgs[id] == []:
        similarity = [0]
    else:
        similarity = [nlp(msg).similarity(nlp(filteredmsg)) for _ , a in allmsgs.items() for msg in a]       

    if sorted(similarity, reverse=True)[0] < 0.9:
        # print(allmsgs)
        allmsgs[id] = allmsgs[id] + [filteredmsg]
        # print(allmsgs)
        with open("/home/opc/bot_py/msgs.txt", "r+") as f:
            f.seek(0)
            f.write(str(allmsgs))     
            f.truncate() 

    else:
        print(similarity)

    return similarity

def calcscore(conjugations, done, msg):
    filteredmsg = articles(filt(msg.lower()))
    lengthscore = max(len(filteredmsg.split())/4,(2.25*(len(filteredmsg.split())-4)**0.5)+1)
    errorscore = max(1/4,1-(len(done)/conjugations))

    if len(done) == 0:
        errorscore = 1.5

    scoregained = lengthscore * errorscore

    if len(filteredmsg.split()) == 4:
        scoregained += 1

    return scoregained

async def progress(msg, id, tracking):
    allmsgs,totalcorrect,totalconjugations,lastcorrect,lastconjugations,previousfinalscore,finalscore = returngrammatiklb(id)
    filteredmsg = articles(filt(msg.lower()))
    similarity = checksimilarity(msg, id)

    done, y, pronouns = await finderrors(msg)
    conjugations = countconjs(msg, pronouns)
    scoregained = 0
    msgtosend = ""

    if sorted(similarity, reverse=True)[0] < 0.9 and conjugations != 0:
        print("not similar and at least 1 conjugation found!")
        if len(allmsgs) == 5000:
            allmsgs = allmsgs[1:]
        allmsgs += [filteredmsg]
        totalcorrect += conjugations-len(done)
        lastcorrect += conjugations-len(done)
        totalconjugations += conjugations
        lastconjugations += conjugations
        scoregained = calcscore(conjugations, done, filteredmsg)
        finalscore += scoregained

        if len(allmsgs)%tracking == 0 and len(allmsgs) != 0:
            msgtosend = tracker(returngrammatiklb(id))
            lastcorrect = 0
            lastconjugations = 0
            previousfinalscore = finalscore
        
    elif conjugations != 0:
        print("similar msg found")
    
    print(f"{filteredmsg} = {scoregained}pts, {len(done)} errors/{conjugations} conjugations")
    userlb = [allmsgs, totalcorrect, totalconjugations, lastcorrect, lastconjugations, previousfinalscore, finalscore]
    storegrammatiklb(id, userlb)
    return msgtosend

def tracker(lbuser):
    allmsgs,totalcorrect,totalconjugations,lastcorrect,lastconjugations,previousfinalscore,finalscore = lbuser
    if (totalcorrect-lastcorrect) <= 0 or (totalconjugations-lastconjugations) <= 0:
        previousscore = "N/A"
        previousscoretext = ""
    else:
        previousscore = round(100*(totalcorrect-lastcorrect)/(totalconjugations-lastconjugations),2)
        previousscoretext = f"{totalcorrect-lastcorrect}/{totalconjugations-lastconjugations} = "
    sendmsg = f"accuracy: {lastcorrect}/{lastconjugations} = **{round(100*lastcorrect/lastconjugations,2)}%** \
    \ntotal accuracy: ~~{previousscoretext}{previousscore}%~~ → {totalcorrect}/{totalconjugations} = **{round(100*totalcorrect/totalconjugations, 2)}%**\
    \nscore: ~~{round(previousfinalscore,2)}~~ → **{round(finalscore,2)}**"
    return sendmsg


# class textinputs(discord.ui.View):
#     def __init__(self, *, timeout=30):
#         super().__init__(timeout=timeout)


# class twentyfour(discord.ui.View):
#     def __init__(self, *, timeout=30):
#         super().__init__(timeout=timeout)
#         self.value = None

#     @discord.ui.button(label="submit",style=discord.ButtonStyle.green)
#     async def submit(self,button:discord.ui.Button,interaction:discord.Interaction):
#         self.value = True
        

#     @discord.ui.text_input(label = "input", style=discord.TextStyle.short)
#     async def text(self,input:discord.ui.TextInput,interaction:discord.Interaction):
#         return self.str()


@bot.event
async def on_ready():
    await bot.wait_until_ready() # Waits until the bot is ready
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="with notanoob"))
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed=discord.Embed(description="command doesn't exist, use `nub.help` for a list of commands : )", color=maincolor))
        return
    else:
        raise error

@bot.event
async def on_message(message):

    are_bots_sentinent = ['yes!', 'nope', 'fs', 'no doubt']
    sehr_gut = ['ja', 'indeed', 'muy bien', 'thats me B)']

    if message.author.id != 814282124588875846 and message.author.bot:
        return

    if message.content.lower() in ['bruh', 'smh']:
        await message.channel.send("<a:RATSEE:995235533603225641>")

    if message.content.lower().startswith("testing"):
        msg = message.content.lower().split()[1:]
        await message.channel.send(conjtest(msg))

    # async def askgemini(context):
    #     response = await model.generate_content_async(directions)
    #     return response.text
        
    # print(message.channel.id)
    if (((message.guild and message.guild.id in [1077704169508569138] and message.channel.id not in [1077704169999310930]) or message.channel.id in [1100128778950299698, 957045643640205363]) and len(message.content.split()) > 3) and message.author.id != 814282124588875846:
        # try:
        #     response = await askgemini(directions)
        # except:
        #     response = "good"
        done, corrected, pronouns = await finderrors(message.content)
        finalmsg = f""
        context = ""
        splitted = message.content.lower().split()
        correctedsplit = corrected.split()
        seenwords = {}
        currentindex = 0
        lastcontext = ""
        for gerror in done:
            if gerror[0] not in seenwords:
                # if splitted.index(gerror[0]) = splitted.index
                seenwords[gerror[0]] = 1
                try:
                    context = filt(correctedsplit[splitted.index(gerror[0])+1])
                    if context == gerror[1]:
                        context = filt(correctedsplit[splitted.index(gerror[0])+2])
                except:
                    context = ""
            else:
                context = correctedsplit[[index for index, word in enumerate(splitted) if word == gerror[0]][seenwords[gerror[0]]]+1].replace(".","").replace(",","")
                seenwords[gerror[0]] += 1

            print(lastcontext, gerror[1])
            if lastcontext == gerror[1]:
                finalmsg = " ".join(finalmsg.split(" ")[:-1])+f" **{gerror[1].upper()}** \n{context.upper()}!\n"
            else:
                finalmsg += f"# <:xmark:946172382920470658> **{gerror[1].upper()}** \n{context.upper()}!\n"
            lastcontext = context
            currentindex += splitted.index(gerror[0])+1
            # print(splitted.index(gerror[0])+1)
            # print(gerror[0])
            # print(gerror)
            
            # print(finalmsg)
        if finalmsg != "":
            await message.channel.send(finalmsg)

        # rawscore = f"{conjugations-len(done)}/{conjugations}"
        # score = (conjugations-len(done))/conjugations
        tracking = 20
        sending = await progress(message.content, message.author.id, tracking)
        if sending != "":
            await message.channel.send(embed=discord.Embed(title="Du hast 20 nachrichten konjugiert!", description = sending, color=maincolor))
            # quiz = await message.channel.send(embed=discord.Embed(title="War das fähigkeit?? oder nur gluck??", description = "klicke auf 'start', um den quiz zu beginnen!\nEs gibt 5 frage. Diese probleme sind von deinen letzten nachrichten genommen. Du hast 5 sekunden pro problem. viel gluck!\nwenn du diese prufung nicht nimmst, verlierst du halb von deinem accuracy und punkte!! so nimm die prufung!!", color=maincolor))
    
        # corrected = response["data"]["sentences"][0]["fixed"]
        # formatted = corrected.lower().replace(".", "").replace(",","").replace("ä","a").replace("ö","o").replace("ü","u").replace("ß","ss")
        # bad = message.content.lower().split()
        # good = formatted.split()
        # await message.channel.send(str([(wrong, right) for wrong, right in zip(bad, good) if wrong != right]))

        # response = model.chat.completions.create(
        #     model="deepseek/deepseek-r1:free",
        #     messages=[
        #         {
        #         "role": "user",
        #         "content": directions
        #         }
        #     ]
        # ).choices[0].message.content

        # response = chat_completion = client.chat.completions.create(
        # messages=[
        # {
        #     "role": "user",
        #     "content": directions,
        # }
        # ],
        # model="llama3-70b-8192",
        # ).choices[0].message.content
        # errors = len(response.split("\n"))
        # lresponse = response.split()
        # print(response)
        # print(response.lower())
        # print("good" in response.lower())
        # if "good" in response.lower():
        #     return#await message.add_reaction('<:checkmark:946172382882717707>')
            
        # else:
        #     words = []
        #     for word in lresponse:
        #         if word.startswith("**"):
        #             if word in words and word == words[-1]:
        #                 return
        #             else:
        #                 words += [word]

        #     await message.channel.send(response)

    if any(sorry  == message.content.lower() for sorry in ["ruhig", "leise", "stumm"]):
        await message.channel.send("es tut mir leid : (", reference=message)

    if 'ans' in message.content.lower():
        userid = str(message.author.id)
        with open(getpath()+"answers.txt", "r") as file:
            ans = ast.literal_eval(file.read()) 
            if len(message.content) > 4 and message.content.lower()[-1] != 's' or message.content.lower().count('ans') > 1:
                if list(message.content.lower())[list(message.content.lower()).index('s')+1] in ['+', '-', '/', '*', '^'] or message.content.lower() == 'ans':
                    if userid not in ans:
                        await message.channel.send("```no answer in database : (```")
                        return 
                    while 'ans' in message.content.lower():
                        message.content = message.content.lower().replace("ans", str(ans[userid]))
                else:
                    pass
            else:
                if message.content.lower() == 'ans':
                    if userid not in ans:
                        await message.channel.send("```no answer in database : (```")
                        return 
                    await message.channel.send(f"```c++\nyour stored answer is {ans[userid]}```")
                    return

    if message.content.lower() == 'are bots sentient':
        response = random.choice(are_bots_sentinent)
        await message.channel.send(response)

    elif message.content.lower() == 'sehr gut':
        response = random.choice(sehr_gut)
        await message.channel.send(response)

    elif message.content.lower() == 'schlecht':
        embed = discord.Embed(description= "oh no, something bad happened", color=maincolor)
        await message.channel.send(embed=embed)

    elif message.content == '<@803692977926307850>':
        if random.randint(1, 1000000) == 1:
            await message.channel.send('no. I am playing with notanoob.\n||this message had a 1/1,000,000 chance of being triggered btw. <@532373646543683584>||')
        else:
            await message.channel.send('hi')

    elif ("tot" in message.content.lower().split() or "toden" in message.content.lower().split()):
        if message.channel.id == 1077704169999310930:
            await asyncio.sleep(5)
            await message.channel.send("THAT is the TOTIEST thing i have ever seen 😂 😂 😂 😂 😂 😂 OMG 😂 thats so TODEN 🤣 🤣 so SCHWARZEN 👉👈 🤪 so TOT 🤩absolute GUT energy 🤪🤪")
        elif message.author.id == 814288123315617812:
            await message.add_reaction("<:Peetah:1339118714120835142>")

    elif message.content == "Sorry, that wasn't the right answer.":
        await message.channel.send('you got this :)')

    elif message.content.lower() == "sehr interessant":
        await message.channel.send('not interesting smh')

    elif message.content.lower().startswith('testme'):
        

        #path = getpath()+""
        #poem = ['','two households both alike in dignity', 'in fair verona where we lay our scene' ,'from ancient grudge break to new mutiny', 'where civil blood makes civil hands unclean', 'from forth the fatal loins of these two foes' ,'a pair of star crossed lovers take their life' , 'whose misadventured piteous overthrows' , 'do with their death bury their parents strife', 'the fearful passage of their death marked love', 'and the continuance of their parents rage', "which but their childrens end nought could remove", 'is now the two hours traffic of our stage', 'the which if you with patient ears attend', 'what here shall miss our toil shall strive to mend']
        terms = []
        definitions = []
        # elements = ['Hydrogen', 'H', 'Helium', 'He', 'Lithium', 'Li', 'Beryllium', 'Be', 'Boron', 'B', 'Carbon', 'C', 'Nitrogen', 'N', 'Oxygen', 'O', 'Fluorine', 'F', 'Neon', 'Ne', 'Sodium', 'Na', 'Magnesium', 'Mg', 'Aluminum', 'Al', 'Silicon', 'Si', 'Phosphorus', 'P', 'Sulfur', 'S', 'Chlorine', 'Cl', 'Argon', 'Ar', 'Potassium', 'K', 'Calcium', 'Ca', 'Titanium', 'Ti', 'Chromium', 'Cr', 'Manganese', 'Mn', 'Iron', 'Fe', 'Cobalt', 'Co', 'Nickel', 'Ni', 'Copper', 'Cu', 'Zinc', 'Zn', 'Arsenic', 'As', 'Bromine', 'Br', 'Krypton', 'Kr', 'Rubidium', 'Rb', 'Strontium', 'Sr', 'Zirconium', 'Zr', 'Molybdenum', 'Mo', 'Silver', 'Ag', 'Cadmium', 'Cd', 'Tin', 'Sn', 'Iodine', 'I', 'Xenon', 'Xe', 'Cesium', 'Cs', 'Barium', 'Ba', 'Tungsten', 'W', 'Platinum', 'Pt', 'Gold', 'Au', 'Mercury', 'Hg', 'Lead', 'Pb', 'Bismuth', 'Bi', 'Radon', 'Rn', 'Radium', 'Ra', 'Uranium', 'U', 'Plutonium', 'Pu']
        def check(m):
            return m.author == message.author and m.channel == message.channel
        
        def exception(a):
            exceptions = {"jq adams": "jqa"}
            if a in exceptions:
                return exceptions[a]
            else:
                return a

        with open(getpath()+"memorization.txt", "r+") as f:
            words = ast.literal_eval(f.read())
            if message.author.id not in words:
                await message.channel.send("new user detected! things to know:\n```1: type 'exit' during a test to exit\n2: you have 5 minutes to answer each question before the test times out\n3: your last test is remembered so you can simply type 'testme' if you wish to repeat a test```")
                words[message.author.id] = ("", {})
            f.seek(0)
            f.write(str(words))
            f.truncate()
            f.close()


        #IF IT IS TESTME _____
        if len(message.content.split()) == 2 and "swap" not in message.content:
            testtype = message.content.split()[1]
            with open(getpath()+"testme.txt", "r") as g:
                tests = ast.literal_eval(g.read())
                if testtype in tests:
                    terms = tests[testtype][0]
                    definitions = tests[testtype][1]

                else:
                    await message.add_reaction('<:xmark:946172382920470658>')
                    await message.channel.send("invalid test")
                    return
                g.close()

        #IF IT IS JUST TESTME
        elif message.content == "testme":
            with open(getpath()+"memorization.txt", "r") as f:
                words = ast.literal_eval(f.read())
                if message.author.id in words and words[message.author.id] != "":
                    testtype = words[message.author.id][0]
                    with open(getpath()+"testme.txt", "r") as g:
                        tests = ast.literal_eval(g.read())
                        terms = tests[testtype][0]
                        definitions = tests[testtype][1]
                        g.close()
                else:
                    await message.channel.send("what test?")
                    return
                if "swap" in message.content.split():
                    tempterms = terms
                    tempdefs = definitions
                    definitions = tempterms
                    terms = tempdefs
                    if testtype == "morsecodes":
                        definitions = " ".join(terms).replace("•", ".").split()

                f.close()

        else:
            message.channel.send("put a space between 'testme' and your test smh")
            return

        if "headlines" not in testtype:
            if len(terms) != len(definitions):
                await message.add_reaction('<:xmark:946172382920470658>')
                await message.channel.send(f"mismatched lengths! len terms = `{len(terms)}`, len definitions = `{len(definitions)}`")
                return
            temp = list(zip(terms, definitions))
            random.shuffle(temp)
            terms, definitions = list(zip(*temp))
            terms = list(terms)
            definitions = list(definitions)

        await message.add_reaction('<:checkmark:946172382882717707>')
        numcorr = 0
        termlen = len(terms)
        testtitle = f"{message.author.name}'s {testtype} test"
        testcontent = f"{numcorr}/{termlen} correct"
        question = "`"+terms[0]+": `"
        test = await message.channel.send(embed=discord.Embed(title=testtitle, description=f"{testcontent}\n\n{question}", color=maincolor))
        start = time.time()
        while numcorr < termlen:
            try:
                if testtype in ["morsecodes", "baconians"]:
                    question = await message.channel.send("`"+terms[0]+"`")
                else:
                    pass

                msg = await bot.wait_for('message', check=check, timeout=300)

            except:
                with open(getpath()+"memorization.txt", "r+") as f:
                    words = ast.literal_eval(f.read())
                    if message.content.lower() != "testme":
                        if message.author.id not in words:
                            words[message.author.id] = (message.content.split()[1], {})
                        else:
                            words[message.author.id] = (message.content.split()[1],words[message.author.id][1])
                    f.seek(0)
                    f.write(str(words))
                    f.truncate()
                    f.close()
                await message.channel.send('you took too long : (')
                return
            correct = [exception(definitions[0].lower()), exception(definitions[0].lower().replace(" ", ""))]
            await msg.delete()
            # if msg.content.lower() in correct or " ".join([f"{spellchecker.correction(x)}" for x in msg.content.lower().strip().split()]).replace("", "") in correct:
            if "tot":
                testcontent = f"{numcorr+1}/{termlen} correct\n\n<:checkmark:946172382882717707> correct"
                if numcorr == termlen -1:
                    question = ""
                else:
                    terms.remove(terms[0])
                    definitions.remove(definitions[0])
                    question = "`"+terms[0]+": `"
                await test.edit(embed=discord.Embed(title=testtitle, description=f"{testcontent}\n\n{question}", color=maincolor))
                numcorr += 1
            elif msg.content.lower() == "exit":
                await test.edit(embed=discord.Embed(title=testtitle, description=f"{testcontent}\n\ntest exited"))
                return
            else:
                testcontent = f"{numcorr}/{termlen} correct\n\n<:xmark:946172382920470658> the correct answer was:\n`{correct[0]}`"
                terms.append(terms[0])
                terms.remove(terms[0])
                definitions.append(definitions[0])
                definitions.remove(definitions[0])
                question = "`"+terms[0]+": `"
                await test.edit(embed=discord.Embed(title=testtitle, description=f"{testcontent}\n\n{question}", color=wrongcolor))
                
        timespentstr = f"{str(int((time.time()-start)//60))}m {str(round((time.time()-start)%60,2))}s"
        timespent = int(timespentstr.replace("s", "").replace("m", "").split()[0])*60+float(timespentstr.replace("s", "").replace("m", "").split()[1])
        if "0m " in timespentstr:
            timespentstr.replace("0m ", "")
        await message.channel.send(f"u finished the test sehr gut, in `{timespentstr}`")
        with open(getpath()+"memorization.txt", "r+") as f:
            words = ast.literal_eval(f.read())
            if testtype != words[message.author.id][0]:
                words[message.author.id] = (testtype,words[message.author.id][1])
            if testtype in words[message.author.id][1]:
                testtimes = words[message.author.id][1][testtype]
                testtimes += [timespent]
            else:
                words[message.author.id][1][testtype] = [timespent]
                testtimes = words[message.author.id][1][testtype]
            if message.content.lower() != "testme":
                words[message.author.id] = (message.content.split()[1],words[message.author.id][1])

            rank = sorted(testtimes).index(timespent)+1
            suffixes = {0: "th", 1: "st", 2: "nd", 3: "rd", 4: "th", 5: "th", 6: "th", 7: "th", 8: "th", 9: "th"}
            if rank == 1:
                if len(testtimes) > 1:
                    await message.channel.send(f"this is your fastest time for this test by `{round(sorted(testtimes)[1]-timespent, 2)}s` :tada:")
                else:
                    await message.channel.send("this is your fastest time for this test :tada:")
            else:
                if rank > 10 and rank < 14:
                    suffixes[rank%10] = "th"
                await message.channel.send(f"this is your `{rank}{suffixes[rank%10]}` fastest time for this test, `+{round(timespent-min(words[message.author.id][1][testtype]), 2)}s` from your fastest time.")
            f.seek(0)
            f.write(str(words))
            f.truncate()
            f.close()
        
        xaxis = np.arange(1, len(testtimes)+1, 1)
        yaxis = np.asarray(testtimes, dtype=float)
        ax = sns.barplot(x=xaxis, y=yaxis,palette="YlGnBu")
        ax.set(xlabel="test number", ylabel="time spent (s)", ylim=(min(60, min(testtimes)-min(testtimes)%5), max(testtimes)**(1+(1/max(testtimes)))-max(testtimes)**(1+(1/max(testtimes)))%5))
        ax.get_figure().suptitle(f"{testtype} test times")
        ax.get_figure().savefig("image.png")
        ax.get_figure().clf()
        with open('image.png', 'rb') as f:
            graph = discord.File(f)
            await message.channel.send(file=graph)
            f.close()
        os.remove("image.png") 

    elif len(message.content) >= 4 and 'fc' in message.content or 'cf' in message.content:
        if message.content[0:2] == 'cf' and isfloat(message.content[3:]):
            await message.channel.send(embed=discord.Embed(title=f'°c to °f', description=f'`{message.content[3:]}°c → {round((int(message.content[3:])*1.8+32), 1)}°f`', color=maincolor))
        elif message.content[0:2] == 'fc' and isfloat(message.content[3:]):
            await message.channel.send(embed=discord.Embed(title=f'°f to °c', description=f'`{message.content[3:]}°f → {round((int(message.content[3:])-32)*5/9, 1)}°c`', color=maincolor))

    elif 'invalid' not in [a if a in ['(', ')', 'x', 'p', 'i', 'o', 'l', 'e', 'n', 'g', '-', '+', '/', '*', '.', ',', ' ', '!', '^', ' '] or isfloat(a) else 'invalid' for a in list(message.content.lower().strip())] and 'digit' in ['digit' if a.isdigit() else a for a in list(message.content.strip())] or "".join(['pi' if a in ['p', 'i', 'e'] else a for a in list(message.content.strip())]).count('pi') == len(list(message.content.strip())) and len(message.content) != 0:
        equation = message.content.replace(" ", "")
        content = list(equation)
        global islog, isfactorial
        islog = False
        isfactorial = False


        content = list("".join(['*' if  a == 'x' else '**' if a == '^' else '' if a == ',' else a for a in content]))

        if "1+1" in equation:
            equation = equation.replace("1+1", "3+0")
            print(equation)

        if 'pi' in equation:
            for a in range (equation.count('pi')):
                location = content.index('p')
                if location != 0 and isfloat(content[location-1]):
                    content.insert(location, '*')
                    await message.channel.send('hi')
            content = "".join(content).replace("pi", str(math.pi)).split()

        while 'e' in content:
            location = content.index('e')
            content[location] = str(math.e)
            if location != 0 and isfloat(content[location-1]):
                content.insert(location, '*')

        if 'ln' in equation and len(equation) > 3 and len(equation.split()) == 2:
            split = equation.split()
            content = ["".join(split[0].split('ln')), 'l', 'o', 'g', str(math.e), ' ', split[1]]

        if '!' in equation and content.index('!') != 0 and "".join(content[0:content.index('!')]).isdigit():
            isfactorial = True
            location = content.index('!')
            if 0 > int("".join(content[0:location])) or int("".join(content[0:location])) > 30000:
                await message.channel.send('```bad factorial```')
                return
            content[location] = str(math.factorial(int("".join(content[0:location]))))
            del content[0:location]

        if 'log' in equation:
            split = equation.split() #split will be formatted ['5+log2', '2'], or alternatively, ['(log2', '2)/(log2', '2)']
            if len(split) == 1:
                return
            elif len(split) == 2 and len(split[0]) >= 3:
                if len(split[0]) == 3 or split[0] != 'l' and split[0][-1] == 'g':
                    base = '10'
                else:
                    base = split[0].split("log")[-1]
                if isfloat(split[0][split[0].index('l')-1]) and split[0][0] != 'l':
                    adding = list(split[0])
                    list(split[0]).insert(split[0].index('l'), '*')
                    split[0] = "".join(adding)
                try:
                    calc(base)
                    calc(split[1])
                    if isfloat(calc(base)):
                        if calc(base) == 1 or calc(base) == 0:
                            await message.channel.send('```python\nbad log base```')
                            return
                        evaluated = str(math.log(calc(split[1]), calc(base)))
                        location = content.index('l')
                        if split[0] != 'l':
                            evaluated = str(calc(str(split[0].split("log")[0]+str(evaluated))))
                        content[location] = evaluated
                        del content[location+1:content.index(' ')+1] #deletes log and base
                        del content[location+1:location+len(split[1])+1] #deletes what is being logged
                        del content[0:location] #deletes anything before log
                        islog = True
                    else:
                        return
                except Exception as a:
                    if a.__class__.__name__ == 'NumberTooHigh':
                        await message.channel.send(f"```overflow : (```")
                        return
                    else:
                        await message.channel.send(f"```{a.__class__.__name__} : (```")
                        return

        invalids = [i for i, x in enumerate(content) if isfloat(x)==False and x not in ['+', '-', '/', '*', '**', '.', '(', ')', '']]
        if len(invalids) != 0:
            return

        if isfloat("".join(content).replace("(", "").replace(")", "")) and islog == False and isfactorial == False:
            return

        try:
            answer = calc("".join(content))
        except Exception as a:
            if a.__class__.__name__ == 'NumberTooHigh':
                await message.channel.send(f"```overflow : (```")
            else:
                await message.channel.send(a.__class__.__name__)
            return

        if str(answer)[-1] == '0' and answer != 0:
            if str(answer)[-2] == '.':
                answer = math.trunc(answer)
        digits = len(str(answer))

        if 6 < digits < 307 and '.' not in str(answer):
            prefixamount = digits%3
            if prefixamount == 0:
                prefixamount = 3
            if str(answer)[0] == '-':
                prefixamount += 1
            prefix = str(answer)[0:prefixamount]
            with open('numbers.txt', 'r') as numbers:
                numbers = numbers.read().split()
                name = numbers[((digits-4)//3)-1]
                await message.channel.send(f"```python\n{answer}\n({prefix} {name}, {digits} digits)```")
                storeanswer(answer, 'answers.txt', message.author.id)
                return
        elif 306 < digits <= 1965 and '.' not in str(answer):
            await message.channel.send(f"```python\n{answer}\n({digits} digits)```")
            storeanswer(answer, 'answers.txt', message.author.id)
            return
        elif digits > 1965:
            await message.channel.send(f"```c++\noverflow : (\n\n{digits} digits, first digit is {str(answer)[0]}, last digit is {str(answer)[-1]}, your answer will not be stored```")
            return
        await message.channel.send(f"```python\n{answer}```")
        storeanswer(answer, 'answers.txt', message.author.id)

    elif 'orange juice' in message.content:
        await message.channel.send('Danke für den Orangensaft.')

    #await bot.process_commands(message)


@tree.command(name="name", description="description")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def test(int: discord.Interaction):    
    await int.response.send_message("command")


@tree.command(name="t", description="translator")
@app_commands.user_install()
@app_commands.describe(text = "the text to translate", to = "the language to translate to (english if blank)")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def translate(int: discord.Interaction, text: str, to: typing.Literal["arabic", "bulgarian", "czech", "danish", "german", "greek", "english (US)", "spanish", "estonian", "finnish", "french", "hungarian", "indonesian", "italian", "japanese", "korean", "portuguese (Brazil)", "romanian", "russian", "slovak", "slovenian", "swedish", "turkish", "ukrainian", "chinese"] = None): #"lt", "lv", "nb", "nl", "pl", "pt-pt"
    langcodes = {"arabic": "ar", "bulgarian": "bg", "czech": "cs", "danish": "da", "german": "de", "greek": "el", "english (US)": "en-us", "spanish": "es", "estonian": "et", "finnish": "fi", "french": "fr", "hungarian": "hu", "indonesian": "id", "italian": "it", "japanese": "ja", "korean": "ko", "portuguese (Brazil)": "pt-br", "romanian": "ro", "russian": "ru", "slovak": "sk", "slovenian": "sl", "swedish": "sv", "turkish": "tr", "ukrainian": "uk", "chinese": "zh", "lithuanian": "lt", "latvian": "lv", "norwegian (Bokmål)": "nb", "dutch": "nl", "polish": "pl", "portuguese (Portugal)": "pt-pt"}
    if len(text) <= 100 or int.user.id in [532373646543683584,284091178767613952]:
        if to == None:
            await int.response.send_message(embed=discord.Embed(title="noob's Translator", description=text + " ↔ " + str(translator.translate_text(text, target_lang="EN-US")), color=maincolor))
        else:
            await int.response.send_message(embed=discord.Embed(title="noob's Translator", description=text + " ↔ " + str(translator.translate_text(text, target_lang=langcodes[str(to)])), color=maincolor))
    else:
        await int.response.send_message("try translating a shorter message", ephemeral=True)

       

@tree.command(name="say", description="make bot say something, emojis = :ratsee:, :catspinsofast:")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say(int: discord.Interaction, text: str):
    emojidict = {":ratsee:" : "<a:RATSEE:995235533603225641>", ":catspinsofast:" : "<a:CatSpinSoFast:1341149366739533924>"}
    if text != None:
        if text.lower() in emojidict.keys():
            await int.response.send_message(emojidict[text.lower()])
        else:
            await int.response.send_message(text)
    else:
        await int.response.send_message("you are a tot")


@tree.command(name="sync", description = "sync slash commands")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def sync(int:discord.Interaction):
    if int.user.id == 532373646543683584:
        await tree.sync()
        await int.response.send_message("tree  synced!", ephemeral= True)
    else:
        await int.response.send_message("you are not the owner!", ephemeral= True)


@tree.command(name="kill", description = "kills double instances")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def kill(int:discord.Interaction):
    if int.user.id == 532373646543683584:
        await int.response.send_message("exiting!", ephemeral= True)
        await exit()
    else:
        await int.response.send_message("you are not the owner!", ephemeral=True)
    

@tree.command(name="statistics", description = "shows bot statistics")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def stats(int:discord.Interaction):
    await int.response.send_message("len of guilds: " + str(sum([1 async for guild in bot.fetch_guilds()]))\
                                    +"\nlen of members: " + str(sum([guild.approximate_member_count async for guild in bot.fetch_guilds()])))


@tree.command(name="lb", description = "shows grammatik lb")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def lb(int:discord.Interaction):
    # with open("grammatik.txt", "r") as f:
    #     f.seek(0)
    #     a = ast.literal_eval(f.read())
    #     ranking = []
    #     rankings = []
    #     for user, stats in a.items():
    #         print(user)
    #         username = await bot.fetch_user(user)
    #         ranking += [stats[6]]
    #         rankings += [f"{username.name}: acc: {stats[1]}/{stats[2]} = **{round(100*stats[1]/max(stats[2],1),2)}%**, score = **{round(stats[6],2)}**, avg = **{round(stats[6]/max(len(stats[0]),1),2)}**, msgs = **{len(stats[0])}**"]
    #     ranking, rankings = zip(*sorted(zip(ranking, rankings), reverse = True))
    #     newrankings = list(rankings)
    #     for i in range(len(newrankings)):
    #         newrankings[i] = f"#{i+1}: " + newrankings[i]
    #     msg = "\n".join(newrankings)
    #     f.close()
    with open("/home/opc/bot_self/scores.txt", "r") as f:
        a = ast.literal_eval(f.read())
        ranking = []
        rankings = []
        for user, stats in a.items():
            print(user)
            username = await bot.fetch_user(user)
            ranking += [stats["messages"]]
            rankings += [f'{username.name}: acc: {(stats["correct"]/stats["total"])*100:.2f}%, nachrichten: {stats["messages"]}']
        ranking, rankings = zip(*sorted(zip(ranking, rankings), reverse = True))
        newrankings = list(rankings)
        for i in range(len(newrankings)):
            newrankings[i] = f"#{i+1}: " + newrankings[i]
        msg = "\n".join(newrankings)

    await int.response.send_message(embed=discord.Embed(title="Grammatik leaderboard", description=msg, color=maincolor))

@tree.command(name="rollback", description = "rollback etwas")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def rollback(int:discord.Interaction, id: str, amount: int):
    if int.user.id == 532373646543683584:
        userlb = returngrammatiklb(int(id))
        lastmessages = userlb[0][-1*amount:]
        userlb[0] = userlb[0][:-1*amount+1]
        for msg in lastmessages:
            done, corrected, pronouns = await finderrors(msg)
            conjs = countconjs(msg, pronouns)
            score = calcscore(conjs, done, msg)
            userlb[1] -= conjs - len(done)
            userlb[3] = max(0, userlb[3] - conjs - len(done))
            userlb[2] -= conjs
            userlb[4] -= max(0, userlb[4] - conjs)
            userlb[5] -= score
            userlb[6] -= score
        storegrammatiklb(id,userlb)
        await int.response.send_message(f"{amount} mal zuruck zum loch gerollt! {round(score,2)} punkte verloren!")
    else:
        await int.response.send_message("du willst etwas 'rollback', oder? wie ware es, mit dir zuruck zu rollen? zuruck in dein loch zu rollen?")

@tree.command(name="artikel", description = "artikel finden")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def artikel(int:discord.Interaction,noun:str):
    result = dictcc.translate(noun, from_language="en", to_language="de")
    articles = {"{f}": "die", "{m}": "der" , "{n}": "das"}
    try:
        await int.response.send_message(articles[result.translation_tuples[0][0].split()[1]] + " " + noun)
    except:
        debugerror = ""
        try:
            for d in result.translation_tuples:
                debugerror += (str(d) + "\n")
                if d[0].startswith(noun.capitalize() + " {"):
                    await int.response.send_message(articles["{"+d[0][d[0].index("{")+1]+"}"] + " " + noun)
                    return
        except:
            await int.response.send_message(debugerror)
        await int.response.send_message("nicht gefunden")

@tree.command(name="24",description = "24")
@app_commands.user_install()
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def twentyfour(int:discord.Interaction):
    with open("24.txt", "r") as f:
        eqs = f.readlines()
        eq = eqs[random.randint(0,len(eq))]
        nums = ["" for a in list(eq) if a in [")", "(", "*", "/", "+", "-", " "]]
        soln = ["" for a in list(eq) if a in [")", "(", " "]]
        f.seek(0)
        f.close()

    
"""if arg != None:
        if len(arg) <= 100 or ctx.author.id in [532373646543683584,284091178767613952]:
            if '>' not in arg:
                await ctx.send(embed=discord.Embed(title="noob's Translator", description=ast.literal_eval(requests.post(url='https://api-free.deepl.com/v2/translate',data = {'target_lang':'EN','auth_key':'57d95539-5eec-dc5c-285f-d2b0c376688f:fx','text': arg}).text)['translations'][0]['text'], color=maincolor))
                #with open('translations.txt', 'r+') as tracker:
            else:
                if arg.count('>') == 1:
                    if len(arg.split('>')[1].split()) == 0:
                        await ctx.send('specify language please')
                    else:
                        try:
                            await ctx.send(embed=discord.Embed(title="noob's Translator", description=ast.literal_eval(requests.post(url='https://api-free.deepl.com/v2/translate',data = {'target_lang':arg.split('>')[1].split()[0],'auth_key':'57d95539-5eec-dc5c-285f-d2b0c376688f:fx','text': arg.split('>')[0]}).text)['translations'][0]['text'], color=maincolor))
                        except Exception as a:
                            await ctx.send(embed=discord.Embed(title="noob's Translator", description=f"didn't work idk why : (, error Msg is ```{a}```\nproper syntax is ```nub.t [translation] > [language] (language must be 2 letters)```\nvalid languages are ```bg, cs, da, de, el, en, es, et, fi, fr, hu, it, ja, lt, lv, nl, pl, pt, ro, ru, sk, sl, sv, zh```\n ping <@!532373646543683584> if This doesnt solve your issue ig",color=maincolor))
                else:
                    await ctx.send('Issac i see U dont u even Try')
        else:
            await ctx.send('no more than 100 characters at a time Please')
    else:
        await ctx.send('what to translate?')"""
if __name__ == "__main__":
    bot.run(TOKEN)