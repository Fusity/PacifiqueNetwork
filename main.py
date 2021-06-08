import discord
import os
import time
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()

def askToken():
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        TOKEN = str(input("Set your TOKEN here :\n>>>"))
    return TOKEN
def askPrefix():
    PREFIX = os.getenv('COMMAND_PREFIX')
    if not PREFIX:
        PREFIX = str(input("Set your PREFIX here :\n>>>"))
    return PREFIX

bot = commands.Bot(command_prefix=askPrefix())

sleep = time.sleep(0.5)
pc = os.getenv('PACIFIQUE_EMOJI')
network = os.getenv('NETWORK_NAME')
link = "https://discord.gg/QPnFqvk"
embed=discord.Embed(title="PacifiqueCreation", description="""**PacifiqueCreation** est une __fédération Discord__, une __communauté discord__ dédié et fondé **__principalement dans un but d'entraide pour tout utilisateurs Discord.__**
    **Pour vous aider dans des démarches de créations/présentations de discord complètes et personnalisés.**""", color=0x122be6)

# Add author, thumbnail, fields, and footer to the embed
#embed.set_author(name="PacifiqueCreation", url="https://discord.gg/QPnFqvk")

#embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

embed.add_field(name="__**Nous proposons des services tels que :**__\n", value=pc, inline=False) 
embed.add_field(name=":gear: : __Création et développement de **serveur discord**__", value=pc, inline=False)
embed.add_field(name=":gear: : __**Création et développement** spécial de **votre** propre **bot discord.**__", value=pc, inline=False)
embed.add_field(name=":gear: : __Création et développement de **graphismes**__", value=pc, inline=False)
embed.add_field(name=":gear: : __Création et développement d'une __**vidéo avec montage** pour la présentation de votre serveur/bot discord/autre chose sous __format vidéo.__", value=pc, inline=False)
embed.add_field(name="Tout cela est conçu par des __personnes professionnelles, compétentes et expérimentés dans leur(s) domaine(s).__", value=pc, inline=False)
embed.add_field(name="__La **PacifiqueCreation** propose des services et des tarifs avec le système network affilié aux communautés créés ou en payant directement le concepteur.__", value=pc, inline=False)

#embed.set_footer(text="Powered by Fusity.tar.gz and ender_creeps")

@bot.event
async def on_ready():
    print('Logged as ')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')
    guild = bot.guilds
    print(guild)
    network_channel = bot.get_channel(name=network, category=None)
    print(network_channel)
    """network_channel = discord.utils.get(guild.text_channels, name=network, category=None)
    print(network_channel)"""
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

    network_channel = discord.utils.get(guild.text_channels, name=network, category=None)

    if not network_channel:
        channel = await guild.create_text_channel(name=network, category=None, position=1)
        await channel.send(embed=embed)
        await channel.send(link)

@bot.event
async def on_message_delete(message):
    guild = message.guild
    channel = discord.utils.get(guild.text_channels, name=network, category=None)

    
    if not message.channel == embed or not message.channel == link and message.channel == channel:
        await message.channel.purge(limit=None)
        await channel.send(embed=embed)
        await channel.send(link)

@bot.event
async def on_message(message):
    guild = message.guild
    channel = discord.utils.get(guild.text_channels, name=network, category=None)
    author = message.author

    if not message.author.bot and message.channel == channel:
        await message.channel.purge(limit=None)
        await message.channel.send(embed=embed)
        await message.channel.send(link)

@bot.command()
async def hello(message):

    guild = message.guild
    a = 21
    total_member = guild.member_count
    server_stats = discord.utils.get(guild.categories, name="SERVER'S STATS")
    member_count = discord.utils.get(guild.voice_channels, name="Member count : {}".format(total_member), category=server_stats)
    
    if not server_stats:
        await guild.create_category(name="SERVER'S STATS", position=0)
    
    #sleep

    elif not member_count:
        await guild.create_voice_channel(name="Member count : {}".format(total_member), category=server_stats)
    #print(total_member)


if __name__ == '__main__':
    bot.run(askToken())