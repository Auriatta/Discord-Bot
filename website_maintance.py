import requests
import re

def getWebsiteContentAsUTF8(adress):
        PageSource = requests.get(adress)
        return PageSource.content.decode("utf-8")

def getAllSolidTextLinesWith_ulList_syntax(Content):
    Content = re.sub(r"<ul.*?>", "<ul>", Content)

    Content_GroupsOfTargetLists = re.findall(r"<ul><li>.*?<\/li><\/ul>",Content)

    for TargetGroupListContent in Content_GroupsOfTargetLists:
        if re.match(r"(?!class=).*", TargetGroupListContent) != None:
            Content_GroupsOfTargetLists.remove(TargetGroupListContent)

    return Content_GroupsOfTargetLists

def removeHTMLsyntax(Content):
    Content = re.sub(r"&.*?;",'', Content)
    Content = re.sub(r"<.*?>",'', Content)
    return Content