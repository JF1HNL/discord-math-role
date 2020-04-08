from discord.ext import commands
import discord
import os
import traceback
import emoji
import data

# token = os.environ['DISCORD_BOT_TOKEN']


import env
token = env.DISCORD_BOT_TOKEN

# bot = commands.Bot(command_prefix='/')


# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')


# bot.run(token)

# -----------------------------------------------------------

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send(f'{message.author.mention} にゃーん')

@client.event  
async def on_raw_reaction_add(payload):
    if str(payload.message_id) not in data.cid_emoji:
        return
    if payload.emoji.name not in data.cid_emoji[str(payload.message_id)]:
        return
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    role_id = data.cid_emoji[str(payload.message_id)][payload.emoji.name]
    geted_role = guild.get_role(role_id)
    await member.add_roles(geted_role)
    return_channel = client.get_channel(697409978067058728)
    await return_channel.send(f"{member.mention} さん：{geted_role}ロールを付与しました。")

@client.event  
async def on_raw_reaction_remove(payload):
    if str(payload.message_id) not in data.cid_emoji:
        return
    if payload.emoji.name not in data.cid_emoji[str(payload.message_id)]:
        return
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    role_id = data.cid_emoji[str(payload.message_id)][payload.emoji.name]
    geted_role = guild.get_role(role_id)
    await member.remove_roles(geted_role)
    return_channel = client.get_channel(697409978067058728)
    await return_channel.send(f"{member.mention} さん：{geted_role}ロールを削除しました。")

# Botの起動とDiscordサーバーへの接続
client.run(token)