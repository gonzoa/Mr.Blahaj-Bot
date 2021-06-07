import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="")

@bot.event
async def on_connect():
  print("Mr.Blahaj has landed.")

@bot.command()
async def Hello(ctx):
  await ctx.send ("Good morning! How are ya?") 

@bot.command()
async def Good(ctx):
  await ctx.send ("That's fintastic")  

@bot.command()
async def Bad(ctx):
  await ctx.send ("I'm sorry to hear that. Can I do anything for you?") 

@bot.command()
async def Won(ctx):
  await ctx.send ("Congratulations!!!") 

@bot.command()
async def Streaming(ctx):
  await ctx.send ("Awesome sauce! Post the link") 

@bot.command()
async def finals(ctx):
  await ctx.send ("Good luck") 

@bot.command()
async def Thanks(ctx):
  await ctx.send ("You're wuite welcome!") 

token=("ODUxNDc4MzMwODI5OTYzMzM1.YL42_Q.AJehTuVmLa8w4FF2khz6WKKIp-s")
bot.run(token)