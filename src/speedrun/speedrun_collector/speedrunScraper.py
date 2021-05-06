from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import csv

from speedrun_collector.data_model import * 

user_urls = []
userName = []
gameTitles = []
game_urls = []
total = 0
count = 0
        
def get_user_games():

    global count

    mc_url = 'https://www.speedrun.com/mc#Any_Glitchless'
    uClient = uReq(mc_url)
    mc_html = uClient.read()
    uClient.close()

    mc_soup = soup(mc_html, "html.parser")
    username = mc_soup.findAll("a",{"class" : "link-username nobr nounderline"})
    total = len(username)

    with open('speedrunData.csv', mode='w') as speedrun_file:
        speedrun_writer = csv.writer(speedrun_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for user in username:
            userLink = user["href"]
            userName.append(userLink[6:])
            user_urls.append("https://www.speedrun.com" + userLink)
            user_speed_link = "https://www.speedrun.com" + userLink

            speedrun_api = 'https://www.speedrun.com/api/v1/users/' + userName[count]

            uClient = uReq(speedrun_api)
            user_html = uClient.read()
            uClient.close()
            user_soup = soup(user_html, "html.parser")
            runs_json = json.loads(user_soup.text)
            user_id = runs_json['data']['id']
            user_id_link = 'https://www.speedrun.com/api/v1/users/' + user_id + '/personal-bests'

            uClient = uReq(user_id_link)
            user_html = uClient.read()
            uClient.close()
            games_soup = soup(user_html, "html.parser")
            games_json = json.loads(games_soup.text)
            game_id_outputs = []
            name_id_outputs = []

            print()
            print(userName[count])
            print('---------------')

            for game in games_json['data']:
                game_id = game['run']['game']
                if(game_id not in game_id_outputs):
                    game_id_outputs.append(game_id)
                    game_id_link = 'https://www.speedrun.com/api/v1/games/' + game_id
                    uClient = uReq(game_id_link)
                    game_html = uClient.read()
                    uClient.close()
                    name_soup = soup(game_html, "html.parser")
                    name_json = json.loads(name_soup.text)
                    name_id = name_json['data']['names']['twitch']
                    if(name_id not in name_id_outputs):
                        name_id_outputs.append(name_id)
                        speedrun_writer.writerow([userName[count], name_id])
                        print(name_id)
                        User.add(userName[count]).games.connect(Game.add(name_id))
            count += 1  