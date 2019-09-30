import discord
from discord.ext import commands

# TODO Change Ping and name to your cog name
class Example(commands.Cog, name='Example'):
    """Classic Ping->Pong example"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def example(self, ctx):
        """Unloads and then loads an extension"""
        # Send when the user says !ping
        await ctx.send("example")


def setup(bot):
    # Tell the bot about our cog
    # TODO Change Ping to your class name
    bot.add_cog(Example(bot))
