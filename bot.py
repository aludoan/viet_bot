import discord, logging
from discord.ext import commands
import os
import asyncio

with open('token.txt') as file:
    vietToken = file.read().strip()
    
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w'),
                              logging.StreamHandler()]) 

logger = logging.getLogger('discord')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='v!', intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            cog_name = f'cogs.{filename[:-3]}'
            bot.load_extension(cog_name)
            print(f'Loaded {cog_name}')

@bot.event
async def on_command_error(ctx, error):
    logger.error(f'Error occurred: {error}', exc_info=True)

load_cogs()
bot.run(vietToken)