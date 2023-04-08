#region lib's

#discord.py
import discord
from discord import app_commands
from discord.ext import commands

#log
import logging

#token
import utils.utils as utils

#api's import
from api.api_Speech import *
from api.api_Waifu import *
from api.api_Friend import *
from api.api_ChatGPT import *
from api.api_GoogleTranslate import *
from api.api_Joke import *

#others
import os
import random
import asyncio

#endregion

#region log.log
logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("cricital")
#endregion

#bot
Aya = commands.Bot(command_prefix='.', intents=utils.intents)


@Aya.event
async def on_ready():
  logging.info('Aya.dev is online!')
  await Aya.change_presence(status=discord.Status.idle,
                            activity=discord.Activity(
                              type=discord.ActivityType.listening,
                              name=".help"))
  try:
    synced = await Aya.tree.sync()
    logging.info(f"Synced {len(synced)} commands")
  except Exception as e:
    logging.critical(e)


@Aya.event
async def on_message(message):
  with open('blacklist.txt', 'r') as blacklist:
    for blackword in blacklist:
      if blackword.strip() in message.content:
        if message.author.name != 'Aya.dev':
          await message.delete()
          await message.channel.send(
            f"Küfür etme {message.author.mention} boomer.")
  await Aya.process_commands(message)


@Aya.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.text_channels, name='general')
  await channel.send(f"{member.mention} Hoşgeldin boomer")


@Aya.event
async def on_member_remove(member):
  channel = discord.utils.get(member.guild.text_channels, name='general')
  await channel.send(f"{member.mention} Siktir git boomer")


@Aya.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, limit=5):
  await ctx.channel.purge(limit=limit)


@Aya.command(alias=["copy"])
@commands.has_permissions(administrator=True)
async def clone_channel(ctx, limit=1):
  for i in range(limit):
    await ctx.channel.clone()


@Aya.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason="None"):
  await member.kick(reason=reason)
  await ctx.channel.send(f'{member.mention} isimli boomer sunucudan atıldı.')


@Aya.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason="None"):
  await member.ban(reason=reason)
  await ctx.channel.send(f'{member.mentionr} isimli boomer siki tuttu.')


@Aya.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for banned_user in banned_users:
    banned_user = banned_user.user
    if (member_name, member_discriminator) == (banned_user.name,
                                               banned_user.discriminator):
      await ctx.guild.unban(banned_user)
      await ctx.channel.send(
        f"{banned_user.mention} isimli boomerın defteri temizlendi.")


@Aya.tree.command(name="raffle", description="Hadi şanslı boomer kim görelim!")
async def raffle(interaction: discord.Interaction):
  lucky_boomer = random.choice(interaction.guild.members)
  await interaction.response.send_message(
    f"{lucky_boomer.mention} çekilişi kazandı!")


@Aya.tree.command(name="speech",
                  description="Hangi mesajı seslendirmemi istersin?")
@app_commands.describe(message="I am Eren Yeager")
async def speech(interaction: discord.Interaction, message: str):
  await interaction.response.defer()
  await asyncio.sleep(1)
  await interaction.followup.send(text_to_speech(message))


@Aya.tree.command(name="waifu", description="'Waifu'na ne söylemek istersin?")
@app_commands.describe(message="Slm")
async def waifu(interaction: discord.Interaction, message: str):
  await interaction.response.defer()
  await asyncio.sleep(1)
  await interaction.followup.send(waifu_chat(message))


@Aya.tree.command(name="chatgpt",
                  description="ChatGPT'ye ne söylemek istersin?")
@app_commands.describe(message="'Hello World' nasıl çalıştırılır?")
async def ai(interaction: discord.Interaction, message: str):
  await interaction.response.defer()
  await asyncio.sleep(1)
  await interaction.followup.send(openai(message))


@Aya.tree.command(name="friend",
                  description="'Arkadaş'ına ne söylemek istersin?")
@app_commands.describe(message="What's up bro?")
async def friend(interaction: discord.Interaction, message: str):
  await interaction.response.defer()
  await asyncio.sleep(1)
  await interaction.followup.send(chat_with_ai(message))


@Aya.tree.command(name="translate",
                  description="Ne çevirmemi istersin? Şuanlık sadece TR->EN")
@app_commands.describe(message="Ben seni sevduğumi da dünyalara bildirdim")
async def translate(interaction: discord.Interaction, message: str):
  await interaction.response.defer()
  await asyncio.sleep(1)
  await interaction.followup.send(translated_text(message))


@Aya.tree.command(name="joke", description="Şaka yapmakta profesyonelim.")
async def joke(interaction: discord.Interaction):
  await interaction.response.send_message(dadjoke())


Aya.run(utils.token)