import discord
from discord.ext import commands

class Vocab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.words = number_translations = [
            {'word': "một", 'translation': "One"},
            {'word': "hai", 'translation': "Two"},
            {'word': "ba", 'translation': "Three"},
            {'word': "bốn", 'translation': "Four"},
            {'word': "năm", 'translation': "Five"},
            {'word': "sáu", 'translation': "Six"},
            {'word': "bảy", 'translation': "Seven"},
            {'word': "tám", 'translation': "Eight"},
            {'word': "chín", 'translation': "Nine"},
            {'word': "mười", 'translation': "Ten"}
        ]


    @commands.command(Name='vocab', help='presents flashcards of vocab')
    async def vocab(self, ctx, args:str):
        for dict in self.words:
            if dict['word'] == args:
                word = args
                translation = dict['translation']
                embed = discord.Embed(
                    color=discord.Color.green(),
                    title = word,
                    description = translation
                )
                embed.set_footer(text='Numbers')
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Vocab(bot))