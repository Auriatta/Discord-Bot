import predef

from keep_alive import keep_alive



def getValidChannelItemAddon(GuildChannel_id):
  for channel_id in predef.ItemAddonChannels:
    if GuildChannel_id == channel_id:
      return channel_id
    
  return -1

def isMessageValidItemAddon(content):
  for command in predef.ItemAddonCommands:
    if content.startswith(command):
      return True
    
  return False


@predef.client.event # INIT
async def on_ready():
  print("Bot get logged in..")


@predef.client.event # NEW MEMBER
async def on_member_join(member):
  print('Member {0} has joined', member.id)
  role = predef.discord.utils.get(member.guild.roles, id=predef.DefaultRole)
  await member.add_roles(role)



@predef.client.event # REACTION ADDED
async def on_raw_reaction_add(event):
  
  channel_id = getValidChannelItemAddon(event.channel_id)
  print(channel_id)
  if channel_id == -1:
    return
  
  channel = predef.client.get_channel(channel_id)
  message = await channel.fetch_message(event.message_id)
  if message.author != predef.client.user:
    return

    
  if isMessageValidItemAddon(message.content) and str(event.emoji) == predef.Button_emoji:
    print('Member {0} has added role', event.user_id)
    member = event.member
    role = predef.discord.Object(message.raw_role_mentions[0])
    await member.add_roles(role)
  


  
@predef.client.event # REACTION REMOVE  
async def on_raw_reaction_remove(event):
  channel_id = getValidChannelItemAddon(event.channel_id)
  if channel_id == -1:
    return
  channel = predef.client.get_channel(channel_id)
  message = await channel.fetch_message(event.message_id)
  if message.author != predef.client.user:
    return

    
  if isMessageValidItemAddon(message.content) and str(event.emoji) == predef.Button_emoji:
    print('Member {0} has removed role', event.user_id)
    role = predef.discord.Object(message.raw_role_mentions[0])
    guild = message.guild
    member = predef.discord.utils.get(guild.members, id=event.user_id)
    await member.remove_roles(role)
  

   
@predef.client.event # MESSAGE 
async def on_message(msg):
  if msg.author == predef.client.user:
    return
    print('New message has been sent')


  channel_id = getValidChannelItemAddon(msg.channel.id)
  if channel_id == -1:
    return
    
  if isMessageValidItemAddon(msg.content):
    print('New item detected')
    Content = msg.content
    await msg.delete()
    msg_new = await msg.channel.send(Content)
    await msg_new.add_reaction(predef.Button_emoji)



keep_alive()
predef.client.run(predef.os.environ['TOKEN'])