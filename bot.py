import discord
import youtube_dl

TOKEN = 'NTk2NTk3NDI0NDMzMTM1NjE3.XTClog.GVhTVMoYL-WC9li0dMf6tTUQz9o'
client = commands.bot(command_prefix = '.')

players = {}

@client.event
async def on_ready():
	print('Bot online')
	
@client.command(pass_context=True)
async def join(ctx):
	 channel = ctx.message.author.boice.voice_channel
	 await Client.join_voice_channel(Channel)
	 
@client.command(pass_context=True)
async def leave(ctx):
	 server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()
	
@client.command(pass_context=True)
async def play(ctx, url):
	server = ctx.message.server
	voice_client =client.voice_client_in(server)
	player = await voice_client.create_ytdl_player(url)
	players[server.id] = player
	player.start()
	
Client.run
