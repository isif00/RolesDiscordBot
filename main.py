#https://discord.com/api/oauth2/authorize?client_id=1136663747025449030&permissions=1477737188384&scope=bot

import os
import pandas as pd

import discord
from dotenv import load_dotenv

file_path = 'info.csv'
column_name = 'discordID'

data_frame = pd.read_csv(file_path)
discord_original = data_frame[column_name].tolist()

discord_ids = set(discord_original)

role_id = 1134192225782349905

load_dotenv()

# Initiating the bot
intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

ids_list = []

@client.event
async def on_ready():
    print('[DONE]: We have logged in as {0.user}'.format(client))

@client.event
# Making Sure the bot doesn't reply to himself
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    
    if message.content.startswith('$assign'):
        print("starting")
        role = message.guild.get_role(role_id)
        for guild in client.guilds:
            for member in guild.members:
                for discord_id in discord_ids:
                    if str(discord_id) == str(member):
                        if role in member.roles:
                            pass
                        else:
                            await member.add_roles(role)
                            print("done!")
client.run(token)