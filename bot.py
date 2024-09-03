import discord, requests, logging
from discord.ext import commands
from googletrans import Translator

vietToken = YourToken

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w'),
                              logging.StreamHandler()]) 

logger = logging.getLogger('discord')
translator = Translator()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='! ', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Event: on_message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    logger.info(f'Received message: {message.content}')
    await bot.process_commands(message)

# Command: translate
@bot.slash_command(name = 'translate', description = 'translates text')
async def translate(ctx, *, text):
    translation = translator.translate(text, src='en', dest='vi')
    response = f"{text} in Vietnamese is **{translation.text}**"
    await ctx.respond(response)
    logger.info(f'Translate command used with argument: {text}')

# Error handling
@bot.event
async def on_command_error(ctx, error):
    logger.error(f'Error occurred: {error}', exc_info=True)

bot.run(vietToken)