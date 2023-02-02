#!/usr/bin/env python3

# Import Python Modules
from dotenv import load_dotenv
import os
import discord
import sys
from datetime import datetime
from datetime import timedelta

discord_variables = {'DISCORD_TOKEN': '', 'DISCORD_GUILD': '', 'DISCORD_ADMINS': ''}


# Checks if .env exists, and creates one if it doesn't
if os.path.isfile('.env') is False:
    with open('.env', 'w') as f:
        f.write('# .env\n')
        for key in discord_variables.keys():
            f.write(key + '=\n')
    quit()
else:
    # Adds the variables from .env to enviromental variables
    load_dotenv()
    for key in discord_variables.keys():
        if key == 'DISCORD_TOKEN':
            discord_variables[key] = os.getenv(key)
        else:
            discord_variables[key] = os.getenv(key).split(',')

# Setting intents to default, and allow access to message content
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in discord_variables['DISCORD_GUILD']:
        guild = discord.utils.get(client.guilds, name=guild)
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


def check_Self_Post(message):
    if message.author == client.user:
        return True

def check_Admins(user):
    if user in discord_variables['DISCORD_ADMINS']:
        return True
   
def restart_Bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def getTimestamp(message):
    timestamp = str(message.created_at)
    timestamp = timestamp[11:19]
    return timestamp

def resetTimeStamp():
    time = datetime.now() + timedelta(hours=1)
    return time

def compareTime(message, resetTime):
    timestamp = getTimestamp(message)
    return timestamp > resetTime

def print_message(message):
    timestamp = getTimestamp(message)
    print(f'{timestamp}:{message.author.name}: {message.content}')

if __name__ == "__main__":
    print("This file contains the basic discord bot functions")
    sys.exit()