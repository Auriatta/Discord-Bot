import os
import discord

intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)

Button_emoji = "🤍"

ItemAddonChannels = {982080480654553108, 990809787983867984, 991111309242404975, 991191533988622356}

ItemAddonCommands = {"Przedmiot","Farba", "Przyszywka", ")>>"}

DefaultRole = 980441084037562439