import predef
import website_maintance
import re
from keep_alive import keep_alive

#This is bot that everyday at 10:00 AM gather one of the random fix notes for game called sims








#keep_alive()


sims4WebSite = website_maintance.html_raw_formater()
url = 'https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022'
siteContent = sims4WebSite.getWebSiteContent('https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022')
#siteContent = sims4WebSite.getWebSiteContent('https://www.ea.com/games/the-sims/the-sims-4/news/update-08-02-2022')

siteContent = re.sub('\n','', siteContent)
siteContent = re.sub('\r','', siteContent)

print('Site target url: ', url)
print('Content site size: ', len(siteContent), ' bytes')


siteContent = sims4WebSite.getWebSiteSpecificPart('Bug Fixes', '<', 'Related News', '<', siteContent)

#cut all <ul (...)> to <ul>

siteContentListsGroups = []
while 1 :
    siteContentListsGroups.append(sims4WebSite.getWebSiteSpecificPart'<ul><li', '>', '</li></ul', '>', siteContent))
    siteContentListsGroupsSize = len(siteContentListsGroups)-1
    siteContent = re.sub(siteContentListsGroups[siteContentListsGroupsSize],'', siteContent)
    if siteContentListsGroups[siteContentListsGroupsSize] == siteContent:
        break

print('Content site size reduced to: ', len(siteContent), ' bytes')

siteContent = siteContent.split('</li>')
siteContent =  sims4WebSite.formatContentList(siteContent)




print('Content view:')
print(siteContent )


#predef.client.run(predef.os.environ['TOKEN'])