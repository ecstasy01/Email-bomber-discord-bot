import discord
import colorama
import asyncio
import json

from colorama import init, Fore
from discord.ext import commands

from bomber import *

colorama.init(autoreset=True)

config = json.loads(
    open('./data/config.json').read()
)

client = commands.Bot(
    command_prefix = config['prefix']
)

client.remove_command('help')

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
processes = set()

@client.event
async def on_ready():
    print('Bot is running')

@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(
        title="Oops shit happened",
        description=f"Oops error: {error}",
        color=0x7289DA
    )

    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Email bomber - Help page",
        description=f"Commands:\n{config['prefix']}bomb (email) (amount)\n\nCredits:\nBased on [bagarrattaa's email bomber](https://github.com/bagarrattaa/email-nuker)\nBot made by: [ecstasy](https://cracked.io/ecstasy)",
        color=0x7289DA
    )

    await ctx.send(embed=embed)

@client.command()
async def bomb(ctx, email, amount: int):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    
    if '@' and '.' not in email:
        embed = discord.Embed(
            title="Oops shit happened",
            description=f"'{email}' is not a valid email",
            color=0x7289DA
        )

        await ctx.send(embed=embed)


    elif amount > config['mail_limit']:

        embed = discord.Embed(
            title="Oops shit happened",
            description=f"{amount} exceeds the limit of {config['mail_limit']}",
            color=0x7289DA
        )

        await ctx.send(embed=embed)


    elif ctx.author.id in processes:
        embed = discord.Embed(
            title="Oops shit happened",
            description=f"You already have a task running please wait.",
            color=0x7289DA
        )

        await ctx.send(embed=embed)

    
    else:
        try:
            processes.add(ctx.author.id)
            embed = discord.Embed(
                title="Enter a subject",
                description=f"Please enter a subject below",
                color=0x7289DA
            )

            ask = await ctx.send(embed=embed)
            subject_ = await client.wait_for("message", check=check, timeout=20)
            subject = subject_.content
            subject = subject.replace(" ","%20")

            await subject_.delete()
            await ask.delete()

            embed = discord.Embed(
                title="Enter a message",
                description=f"Please enter a message below",
                color=0x7289DA
            )

            ask = await ctx.send(embed=embed)
            message_ = await client.wait_for("message", check=check, timeout=20)
            message = message_.content
            message = message.replace(" ","%20")

            await message_.delete()
            await ask.delete()

            embed = discord.Embed(
                title="Starting to send emails..",
                description=f"Please wait while we send out emails to {email}",
                color=0x7289DA
             )

            discord_message = await ctx.send(embed=embed)

            send = await allah(email, subject, message, amount)
            
            embed = discord.Embed(
                title = send[0],
                description = send[1],
                color=0x7289DA
            )

            await discord_message.edit(embed=embed)
            processes.remove(ctx.author.id)

        except asyncio.TimeoutError:
            processes.remove(ctx.author.id)
            await ask.delete()

            embed = discord.Embed(
                title="Some oops shit happened",
                description=f"Your bitch ass is so slow reply faster next time.",
                color=0x7289DA
            )

            await ctx.send(embed=embed)

if __name__ == '__main__':
    client.run(config['token'])
