import discord
from discord.ext import commands

# 設定
bot = commands.Bot(command_prefix='s!')
bot.remove_command('help')

# コマンド
@bot.command()
async def help(ctx, tohelp='all'):
    if tohelp == 'all':
        embed = discord.Embed(title='SyoBOnT', description='現在利用可能なコマンドは以下のとおりです。:', color=0x3daee9)
        embed.add_field(name='s!say', value='任意のテキストを送信します。現在、空白は二個まで対応しています。', inline=False)
        embed.add_field(name='s!check', value='BOTの稼働を確認します。他のコマンドが使えないときにお試しください。', inline=False)
        embed.add_field(name='s!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法　s!say 文字列', description='任意のテキストを送信します。現在、空白は二個まで対応しています。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'check':
        embed = discord.Embed(title='使用方法　s!check', description='BOTの稼働を確認します。他のコマンドが使えないときにお試しください。', color=0x3daee9)
        await ctx.send(embed=embed)

@bot.command()
async def say(ctx, first='テキストを入れてください', second='', third=''):
    await ctx.send(first + ' ' + second + ' ' + third)

@bot.command()
async def check(ctx):
    await ctx.send('稼働中です')

# Botの起動とDiscordサーバーへの接続
bot.run('NjEwMzU3OTA3OTAwNDY1MTky.XVEJKg.ksWbKRLkGD3ucm41LZf5B05QznI')