import predef
import website_maintance

from keep_alive import keep_alive

#This is bot that everyday at 10:00 AM gather one of the random fix notes for game called sims








#keep_alive()


sims4WebSite = website_maintance.html_sims_getter()

siteContent = sims4WebSite.getWebsiteContent('https://www.ea.com/games/the-sims/the-sims-4/news/update-11-01-2022')

siteContent = sims4WebSite.getArrayBugFixListWebSitePart('Bug Fixes</h1>','latest-news-article-section', siteContent)

print(sims4WebSite.getOneValidListItem(siteContent, predef.random.randint(0, len(siteContent))))


#predef.client.run(predef.os.environ['TOKEN'])