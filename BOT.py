from discord.ext import commands

# 設定
bot = commands.Bot(command_prefix='s!')

# コマンド
@bot.command()
async def say(ctx, content='メンテナンス中'):
    await ctx.send(content)


@bot.command()
async def check(ctx):
    await ctx.send("稼働中です")

# Botの起動とDiscordサーバーへの接続
bot.run('NjEwMzU3OTA3OTAwNDY1MTky.XVEJKg.ksWbKRLkGD3ucm41LZf5B05QznI')