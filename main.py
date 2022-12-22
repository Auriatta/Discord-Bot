import predef
import random
from keep_alive import keep_alive

#This is bot that everyday at 10:00 AM gather one of the random fix notes for game called sims




def getTextFromSource_HTML(raw_html):
  cleantext = predef.re.sub(predef.CLEANR, '', raw_html)
  return cleantext

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



#keep_alive()


PageSource = predef.requests.get('https://www.ea.com/games/the-sims/the-sims-4/news/update-11-01-2022')
SiteContent = PageSource.content.decode("utf-8")
# get html site and turn it into readable utf-8 format

StartIndex = SiteContent.find('Bug Fixes</h1>')
EndIndex = SiteContent.find('latest-news-article-section')
# find Bug list part

SiteContent = SiteContent[StartIndex:EndIndex]
# Cut only part with bug list



SiteContent = SiteContent.split('</li>')
# sort every bullet list item into different container
# First and last container is always about some additional dirty html stuff

RandomIndex = random.randint(1,len(SiteContent)-1)

OneListItem  = predef.re.sub('<li>','', SiteContent[RandomIndex])
OneListItem = predef.re.sub('<li>','', OneListItem)


StartIndex = OneListItem.find('</ul>')
EndIndex = OneListItem.find('<ul>')

OneListItem = predef.re.sub(OneListItem[StartIndex:EndIndex],'',OneListItem)
OneListItem = predef.re.sub('<ul>','', OneListItem)
print('Index: ')
print(RandomIndex)
print('ContentLen: ')
print(len(OneListItem))
print('Content: ')
print(OneListItem)

#len = 1 mean that is empty and should be randomise again



#predef.client.run(predef.os.environ['TOKEN'])