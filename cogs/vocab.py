import discord
import json
from discord.ext import commands

class Vocab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='vocab', help='presents flashcards of vocab')
    async def vocab(self, ctx, category:str):
        if category == "categories":
            embed = discord.Embed(
                color = discord.Color.blue(),
                title = 'Vocabulary Categories',
                description='• Numbers\n'
            )
            await ctx.send(embed=embed)
            return
        # Send initial page
        current_page = 0
        with open("cogs/data/vocab/" + category + ".json", 'r', encoding='utf-8') as file:
            self.words = json.load(file)['words']
        word = self.words[0]
        embed = discord.Embed(
            color = discord.Color.green(),
            title = word['vietnamese'],
            description = '**Translation:** ' + word['english'] + '\n' + '**Example: **' + word['example']
        )
        embed.set_footer(text='Numbers | Page ' + str(current_page + 1) + " of " + str(len(self.words)))
        message = await ctx.send(embed=embed)
        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")

        def check(reaction, user):
            return (user == ctx.author and reaction.message.id == message.id and 
                    str(reaction.emoji) in ["⬅️", "➡️"])
        
        # Option for flipping embedded pages
        while True:
            reaction,user = await self.bot.wait_for(
                "reaction_add",
                timeout = 60.0,
                check = check)
            
            if str(reaction.emoji) == "➡️" and (current_page + 1) != len(self.words):
                current_page += 1
            elif str(reaction.emoji) == "⬅️" and (current_page - 1) != -1:
                current_page -= 1

            word = self.words[current_page]
            new_embed = discord.Embed(
                color=discord.Color.green(),
                title = word['vietnamese'],
                description = '**Translation:** ' + word['english'] + '\n' + '**Example: **' + word['example']
            )

            await message.edit(embed=new_embed)

def setup(bot):
    bot.add_cog(Vocab(bot))