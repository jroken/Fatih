import discord
from discord.ext.commands import Bot

TOKEN = "TOKENİNİZ"

client = discord.Client()
bot = Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot Hazır " + str(bot.user))
    

@bot.event
async def on_message(message):
    if message.author == client.user:
        return



    if message.content == "Fatih":
        await message.channel.send("Efm Knks")
        
#Buradan İtibaren yukardaki kodu kopyalayıp istediğiniz komutları ekleyebilirsiniz


bot.run(TOKEN)
