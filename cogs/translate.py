import discord
from discord.ext import commands
from googletrans import Translator

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()
    
    @commands.command(name = 'translate', help = 'translates text')
    async def translate(self, ctx, *, text: str):
        translation = self.translator.translate(text, src='en', dest='vi')
        if translation.pronunciation:
            response = response = f"'Translation: **{translation.text} (translation.pronunciation)**"
        else:
            response = f"Translation: **{translation.text}**"
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Translate(bot))


