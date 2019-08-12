import datetime
import discord
from discord.ext import commands

# 設定
dt_now = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
)
update = dt_now.strftime('%Y年%m月%d日 %H:%M')
bot = commands.Bot(command_prefix='s!')
bot.remove_command('help')

# コマンド
@bot.command()
async def help(ctx, tohelp='all'):
    if tohelp == 'all':
        embed = discord.Embed(title='現在利用可能なコマンドは以下のとおりです。', description='', color=0x3daee9)
        embed.add_field(name='s!say', value='任意のテキストを送信します。', inline=False)
        embed.add_field(name='s!check', value='このBOTの稼働を確認します。他のコマンドが使えないときにお試しください。', inline=False)
        embed.add_field(name='s!embed', value='埋め込みを作ります。詳しくは`s!help embed`をご覧ください。', inline=False)
        embed.add_field(name='s!latestupdate', value='BOTが最後に更新された時間を表示します。', inline=False)
        embed.add_field(name='s!dm', value='BOTがあなたにDMしてきます。', inline=False)
        embed.add_field(name='s!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法 ： `s!say <文字列>`', description='任意のテキストを送信します。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'check':
        embed = discord.Embed(title='使用方法 : `s!check`', description='BOTの稼働を確認します。他のコマンドが使えないときにお試しください。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'embed':
        embed = discord.Embed(title='使用方法 : `s!embed <タイトル> <説明>`', description='埋め込みを作成できます。現在はタイトルと説明のみに対応していますが、後々その他の項目も追加できるようにする予定です。\rタイトルや説明に空白を入れたい場合は、`"`で挟んでください。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'latestupdate':
        embed = discord.Embed(title='使用方法 : `s!latestupdate`', description='BOTが最後に更新された時間を表示します。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'dm':
        embed = discord.Embed(title='使用方法 : `s!dm <文字列>`', description='BOTがあなたにDMしてきます。', color=0x3daee9)
        await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, arg='使用方法 ： `s!say 文字列`'):
    await ctx.send(arg)

@bot.command()
async def check(ctx):
    await ctx.send('稼働中です')

@bot.command()
async def embed(ctx, title='', description=''):
    embed = discord.Embed(title=title, description=description)
    await ctx.send(embed=embed)

@bot.command()
async def latestupdate(ctx):
    await ctx.send(update)

@bot.command()
async def dm(ctx, *, message=''):
    if message == '':
        await ctx.send('送信する文字列を指定してください。')
    await ctx.message.author.send(message)

# Botの起動とDiscordサーバーへの接続
bot.run('NjEwMzU3OTA3OTAwNDY1MTky.XVEJKg.ksWbKRLkGD3ucm41LZf5B05QznI')