import predef
import website_script
import datetime
import discord
intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)
from discord.ext import tasks

time = datetime.time(hour=10, minute=30)

@tasks.loop(seconds=30.0)
async def SendSimsBugDescriptionToMainChannel():
    message = website_script.getOneRandomBugFixListItemFromSimsGameSite()
    channel = client.get_channel(int(predef.os.environ['ChannelID']))
    await channel.send("> " + message)

@client.event # INIT
async def on_ready():
  print("Bot get logged in..")
  await client.wait_until_ready()
  SendSimsBugDescriptionToMainChannel.start()


  


   
@client.event # MESSAGE 
async def on_message(msg):
  if msg.author == client.user:
    return
    print('New message has been sent')

