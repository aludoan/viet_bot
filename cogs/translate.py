import discord
from discord.ext import commands
from deep_translator import GoogleTranslator

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = GoogleTranslator(source='en', target='vi')
    
    @commands.command(name='translate', help='translates text from English to Vietnamese')
    async def translate(self, ctx, *, text: str):
        try:
            translation = self.translator.translate(text)
            response = f"Translation: **{translation}**"
            await ctx.send(response)
        except Exception as e:
            await ctx.send(f"❌ Translation error: {str(e)}")

def setup(bot):
    bot.add_cog(Translate(bot))