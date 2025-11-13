import discord
import os
import random
import asyncio
import shutil
from discord.ext import commands

class Listen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def load_files(self, category: str):
        self.d = {}
        for num, filename in enumerate(os.listdir('cogs/data/audio/' + category)):
            letter = filename[:-4]
            filepath = os.path.join('cogs/data/audio/' + category, filename)
            self.d[num] = (letter, filepath)
        return 

    @commands.command(name= 'listen', help='trains listening skills')
    async def listen(self, ctx, category: str):
        self.load_files(category)

        await ctx.send(
            'The trainer will begin. Type **stop** to close the trainer'
        )

        correct = 0
        attempted = 0
        
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        
        last_pick = 0
        pick = last_pick
        while True:
            while pick == last_pick:
                pick = random.randint(0, len(self.d)-1)
            last_pick = pick
            letter, filepath = self.d[pick][0], self.d[pick][1]

            # Create and Send temp mp3 file
            new_filename = 'Guess!.mp3'
            temp_file_path = os.path.join('cogs/data/audio/' + category, new_filename)
            shutil.copyfile(filepath, temp_file_path)
            await ctx.send('**Which letter/word is this**?', file=discord.File(temp_file_path))
            os.remove(temp_file_path)

            try:
                user_answer = await self.bot.wait_for(
                    "message",
                    timeout=15.0, 
                    check=check
                )
            except asyncio.TimeoutError:
                await ctx.send(
                    f'You took too long. Try answering under 15 seconds next time'
                )
                continue
            else:
                if user_answer.content.lower() == 'stop':
                    await ctx.send(f'Score: {correct}/{attempted}')
                    if attempted == 0:
                        await ctx.send('See you next time!')
                    elif correct/attempted == 10/10:
                        await ctx.send('Perfect! 🎉🎉🎉')
                    elif correct/attempted > 8.5/10:
                        await ctx.send('Good Job! 👍')
                    elif correct/attempted > 6.9/10:
                        await ctx.send('You were almost there!')
                    else:
                        await ctx.send('There\'s always a next time!')
                    break
                elif user_answer.content.lower() == letter:
                    correct += 1
                    attempted += 1
                    await ctx.send(f'Correct')
                else:
                    attempted += 1
                    await ctx.send(f'Incorrect, the correct answer was **{letter}**')

def setup(bot):
    bot.add_cog(Listen(bot))

            