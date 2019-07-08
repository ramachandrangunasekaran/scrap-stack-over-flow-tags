from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import asyncio





async def fetchAndParse(url):
    tags = []
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    tagsContainer = page_soup.select('#tags_list')
    tagCell = tagsContainer[0].findAll("div",{"class": "tag-cell"})
    for singleTag in tagCell:
        tag_temp = singleTag.findAll("a", {"class": "post-tag"})
        tags.append(tag_temp[0].contents[1] if len(tag_temp[0].contents)> 1 else tag_temp[0].contents[0])
    f = open("tags.txt", "a")
    f.write(','.join(tags))
    f.write('\n\n\n')
    f.close()
    return True

async def scrapperPage():
    for x in range(1628):
        url = "https://stackoverflow.com/tags?page="+str(x+1)+"&tab=popular"
        print("page:"+ str(x+1))
        await fetchAndParse(url)
   
        
    

if __name__== "__main__":
    loop = asyncio.get_event_loop()  
    loop.run_until_complete(scrapperPage())  
    loop.close()