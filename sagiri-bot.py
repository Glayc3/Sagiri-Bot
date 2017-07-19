import discord, asyncio, random, importlib, datetime
from discord.ext.commands import Bot
from discord.ext import commands
sagiri_bot = Bot(command_prefix=".")


glayce_mention = "<@274250969322356747>"
oban_mention = "<@332608659609747456>"

puns=[]
mixtapes=[]
now = datetime.datetime.now()

@sagiri_bot.event
async def on_message(message):

    mesg_lower = message.content.lower()
    auth_mention = message.author.mention


    if mesg_lower in ["hello", "yo", "hi", "hey"] and not message.author.bot:

        reply = random.choice(["wUS pOPPING jIMBO???","ayy","ey","hi","ayop","hello"]) + " " + auth_mention

        await sagiri_bot.send_message(message.channel, reply)

    elif mesg_lower == "waddup" or mesg_lower == "wassup":
        await sagiri_bot.send_message(message.channel, "The ceiling")##

    elif mesg_lower == "speak python":
        await sagiri_bot.send_message(message.channel,"sorry if my python is a bit rusty\nit's been a while\nprint \'hello world\'")

    elif mesg_lower.startswith( "what languages can you speak " + sagiri_bot.user.mention ):
        await sagiri_bot.send_message(message.channel, "while i was raised in python, alas I only know english\nblame " + glayce_mention)

    elif mesg_lower == "is glayce cool?":
        await sagiri_bot.send_message(message.channel,"glayce is a gay idiot also here's his channel\nhttps://www.youtube.com/channel/UCRyRCqipLrzqmMBBMyfBHvQ/featured")

    elif mesg_lower.startswith( "who are you " + sagiri_bot.user.mention ):
        await sagiri_bot.send_message(message.channel, "a higher intellegence who has descended onto the world as a guardian angel though reincarnated as a discord bot")

    elif mesg_lower.startswith( "what is the answer to life, the universe and everything" ):
        await sagiri_bot.send_message(message.channel,"42")

    elif mesg_lower.startswith( "who shot first" ):
        await sagiri_bot.send_message(message.channel,"say han or i'll be the first to shoot here buddy")

    elif mesg_lower.startswith( "you mad " + sagiri_bot.user.mention ):
        await sagiri_bot.send_message(message.channel,"um no\nhttp://i.imgur.com/zGgTrZW.gif")

    elif mesg_lower == "puns pls":
        await sagiri_bot.send_message(message.channel,puns[random.randint(0,len(puns)-1)0)

    elif mesg_lower == "send me some fire mixtapes":
        await sagiri_bot.send_message(message.channel,mixtapes[random.randint(0,len(mixtapes)-1)0)

    elif mesg_lower == "encouragement pls":
        pass #same as above

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
