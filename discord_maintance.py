import predef

import discord
intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)


@client.event # INIT
async def on_ready():
  print("Bot get logged in..")


   
@client.event # MESSAGE 
async def on_message(msg):
  if msg.author == client.user:
    return
    print('New message has been sent')

