import os
import discord
import re
import requests


intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)
HTMLS = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') 
Website_Adress_Sims = "https://www.ea.com/games/the-sims/the-sims-4/news/update-11-01-2022"
