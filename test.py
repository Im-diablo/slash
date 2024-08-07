import os 
import discord
from discord import app_commands
from discord.ext import commands
import gdown

bot = commands.Bot(command_prefix="n", intents=discord.Intents.all())
url = 'https://drive.google.com/u/0/uc?id=1D0RKtHoBIPLS8EQSVtiYT-DsTxSh9B2R'
output = 'token.txt'
gdown.download(url, output, quiet=False)

with open('token.txt') as f:
      TOKEN = f.readline()
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hey {interaction.user.mention}! My latency is {round(bot.latency * 1000)}ms", ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "synced")
async def say(interaction: discord.Interaction, thing_to_say: str, to: discord.Member): 
    await interaction.response.send_message(f"{interaction.user.mention} said: '{thing_to_say}' to {to.mention}")
        
bot.run(TOKEN)
