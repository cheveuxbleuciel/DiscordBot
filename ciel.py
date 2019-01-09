import discord
import configparser

inifile = configparser.ConfigParser()
inifile.read('./ciel.ini','UTF-8')

channel_id=inifile.get('text_channel','id')
bot_token=inifile.get('bot','token')

text_channel = discord.Object(id=channel_id)
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん!"
            await client.send_message(text_channel, m)

client.run(bot_token)
