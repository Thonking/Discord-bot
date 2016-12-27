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
async def shiet():
    await bot.say('shiet ' * 5) 
    await bot.say('shiet ' * 5)     
    await bot.say('shiet ' * 5) 
    await bot.say('shiet ' * 5) 
    await bot.say('shiet ' * 5) 

@bot.command()
async def RNA2Protein(content='RNA'):
    for i in content:
            if i is not 'G' and i is not 'C' and i is not 'A' and i is not 'U':
                await bot.say('Only G, A, C, or U please.')
                break

    if len(content) % 3 != 0:
        await bot.say('Please give a sequence that has a number of bases that is divisible by 3')
        
    else:
        amino_acids = {'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L', 'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L', 'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M', 'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V', 'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S', 'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A', 'UAU' : 'Y', 'UAC' : 'Y', 'UAA' : 'Stop', 'UAG' : 'Stop', 'CAU' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K', 'GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'UGU' : 'C', 'UGC' : 'C', 'UGA' : 'Stop', 'UGG' : 'W', 'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGU' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R', 'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'}
        codons = [content[i:i+3] for i in range(0, len(content), 3)]
        protein = [amino_acids[x] for x in codons]
        await bot.say(''.join(protein))



@bot.command()
async def DNA2RNA(content='DNA'):
    for base in content:
        if base is not 'G' and base is not 'C' and base is not 'A' and base is not 'T':
            await bot.say('Only G, A, C, or T please.')
            break
    transcribe = {'A' : 'U', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
    sequence = list(content)
    sequence = [transcribe[base] for base in sequence]
    await bot.say(''.join(sequence))
    

@bot.command()
async def stephcurry():
    await bot.say('Steph Curry my ass.')



bot.run('lul')
