from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#from speedrun_collector.speedrunScraper import *

user_urls = []
userName = []
gameTitle = []

def user_scraper():

    mc_url = 'https://www.speedrun.com/mc#Any_Glitchless'
    uClient = uReq(mc_url)
    mc_html = uClient.read()
    uClient.close()

    mc_soup = soup(mc_html, "html.parser")
    username = mc_soup.findAll("a",{"class" : "link-username nobr nounderline"})

    #print(len(username))
    #print(username[2])
    #user = username[0]
    #print(user)
    #print(user["href"])   

    for user in username:
        userLink = user["href"]
        #print(userLink[6:])
        userName.append(userLink[6:])
        user_urls.append("https://www.speedrun.com" + userLink)
        print("https://www.speedrun.com" + userLink)
        
        #first_game = Game(title='Minecraft').save()

        #speedrun.get(SpeedrunNode, userLink[6:])
    
    game_scraper()

def game_scraper():

    for user_url in user_urls:
        uClient = uReq(user_url)
        user_html = uClient.read()
        uClient.close()

        user_soup = soup(user_html, "html.parser")
        game = user_soup.findAll("main",{"class" : "container"})

    print(user_soup.findAll("div",{"id" : "leaderboarddiv"}))
    #print(user_soup.main)
    #print(len(game))
        