import discord
import emoji

import env
token = env.DISCORD_BOT_TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('リアクションつける用のサーバー起動')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    await message.add_reaction(emoji.se.one)
    await message.add_reaction(emoji.se.two)
    await message.add_reaction(emoji.se.three)

# Botの起動とDiscordサーバーへの接続
client.run(token)