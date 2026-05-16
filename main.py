import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name= attachment.filename
            if not file_name.lower().endswith((".png", ".jpg", ".jpeg")):
              await ctx.send("lütfen png, jpg veya jpeg formatında bir dosya gönderin!!")
              continue
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send(f"dosya kaydedildi: {file_name}")
            await ctx.send(get_class(model_path='keras_model.h5', labels_path="labels.txt",image_path= file_name))
        
    else:   
        await ctx.send("Dosya göndermeyi unuttun!!")

bot.run("")
