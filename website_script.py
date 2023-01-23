import predef
from predef import Sims4MainNewsUrl
from predef import random
import website_maintance
import re

def getAllUpdateSitesFromMainNewsSite(url):
    siteContent = website_maintance.getWebsiteContentAsUTF8(url)
    siteContent = website_maintance.removeSpecialKeys(siteContent)
    
    urls_extentions = re.findall(r"Update ..?\/..\/....", siteContent)
    urls_extentions_formated = []


    for url_ext in urls_extentions:
        url_ext = url_ext.replace('U', 'u')
        urls_extentions_formated.append(url + '/' + re.sub(r"[ /]", '-', url_ext))
    
    return urls_extentions_formated


def getBugFixListGroupsFromWebsite(url):
    siteContent = website_maintance.getWebsiteContentAsUTF8(url)

    print('Site target url: ', url)
    print('Content site size: ', len(siteContent), ' bytes')

    siteContent = website_maintance.removeSpecialKeys(siteContent)

    try:
        siteContent = re.search(r"Bug Fixes<.(.*)</div>", siteContent).group(1)
    except:
        return []
    
    siteContent = re.sub(r"<ul.*?>", "<ul>", siteContent)

    print('Content site size reduced to: ', len(siteContent), ' bytes')

    siteContent_GroupsOfTargetLists = website_maintance.getAllSolidTextLinesWith_ulList_syntax(siteContent)

    

    return siteContent_GroupsOfTargetLists

def gatherAndSyncBugFixesFromAllAvailableWebsites(urls):
    siteContent_GroupsOfTargetLists = []
    for url in urls:
        siteContent_GroupsOfTargetLists += getBugFixListGroupsFromWebsite(url)

    return siteContent_GroupsOfTargetLists



def getOneRandomBugFixListItemFromSimsGameSite():
    
    siteExtentionedUrls = getAllUpdateSitesFromMainNewsSite(Sims4MainNewsUrl)
    siteContent_GroupsOfTargetLists = gatherAndSyncBugFixesFromAllAvailableWebsites(siteExtentionedUrls)
    siteContent_RandomPickedListGroup = siteContent_GroupsOfTargetLists[random.randint(0, (len(siteContent_GroupsOfTargetLists) - 1) )]
    siteContent_RandomPickedListGroup = re.sub(r"<[/]?ul>",'', siteContent_RandomPickedListGroup)

    siteContent_FinalTargetList = re.findall(r"<li>.*?</li>", siteContent_RandomPickedListGroup)

    siteContent_FinalTargetList_Item = siteContent_FinalTargetList[random.randint(0,(len(siteContent_FinalTargetList)-1))]

    siteContent_FinalTargetList_Item = website_maintance.removeHTMLsyntax(siteContent_FinalTargetList_Item)


    print('Content View')

    print('\033[96m TargetGroupLists view: \033[37m')

    print(siteContent_GroupsOfTargetLists )
    print('\033[96m TargetPickedList view: \033[37m')
    print(siteContent_FinalTargetList )
    print('\033[96m TargePickedListItem view: \033[37m')
    print(siteContent_FinalTargetList_Item)


    return siteContent_FinalTargetList_Item