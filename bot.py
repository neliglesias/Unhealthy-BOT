from pickle import FALSE # Don't know what this library did anymore
import discord # The Discord.py library
from discord import app_commands # The app_commands library (don't know if this one is getting used anymore, don't think so)
from discord.ext import commands # The commands library that makes it possible for us to create or own prefix (!lpb )


TOKEN = '[YOUR TOKEN HERE]' # Add your bot TOKEN, removed ours since it should be top secret...


bot = commands.Bot(command_prefix="!lpb ", intents = discord.Intents.all()) # Creating the prefix
allowed_rank = 'Mods' # The only rank that can use the bot commands on the server
playing_now = 1111111111111111111 # Change this to the temporary text-channel-id where the bot is going to output it's embeds

# This list right here is the coded list where all the songs of the new album should be put into. 
#
# [SONGID, 'SONGTITLE', 'MP3 LOCATION OF THE SONG', 'THE ALBUM NAME - ARTIST OF THE ALBUM', 'ARTISTS ON THIS SONG', 'ALBUM COVER'],
# EXAMPLE:
# [1, 'x2', '/Users/neliglesias/Unhealthy BOT/Album/Therapy/x2.mp3', 'Therapy - Anne-Marie', 'Anne-Marie', 'https://www.neliglesias.be/BOTS/unhealthybot/therapy.jpeg'],
# [2, 'Dont Play', '/Users/neliglesias/Unhealthy BOT/Album/Therapy/DontPlay.mp3', 'Therapy - Anne-Marie', 'Anne-Marie, KSI & Digital Farm Animals', 'https://www.neliglesias.be/BOTS/unhealthybot/therapy.jpeg'],
# And so on
mp3_files = [
    [1, 'x2', '/Users/neliglesias/Unhealthy BOT/Album/Therapy/x2.mp3', 'Therapy - Anne-Marie', 'Anne-Marie', 'https://www.neliglesias.be/BOTS/unhealthybot/therapy.jpeg'],
    [2, 'Dont Play', '/Users/neliglesias/Unhealthy BOT/Album/Therapy/DontPlay.mp3', 'Therapy - Anne-Marie', 'Anne-Marie, KSI & Digital Farm Animals', 'https://www.neliglesias.be/BOTS/unhealthybot/therapy.jpeg'],

    # Add more songs as needed
]

# Just for the log when the bot is being ran so when know if it succesfully logged or not
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Unmute the bot, this has been implemented because when creating the bot it had selfmuted and we needed to unmute the bot though code...
@bot.command()
@commands.has_role(allowed_rank)
async def unmute(ctx):
    if ctx.voice_client:
        # Unmute the bot in the voice channel
        await ctx.voice_client.guild.change_voice_state(
            channel=ctx.voice_client.channel, self_mute=False
        )

        await ctx.send("Bot has been unmuted.")
    else:
        await ctx.send("Bot is not in a voice channel.")

# Mute the bot, this has been implemented because otherwise the bot won't unmute...
@bot.command()
@commands.has_role(allowed_rank)
async def mute(ctx):
    if ctx.voice_client:
        # Mute the bot in the voice channel
        await ctx.voice_client.guild.change_voice_state(
            channel=ctx.voice_client.channel, self_mute=True
        )

        await ctx.send("Bot has been muted.")
    else:
        await ctx.send("Bot is not in a voice channel.")

# The bot joins the voice channel/stage the user who invoked the command is in.
@bot.command()
@commands.has_role(allowed_rank)
async def join(ctx):
    voice_state = ctx.author.voice
    if voice_state is None or voice_state.channel is None:
        await ctx.send('Please join a voice channel first to summon the bot.')
        return
    
    voice_channel = voice_state.channel
    voice_client = await voice_channel.connect()
    await ctx.send(f'Joined voice channel: {voice_channel}')

# The bot leaves the channel/stage it is in otherwise it will stay in it.
@bot.command()
@commands.has_role(allowed_rank)
async def leave(ctx):
    voice_client = ctx.voice_client
    if voice_client is not None:
        await voice_client.disconnect()
        await ctx.send('Left the voice channel.')

# This is a command only for the MODS, this is to see the raw list that is saved in the code (the output is not shown in the public text-channel)
@bot.command()
@commands.has_role(allowed_rank)
async def privatelist(ctx):
    songs_list = '\n'.join(f'{song[0]}. {song[1]}' for song in mp3_files)
    await ctx.send(f'Available songs:\n{songs_list}')

# Sends an embedded message into specific public text-channel, this shows the new album and which songs we're going to be listening to.
@bot.command()
@commands.has_role(allowed_rank)
async def publiclist(ctx):
    target_channel = bot.get_channel(playing_now)

    embed = discord.Embed(title="UNHEALTHY (DELUXE) - ANNE-MARIE",
                          url="https://anne-marie.lnk.to/Unhealthy",
                          description="🍦🍔🍩🍟🍬🍕🍭\n\n> 1.      **SUCKS TO BE YOU** - *Anne-Marie*\n> 2.     **SAD B!TCH** - *Anne-Marie*\n> 3.     **PSYCHO** - *Anne-Marie & Aitch*\n> 4.     **HAUNT YOU** - *Anne-Marie*\n> 5.     **TRAINWRECK** - *Anne-Marie*\n> 6.     **GRUDGE** - *Anne-Marie*\n> 7.     **OBSESSED** - *Anne-Marie*\n> 8.     **KILLS ME TO LOVE YOU** - *Anne-Marie*\n> 9.     **UNHEALTHY (feat. Shania Twain)** - *Anne-Marie*\n> 10.    **IRISH GOODBYE** - *Anne-Marie*\n> 11.     **CUCKOO** - *Anne-Marie*\n> 12.    **YOU & I (feat. Khalid)** - *Anne-Marie*\n> 13.    **NEVER LOVED ANYONE BEFORE** - *Anne-Marie & Aitch*\n> 14.    **BETTER OFF** - *Anne-Marie*\n> 15.    **ICK** - *Anne-Marie*\n> 16.    **EXPECTATIONS** - *Anne-Marie, Minnie & (G)I-IDLE*\n.",
                          colour=0xff38d4)

    embed.set_author(name="List",
                     icon_url="https://i.scdn.co/image/ab6761610000e5eb67013e289b84440ce3d1c88e")

    embed.add_field(name="🍟🍬 UNHEALTHY OUT NOW! 🍭🍿",
                    value="Listen to Anne-Marie's highly anticipated new album called 'UNHEALTHY' out now! More info [here](https://anne-marie.lnk.to/Unhealthy)")

    embed.set_image(url="https://www.neliglesias.be/BOTS/unhealthybot/unhealthyxbanner.jpeg")

    embed.set_footer(text=".A MAJOR TOMS / ASYLUM RECORD RELEASE, © 2023 WARNER MUSIC UK LIMITED.")

    await target_channel.send(embed=embed)

# This command plays the preferred song off the mp3_list.
@bot.command()
@commands.has_role(allowed_rank)
async def play(ctx, song_id: int):
    # Find the song with the given ID
    song_info = '\n'.join(f'{song[2]}. {song[1]}' for song in mp3_files)
    song = next((entry for entry in mp3_files if entry[0] == song_id), None)
    if song:
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            voice_client = await voice_channel.connect()
        else:
            voice_client = ctx.voice_client

        if not voice_client.is_playing():
            source = discord.FFmpegPCMAudio(song[2])
            voice_client.play(source)

            # Get the channel you want to send the embed message to
            target_channel = bot.get_channel(playing_now)

            # Create the embed message
            embed = discord.Embed(
                title=song[3],
                url="https://anne-marie.lnk.to/Unhealthy",
                color=0xff38d4
            )
            embed.set_author(
                name="Playing now",
                url=None,
                icon_url="https://i.scdn.co/image/ab6761610000e5eb67013e289b84440ce3d1c88e"
            )
            embed.set_thumbnail(
                url=song[5]
            )
            embed.add_field(
                name=song[1],
                value=song[4],
                inline=True
            )

            await target_channel.send(embed=embed)
        else:
            await ctx.send('I am already playing a song.')
    else:
        await ctx.send('Invalid song number.')

# This command stops the bot from playing the sing it is currently playing, this is not a pause command but really a skip/stop command.
@bot.command()
@commands.has_role(allowed_rank)
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client is None or not voice_client.is_playing():
        await ctx.send('There is no song currently playing.')
        return
    
    voice_client.stop()
    await ctx.send('Stopped playing.')

bot.run(TOKEN)