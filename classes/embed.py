import discord
from discord.ext import commands
import asyncio
from . import battle

class battleCog(commands.Cog):
    def __init__(self, bot, ctx):
        self.bot = bot  
        self.authorName = ctx.author.name

    @commands.command(name='battle', aliases=['b'])
    async def rouletteGame(self, ctx):
        embedMessage = discord.Embed(
            title = f"{self.authorName} quer batalhar!",
            description = "Reaja com ⚔️ para aceitar a batalha!",
            color = discord.Colour.red()
        )
        
        self.battleMessage = await ctx.send(embed = embedMessage)
        await self.battleMessage.add_reaction('⚔️')
        
        try:
            reaction, user = await self.botWaitFor(
                'reaction_add',
                check = lambda reaction, user: user != self.bot.user and user != self.authorName and reaction.emoji == '⚔️',
                timeout = 30.0
            )
            await self.startBattle(user)
        except asyncio.TimeoutError:
            await self.battleMessage.edit(embed = self.timeoutEmbed())
        
        async def startBattle(self, opponent):
            self.battleAccepted = True
            await self.battleMessage.edit(embed = self.battleAccepted(opponent))
            battle.startGame(self.authorName, opponent, self.battleMessage)
        
        def battleAccepted(self, opponent):
            return discord.Embed(
                title = f"A batalha entre {self.authorName} e {opponent} começou!"
            )
        
        def timeoutEmbed(self):
            return discord.Embed(
                title = f"Ninguém aceitou batalhar com {self.authorName}!",
                color = discord.Colour.yellow()
            )
            
def setup(bot):
    bot.add_cog(battleCog(bot))