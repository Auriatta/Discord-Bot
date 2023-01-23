import discord_bot
from discord_bot import client
import website_script
import predef
from keep_alive import keep_alive



#This is bot that everyday at 10:00 AM gather one of the random fix notes for sims game series



#keep_alive()

#discord_bot.client.run(predef.os.environ['TOKEN'])
website_script.getOneRandomBugFixListItemFromSimsGameSite()
