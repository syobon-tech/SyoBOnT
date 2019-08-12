from discord.ext import commands

# 設定
bot = commands.Bot(command_prefix='s!')

# コマンド
@bot.command()
async def help(ctx, tohelp='all'):
    if tohelp == 'all':
        await ctx.send('現在使用できるコマンドは以下のとおりです。\r```\rsay   任意のテキストを送信します。現在空白は2つまで対応しています。\rcheck BOTの稼働を確認します。他のコマンドが使えないときにお試しください。\r```')
    if tohelp == 'say':
        await ctx.send('使用方法  `s!say 文字列`\r「文字列」で指定したテキストを送信します。')
    if tohelp == 'check':
        await ctx.send('使用方法  `s!check`\rBOTの稼働を確認します。他のコマンドが使えないときにお試しください。')

@bot.command()
async def say(ctx, first='テキストを入れてください', second='', third=''):
    await ctx.send(first + ' ' + second + ' ' + third)

@bot.command()
async def check(ctx):
    await ctx.send("稼働中です")

# Botの起動とDiscordサーバーへの接続
bot.run('NjEwMzU3OTA3OTAwNDY1MTky.XVEJKg.ksWbKRLkGD3ucm41LZf5B05QznI')