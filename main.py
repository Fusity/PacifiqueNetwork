import discord
import os
import time
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = str(input("Set your token here :\n>>>"))
PREFIX = os.getenv('COMMAND_PREFIX')

bot = commands.Bot(command_prefix=PREFIX)

sleep = time.sleep(0.5)

@bot.event
async def on_ready():
    print('Logged as ')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')
'''async def on_message(message):
    if message.author.bot:
        return'''

@bot.event
async def on_member_join(member):
    print("Konsole")
'''    guild = member.guild
    total_member = guild.member_count
    server_stats = discord.utils.get(guild.categories, name="Server's Stats")
    member_count = discord.utils.get(guild.voice_channels, name="Member count : {}".format(total_member), category=server_stats)
    
    


    if not server_stats:
        await guild.create_category(name="Server's Stats", position=0)
    if not member_count:
        await guild.create_voice_channel(name="Member count : {}".format(total_member), category=server_stats)
    await guild.create_text_channel(name="Welcome")'''


@bot.event
async def on_guild_channel_delete(channel):
    guild = channel.guild

    network_channel = discord.utils.get(guild.text_channels, name="network", category=None)

    if not network_channel:
        channel = await guild.create_text_channel(name="network", category=None, position=1)
        await channel.send("""***La PacifiqueCreation :***

**PacifiqueCreation** est une __fédération Discord__, une __communauté discord__ dédié et fondé **__principalement dans un but d'entraide pour tout utilisateurs Discord.__**
**Pour vous aider dans des démarches de créations/présentations de discord complètes et personnalisés.**

__**Nous proposons des services tels que :**__

:gear: : __Création et développement de **serveur discord**__

:gear: : __**Création et développement** spécial de **votre** propre **bot discord.**__

:gear: : __Création et développement de **graphismes**__ 

:gear: : __Création et développement d'une __**vidéo avec montage** pour la présentation de votre serveur/bot discord/autre chose sous __format vidéo.__

Tout cela est conçu par des __personnes professionnelles, compétentes et expérimentés dans leur(s) domaine(s).__

__La **PacifiqueCreation** propose des services et des tarfis avec le système network affilé aux communautés créés ou en payant directement le concepteur.__

**__DISCORD :__** https://discord.gg/QPnFqvk""")
 

@bot.command()
async def hello(message):

    guild = message.guild
    a = 21
    total_member = guild.member_count
    server_stats = discord.utils.get(guild.categories, name="Server's Stats")
    member_count = discord.utils.get(guild.voice_channels, name="Member count : {}".format(total_member), category=server_stats)
    
    if not server_stats:
        await guild.create_category(name="Server's Stats", position=0)
    
    #sleep

    elif not member_count:
        await guild.create_voice_channel(name="Member count : {}".format(total_member), category=server_stats)
    #print(total_member)


if __name__ == '__main__':
    bot.run(TOKEN)