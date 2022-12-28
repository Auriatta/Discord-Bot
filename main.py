import predef
import website_maintance

from keep_alive import keep_alive

#This is bot that everyday at 10:00 AM gather one of the random fix notes for game called sims








#keep_alive()


sims4WebSite = website_maintance.html_raw_formater()

siteContent = sims4WebSite.getWebSiteContent('https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022')
print('Content site size: ', len(siteContent), ' bytes')
siteContent = sims4WebSite.getWebSiteSpecificPart('Bug Fixes', '<', 'Related News', '<', siteContent)

#siteContent = sims4WebSite.splitIntoList(siteContent)ń

#siteContent = sims4WebSite.formatContentList(siteContent)
#sims4WebSite.getOneValidListItem(siteContent, predef.random.randint(0, len(siteContent)))
#index = predef.random.randint(0, len(newsiteContent))

print('Content site size reduced to: ', len(siteContent), ' bytes')
print('Content view:')
print(siteContent)


#predef.client.run(predef.os.environ['TOKEN'])