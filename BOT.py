import io
import os
import sys
import subprocess
import math
import discord
from discord.ext import commands
from discord.ext import tasks
import datetime
import time
import asyncio
import urllib.request
import random

# 設定
bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')
startup = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=9))
    )
waiting_url = []
waiting_file = []
shingekined = False

# 自動
@bot.listen()
async def on_member_join(member):
    if member.guild.id == 486487795293093888:
        channel = member.guild.system_channel
        if channel is not None:
            dt_join = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=9))
            )
            embed = discord.Embed(title='ようこそ！', description='{0.mention}さん、とある宇宙の超雑談鯖へようこそ！\r「ルール関係」カテゴリにあるチャンネルはよく読んでおくことを推奨します。\r<#601046942092623924>には特に重要なことが書いてありますので、ご一読ください。'.format(member), timestamp=dt_join, color=0x3daee9)
            embed.set_thumbnail(url='https://i.imgur.com/Q8RRC0c.png')
            await channel.send(embed=embed)

            online = member.guild.get_role(682180183595417650)
            await member.add_roles(online)


@bot.listen()
async def on_member_remove(member):
    if member.guild.id == 486487795293093888:
        channel = member.guild.system_channel
        if channel is not None:
            dt_left = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=9))
            )
            LeftTime = dt_left.strftime('%Y年%m月%d日 %H:%M')
            await channel.send('{0.name}さんがサーバーを抜けました。\n - '.format(member) + LeftTime)

@bot.listen()
async def on_raw_reaction_add(ctx):
    if ctx.channel_id == 601396253301014580:
        if ctx.guild_id == 486487795293093888:
            guild = bot.get_guild(486487795293093888)
            user = guild.get_member(ctx.user_id)
            if ctx.emoji.name == '🎵':
                role = guild.get_role(499891499761270826)
            elif ctx.emoji.name == '🀄':
                role = guild.get_role(638367989565095946)
            elif ctx.emoji.name == '🔢':
                role = guild.get_role(601729109281996800)
            elif ctx.emoji.name == '🔡':
                role = guild.get_role(602807063550099457)
            elif ctx.emoji.name == '⏪':
                role = guild.get_role(601384237530087424)
            elif ctx.emoji.name == '🔔':
                role = guild.get_role(605187648927039519)
            elif ctx.emoji.name == '🎧':
                role = guild.get_role(497004207782494218)
            elif ctx.emoji.name == '🔕':
                role = guild.get_role(603965872456859651)
            else:
                return
            await user.add_roles(role)
            await user.send('`' + role.name + '`役職を付与しました。')

@bot.listen()
async def on_raw_reaction_remove(ctx):
    if ctx.channel_id == 601396253301014580:
        if ctx.guild_id == 486487795293093888:
            guild = bot.get_guild(486487795293093888)
            user = guild.get_member(ctx.user_id)
            if ctx.emoji.name == '🎵':
                role = guild.get_role(499891499761270826)
            elif ctx.emoji.name == '🀄':
                role = guild.get_role(638367989565095946)
            elif ctx.emoji.name == '🔢':
                role = guild.get_role(601729109281996800)
            elif ctx.emoji.name == '🔡':
                role = guild.get_role(602807063550099457)
            elif ctx.emoji.name == '⏪':
                role = guild.get_role(601384237530087424)
            elif ctx.emoji.name == '🔔':
                role = guild.get_role(605187648927039519)
            elif ctx.emoji.name == '🎧':
                role = guild.get_role(497004207782494218)
            elif ctx.emoji.name == '🔕':
                role = guild.get_role(603965872456859651)
            else:
                return
            await user.remove_roles(role)
            await user.send('`' + role.name + '`役職を削除しました。')

@tasks.loop(hours=24)
async def checkrenew():
    global startup
    now = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=9))
        )
    workdays = now - startup
    if workdays.days >= 9:
        user = bot.get_user(371837989619499018)
        await user.send('BOT稼働から9日が経過しました。Renewしてください。')

@tasks.loop(hours=168)
async def resetshingekined():
    global shingekined
    shingekined = False

@bot.listen()
async def on_ready():
    if checkrenew.get_task() is None:
        checkrenew.start()
    if resetshingekined.get_task() is None:
        resetshingekined.start()

# コマンド
@bot.command()
async def help(ctx, tohelp='all'):
    if tohelp == 'all':
        await ctx.send('コマンドリスト：\nhttps://syobon-tech.github.io/SyoBOnT/')
    if tohelp == 'say':
        embed = discord.Embed(title='使用方法 ： `!!say (delete) <文字列>`', description='BOTに任意の文字列を送信させることができます。\n文字列の前にdeleteを入れることにより、本当にBOTが話しているように見せることもできます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'check':
        embed = discord.Embed(title='使用方法 : `!!check`', description='BOTの稼働を確認します。他のコマンドが使えないときにお試しください。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'embed':
        embed = discord.Embed(title='使用方法 : `!!embed <タイトル> <説明>`', description='埋め込みを作成できます。現在はタイトルと説明のみに対応していますが、後々その他の項目も追加できるようにする予定です。\rタイトルや説明に空白を入れたい場合は、`"`で挟んでください。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'dm':
        embed = discord.Embed(title='使用方法 : `!!dm <文字列>`', description='BOTがあなたにDMしてきます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'calc':
        embed = discord.Embed(title='使用方法 ： `!!calc <式>`', description='BOTに計算させることができます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'python':
        embed = discord.Embed(title='使用方法 ： `!!python <コマンド>', description='Pythonのコマンドを実行し、実行結果を返します。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'poll':
        embed = discord.Embed(title='使用方法 ： `!!poll タイトル|選択肢1|選択肢2|選択肢3|...`', description='投票を行えます。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'join':
        embed = discord.Embed(title='使用方法 ： `!!join`', description='音声チャンネルに入ります。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'play' or tohelp == 'p':
        embed = discord.Embed(title='使用方法 ： `!!play <URL>`', description='音声チャンネル内で動画を再生します。`!!p <URL>`でもOKです。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'queue' or tohelp == 'q':
        embed = discord.Embed(title='使用方法 ： `!!queue`', description='動画再生のキューを表示します。`!!q`でもOKです。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'skip' or tohelp == 's':
        embed = discord.Embed(title='使用方法 ： `!!skip`', description='再生中の動画をスキップします。`!!s`でもOKです。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'disconnect' or tohelp == 'dis':
        embed = discord.Embed(title='使用方法 ： `!!disconnect`', description='音声チャンネルから抜けます。`!!dis`でもOKです。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'mute':
        embed = discord.Embed(title='使用方法 ： `!!mute <ユーザー>', description='ユーザーをMutedにします。管理者にしか使用できません。', color=0x3daee9)
        await ctx.send(embed=embed)
    if tohelp == 'unmute':
        embed = discord.Embed(title='使用方法 ： `!!unmute <ユーザー>', description='ユーザーのMutedを解除します。管理者にしか使用できません。', color=0x3daee9)
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
    await ctx.send('稼働中です。')


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
    result = eval(formula)
    result = str(result)
    if len(result) >= 2000:
        loop = 0
        start = 0
        end = 2000
        finish = len(result)
        while loop == 0:
            if end >= finish:
                await ctx.send(result[start:])
                break
            await ctx.send(result[start:end])
            start = end
            end += 2000
    await ctx.send(eval(formula))


@bot.command()
async def python(ctx, *, toexe='print("コマンドを入力してください。")'):
    DoAlthoughOver2000 = toexe.startswith('over2000')
    if DoAlthoughOver2000 == True:
        toexe = toexe.split(None, 1)
        if len(toexe) >= 2:
            toexe = toexe[1]
        else:
            toexe = 'print("コマンドを入力してください。")'

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
async def poll(ctx, *, poll):
    await discord.ext.commands.bot.discord.message.Message.delete(ctx.message)
    poll = poll.split('|')
    if len(poll) <= 2:
        error = await ctx.send('構文が間違っているか、選択肢が少なすぎます。')
        await asyncio.sleep(5)
        await discord.ext.commands.bot.discord.message.Message.delete(error)
    else:
        out = ':regional_indicator_q: ' + poll[0]
        loop = len(poll) - 1
        loop = loop / 10
        loop = math.ceil(loop)
        for i in range(loop):
            num = i * 10
            if len(poll) >= num + 2:
                if i >= 1:
                    out = ':one: ' + poll[num + 1]
                else:
                    out += '\n\n:one: ' + poll[num + 1]
            if len(poll) >= num + 3:
                out += '\n:two: ' + poll[num + 2]
            if len(poll) >= num + 4:
                out += '\n:three: ' + poll[num + 3]
            if len(poll) >= num + 5:
                out += '\n:four: ' + poll[num + 4]
            if len(poll) >= num + 6:
                out += '\n:five: ' + poll[num + 5]
            if len(poll) >= num + 7:
                out += '\n:six: ' + poll[num + 6]
            if len(poll) >= num + 8:
                out += '\n:seven: ' + poll[num + 7]
            if len(poll) >= num + 9:
                out += '\n:eight: ' + poll[num + 8]
            if len(poll) >= num + 10:
                out += '\n:nine: ' + poll[num + 9]
            if len(poll) >= num + 11:
                out += '\n:keycap_ten: ' + poll[num + 10]
            msg = await ctx.send(out)
            if len(poll) >= num + 2:
                await msg.add_reaction('1️⃣')
            if len(poll) >= num + 3:
                await msg.add_reaction('2️⃣')
            if len(poll) >= num + 4:
                await msg.add_reaction('3️⃣')
            if len(poll) >= num + 5:
                await msg.add_reaction('4️⃣')
            if len(poll) >= num + 6:
                await msg.add_reaction('5️⃣')
            if len(poll) >= num + 7:
                await msg.add_reaction('6️⃣')
            if len(poll) >= num + 8:
                await msg.add_reaction('7️⃣')
            if len(poll) >= num + 9:
                await msg.add_reaction('8️⃣')
            if len(poll) >= num + 10:
                await msg.add_reaction('9️⃣')
            if len(poll) >= num + 11:
                await msg.add_reaction('🔟')

@bot.command()
async def mute(ctx, user, limit=0):
    role = ctx.guild.get_role(615091084372213760)
    if ctx.author in role.members:
        channel = ctx.guild.get_channel(501317011490734080)
        isint = type(limit) is int
        if isint == False:
            await ctx.send("使い方が間違っています。")
        else:
            muted = ctx.guild.get_role(500283244613468175)
            user = ctx.message.mentions
            await user[0].add_roles(muted)
            if limit == 0:
                await channel.send(user[0].name + 'さんがMuteされました。')
            else:
                await channel.send(user[0].name + 'さんが' + str(limit) + '分間Muteされました。')
                limit = limit * 60
                await asyncio.sleep(limit)
                await user[0].remove_roles(muted)
                await channel.send(user[0].name + 'さんのMute期間が終わりました。')

@bot.command()
async def unmute(ctx):
    role = ctx.guild.get_role(615091084372213760)
    if ctx.author in role.members:
        channel = ctx.guild.get_channel(501317011490734080)
        muted = ctx.guild.get_role(500283244613468175)
        user = ctx.message.mentions
        await user[0].remove_roles(muted)
        await channel.send(user[0].name + 'さんのMuteが解除されました。')

@bot.command()
async def shingekin(ctx, number=-1):
    if ctx.channel.id == 624886257771872256:
        global shingekined
        if shingekined:
            await ctx.send('1週間以内に`!shingekin`コマンドが実行されています。時間を開けて再試行してください。')
        else:
            shingekined = True
            if number == -1:
                number = random.randint(1, 17)
            filepath = '/app/shingekin/' + str(number) + '.jpg'
            with open(filepath, "rb") as f:
                await ctx.send(file=discord.File(fp=f))




@bot.command()
async def join(ctx):
    global voice_client
    try:
        voice_client
    except NameError:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
        await ctx.send('接続しました。')
        voice_client = ctx.message.guild.voice_client
        if os.path.isfile('./temp.opus'):
            subprocess.run(['rm', './temp.opus'])

@bot.command(aliases=['p'])
async def play(ctx, url=''):
    if url == '' and not ctx.message.attachments:
        ctx.send('URLを指定するか、ファイルを添付してください。')
    global voice_client
    try:
        voice_client
    except NameError:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
        voice_client = ctx.message.guild.voice_client
        if os.path.isfile('./temp.opus'):
            subprocess.run(['rm', './temp.opus'])
    if voice_client.is_playing():
        if ctx.message.attachments:
            global waiting_file
            waiting_file.append(ctx.message.attachments[0])
            url = 'メッセージに添付されたファイル'
        global waiting_url
        waiting_url.append(url)
        if autonext.get_task() is None:
            autonext.start()
        await ctx.send('キューに追加しました。')
    else:
        if ctx.message.attachments:
            await ctx.send('ファイルをロード中...')
            await ctx.message.attachments[0].save('temp.opus')
        else:
            await ctx.send('URLを解析中...')
            if url in '.':
                urllib.request.urlretrieve(url, 'temp.opus')
            else:
                result = subprocess.run(['python', './youtube-dl', url, '--audio-format', 'opus', '-x', '-q', '-o', './temp.opus'])
                if result.returncode != 0:
                    await ctx.send('URLの解析に失敗しました。')
        source = discord.FFmpegPCMAudio('./temp.opus')
        voice_client.play(source)
        await ctx.send('再生開始しました。')

@bot.command(aliases=['dis'])
async def disconnect(ctx):
    global voice_client
    global waiting_url
    if voice_client:
        autonext.stop()
        waiting_url = []
        if os.path.isfile('./temp.opus'):
            subprocess.run(['rm', './temp.opus'])
        await voice_client.disconnect()
        await ctx.send('切断しました。')

@bot.command(aliases=['s'])
async def skip(ctx):
    global voice_client
    global waiting_url
    global waiting_file
    if not voice_client == None:
        voice_client.stop()
        await ctx.send('スキップします。')
        if len(waiting_url) != 0:
            if len(waiting_url) == 1:
                autonext.stop()
            subprocess.run(['rm', './temp.opus'])
            if waiting_url[0] == 'メッセージに添付されたファイル':
                await ctx.send('ファイルをロード中...')
                await waiting_file[0].save('temp.opus')
                waiting_file.pop(0)
            else:
                await ctx.send('次の曲のURLを解析中...')
                if waiting_url[0] in '.':
                    urllib.request.urlretrieve(waiting_url[0], 'temp.opus')
                else:
                    result = subprocess.run(['python', './youtube-dl', waiting_url[0], '--audio-format', 'opus', '-x', '-q', '-o', './temp.opus'])
                    if result.returncode != 0:
                        await ctx.send('URLの解析に失敗しました。')
            source = discord.FFmpegPCMAudio('./temp.opus')
            voice_client.play(source)
            await ctx.send('スキップしました。')
            waiting_url.pop(0)

@bot.command(aliases=['q'])
async def queue(ctx):
    global waiting_url
    if len(waiting_url) != 0:
        text = 'キュー：\n```\n'
        i = 1
        for url in waiting_url:
            text += str(i) + ' : ' + url + '\n'
            i += 1
        text += '```'
        await ctx.send(text)
    else:
        await ctx.send('キューは空です。')

@bot.command(aliases=['rm'])
async def remove(ctx, number:int):
    global waiting_url
    number -= 1
    if len(waiting_url) >= number:
        if waiting_url[number] == 'メッセージに添付されたファイル':
            files = 0
            for i in range(0, number - 1):
                if waiting_url[i] == 'メッセージに添付されたファイル':
                    files += 1
            del waiting_file[files]
        del waiting_url[number]
        ctx.send('キューから' + str(number) + '番を削除しました。')

@tasks.loop(seconds=3)
async def autonext():
    global voice_client
    global waiting_url
    if not voice_client.is_playing():
        subprocess.run(['rm', './temp.opus'])
        if waiting_url[0] == 'メッセージに添付されたファイル':
            await waiting_file[0].save('temp.opus')
        else:
            if waiting_url[0] in '.':
                urllib.request.urlretrieve(waiting_url[0], 'temp.opus')
            else:
                subprocess.run(['python', './youtube-dl', waiting_url[0], '--audio-format', 'opus', '-x', '-q', '-o', './temp.opus'])
        source = discord.FFmpegPCMAudio('./temp.opus')
        voice_client.play(source)
        if len(waiting_url) == 1:
            waiting_url = []
            autonext.stop()
        else:
            waiting_url.pop(0)


# 2021まで封印
'''
@bot.command()
async def CountdownStart(ctx):
    now = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
    )
    next_year_int=now.year + 1
    next_year = datetime.datetime(year=next_year_int, month=1, day=1, hour=0, minute=0, second=0)
    year = now.year
    while year >= 0:
        now = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        )
        year = now.year
        if year == next_year_int:
            await ctx.send('@everyone\nHappy New Year !!!')
            break
        now = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
        sabun = next_year - now
        sabun = (sabun.days * 86400) + sabun.seconds
        if sabun <= 60:
            await ctx.send(str(next_year_int) + '年まであと' + str(sabun) + '秒')
            await asyncio.sleep(1)
        else:
            if now.second == 0:
                sabun = sabun / 60
                await ctx.send(str(next_year_int) + '年まであと' + str(int(sabun)) + '分')
                await asyncio.sleep(5)
'''

# Botの起動とDiscordサーバーへの接続
bot.run(os.environ['TOKEN'])