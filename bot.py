import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")  # TOKEN pobierany z Railway, NIE wpisujemy go tutaj

BOOKING_LINK = "https://link-do-umawiania-wizyt.pl"
PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot jest online jako {bot.user}")

@bot.command()
async def wizyta(ctx):
    embed = discord.Embed(
        title="✂️ Umów wizytę u barbera!",
        description=f"Kliknij w link poniżej:\n➡️ {BOOKING_LINK}",
        color=0x00ff99
    )
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    keywords = ["wizyta", "umów", "umow", "termin", "strzyżenie", "strzyzenie"]

    if any(word in message.content.lower() for word in keywords):
        embed = discord.Embed(
            title="✂️ Chcesz umówić wizytę?",
            description=f"Zrobisz to tutaj:\n➡️ {BOOKING_LINK}",
            color=0x0099ff
        )
        await message.channel.send(embed=embed)

    await bot.process_commands(message)

bot.run(TOKEN)
