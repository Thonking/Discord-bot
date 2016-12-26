import discord
from discord.ext import commands
import random
import asyncio

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

@bot.command()
async def shiet(content='content'):
    await bot.say('shiet ' * 5) 
    await bot.say('shiet ' * 5)     
    await bot.say('shiet ' * 5) 
    await bot.say('shiet ' * 5) 
    await bot.say('shiet ' * 5) 

@bot.command()
async def RNA2Protein(content='RNA'):
    if len(content) % 3 != 0:
        await bot.say('Please give a sequence that has a number of bases that is divisible by 3')

    for i in content:
        if i is not 'G' or i is not 'C' or i is not 'A' or i is not 'U':
            await bot.say('Only G, A, C, or U please.')
            break

@bot.command()
async def DNA2RNA(content='DNA'):
    
    for i in content:
        
        if i is 'A':
            await bot.say('U', end="")
        elif i is 'G':
            await bot.say('C', end="")
        elif i is 'C':
            await bot.say('G', end="")
        elif i is 'T':
            await bot.say('A', end="")
        else: 
            await bot.say('Only G, A, C, or T please.')
            break
    

@bot.command()
async def stephcurry(content='stephcurry'):
    await bot.say('Steph Curry my ass.')



bot.run('lul')
