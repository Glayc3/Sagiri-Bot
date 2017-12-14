import discord, asyncio, random, importlib, datetime
from discord.ext.commands import Bot
from discord.ext import commands
sagiri_bot = Bot(command_prefix = ".")


glayce_mention = "<@274250969322356747>"
oban_mention = "<@332608659609747456>"

helpTitle = "Sagiri will help you!!"
debugTitle = "Debug menu"
infoTitle = "Info"
helpText = """```         funky things i can do
 
         Hey - Caps don't matter
```
```
              **Random Chat**
```
-hello / yo / hi / hey
-waddup / wassup
-speak Python
-what languages can you speak @sagiri-bot?
-is Glayce cool?
-who are you @sagiri-bot?
-what is the answer to life, the universe and everything?
-who shot first
-u mad @sagiri-bot?
-puns pls
-encouragement pls
-i love you @sagiri-bot
```
                  **Memes**
```
-it's Wednesday my dudes
-free robux/roblox hacks/how to watch big time rush for free
-welcome to my mine
-understandable
-cracking a cold one with the boys/crack a cold one with the boys
-send me some fire mixtapes @sagiri-bot
-roast me @sagiri-bot
```
                  **NSFW**
```
-hentai please
```
          **Other/Unimplemented**
```
-ping
-help me @sagiri-bot
-info @sagiri-bot
"""
debugText = """-send all mixtapes @sagiri-bot"""
infoText = """``` ***Sagiri-Bot***```
**Made by Glayce**
*Special thanks to ibby*

```
Links
```
[Youtube](https://www.youtube.com/c/glayce)
[Github](https://github.com/Glayc3)
"""
helpColour = 0xFFC5FE

puns=[]
mixtapes=[]
roasts = []

now = datetime.datetime.now()


@sagiri_bot.event
async def on_message(message):

    mesg_lower = message.content.lower()
    auth_mention = message.author.mention


    if mesg_lower == "help me " + sagiri_bot.user.mention:
        helpme = discord.Embed(title = helpTitle, description = helpText, colour = helpColour)
        await sagiri_bot.send_message(message.channel, embed = helpme)

    elif mesg_lower == "debug menu":
        author = str(message.author)
        if author.lower() == "glayce#2155":
            debugmenu = discord.Embed(title = debugTitle, description = debugText, colour = helpColour)
            await sagiri_bot.send_message(message.channel, embed=debugmenu)
        else:
            await sagiri_bot.send_message(message.channel, "you're not glayce scrub")

    elif mesg_lower == "info " + sagiri_bot.user.mention:
        infobox = discord.Embed(title = infoTitle, description = infoText, colour = helpColour)
        await sagiri_bot.send_message(message.channel, embed = infobox)


    elif mesg_lower in ["hello","yo","hi","hey"] and not message.author.bot:

        reply = random.choice(["wUS pOPPING jIMBO???","ayy","ey","hi","ayop","hello"]) + " " + auth_mention

        await sagiri_bot.send_message(message.channel, reply)

    elif mesg_lower == "waddup" or mesg_lower == "wassup":
        await sagiri_bot.send_message(message.channel, "The ceiling")

    elif mesg_lower == "speak python":
        await sagiri_bot.send_message(message.channel,"sorry if my python is a bit rusty\nit's been a while\nprint \'hello world\'")

    elif mesg_lower.startswith("what languages can you speak " + sagiri_bot.user.mention):
        await sagiri_bot.send_message(message.channel, "while i was raised in python, alas I only know english\nblame " + glayce_mention)

    elif mesg_lower == "is glayce cool?":
        await sagiri_bot.send_message(message.channel,"glayce is a gay idiot also here's his channel\nhttps://www.youtube.com/channel/UCRyRCqipLrzqmMBBMyfBHvQ/featured")

    elif mesg_lower.startswith("who are you " + sagiri_bot.user.mention):
        await sagiri_bot.send_message(message.channel, "a higher intellegence who has descended onto the world as a guardian angel though reincarnated as a discord bot")

    elif mesg_lower.startswith("what is the answer to life, the universe and everything"):
        await sagiri_bot.send_message(message.channel,"42")
o
    elif mesg_lower.startswith("who shot first"):
        await sagiri_bot.send_message(message.channel,"say han or i'll be the first to shoot here buddy")

    elif mesg_lower.startswith("you mad " + sagiri_bot.user.mention):
        await sagiri_bot.send_message(message.channel,"um no\nhttp://i.imgur.com/zGgTrZW.gif")

    elif mesg_lower == "puns pls":
        await sagiri_bot.send_message(message.channel,puns[random.randint(0,len(puns)-1)])

     elif mesg_lower == "encouragement pls":
        await sagiri_bot.send_message(message.channel, "https://pics.me.me/if-u-feel-sad-remember-that-the-world-is-4-5-19131844.png")

    elif mesg_lower.startswith("i love you "+ sagiri_bot.user.mention):
        await sagiri_bot.send_message(message.channel, "https://cdn.ram.moe/BJjSz0zxx.gif")

    elif mesg_lower == "it's wednesday my dudes":
        if now.strftime("%A").lower() == "wednesday":
            await sagiri_bot.send_message(message.channel,"yea boiiii")
        else:
            await sagiri_bot.send_message(message.channel,"actually it's "+ now.strftime("%A").lower())

    elif mesg_lower in [ "free robux", "roblox hacks", "how to watch big time rush for free" ]:
        await sagiri_bot.send_message(message.channel,"why is the FBI here?")

    elif mesg_lower.startswith("welcome to my mine") and not message.author.bot:

        lyrics = [
                "wE aRe MiNiNg DiAMoNdS",
                "We DoN't GoTtA sTrIp MiNe",
                "We DoN't HaVe To FiGhT mObS",
                "wElCoMe tO mY mInE",
                "pLaY tHaT nOtE bLoCk nIcElY",
                "sHoW mE aLl tHoSe eMeRaLdS",
                "wE dOn'T gOtTa dOdGe lAvA"
                ]

        for line in lyrics:
            await sagiri_bot.send_message(message.channel, line)
            await asyncio.sleep(1)

    elif mesg_lower == "understandable":
        await sagiri_bot.send_message(message.channel,"have a great day")

    elif mesg_lower == "crack a cold one with the boys" or mesg_lower == "cracking a cold one with th boys":
        await sagiri_bot.send_message(message.channel,"is this enough?\nhttps://images-na.ssl-images-amazon.com/images/I/81vK-0Gd6IL._SX522_.jpg")

    elif mesg_lower == "send me some fire mixtapes " +sagiri_bot.user.mention:
        await sagiri_bot.send_message(message.channel,mixtapes[random.randint(0,len(mixtapes)-1)])
    elif mesg_lower == "roast me " + sagiri_bot.user.mention:
        await sagiri_bot.send_message(message.channel, roasts[(random.randint(0, len(roasts)-1))]+ " " + auth_mention)

    elif mesg_lower == "hentai please" or mesg_lower == "porn please":
        await sagiri_bot.send_message(message.channel,"https://cdn.ram.moe/ryWB210zgl.png")

    elif mesg_lower == "ping":
        ping_message = [
            "pong :)",
            "what? did you think I could ping?",
            "honestly, you expect too much from " + glayce_mention
            ]
        for line in ping_message:
            await sagiri_bot.send_message(message.channel, line)
            await asyncio.sleep(1)


sagiri_bot.run("TOKEN HERE")
