import datetime
import random
import os

random.seed(datetime.datetime.now().day * (1 + datetime.datetime.now().microsecond))

os.environ["TOKEN"] = ""
os.environ["ChannelID"] = "979765004729450496"
urls = ['https://www.ea.com/games/the-sims/the-sims-4/news/update-08-02-2022', 'https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022']
