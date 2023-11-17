import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os
import datetime

# Load values from .env file
load_dotenv()

# Access the bot token from the environment variables
bot_token = os.getenv('bot_token2')

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='.', intents=intents)

# Dictionary to store the last time each user used the !roll command

@client.event
async def on_ready():
    print('Spinner bot is ready.')
    print('---------------------------')

@client.command()
async def spin(ctx):

    # Generate a random number between 0 and the chosen number
    rolled_number = random.randint(1, 25)

    # Define usable emojis
    diceEmoji = discord.utils.get(client.emojis, name='4dicepink')
    bunnySpinEmoji = discord.utils.get(client.emojis, name='emoji_2')

     # Define the messages for different rolled numbers
    messages = {
        1: f"{diceEmoji} You rolled {rolled_number}! you won a ***full body nude***! {bunnySpinEmoji}",
        2: f"{diceEmoji} You rolled {rolled_number}! you won a ***feetpic x2***! {bunnySpinEmoji}",
        3: f"{diceEmoji} You rolled {rolled_number}! you won a ***pussy pic x2***! {bunnySpinEmoji}",
        4: f"{diceEmoji} You rolled {rolled_number}! you won a ***pussy rub vid***! {bunnySpinEmoji}",
        5: f"{diceEmoji} You rolled {rolled_number}! you won a ***ass pic x3*** ! {bunnySpinEmoji}",
        6: f"{diceEmoji} You rolled {rolled_number}! Oops you won ***nothing*** ! {bunnySpinEmoji}",
        7: f"{diceEmoji} You rolled {rolled_number}! ***Spin again*** ! {bunnySpinEmoji}",
        8: f"{diceEmoji} You rolled {rolled_number}! Oops you won ***nothing*** ! {bunnySpinEmoji}",
        9: f"{diceEmoji} You rolled {rolled_number}! you won a ***boob pic x2***! {bunnySpinEmoji}",
        10: f"{diceEmoji} You rolled {rolled_number}! you won a ***full body nude***! {bunnySpinEmoji}",
        11: f"{diceEmoji} You rolled {rolled_number}! you won a ***cute outfit pic***! {bunnySpinEmoji}",
        12: f"{diceEmoji} You rolled {rolled_number}! you won a ***thigh***! {bunnySpinEmoji}",
        13: f"{diceEmoji} You rolled {rolled_number}! you won a ***feet vid***! {bunnySpinEmoji}",
        14: f"{diceEmoji} You rolled {rolled_number}! you won a ***sexy lingerie gif***! {bunnySpinEmoji}",
        15: f"{diceEmoji} You rolled {rolled_number}! you won a ***ass vid***! {bunnySpinEmoji}",
        16: f"{diceEmoji} You rolled {rolled_number}! you won a ***feetpic***! {bunnySpinEmoji}",
        17: f"{diceEmoji} You rolled {rolled_number}! you won a ***naked in bed pic***! {bunnySpinEmoji}",
        18: f"{diceEmoji} You rolled {rolled_number}! ***Spin again***! {bunnySpinEmoji}",
        19: f"{diceEmoji} You rolled {rolled_number}! you won a ***vibrator vid***! {bunnySpinEmoji}",
        20: f"{diceEmoji} You rolled {rolled_number}! Oops you won ***nothing***! {bunnySpinEmoji}",
        21: f"{diceEmoji} You rolled {rolled_number}! you won a ***pussy pic x2***! {bunnySpinEmoji}",
        22: f"{diceEmoji} You rolled {rolled_number}! you won a ***boob pic***! {bunnySpinEmoji}",
        23: f"{diceEmoji} You rolled {rolled_number}! you won a ***dildo ride vid***! {bunnySpinEmoji}",
        24: f"{diceEmoji} You rolled {rolled_number}! you won a ***pussy pic***! {bunnySpinEmoji}",
        25: f"{diceEmoji} You rolled {rolled_number}! you won a ***buttplug insert vid***! {bunnySpinEmoji}",

    }

    await ctx.send(messages[rolled_number])
    

client.run(bot_token)