import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup

filePathMaster = "/home/RRADAR/rob.adams/Documents/News_Web_Crawler_Scrapers/"
filenameSHPCulandBeh = filePathMaster +"Crawled Data SHP Culture and Behaviour/"
filenameSHPCourt = filePathMaster + "Crawled Data SHP Court/"
filenameHSE = filePathMaster + "Crawled Data HSE/"

def HSEScrape():
    urlHSE = 'http://news.hse.gov.uk/'

    sourceHSE = urllib.request.urlopen(urlHSE)
    soupHSE = BeautifulSoup(sourceHSE, 'html.parser')
    substring = '³'
    urlsHSE =[]
    for hHSE in soupHSE.findAll(class_="entry-title"):
            aTagHSE = hHSE.find('a')
            urlsHSE.append(aTagHSE.attrs['href'])

    try:
        i = 0
        urlsHSE = [iHSE.replace(substring, '%C2%B3')for iHSE in urlsHSE]
        for webTextHSE in urlsHSE:
            fHSE = open(filenameHSE + "HSE Scraped Content%s" %(i) + ".html", "w")
        #print(webText)
            sourceHSE2 = urllib.request.urlopen(webTextHSE).read()
            soupHSE2 = BeautifulSoup(sourceHSE2, 'html.parser')
            for webExtractHSE in soupHSE2.findAll('p'):
    #            print(webExtractHSE.text)
                fHSE.write(webExtractHSE.text)
            i+=1
            fHSE.close()
    except Exception:
        print("\n\n\n\nHTTP Error")
        pass


def SHPScrape():
    urlSHP = 'https://www.shponline.co.uk/prosecution-and-in-court/?cid=nav'
    sourceSHP = urllib.request.urlopen(urlSHP)
    soupSHP = BeautifulSoup(sourceSHP, 'html.parser')

    urlsSHP =[]
    for hSHP in soupSHP.findAll(class_="ec-article row ec-linkContainer ec-articleHoverTitle"):
        aTagSHP = hSHP.find('a')
    #    print (urlsSHP)
        urlsSHP.append(aTagSHP.attrs['href'])
    try:
        i = 0
        for webTextSHP in urlsSHP:
            fSHP = open(filenameSHPCourt + "SHP Scraped Contents%s" %(i) + ".html", "w")
        #print(webText)
            sourceSHP2 = urllib.request.urlopen(webTextSHP).read()
            soupSHP2 = BeautifulSoup(sourceSHP2, 'html.parser')
            for webExtractSHP in soupSHP2.findAll('p'):
    #            print(webExtractSHP.text)
                fSHP.write(webExtractSHP.text)
            i+=1
            fSHP.close()
    except:
        print("\n\n\n\nHTTP Error")
        pass

def SHPCulandBeh():
    urlSHPCulandBeh = 'https://www.shponline.co.uk/culture-and-behaviours/?cid=nav'
    sourceSHPCulandBeh = urllib.request.urlopen(urlSHPCulandBeh)
    soupSHPCulandBeh = BeautifulSoup(sourceSHPCulandBeh, 'html.parser')
    urlsSHPCulandBeh =[]
    for hSHPCulandBeh in soupSHPCulandBeh.findAll(class_="ec-article row ec-linkContainer ec-articleHoverTitle"):
        aTagSHPCulandBeh = hSHPCulandBeh.find('a')
    #    print (urlsSHPCulandBeh)
        urlsSHPCulandBeh.append(aTagSHPCulandBeh.attrs['href'])

    try:
        i = 0
    #fSHPCulandBeh = open("SHPCulandBeh Scraped Contents.docx", "w")
        for webTextSHPCulandBeh in urlsSHPCulandBeh:
            fSHPCulandBeh = open(filenameSHPCulandBeh + "SHPCulandBeh Scraped Contents%s" %(i) + ".html", "w")
    #print(webText)
            sourceSHPCulandBeh2 = urllib.request.urlopen(webTextSHPCulandBeh).read()
            soupSHPCulandBeh2 = BeautifulSoup(sourceSHPCulandBeh2, 'html.parser')
            for webExtractSHPCulandBeh in soupSHPCulandBeh2.findAll('p'):

#            print(webExtractSHPCulandBeh.text)
                fSHPCulandBeh.write(webExtractSHPCulandBeh.text)
            i+=1
            fSHPCulandBeh.close()

    except:
        print("\n\n\n\nHTTP Error")
        pass


HSEScrape()
SHPScrape()
SHPCulandBeh()
