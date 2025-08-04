import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from gpt_engine import get_trade_idea

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

@bot.tree.command(name="analyze", description="Get an AI-based trade idea for any symbol")
async def analyze(interaction: discord.Interaction, symbol: str):
    await interaction.response.defer()
    result = get_trade_idea(symbol)
    await interaction.followup.send(f"📊 Trade idea for `{symbol.upper()}`:\n\n{result}")

bot.run(TOKEN)
