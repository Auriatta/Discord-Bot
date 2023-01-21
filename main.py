import predef
import website_maintance
import re
from keep_alive import keep_alive

#This is bot that everyday at 10:00 AM gather one of the random fix notes for game called sims








#keep_alive()


sims4WebSite = website_maintance.html_raw_formater()
url = 'https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022'

#rand from valid urls

siteContent = sims4WebSite.getWebSiteContent('https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022')
#siteContent = sims4WebSite.getWebSiteContent('https://www.ea.com/games/the-sims/the-sims-4/news/update-08-02-2022')

siteContent = re.sub('\n','', siteContent)
siteContent = re.sub('\r','', siteContent)
siteContent = re.sub('\t','', siteContent)

print('Site target url: ', url)
print('Content site size: ', len(siteContent), ' bytes')


siteContent = re.search(r"Bug Fixes<.(.*)</div>", siteContent).group(1)

siteContent = re.sub(r"<ul.*?>", "<ul>", siteContent)

siteContentListsGroups = re.findall(r"<ul><li>.*?</li></ul>",siteContent)
print('Content site size reduced to: ', len(siteContent), ' bytes')

# rand from siteContentListsGroups
# split into list <li></li>
# rand from list and print

print('Content view:')
print(siteContentListsGroups )


#predef.client.run(predef.os.environ['TOKEN'])