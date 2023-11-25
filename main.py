import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta

# Load values from .env file
load_dotenv()

# Access the bot token from the environment variables
bot_token = os.getenv('bot_token')

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='.', intents=intents)

# Dictionary to store the last time each user used the !roll command
user_last_roll = {}

# Dictionary to store the join time of each user
user_join_time = {}

@client.event
async def on_ready():
    print('Bot is ready.')
    print('---------------------------')
    
    for guild in client.guilds:
        # Fetch members to ensure the most up-to-date information
        async for member in guild.fetch_members(limit=None):
            user_join_time[member.id] = member.joined_at

    # for i in user_join_time:
        # print(f'{i}: {user_join_time[i]}')
    
    # Loop through all members and print their join times in order
    # for guild in client.guilds:
        # print(f'Guild: {guild.name}')
        # sorted_members = sorted(guild.members, key=lambda m: m.joined_at)
        # for member in sorted_members:
            # print(f'{member.name} joined at: {member.joined_at}')

@client.command()
async def roll(ctx, chosen_number: int):

    # Check if the user is an admin
    is_admin = any(role.permissions.administrator for role in ctx.author.roles)

    # If the user is not an admin, check if they have been in the server for at least 24 hours
    join_time = user_join_time.get(ctx.author.id, ctx.author.joined_at)
    time_in_server = datetime.now(timezone.utc) - join_time
    if not is_admin and time_in_server.total_seconds() < 86400:
        await ctx.send("You must be in the server for at least 24 hours to use the .roll command.")
        return
        # will end the command here if the user is not an admin and has not been in the server for at least 24 hours

    # Check if the user has used the command in the last 24 hours
    # if not is_admin:
    last_roll_time = user_last_roll.get(ctx.author.id, datetime.now(timezone.utc) - timedelta(days=1))
    current_time = datetime.now(timezone.utc)
    time_difference = current_time - last_roll_time
    time_remaining = timedelta(seconds=86400 - time_difference.total_seconds())
    time_remaining_str = str(time_remaining).split(".")[0]  # Remove the microseconds part

    # If less than 24 hours have passed, inform the user and exit the command
    if not is_admin and time_difference.total_seconds() < 86400:
        await ctx.send(f"You've already rolled in the last 24 hours. You can roll again in: {time_remaining_str}")
        return

    # Generate a random number between 0 and the chosen number
    rolled_number = random.randint(0, chosen_number)

    # Define usable emojis
    diceEmoji = discord.utils.get(client.emojis, name='4dicepink')
    catGirlHelloEmoji = discord.utils.get(client.emojis, name='catgirlhello')
    bunnySpinEmoji = discord.utils.get(client.emojis, name='emoji_2')

     # Define the messages for different rolled numbers
    messages = {
        0: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***naked full body in bed pic*** for free! DM me now! {bunnySpinEmoji}",
        10: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***detailed dick rate*** for free! DM me now! {bunnySpinEmoji}",
        20: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***feet with ass pic*** for free! DM me now! {bunnySpinEmoji}",
        30: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***boob pic*** for free! DM me now! {bunnySpinEmoji}",
        40: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***pussy pic*** for free! DM me now! {bunnySpinEmoji}",
        50: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***feet pic*** for free! DM me now! {bunnySpinEmoji}",
        69: f"{catGirlHelloEmoji} WOW! You rolled {rolled_number}! you won a ***sexy lingerie pic*** for free! DM me now! {bunnySpinEmoji}"
    }

    if rolled_number in messages:
        await ctx.send(messages[rolled_number])
    else: # Send a message with the rolled number
        await ctx.send(f'{diceEmoji} **You rolled {rolled_number} in the range 0-{chosen_number}. Try again tomorrow** {diceEmoji}')

    # Update the last roll time for the user
    user_last_roll[ctx.author.id] = datetime.now(timezone.utc)

@client.command()
async def timeout(ctx, user: discord.User):

    # Check if the user is an admin
    is_admin = any(role.permissions.administrator for role in ctx.author.roles)

    # Check if the specified user has used the command in the last 24 hours
    if not is_admin and user.id in user_last_roll:
        last_roll_time = user_last_roll[user.id]
        current_time = datetime.now(timezone.utc)
        time_difference = current_time - last_roll_time

        # If less than 24 hours have passed, calculate and send the time remaining
        if time_difference.total_seconds() < 86400:
            time_remaining = timedelta(seconds=86400 - time_difference.total_seconds())
            time_remaining_str = str(time_remaining).split(".")[0]  # Remove the microseconds part
            await ctx.send(f"{user.name}'s time remaining before they can roll again: {time_remaining_str}")
        else:
            await ctx.send(f"{user.name} is not in timeout. They can roll anytime.")
    else:
        await ctx.send(f"{user.name} is not in timeout. They can roll anytime.")

client.run(bot_token)