#!/usr/bin/env python3

# Importing Python Modules
import time

# Importing Script Modules
import discord_functions
import oracle_deck

token = discord_functions.discord_variables['DISCORD_TOKEN']
decks = []

@discord_functions.client.event
async def on_message(message):
    self_post = discord_functions.check_Self_Post(message)
    if self_post:
        return
    
    admin_check = discord_functions.check_Admins(message.author.name)
    if admin_check:
        if message.content.startswith('?restart'):
            await message.channel.send('Restarting')
            discord_functions.restart_Bot()
    discord_functions.print_message(message)

    if message.content.startswith('?reading'):
            deck = oracle_deck.Deck()
            card = deck.drawCard()
            await message.channel.send(file=discord_functions.discord.File(card))
            return

if __name__ == "__main__":
    discord_functions.client.run(token)
