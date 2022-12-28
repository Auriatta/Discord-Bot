import re
import requests

#By auriatta.com

class html_raw_formater:
    
    @staticmethod
    def getWebSiteContent(adrress):
        PageSource = requests.get(adrress)
        return PageSource.content.decode("utf-8")
    
    @staticmethod
    def getIndexRangeByKeywords(keyword1, keyword2, content):
        StartIndex = content.find(keyword1)
        EndIndex = content.find(keyword2)
        return (StartIndex, EndIndex)

    @staticmethod
    def excludeIntoListBySpecificSyntax(startSyntax, endSyntax, content):
        listedContent = []

        while 1 :
            indexRange = html_raw_formater.getIndexRangeByKeywords(startSyntax, endSyntax, content)
            if indexRange[0] == -1 or indexRange[1] == -1:
                break
            listedContent.append(content[indexRange[0] + len(startSyntax) : indexRange[1]])
            content = str(content).replace(content[indexRange[0] + len(startSyntax) : indexRange[1]], '')

        return listedContent

    @staticmethod
    def getWebSiteSpecificPart(keyword_1, keyword_1_validation, keyword_2, keyword_2_validation, content):

        index = 0
        keyword_1_validation = keyword_1_validation[0]
        keyword_2_validation = keyword_2_validation[0]

        while index != -1:
            index = content.find(keyword_1)
            if index == -1:
                print('Not found upper keyword: ', keyword_1)
                break

            if content[index + len(keyword_1)] != keyword_1_validation:  #char next to header should be validation char
                print('Upper Content site reduction size: ', len(content[0 : index + len(keyword_1)]), ' bytes')
                content = str(content).replace(content[0 : index + len(keyword_1)],'')
            else:
                print('Upper Content site reduction size: ', len(content[0 : index + len(keyword_1)]), ' bytes')
                content = str(content).replace(content[0 : index + len(keyword_1)],'')
                break
        #upper part cut
        
        index = 0
        while index != -1 :
            
            index = content.find(keyword_2, index)
            print('Lower Content site: Index: ', index)

            if index == -1:
                print('Not found lower keyword: ', keyword_2)
                break

            
            if content[index + len(keyword_2)] != keyword_2_validation:
                print('Lower Content site: found index is not valid, next aproach ')
                index = index + 1
            else:
                print('Lower Content site reduction size: ', len(content[index : len(content)]), ' bytes')
                content = str(content).replace(content[index : len(content)],'')
                break
        #lower part cut
       

        return content

    @staticmethod
    def removeHTMLSyntax(startSyntax, endSyntax, Content):
        
        startSyntax = re.sub('>','', startSyntax) # in a case someone put full syntax <>
        StartIndex = Content.find(startSyntax)
        EndIndex = Content.find('>')

        Content = re.sub(Content[StartIndex:EndIndex+1],'',Content)
        Content = re.sub(endSyntax,'', Content)
        return Content

    @staticmethod
    def formatContentList(content):

        formatedcontent = []
        formatedItem = ''
        for item in content:
            formatedItem = html_raw_formater.formatListItem(item)
            if len(formatedItem) > 5 : formatedcontent.append(formatedItem)
        
        return formatedcontent


    @staticmethod
    def formatListItem( content):

        OneListItem = re.sub('<li>','', content)

        StartIndex = OneListItem.find('</ul>')
        EndIndex = OneListItem.find('<ul>')
        print(OneListItem)
        OneListItem = re.sub(OneListItem[StartIndex:EndIndex],'',OneListItem)
        OneListItem = re.sub('<ul>','', OneListItem)


        OneListItem = html_raw_formater.removeHTMLSyntax('<a>','</a>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<p>','</p>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<h6>','</h6>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<h5>','</h5>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<h4>','</h4>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<h3>','</h3>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<h2>','</h2>', OneListItem)
        OneListItem = html_raw_formater.removeHTMLSyntax('<h1>','</h1>', OneListItem)

        
        #len = 1 mean that is empty
        return OneListItem


    @staticmethod
    def splitIntoList(content):

        content = content.split('</li>')
        # sort every bullet list item into different container
       
        del content[0]
        # First and last container is always about some additional dirty html stuff

        for item in content:
            if len(item) < 3:
                content.remove(item)
        # Reomve empty list items

        return content


    
       



