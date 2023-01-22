import predef
import website_maintance
import re
import random
import datetime
from keep_alive import keep_alive

#This is bot that everyday at 10:00 AM gather one of the random fix notes for sims game series

random.seed(datetime.datetime.now().day * (1 + datetime.datetime.now().microsecond))

#keep_alive()


sims4WebSite = website_maintance.html_raw_formater()
urls = ['https://www.ea.com/games/the-sims/the-sims-4/news/update-08-02-2022', 'https://www.ea.com/games/the-sims/the-sims-4/news/update-07-26-2022']

url = urls[random.randint(0, (len(urls) - 1) )]

siteContent = sims4WebSite.getWebSiteContent(url)

print('Site target url: ', url)
print('Content site size: ', len(siteContent), ' bytes')


siteContent = re.sub('\n','', siteContent)
siteContent = re.sub('\r','', siteContent)
siteContent = re.sub('\t','', siteContent)

siteContent = re.search(r"Bug Fixes<.(.*)</div>", siteContent).group(1)

siteContent = re.sub(r"<ul.*?>", "<ul>", siteContent)

print('Content site size reduced to: ', len(siteContent), ' bytes')

siteContent_GroupsOfTargetLists = re.findall(r"<ul><li>.*?<\/li><\/ul>",siteContent)


for TargetGroupListContent in siteContent_GroupsOfTargetLists:
    if re.match(r"(?!class=).*", TargetGroupListContent) != None:
        siteContent_GroupsOfTargetLists.remove(TargetGroupListContent)

siteContent_RandomPickedListGroup = siteContent_GroupsOfTargetLists[random.randint(0, (len(siteContent_GroupsOfTargetLists) - 1) )]
siteContent_RandomPickedListGroup = re.sub(r"<[/]?ul>",'', siteContent_RandomPickedListGroup)
siteContent_FinalTargetList = re.findall(r"<li>.*?</li>", siteContent_RandomPickedListGroup)
siteContent_FinalTargetList_Item = siteContent_FinalTargetList[random.randint(0,(len(siteContent_FinalTargetList)-1))]
siteContent_FinalTargetList_Item = re.sub(r"<[/]?li>",'', siteContent_FinalTargetList_Item)
siteContent_FinalTargetList_Item = re.sub(r"&.*?;",'', siteContent_FinalTargetList_Item)
siteContent_FinalTargetList_Item = re.sub(r"<.*?>",'', siteContent_FinalTargetList_Item)


print('Content View')

print('\033[96m TargetGroupLists view: \033[37m')

print(siteContent_GroupsOfTargetLists )
print('\033[96m TargetPickedList view: \033[37m')
print(siteContent_FinalTargetList )
print('\033[96m TargePickedListItem view: \033[37m')
print(siteContent_FinalTargetList_Item)


#predef.client.run(predef.os.environ['TOKEN'])