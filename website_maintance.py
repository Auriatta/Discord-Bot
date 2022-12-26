import re
import requests



class html_sims_getter:
    
    @staticmethod
    def getWebsiteContent(adrress):
        PageSource = requests.get(adrress)
        return PageSource.content.decode("utf-8")
    
    @staticmethod
    def getIndexRangeByKeywords(keyword1, keyword2, siteContent):
        StartIndex = siteContent.find(keyword1)
        EndIndex = siteContent.find(keyword2)
        return (StartIndex, EndIndex)
        
    def getArrayBugFixListWebSitePart(self, keyword1,keyword2, siteContent):

        IndexRange = self.getIndexRangeByKeywords(keyword1, keyword2, siteContent)
        # find Bug list part

        SiteContent = siteContent[IndexRange[0]:IndexRange[1]]
        # Cut only part with bug list

        SiteContent = SiteContent.split('</li>')
        # sort every bullet list item into different container
       
        del SiteContent[0]
        del SiteContent[len(SiteContent)-1]
        # First and last container is always about some additional dirty html stuff


        while( "" in SiteContent):
            SiteContent.remove("")
        # Reomve empty list items

        return SiteContent

    @staticmethod
    def getOneValidListItem(SiteContent, index):
        
        OneListItem  = re.sub('<li>','', SiteContent[index])
        OneListItem = re.sub('<li>','', OneListItem)

        StartIndex = OneListItem.find('</ul>')
        EndIndex = OneListItem.find('<ul>')

        OneListItem = re.sub(OneListItem[StartIndex:EndIndex],'',OneListItem)
        OneListItem = re.sub('<ul>','', OneListItem)

        #len = 1 mean that is empty
        return OneListItem

    
       



