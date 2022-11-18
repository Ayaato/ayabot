import discord
from discord.ext import commands
import utils
from logging import *
import os
import random

basicConfig(level=INFO, filename="log.log", filemode="w",
            format="%(asctime)s - %(levelname)s - %(message)s")

debug("debug")
info("info")
warning("warning")
error("error")
critical("cricital")


Ayabot = commands.Bot(command_prefix='*', intents=utils.intents)


@Ayabot.event
async def on_ready():
    info('ready.')


@Ayabot.event
async def on_message(message):
    with open('blacklist.txt', 'r') as blacklist:
        for blackword in blacklist:
            if blackword.strip() in message.content:
                await message.delete()
                await message.channel.send(f"Don't swear boomer. {message.author.mention}")
                await message.delete()
    await Ayabot.process_commands(message)


@Ayabot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    await channel.send(f"{member.mention} Welcome boomer")


@Ayabot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    await channel.send(f"{member.mention} Sg boomer")


@Ayabot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, limit=5):
    await ctx.channel.purge(limit=limit)


@Ayabot.command(alias=["copy"])
@commands.has_permissions(administrator=True)
async def clone_channel(ctx, limit=1):
    for i in range(limit):
        await ctx.channel.clone()


@Ayabot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason="None"):
    await member.kick(reason=reason)
    await ctx.channel.send(f'{member.mention} is a kicked boomer.')


@Ayabot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason="None"):
    await member.ban(reason=reason)
    await ctx.channel.send(f'{member.mentionr} is a fucked boomer.')


@Ayabot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_user in banned_users:
        banned_user = banned_user.user
        if (member_name, member_discriminator) == (banned_user.name, banned_user.discriminator):
            await ctx.guild.unban(banned_user)
            await ctx.channel.send(f"{banned_user.mention}'s notebook cleaned.")

@Ayabot.command()
async def raffle(ctx):
    lucky_boomer = random.choice(ctx.guild.members)
    await ctx.channel.send(f"{lucky_boomer.mention} won the raffle!")

Ayabot.run(utils.token)
