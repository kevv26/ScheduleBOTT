import discord
from discord.ext import commands
from logic import ScheduleButton

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Logged in as", bot.user)
    channel = bot.get_channel(913603642056122422)
    await channel.send("Hello! type !schedule to get started or !guide to know how it works.")

@bot.command()
async def schedule(ctx):
    await ctx.send("Choose an option: \n", view=ScheduleButton())

@bot.command()
async def guide(ctx):
    await ctx.send(file=discord.File("ScheduleBOTT/image/guide.png"))