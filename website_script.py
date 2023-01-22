import predef
from predef import urls
from predef import random
import website_maintance
import re


def getOneRandomBugFixListItemFromSimsGameSite():
    url = urls[random.randint(0, (len(urls) - 1) )]

    siteContent = website_maintance.getWebsiteContentAsUTF8(url)

    print('Site target url: ', url)
    print('Content site size: ', len(siteContent), ' bytes')


    siteContent = re.sub('\n','', siteContent)
    siteContent = re.sub('\r','', siteContent)
    siteContent = re.sub('\t','', siteContent)

    siteContent = re.search(r"Bug Fixes<.(.*)</div>", siteContent).group(1)

    siteContent = re.sub(r"<ul.*?>", "<ul>", siteContent)

    print('Content site size reduced to: ', len(siteContent), ' bytes')

        
    siteContent_GroupsOfTargetLists = website_maintance.getAllSolidTextLinesWith_ulList_syntax(siteContent)

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