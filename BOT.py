import io
import sys
import subprocess
import discord
from discord.ext import commands
import datetime
import time

# 設定
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')

# 自動
@bot.listen()
async def on_connect():
    channel = bot.get_channel(610463906896412685)
    await channel.send('BOTが更新され(もしくは復活し)ました')

@bot.listen()
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        dt_join = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        )
        embed = discord.Embed(title='ようこそ！', description='{0.mention}さん、とある宇宙の超雑談鯖へようこそ！\r「ルール関係」カテゴリにあるチャンネルはよく読んでおくことを推奨します。\r<#601046942092623924>には特に重要なことが書いてありますので、ご一読ください。'.format(
            member), timestamp=dt_join, color=0x3daee9)
        embed.set_thumbnail(url='https://i.imgur.com/Q8RRC0c.png')
        await channel.send(embed=embed)


@bot.listen()
async def on_member_remove(member):
    channel = member.guild.system_channel
    if channel is not None:
        dt_left = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        )
        LeftTime = dt_left.strftime('%Y年%m月%d日 %H:%M')
        await channel.send('{0.name}さんがサーバーを抜けました。\n - '.format(member) + LeftTime)

# コマンド
@bot.command()
async def help(ctx, tohelp='all'):
    if tohelp == 'all':
        embed = discord.Embed(title='現在利用可能なコマンドは以下のとおりです。',
                              description='', color=0x3daee9)
        embed.add_field(name='!!say', value='任意のテキストを送信します。', inline=False)
        embed.add_field(
            name='!!embed', value='埋め込みを作ります。詳しくは`s!help embed`をご覧ください。', inline=False)
        embed.add_field(name='!!dm', value='BOTがあなたにDMしてきます。', inline=False)
        embed.add_field(
            name='!!calc', value='BOTに計算させることができます。Pythonの標準機能を使用するため、高度なことはできません。', inline=False)
        embed.add_field(name='!!python',
                        value='Pythonのコマンドを実行し、実行結果を返します。', inline=False)
        embed.add_field(
            name='!!check', value='このBOTの稼働を確認します。他のコマンドが使えないときにお試しください。', inline=False)
        embed.add_field(name='!!mute', value='ユーザーをMutedにします。', inline=False)
        embed.add_field(name='!!unmute',
                        value='ユーザーのMutedを解除します。', inline=False)
        embed.add_field(name='!!help', value='この一覧を表示します。', inline=False)
        await ctx.send(embed=embed)
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法 ： `!!say (delete) <文字列>`', description='BOTに任意の文字列を送信させることができます。\n文字列の前にdeleteを入れることにより、本当にBOTが話しているように見せることもできます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'check':
        embed = discord.Embed(
            title='使用方法 : `s!check`', description='BOTの稼働を確認します。他のコマンドが使えないときにお試しください。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'embed':
        embed = discord.Embed(title='使用方法 : `s!embed <タイトル> <説明>`',
                              description='埋め込みを作成できます。現在はタイトルと説明のみに対応していますが、後々その他の項目も追加できるようにする予定です。\rタイトルや説明に空白を入れたい場合は、`"`で挟んでください。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'dm':
        embed = discord.Embed(title='使用方法 : `s!dm <文字列>`',
                              description='BOTがあなたにDMしてきます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'calc':
        embed = discord.Embed(title='使用方法 ： `!!calc <式>`',
                              description='BOTに計算させることができます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'python':
        embed = discord.Embed(title='使用方法 ： `!!python <コマンド>',
                              description='Pythonのコマンドを実行し、実行結果を返します。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'mute':
        embed = discord.Embed(title='使用方法 ： `!!mute <ユーザー>',
                              description='ユーザーをMutedにします。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'python':
        embed = discord.Embed(title='使用方法 ： `!!unmute <ユーザー>',
                              description='ユーザーのMutedを解除します。', color=0x3daee9)
        await ctx.send(embed=embed)


@bot.command()
async def say(ctx, *, message='使用方法 ： `!!say (delete) 文字列`'):
    if message.startswith('delete') == True:
        await discord.ext.commands.bot.discord.message.Message.delete(ctx.message)
        message = message.split()
        message[0] = ''
        message = ' '.join(message)
        message = message.strip()

    await ctx.send(message)


@bot.command()
async def check(ctx):
    await ctx.send('稼働中です')


@bot.command()
async def embed(ctx, title='', description=''):
    embed = discord.Embed(title=title, description=description)
    await ctx.send(embed=embed)


@bot.command()
async def dm(ctx, *, message=''):
    if message == '':
        await ctx.send('送信する文字列を指定してください。')
    await ctx.message.author.send(message)


@bot.command()
async def calc(ctx, *, formula):
    await ctx.send(eval(formula))


@bot.command()
async def python(ctx, *, toexe='print("コマンドを入力してください")'):
    DoAlthoughOver2000 = toexe.startswith('over2000')
    if DoAlthoughOver2000 == True:
        toexe = toexe.split(None, 1)
        if len(toexe) >= 2:
            toexe = toexe[1]
        else:
            toexe = 'print("コマンドを入力してください")'

    with open("temp.py", "w") as f:
        print(toexe, file=f)

    result = subprocess.run(
        'python temp.py', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    result = result.stdout.decode('utf-8')
    if len(result) + 6 >= 2000:
        if DoAlthoughOver2000 == True:
            result = result.splitlines()
            i = 1
            startline = 0
            for i in range(1, len(result) + 1):
                temp = result[startline:i]
                temp = '\n'.join(temp)
                if len(temp) + 6 >= 2000:
                    endline = i - 1
                    content = result[startline:endline]
                    content = '```\n' + '\n'.join(content) + '\n```'
                    startline = endline + 1
                    await ctx.send(content)
                else:
                    endline = i
            content = result[startline:endline]
            content = '```\n' + '\n'.join(content) + '\n```'
            await ctx.send(content)
        else:
            await ctx.send('出力された文字数が2000を超えています。続行するには`over2000`オプションをつけてください。')
    else:
        result = '```\n' + result + '\n```'
        await ctx.send(result)


@bot.command()
async def mute(ctx, user):
    muted = discord.abc.Snowflake
    muted.id = 500283244613468175
    user = ctx.message.mentions
    await user[0].add_roles(muted)


@bot.command()
async def unmute(ctx):
    muted = discord.abc.Snowflake
    muted.id = 500283244613468175
    user = ctx.message.mentions
    await user[0].remove_roles(muted)

# Botの起動とDiscordサーバーへの接続
bot.run('NjEwMzU3OTA3OTAwNDY1MTky.XZ1_ew.shpOyVFnjChZnTV1cSzdbh14oJU')
