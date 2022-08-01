from random import random
import discord
from discord.ext import commands
import youtube_dl
import datetime

class music(commands.Cog):    
    def __init__(self, client):
        self.client = client
        self.vc = None # voice channel
        self.is_playing = False

        # queue with all the songs [url, title, uploader, duration]
        self._queue = []
        
        # audio config
        self.YDL_OPTIONS = {'format':'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        
        print('\n\n link start :>\n\n')

# ============== FUNCTIONS ========================

    def search_yt(self, item):
        with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title'], 'uploader': info['uploader'], 'duration': info['duration']}

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=

    async def play_next(self, ctx):
        if len(self._queue) > 0:
            self.is_playing = True
            url = self._queue[0]['source']

            if self.vc == None:
                await ctx.send('Could not connect to the voice channel')
                return

            em = discord.Embed(title=self._queue[0]['title'], url=self._queue[0]['source'] ,description=self._queue[0]['uploader'], colour=0x36393e)

            em.set_author(name="", icon_url=self._queue[0]['source'])

            em.add_field(name="Duration", value= str(datetime.timedelta(seconds=self._queue[0]['duration'])), inline=True)
            em.add_field(name="Requested By", value=ctx.author.name, inline=True)
            ctx.send(embed=em)

            self._queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(source=url, executable="C:/ffmpeg", **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
        else:
            self.is_playing = False

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=

    async def play_music(self, ctx):
        if len(self._queue) > 0:
            self.is_playing = True
            url = self._queue[0]['source']

            if self.vc == None:
                await ctx.send('Could not connect to the voice channel')
                return

            em = discord.Embed(title=self._queue[0]['title'], url=url ,description=self._queue[0]['uploader'], colour=0x36393e)
            em.add_field(name="Duration", value= str(datetime.timedelta(seconds=self._queue[0]['duration'])), inline=True)
            em.add_field(name="Requested By", value=ctx.author.name, inline=True)
            await ctx.send(embed=em)

            self._queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(source=url, executable="C:/ffmpeg", **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
        else:
            self.is_playing = False

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=

    @commands.command()
    async def join(self, ctx):
        if self.vc != None:
            return
        if ctx.author.voice is None:
            await ctx.send("Connect to a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=

    @commands.command()
    async def leave(self, ctx):
        if self.vc != None:
            await ctx.voice_client.disconnect()

# -------- MUSIC ----------

    @commands.command(name='p')
    async def play(self,ctx, *args):
        query = " ".join(args)
        
        self.vc = ctx.voice_client

        if self.vc is None:
            await ctx.send("Connect to a voice channel")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song. Incorrect format, try a different keyword")
            else:
                self._queue.append(song)
                if self.is_playing == True:
                    await ctx.send("Song added to the queue")
                else:
                    await self.play_music(ctx)

    @commands.command()
    async def queue(self,ctx):
        await ctx.send("**--- Queue ---**\n")
        for i in range(len(self._queue)):
            if i == 0:
                await ctx.send("\n **Next Song: **" + self._queue[i]['title'])
            else:
                await ctx.send("\n**" + str(i) + ")** " + self._queue[i]['title'])


    @commands.command()
    async def skip(self, ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            await self.play_music(ctx)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resume")

    @commands.command()
    async def stop(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        voice_channel.stop()

    @commands.command()
    async def remove(self, ctx, number):
        try:
            del(self.queue[number])
        except:
            await ctx.send('Queue is **empty** or index is **out of bounds**')

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'Latency: {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def shuffle(self,ctx):
        if len(self._queue) < 1:
            await ctx.send("Not enough elements to shuffle")
        else:
            random.shuffle(self._queue)
            await ctx.send("Queue shuffled! -queue to see the results")

    @commands.command()
    async def clear(self, ctx):
        if len(self._queue) != 0:
            self._queue = []
            self.vc.stop()

def setup(client):
    client.add_cog(music(client))