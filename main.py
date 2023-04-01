#import discord
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
import pandas as pd
import time
import sqlite3
import datetime
import random
from unidecode import unidecode
from datetime import datetime as dt
from bs4 import BeautifulSoup
import time
import aiofiles
import asyncio
import matplotlib.pyplot as plt
#import socketio
#import websockets
from websocket import create_connection
import json
from asyncio import sleep
#from discord.ext import commands
import interactions
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ClientPresence, StatusType, PresenceActivity, PresenceActivityType, CommandContext, ComponentContext, Modal, TextInput, TextStyleType
from interactions.ext.paginator import Page, Paginator
from interactions.ext.files import command_send
from interactions.ext.tasks import IntervalTrigger, create_task
from secret_data import bodLL, midgardLL, smLL, dc_discord_bot_testy_token, dc_bod_token, dc_discord_bot_testy, dc_bod, dc_sm, cookies, headers, groove_headers, groove_cookies, groove_websocket

#bot = interactions.Client(token = dc_bod_token, presence=ClientPresence(activities=[PresenceActivity(name="Margonem", type=PresenceActivityType.GAME, created_at=0)],status=StatusType.ONLINE, afk=False))
bot = interactions.Client(token = dc_discord_bot_testy_token, presence=ClientPresence(activities=[PresenceActivity(name="Margonem", type=PresenceActivityType.GAME, created_at=0)],status=StatusType.ONLINE, afk=False))
#lb
bicia = 0
uni = 0
hera = 0
legi = 0
rok = ""

#Tanroth
TanrothLegi = ["lega1", "lega2", "lega3", "lega4", "lega5", "lega6"]
TanrothHera = ["hero1", "hero2", "hero3", "hero4", "hero5", "hero6", "hero7", "hero8", "hero9", "hero10", "hero11", "hero12", "hero13", "hero14", "hero15", "hero16", "hero17", "hero18", "hero19", "hero20", "hero21", "hero22"]
TanrothUni = ["uni1", "uni2", "uni3", "uni4", "uni5", "uni6", "uni7"]

#rn
wynikiNick = []
wynikiId = []
wynikiRN = []
wynikiProfil = []
wynikiRank = []
page = 1
position = 1

store = {}

store_quiz_user = {}

store_quiz_server = {}


has_quiz_started = 0
quiz_cd = 20
current_riddle = ""
current_answer = []
quiz_task = None
quiz_number = 0
channel_quiz = None


mob_lvl_heros = {
    'domina ecclesiae': 23,
    'mietek zul': 25,
    'mroczny patryk': 35,
    'karmazynowy msciciel': 40,
    'zlodziej': 50,
    'zly przewodnik': 63,
    'piekielny kosciej': 74,
    'opetany paladyn': 85,
    'kochanka nocy': 100,
    'ksiaze kasim': 116,
    'baca bez lowiec': 123,
    'lichwiarz grauhaz': 127,
    'oblakany lowca orkow': 144,
    'czarujaca atalia': 157,
    'swiety braciszek': 165,
    'viviana nandin': 174,
    'mulher ma': 197,
    'demonis pan nicosci': 210,
    'vapor veneno': 227,
    'deborozec': 242,
    'tepeyollotl': 260,
    'negthotep czarny kaplan': 271,
    'mlody smok': 282
    }

mob_lvl_tytan = {
    'dziewicza orlica': 51,
    'zabojczy krolik': 70,
    'renegat baulus': 101,
    'piekielny arcymag': 131,
    'versus zoons': 154,
    'lowczyni wspomnien': 177,
    'przyzywacz demonow': 204,
    'maddok magua': 231,
    'tezcatlipoca': 258,
    'barbatos smoczy straznik': 285,
    'tanroth': 300
    }

mob_name_tytan = [
    'dziewicza orlica',
    'zabojczy krolik',
    'renegat baulus',
    'piekielny arcymag',
    'versus zoons',
    'lowczyni wspomnien',
    'przyzywacz demonow',
    'maddok magua',
    'tezcatlipoca',
    'barbatos smoczy straznik',
    'tanroth'
    ]

#players_online_run_forever
df_players_online_run_forever_col = ({'Nickname':["temp"], 'Minutes_online':[60], 'Account_id':[1111111], 'Char_id':[1111]})
df_players_online_run_forever = pd.DataFrame(df_players_online_run_forever_col)
df_players_online_run_forever = df_players_online_run_forever.drop(df_players_online_run_forever.index[[0]])


ros_tanroth = ["Ayenn", "Soboll", "Ratheos", "Lascove", "Lubuski Talent", "Mistrz Emifx", "Knoperrs Kokosowy", "Kariston", "Lizeer", "Kompleks Steryda", "Romaren", "Trop kox", "Pinguinek", "Esechjon", "Efate", "FreeFall", "dr reh inż Fri", "Flights", "Whitely", "Fluki", "Rawage", "Nocny Zonk", "Łoś Bibiś", "Shirukibi", "Thahku", "Tamirath", "Antharax", "Teximus", "Cattney", "Roswell", "Biały Lotus", "Moafio", "Popsuted Trop", "Mleczna Milka", "Fallen Wolf", "Mokotowiak", "Rebam", "Delattre", "Puk Puk To Ja", "Po Prostu Sammy", "The Hrynio", "Javek", "Adean", "Soból", "Santhos", "Kakarrot", "Skillzone", "Yamatto"]
ros_teza = ["Elisha", "Lubisz Bigosik", "Katucham", "Nikiss", "Kapitan Chak", "Emifx", "Be Li Bi", "Karistonka", "Wąż boa", "Pinguin", "Esechion", "Efavtu", "Bapple Jack", "Sethaviel", "Bimkie Guy", "Aziz Kallah", "Nikushimi", "Vexez", "Kolorowy Ponczek", "Kolorowa Delicja", "szagor", "Moławio", "Unluckyy Boyy", "Seetu", "Ikohn", "Kinnerad", "Hrynionafide", "Dymcio", "Yerpen", "Sobólowaty", "Sant", "Lokfuhrer"]
ros_magua = ["Laileen", "Ćpałeś", "Emisiek", "Ellectro", "Eysu", "Baksior", "Darkly", "Mejdż Riwejdż", "Ścichapęk", "Rachel Platten", "Inoeki", "Anayessa", "Smakosz Kiwi", "Michał Cartman", "Słoneczny Zarządca", "Go Ahead", "Hrynio Love", "Kochion", "Teturgoth", "Dos Santos", "Szalony Wojtula", "Zuy Dawid"]
ros_przyzy = ["Ninde", "hahaha beka z cb lol", "Katudałn", "Quarsin", "Flaruch", "Valar Morghulis", "Ukered", "ma ktos paje", "Esechionka", "Jędrek Konfident", "Latts Razzi", "Brownly", "Ushuriel", "Evelienn", "Manos Arriba", "Hiddens", "Catte Latte", "Toxic Muchomorek", "Kiui Majipan", "Chryzantem Złocisty", "Kung Fu Adi", "Javcio", "Szoból", "Howard", "Rynuś"]
ros_lowka = ["Virgax", "Szczebiotka", "Nimaster", "Chromosom z Fobosa", "Karistonkeł", "Yazaey", "Noob", "Jesko", "Takeru", "Crimsonly", "Lethaviel", "Zonkuś", "Garram Bad", "Riwaldox", "Alicja Delicja", "Hot Bombel", "Meshy", "Ikoon", "Shaarmus", "Eriten", "Attash", "Fochmistrz", "Ale Mad", "Sebbav"]
ros_zoons = ["Virgax", "Szczebiotka", "Chromosom z Fobosa", "Yazaey", "Takeru", "Crimsonly", "Lethaviel", "Zonkuś", "Riwaldox", "Cattcia", "Alicja Delicja", "Hot Bombel", "Meshy", "Ikoon", "Fochmistrz", "Ale Mad", "Sebbav", "Zły Daimyo"]
ros_arcy = ["Wrzucam Do Pieca", "Dokąd nocą tupta jeż", "Eysunaf", "czwarty skład nigdy", "Cobratate", "Lokadr", "dawid uwu mag", "Kazel", "La Liberta", "Mag Emiś", "Esencion", "trzeci skład w nocy", "Mighty Wolf", "Young Moko", "dawać pierwszy skład"]
ros_renio = ["Payne", "Ojciec Platynov", "Sobollxtorpeda", "Avonex", "Dymciowa", "Pierwsza Klasa", "Catt", "Krayt", "Redly", "Ese", "Sosnowiczanin", "Noiessa", "Rosweluś", "Latrivan", "Takermin", "Pingeł", "Hezuuś", "Elektronicky Mordulec", "Daksanius", "Arnielsem", "Olivitess", "Toverk Furrim", "Etaine", "Dredge", "Helmut Byk", "Pe Pe Ga", "Dark Wolfik", "Norman Parke", "Moawio", "Insel"]
ros_krolik = ["Casmot", "Rozpacz", "Katudar", "Cold Bombel", "B o o b a", "Blackly", "Patoshi", "Sobólek", "Thrawn", "Emisiowaty", "Szkoda", "Rycerz Ortalionu", "Bździągwa", "Pukecz", "Rudy Z Wrocławia", "Lucypher", "Bodawio", "Zua Flarusia", "Vexteron", "Vadosu", "Xaiket", "Obrona Sycylijska", "Smakołysz Muszity", "Karistołek", "Lil Moko", "Fiubździu", "One six nine", "Sir Flookie"]
ros_orla = ["Katudar", "Vadosu", "Xaiket", "Obrona Sycylijska", "Smakołysz Muszity", "Karistołek", "Lil Moko", "Fiubździu", "One six nine", "Sir Flookie"]

west_tanroth = ["Młody Charlie", "Shiranoy", "Hozukimaru", "Opunaa", "Yetiuszek", "Brad Bellick", "Teriash", "Vexuss", "Piłem aż Wypiłem", "Treno", "Mr Valex", "Głośnik", "Ałuś"]
west_teza = ["Akri Partenopajos", "Agilla", "Valeksik", "Presir"]
west_magua = ["Massey", "Vexuso", "Fluxe"]
west_przyzy = ["Thorin X", "Wolyo", "Jermaen", "Mały Yeti", "Xenaes", "Reswesin", "Valex", "Vexusik", "Riserp", "Flyleaf", "Mecenas Diabła"]
west_lowka = ["Baltazarek", "Xiądz Robak", "Faraya", "Little Opun", "Majsterek Valexa", "Karramba", "Treo", "Demixo", "Michael Scofield", "Ivar Ragnarsson", "Vimarth"]
west_zoons = ["Baltazarek", "Xiądz Robak", "Faraya", "Little Opun", "Majsterek Valexa", "Karramba", "Treo", "Demixo", "Michael Scofield", "Ivar Ragnarsson", "Vimarth"]
west_arcy = ["Ciemnogród z Rzucowa", "kox woj ever", "Opun", "Mc Donald", "Don Ciasteczko", "Zuy Teri"]
west_renio = ["Tańczący Charlie", "Jacques de Molay", "Katharin", "Doribi", "Orriz", "Don Self", "Owocowy Eklerek", "Suxev", "Max Bombel", "Sprośny Jelonek", "Fasen"]
west_krolik = ["Tharik Lokfor", "Słodki Valex", "Shellma", "Przesłodzony Demi", "Silrass", "Tarantóla"]
west_orla = []


async def get_data(arg, argOrig):
    global bicia, uni, hera, legi, rok
    odpowiedz = requests.get(arg, cookies=cookies, headers=headers)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    soup.find_all('div', class_='item col-md-12 row-shadow')
    bicia += len(soup.find_all('div', class_='item col-md-12 row-shadow'))

    for i in soup.find_all('div', class_='item col-md-12 row-shadow'):
        rok = i.find_all('div', class_='col-md-1')

        for j in i.find_all('img'):
            if str(j).find("unique")>0:
                uni += 1;
            elif str(j).find("heroic")>0:
                hera += 1;
            elif str(j).find("legendary")>0:
                legi += 1;
    print(str(bicia) + " | " + str(uni) + " | " + str(hera) + " | " + str(legi))

    if len(soup.find_all('a', class_='btn next')) > 0:
        for i in soup.find_all('a', class_='btn next'):
            await get_data(argOrig+str(i['href'])[str(i['href']).find(","):], argOrig)

async def get_timer(embed):
    try:
        global mob_lvl_heros, mob_lvl_tytan, mob_name_tytan
        odpowiedz = requests.get(bodLL + "/timer", cookies=cookies, headers=headers)
        soup = BeautifulSoup(odpowiedz.text, 'html.parser')
        soup = soup.find_all('div', class_='timer item col-md-12 row-shadow center')
        #print(len(soup))

        df_timer_col = ({'Mob':["temp"], 'Resp_min':[60], 'Resp_max':[1111111], 'Lvl':[1]})
        df_timer_herosi = pd.DataFrame(df_timer_col)
        df_timer_herosi = df_timer_herosi.drop(df_timer_herosi.index[[0]])
        df_timer_tytani = pd.DataFrame(df_timer_col)
        df_timer_tytani = df_timer_tytani.drop(df_timer_tytani.index[[0]])
        #print(len(df_timer_herosi))
        embed_value_str_herosi = ""
        embed_value_str_tytani = ""

        for i in soup:
            mob = i.find('b', class_='color').string
            resp = i.find_all('div', class_='time color')
            #print(resp)
            resp_min = int(resp[0]['data-time'])
            resp_max = int(resp[1]['data-time'])

            if(resp_min == resp_max):
                continue
            if(resp_min > 1000000 or resp_max > 1000000):
                continue

            if(mob in mob_name_tytan):
                df_timer_tytani = df_timer_tytani.append({'Mob':mob, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(mob_lvl_tytan[mob])}, ignore_index=True)
            elif(mob_lvl_heros[mob]):
                df_timer_herosi = df_timer_herosi.append({'Mob':mob, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(mob_lvl_heros[mob])}, ignore_index=True)
            else:
                df_timer_herosi = df_timer_herosi.append({'Mob':mob, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':350}, ignore_index=True)

        df_timer_herosi.sort_values(by=['Lvl'], inplace=True)
        df_timer_tytani.sort_values(by=['Lvl'], inplace=True)
        print(df_timer_herosi)
        print(df_timer_tytani)

        if(len(df_timer_herosi) > 0):
            for index, row in df_timer_herosi.iterrows():
                if(row['Resp_min'] < 0 and row['Resp_max'] < 0):
                    embed_value_str_herosi = embed_value_str_herosi + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " po maksymalnym respie\n"
                elif(row['Resp_min'] > 0 and row['Resp_max'] > 0):
                    embed_value_str_herosi = embed_value_str_herosi + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_min']))) + " do minimalnego respa\n"
                elif(row['Resp_min'] < 0 and row['Resp_max'] > 0):
                    embed_value_str_herosi = embed_value_str_herosi + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " do maksymalnego respa\n"
                else:
                    print("Cos nie tak bo nie powinno")

            embed_value_str_herosi = embed_value_str_herosi[:-1]
            embed.add_field(name="Herosi:", value=embed_value_str_herosi, inline=False)
        else:
            embed_value_str_herosi = "Brak timerów herosów"
            embed.add_field(name="Herosi:", value=embed_value_str_herosi, inline=False)

        if(len(df_timer_tytani) > 0):
            for index, row in df_timer_tytani.iterrows():
                if(row['Resp_min'] < 0 and row['Resp_max'] < 0):
                    embed_value_str_tytani = embed_value_str_tytani + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " po maksymalnym respie\n"
                elif(row['Resp_min'] > 0 and row['Resp_max'] > 0):
                    embed_value_str_tytani = embed_value_str_tytani + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_min']))) + " do minimalnego respa\n"
                elif(row['Resp_min'] < 0 and row['Resp_max'] > 0):
                    embed_value_str_tytani = embed_value_str_tytani + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " do maksymalnego respa\n"
                else:
                    print("Cos nie tak bo nie powinno")

            embed_value_str_tytani = embed_value_str_tytani[:-1]
            embed.add_field(name="Tytani:", value=embed_value_str_tytani, inline=False)
        else:
            embed_value_str_tytani = "Brak timerów tytanów"
            embed.add_field(name="Tytani:", value=embed_value_str_tytani, inline=False)
    except Exception as e: 
        print(e)


async def add_timer(ctx, mob_name):
    global groove_headers, groove_cookies
    groove_cookie_string = "; ".join([str(x)+"="+str(y) for x,y in groove_cookies.items()])

    if(int(ctx.author.user.id) == 349851438228439040 or int(ctx.author.user.id) == 372381114809188362):
        try:
            ws = create_connection(groove_websocket, header = groove_headers, cookie = groove_cookie_string)
            ws.send('42' + json.dumps(["data",{"name":mob_name,"action":"addhottimer","clan":"blade_of_destiny_narwhals","clanID":1834,"aid":"5897579"}]))
            ws.close()
            return 1
        except:
            return 3
    else:
        return 2
    

async def get_timer_alt(embed):
    global groove_headers, groove_cookies, mob_lvl_heros, mob_lvl_tytan, mob_name_tytan
    groove_cookie_string = "; ".join([str(x)+"="+str(y) for x,y in groove_cookies.items()])
    ws = create_connection(groove_websocket, header = groove_headers, cookie = groove_cookie_string)
    ws.send('42' + json.dumps(["data",{"action":"init","clan":"blade_of_destiny_narwhals","clanID":1834,"aid":"5897579"}]))
    for i in range(10):
        result =  ws.recv()
        if(result[15:21] == 'timers'):
            df_timer_col = ({'Mob':["temp"], 'Resp_min':[60], 'Resp_max':[1111111], 'Lvl':[1]})
            df_timer_herosi = pd.DataFrame(df_timer_col)
            df_timer_herosi = df_timer_herosi.drop(df_timer_herosi.index[[0]])
            df_timer_tytani = pd.DataFrame(df_timer_col)
            df_timer_tytani = df_timer_tytani.drop(df_timer_tytani.index[[0]])
            embed_value_str_herosi = ""
            embed_value_str_tytani = ""

            data  = json.loads(result[13:-1])
            data = data['timers']
            for j in range(len(data)):
                print(data[j])
                mob = data[j]['name']
                #print(resp)
                resp_min = int(data[j]['minRespTime'])
                resp_max = int(data[j]['maxRespTime'])

                if(resp_min == resp_max):
                    continue
                if(resp_min > 1000000 or resp_max > 1000000):
                    continue

                #print(mob, resp_min, resp_max)
                s = ' '.join(word[0].upper() + word[1:] for word in mob.split())
                if(mob in mob_name_tytan):
                    df_timer_tytani = df_timer_tytani.append({'Mob':s, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(mob_lvl_tytan[mob])}, ignore_index=True)
                elif(mob in mob_lvl_heros):
                    df_timer_herosi = df_timer_herosi.append({'Mob':s, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(mob_lvl_heros[mob])}, ignore_index=True)
                else:
                    df_timer_herosi = df_timer_herosi.append({'Mob':s, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':350}, ignore_index=True)
            df_timer_herosi.sort_values(by=['Lvl'], inplace=True)
            df_timer_tytani.sort_values(by=['Lvl'], inplace=True)
            print(df_timer_herosi)
            print(df_timer_tytani)

            if(len(df_timer_herosi) > 0):
                for index, row in df_timer_herosi.iterrows():
                    if(row['Resp_min'] < 0 and row['Resp_max'] < 0):
                        embed_value_str_herosi = embed_value_str_herosi + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " po maksymalnym respie\n"
                    elif(row['Resp_min'] > 0 and row['Resp_max'] > 0):
                        embed_value_str_herosi = embed_value_str_herosi + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_min']))) + " do minimalnego respa\n"
                    elif(row['Resp_min'] < 0 and row['Resp_max'] > 0):
                        embed_value_str_herosi = embed_value_str_herosi + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " do maksymalnego respa\n"
                    else:
                        print("Cos nie tak bo nie powinno")

                embed_value_str_herosi = embed_value_str_herosi[:-1]
                embed.add_field(name="Herosi:", value=embed_value_str_herosi, inline=False)
            else:
                embed_value_str_herosi = "Brak timerów herosów"
                embed.add_field(name="Herosi:", value=embed_value_str_herosi, inline=False)

            if(len(df_timer_tytani) > 0):
                for index, row in df_timer_tytani.iterrows():
                    if(row['Resp_min'] < 0 and row['Resp_max'] < 0):
                        embed_value_str_tytani = embed_value_str_tytani + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " po maksymalnym respie\n"
                    elif(row['Resp_min'] > 0 and row['Resp_max'] > 0):
                        embed_value_str_tytani = embed_value_str_tytani + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_min']))) + " do minimalnego respa\n"
                    elif(row['Resp_min'] < 0 and row['Resp_max'] > 0):
                        embed_value_str_tytani = embed_value_str_tytani + row['Mob'] + " " + str(datetime.timedelta(seconds=abs(row['Resp_max']))) + " do maksymalnego respa\n"
                    else:
                        print("Cos nie tak bo nie powinno")

                embed_value_str_tytani = embed_value_str_tytani[:-1]
                embed.add_field(name="Tytani:", value=embed_value_str_tytani, inline=False)
            else:
                embed_value_str_tytani = "Brak timerów tytanów"
                embed.add_field(name="Tytani:", value=embed_value_str_tytani, inline=False)
            break
    ws.close()
    return 1



async def setLink(arg):
    global bodLL, midgardLL, smLL
    if arg.lower() == "bod":
        return bodLL
    elif arg.lower() == "midgard":
        return midgardLL
    elif arg.lower() == "sm":
        return smLL
    else:
        return "BRAK"

async def getMobData(argEmbed, argLink, argMobName, argMobLvl):
    global bicia, uni, hera, legi
    await get_data(argLink + "monster-" + argMobName, argLink + "monster-" + argMobName)
    sumaBic = uni + hera + legi
    if sumaBic == 0:
        sumaBic = 1
    argEmbed.add_field(name=argMobName + "(" + argMobLvl + " lvl):", value="**Bicia: **" + str(bicia) + "\t**Unikaty: **" + str(uni) + "\t**Heroiki: **" + str(hera) + "\t**Legendy: **" + str(legi) + "\n**Procentowy udzial legend: **" + str(round(float(legi)/float(sumaBic)*100, 2)) + "%", inline=False)
    bicia = 0
    uni = 0
    hera = 0
    legi = 0

async def resetWyniki():
    global page, position
    wynikiNick.clear()
    wynikiId.clear()
    wynikiRN.clear()
    wynikiProfil.clear()
    wynikiRank.clear()
    page = 1
    position = 1

async def get_data_darro():
    global page, position
    odpowiedz = requests.get("https://narwhals.darro.eu/?t=currency&page=" + str(page))
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    print(page)
    print(len(soup.find_all('td'))/2)
    if (len(soup.find_all('td'))>0):
        for i in soup.find_all("td"):
            if len(i)>=5:
                wynikiNick.append(i.a.string)
                wynikiProfil.append(i.a['href'])
                wynikiId.append(i.a['href'].replace('https://www.margonem.pl/?task=profile&id=', ''))
                wynikiRank.append(str(position))
                position+=1
            else:
                wynikiRN.append(i.string)
        page += 1
        await get_data_darro()

async def get_data_absency(ctx, df, world, link, page):
    odpowiedz = requests.get(link + str(page))
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    table = soup.find('table', class_='table--separators w-100')
    table = soup.find('tbody')
    try:
        length = len(table.find_all('tr'))
    except:
        length = 0
    if(length>1):
        for i in table.find_all('tr'):
            data = i.find_all("td")
            nickname = data[1].a.string[37:-32]
            lvl = data[2].string[33:-28]
            last_online = data[5].string[33:-28]
            last_online = last_online[:-9]
            try:
                last_online = int(last_online)
            except:
                last_online = 1
                
            list = [nickname, lvl, last_online]
            df.loc[len(df)] = list
        time.sleep(0.5)
        await get_data_absency(ctx, df, world, link, page+1)
    else:
        #df = df.sort_values(by=['Last online'], ascending=False).head(int(arg))
        df = df.sort_values(by=['Last online'], ascending=False).head(100)
        df = df.reset_index()

        current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        date_today = dt.strptime(current_daytime, "%Y-%m-%d %H:%M:%S")
        #print(df2)
        await delete_data_in_db_absency(world)
        #for index, row in df.iterrows():
            #await update_data_in_db_absency(world, row['Nickname'], row['Lvl'], row['Last online'])
        
        await absency_df(ctx, world, df, current_daytime)
        
        #del embed_value, df, df2, length, table, soup, odpowiedz


async def absency_df(ctx, world, df, current_daytime):
    embed_value1 = ""
    embed_value2 = ""
    embed_value3 = ""
    embed_value4 = ""
    iteration = 0
    embed1=interactions.Embed(title="Lista 100 graczy z najdłuższą nieaktywnością na świecie " + world + ", stan na " + current_daytime[8:10] + "-" + current_daytime[5:7] + "-" + current_daytime[0:4] + " " + current_daytime[11:16])
    embed2=interactions.Embed(title="Lista 100 graczy z najdłuższą nieaktywnością na świecie " + world + ", stan na " + current_daytime[8:10] + "-" + current_daytime[5:7] + "-" + current_daytime[0:4] + " " + current_daytime[11:16])
    embed3=interactions.Embed(title="Lista 100 graczy z najdłuższą nieaktywnością na świecie " + world + ", stan na " + current_daytime[8:10] + "-" + current_daytime[5:7] + "-" + current_daytime[0:4] + " " + current_daytime[11:16])
    embed4=interactions.Embed(title="Lista 100 graczy z najdłuższą nieaktywnością na świecie " + world + ", stan na " + current_daytime[8:10] + "-" + current_daytime[5:7] + "-" + current_daytime[0:4] + " " + current_daytime[11:16])
    for index, row in df.iterrows():
        #print(row['Nickname'], row['Lvl'], row['Last online'])
        await update_data_in_db_absency(world, row['Nickname'], row['Lvl'], row['Last online'])
        if(iteration <= 24):
            embed_value1 = embed_value1 + row['Nickname'] + "(" + str(row['Lvl']) + ")  :  " + str(row['Last online']) + "\n"
        elif(iteration <= 49):
            embed_value2 = embed_value2 + row['Nickname'] + "(" + str(row['Lvl']) + ")  :  " + str(row['Last online']) + "\n"
        elif(iteration <= 74):
            embed_value3 = embed_value3 + row['Nickname'] + "(" + str(row['Lvl']) + ")  :  " + str(row['Last online']) + "\n"
        elif(iteration <= 99):
            embed_value4 = embed_value4 + row['Nickname'] + "(" + str(row['Lvl']) + ")  :  " + str(row['Last online']) + "\n"
        iteration = iteration + 1
    embed1.add_field(name="(1/4)", value=embed_value1, inline=False)
    embed2.add_field(name="(2/4)", value=embed_value2, inline=False)
    embed3.add_field(name="(3/4)", value=embed_value3, inline=False)
    embed4.add_field(name="(4/4)", value=embed_value4, inline=False)

    online_pages = await Paginator(
        client = bot,
        ctx=ctx,
        pages=[
            Page(embeds = embed1, title = "(1/4)"),
            Page(embeds = embed2, title = "(2/4)"),
            Page(embeds = embed3, title = "(3/4)"),
            Page(embeds = embed4, title = "(4/4)"),
        ],
        timeout = 600,
        remove_after_timeout = True,
    ).run()

async def create_database():
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    #cur.execute("CREATE TABLE absency_last_update(world, date)")
    #cur.execute("CREATE TABLE absency(world, nickname, lvl, days_offline)")
    cur.execute("CREATE TABLE quiz_results(server_id, user_id, nickname, hash, tried, points, won, lost)")

async def check_data_in_db_absency_last(world, ctx):
    current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    date_today = dt.strptime(current_daytime, "%Y-%m-%d %H:%M:%S")
    #print(type(date_today))
    print("Today:" + str(date_today))
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    #cur.execute("INSERT INTO currency_rates VALUES(1, 22, 11, 16, 'currency', 'value')")
    sql = ''' SELECT date
              FROM absency_last_update
              WHERE world = ?'''
    res = cur.execute(sql, [world])
    res2 = res.fetchone()
    #print(res.fetchone()[0])
    #print(type(res.fetchone()[0]))
    if(res2 is None):
        print("Brak daty, dodaje wpis")
        data = (world, current_daytime)
        sql = ''' INSERT INTO absency_last_update(world, date)
                  VALUES(?, ?)'''
        cur.execute(sql, data)
        con.commit()
        #print("Wpis dodany")
        return True
    else:
        date_last_update = dt.strptime(str(res2)[2:-3], "%Y-%m-%d %H:%M:%S")
        ts_last_update = dt(date_last_update.year, date_last_update.month, date_last_update.day, date_last_update.hour, date_last_update.minute, date_last_update.second).timestamp()
        ts_today = dt(date_today.year, date_today.month, date_today.day, date_today.hour, date_today.minute, date_today.second).timestamp()
        print("Last update:" + str(ts_last_update))
        print("Today:" + str(ts_today))
        if(ts_today>ts_last_update + 21000):
            print("Aktualizacja danych")
            data = (current_daytime, world)
            sql = ''' UPDATE absency_last_update
                      SET date = ?
                      WHERE world = ?'''
            cur.execute(sql, data)
            con.commit()
            print("OK")
            return True
        else:
            print("Dane w bazie sa aktualne")

            path = 'database.db'
            con = sqlite3.connect(path)
            cur = con.cursor()
            #cur.execute("INSERT INTO currency_rates VALUES(1, 22, 11, 16, 'currency', 'value')")
            sql = ''' SELECT nickname, lvl, days_offline
                    FROM absency
                    WHERE world = ?'''
            res = cur.execute(sql, [world])
            res3 = res.fetchall()
            #print(res2)
            df = pd.DataFrame (res3, columns = ['Nickname', 'Lvl', 'Last online'])
            #print(df['currency'].values[0])
            df['Lvl'] = df['Lvl'].astype(int)
            df['Last online'] = df['Last online'].astype(int)

            #print(df)
            df2 = df.head(100)

            await absency_df(ctx, world, df2, str(res2)[2:-3])
            
            return False


async def update_data_in_db_absency(world, nickname, lvl, last_online):
    data = (world, nickname, lvl, last_online)
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = ''' INSERT INTO absency(world, nickname, lvl, days_offline)
              VALUES(?, ?, ?, ?)'''
    cur.execute(sql, data)
    con.commit()
    #print("Wpis dodany")

async def delete_data_in_db_absency(world):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = ''' DELETE FROM absency
              WHERE world = ?'''
    cur.execute(sql, [world])
    con.commit()
    print("Wpis dodany")


async def check_data_in_db_tanroth_last_update(id):
    current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    date_today = dt.strptime(current_daytime, "%Y-%m-%d %H:%M:%S")
    #print(type(date_today))
    #print("Today:" + str(current_daytime))
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    #cur.execute("INSERT INTO currency_rates VALUES(1, 22, 11, 16, 'currency', 'value')")
    sql = ''' SELECT date
              FROM tanroth_last_update
              WHERE id = ?'''
    res = cur.execute(sql, [id])
    res2 = res.fetchone()
    #print(res.fetchone()[0])
    #print(type(res.fetchone()[0]))
    if(res2 is None):
        #print("Brak daty, dodaje wpis")
        data = (id, current_daytime)
        sql = ''' INSERT INTO tanroth_last_update(id, date)
                  VALUES(?, ?)'''
        cur.execute(sql, data)
        con.commit()
        #print("Wpis dodany")
        return 1
    else:
        #str_res2 = str(res2)
        #str_res2 = str_res2[2:-3]
        #print(str_res2)
        #print(res2)
        date_last_update = dt.strptime(str(res2)[2:-3], "%Y-%m-%d %H:%M:%S")
        #print(date_last_update)
        #print(type(date_last_update))
        #print(type(date_today))
        #ts_last_update = dt(date_last_update).timestamp()
        #ts_today = dt(date_today).timestamp()
        ts_last_update = dt(date_last_update.year, date_last_update.month, date_last_update.day, date_last_update.hour, date_last_update.minute, date_last_update.second).timestamp()
        ts_today = dt(date_today.year, date_today.month, date_today.day, date_today.hour, date_today.minute, date_today.second).timestamp()
        print("Last update:" + str(ts_last_update))
        print("Today:" + str(ts_today))
        if(ts_today>ts_last_update + 600):
            data = (current_daytime, id)
            sql = ''' UPDATE tanroth_last_update
                      SET date = ?
                      WHERE id = ?'''
            cur.execute(sql, data)
            con.commit()
            print("OK")
            return 1
        else:
            print("Zaczekaj...")
            print(type(ts_today - ts_last_update))
            return ts_today - ts_last_update

async def check_data_in_characters_in_game(server_id, user_id, player_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (int(server_id), int(user_id))
    sql = ''' SELECT player_id
              FROM characters_in_game
              WHERE server_id = ? AND user_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        data = (int(server_id), int(user_id), player_id)
        sql = ''' INSERT INTO characters_in_game(server_id, user_id, player_id)
                  VALUES(?, ?, ?)'''
        cur.execute(sql, data)
        con.commit()
        return 1
    else:
        return res2[0]


async def update_characters_in_game(server_id, user_id, player_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (player_id, int(server_id), int(user_id))
    sql = ''' UPDATE characters_in_game
              SET player_id = ?
              WHERE server_id = ? AND user_id = ?'''
    cur.execute(sql, data)
    con.commit()


async def update_characters_in_game_temp(user_id, player_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = ''' SELECT player_id
              FROM characters_in_game_temp
              WHERE user_id = ?'''
    res = cur.execute(sql, [int(user_id)])
    res2 = res.fetchone()
    print(res2)
    #print(res.fetchone()[0])
    #print(type(res.fetchone()[0]))
    if(res2 is None):
        #print("Brak daty, dodaje wpis")
        data = (int(user_id), player_id)
        sql = ''' INSERT INTO characters_in_game_temp(user_id, player_id)
                  VALUES(?, ?)'''
        cur.execute(sql, data)
        con.commit()
        #print("Wpis dodany")
    else:
        data = (player_id, int(user_id))
        sql = ''' UPDATE characters_in_game_temp
                  SET player_id = ?
                  WHERE user_id = ?'''
        cur.execute(sql, data)
        con.commit()

async def select_characters_in_game_temp(user_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = ''' SELECT player_id
              FROM characters_in_game_temp
              WHERE user_id = ?'''
    res = cur.execute(sql, [int(user_id)])
    res2 = res.fetchone()
    return res2[0]


async def check_data_in_tanroth_drops(server_id, user_id, drop):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (int(server_id), int(user_id))
    sql = ''' SELECT uni
              FROM tanroth_drops
              WHERE server_id = ? AND user_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        data = (int(server_id), int(user_id), 0, 0, 0)
        sql = ''' INSERT INTO tanroth_drops(server_id, user_id, uni, hera, legi)
                  VALUES(?, ?, ?, ?, ?)'''
        cur.execute(sql, data)
        con.commit()
        await update_tanroth_drops(server_id, user_id, drop)
    else:
        await update_tanroth_drops(server_id, user_id, drop)

async def update_tanroth_drops(server_id, user_id, drop):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    if(drop == "uni"):
        data = (1 + int(await select_tanroth_drops(server_id, user_id, drop)), int(server_id), int(user_id))
        sql = ''' UPDATE tanroth_drops
                  SET uni = ?
                  WHERE server_id = ? AND user_id = ?'''
    elif(drop == "hero"):
        data = (1 + int(await select_tanroth_drops(server_id, user_id, drop)), int(server_id), int(user_id))
        sql = ''' UPDATE tanroth_drops
                  SET hera = ?
                  WHERE server_id = ? AND user_id = ?'''
    elif(drop == "lega"):
        data = (1 + int(await select_tanroth_drops(server_id, user_id, drop)), int(server_id), int(user_id))
        sql = ''' UPDATE tanroth_drops
                  SET legi = ?
                  WHERE server_id = ? AND user_id = ?'''       
    cur.execute(sql, data)
    con.commit()

async def select_tanroth_drops(server_id, user_id, drop):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (int(server_id), int(user_id))
    if(drop == "uni"):
        sql = ''' SELECT uni
                  FROM tanroth_drops
                  WHERE server_id = ? AND user_id = ?'''
    elif(drop == "hero"):
        sql = ''' SELECT hera
                  FROM tanroth_drops
                  WHERE server_id = ? AND user_id = ?'''
    elif(drop == "lega"):
        sql = ''' SELECT legi
                  FROM tanroth_drops
                  WHERE server_id = ? AND user_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    return res2[0]


async def select_all_tanroth_drops(server_id, user_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (int(server_id), int(user_id))
    sql = ''' SELECT uni, hera, legi
              FROM tanroth_drops
              WHERE server_id = ? AND user_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    return res2

async def random_tanroth_item(server_id, user_id):
    random_number = random.randint(1,1000)
    print(random_number)
    if(random_number <= 5):         #1/200
        print("Wylosowales: " + TanrothLegi[random.randint(0,len(TanrothLegi)-1)])
        await check_data_in_tanroth_drops(server_id, user_id, "lega")
        return TanrothLegi[random.randint(0,len(TanrothLegi)-1)]
    elif(random_number >= 6 and random_number <= 405):          #40%
        print("Wylosowales: " + TanrothHera[random.randint(0,len(TanrothHera)-1)])
        await check_data_in_tanroth_drops(server_id, user_id, "hero")
        return TanrothHera[random.randint(0,len(TanrothHera)-1)]
    else:
        print("Wylosowales: " + TanrothUni[random.randint(0,len(TanrothUni)-1)])
        await check_data_in_tanroth_drops(server_id, user_id, "uni")
        return TanrothUni[random.randint(0,len(TanrothUni)-1)]
    

async def update_data_in_db_quiz(server_id, zagadka, odpowiedz):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = [server_id]
    sql = ''' SELECT odpowiedz
              FROM quiz
              WHERE server_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        data = (server_id, zagadka, odpowiedz)
        sql = ''' INSERT INTO quiz(server_id, zagadka, odpowiedz)
                  VALUES(?, ?, ?)'''
        cur.execute(sql, data)
        con.commit()
    else:
        data = (zagadka, odpowiedz, server_id)
        sql = ''' UPDATE quiz
                  SET zagadka = ?, odpowiedz = ?
                  WHERE server_id = ?'''
        cur.execute(sql, data)
        con.commit()


async def add_data_in_db_quiz(server_id, zagadka, odpowiedz):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (server_id, zagadka, odpowiedz)
    sql = ''' INSERT INTO quiz(server_id, zagadka, odpowiedz)
              VALUES(?, ?, ?)'''
    cur.execute(sql, data)
    con.commit()


async def delete_data_in_db_quiz(server_id, zagadka, odpowiedz):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = [server_id]
    sql = ''' SELECT *
              FROM quiz
              WHERE server_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        return 2
    else:
        data = (server_id, zagadka, odpowiedz)
        sql = ''' DELETE FROM quiz
                WHERE server_id = ? AND zagadka = ? AND odpowiedz = ?'''
        cur.execute(sql, data)
        con.commit()
        return 1
    

async def delete_all_data_in_db_quiz(server_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = [server_id]
    sql = ''' SELECT *
              FROM quiz
              WHERE server_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        return 2
    else:
        sql = ''' DELETE FROM quiz
                  WHERE server_id = ?'''
        cur.execute(sql, [server_id])
        con.commit()
        return 1
    
    
async def get_data_in_db_quiz(server_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = [server_id]
    sql = ''' SELECT zagadka, odpowiedz
              FROM quiz
              WHERE server_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchall()
    return res2



async def check_data_in_db_quiz_results(server_id, user_id, nickname, hash):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (server_id, user_id)
    sql = ''' SELECT won, tried
              FROM quiz_results
              WHERE server_id = ? AND user_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        data = (server_id, user_id, nickname, hash, 0, 0, 0, 0)
        sql = ''' INSERT INTO quiz_results(server_id, user_id, nickname, hash, tried, points, won, lost)
                  VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
        cur.execute(sql, data)
        con.commit()
        return 0
    else:
        return res2[0]
    

async def update_data_in_db_quiz_results(server_id, user_id, tried, points, won, lost):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (tried, points, won, lost, server_id, user_id)
    sql = ''' UPDATE quiz_results
              SET tried = ?, points = ?, won = ?, lost = ?
              WHERE server_id = ? AND user_id = ?'''
    cur.execute(sql, data)
    con.commit()


async def reset_data_in_db_quiz_results(server_id, user_id, what_to_reset):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    if(what_to_reset == "results"):
        data = (0, 0, 0, 0, server_id)
        sql = ''' UPDATE quiz_results
                SET tried = ?, points = ?, won = ?, lost = ?
                WHERE server_id = ?'''
    elif(what_to_reset == "won"):
        data = (0, server_id)
        sql = ''' UPDATE quiz_results
                SET won = ?
                WHERE server_id = ?'''
    elif(what_to_reset == "all"):
        data = [server_id]
        sql = ''' DELETE FROM quiz_results
                  WHERE server_id = ?'''
    cur.execute(sql, data)
    con.commit()


async def get_data_in_db_quiz_results(server_id, user_id = None):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    if(user_id is None):
        data = [server_id]
        sql = ''' SELECT *
                FROM quiz_results
                WHERE server_id = ?'''
    else:
        data = (server_id, user_id)
        sql = ''' SELECT *
                FROM quiz_results
                WHERE server_id = ? AND user_id = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchall()
    return res2


async def players_online(ctx, swiat):
    try:
        URL = "https://public-api.margonem.pl/info/online/"+ swiat.lower() +".json"
        r = requests.get(url = URL)
        data = r.json()
    except:
        await ctx.send("Nie udało się pobrać listy graczy online, prawdopodobnie serwery Margonem leżą")
        return
    #data = []
    #print(data)
    #print(len(data))
    if(len(data) == 0):
        await ctx.send("**Gracze online na swiecie " + swiat + "**\n" + "Brak graczy online")
        return
    online_string = ""
    header_sent = 0
    for i in data:
        online_string = online_string + i['n'] + "(" + i['l'] + i['p'] + ")" + ", "
        if(len(online_string) > 1900):
            online_string = online_string[:-2]
            if(header_sent):
                await ctx.send("...\n" + online_string + "\n...")
            else:
                await ctx.send("**Gracze online na swiecie " + swiat + "**\n" + online_string + "\n...")
            online_string = ""
            header_sent = 1
    online_string = online_string[:-2]
    if(header_sent):
        await ctx.send("...\n" + online_string)
    else:
        await ctx.send("**Gracze online na swiecie " + swiat + "**\n" + online_string)


async def players_online_run_forever(swiat):
    global df_players_online_run_forever, ros_tanroth, ros_teza, ros_magua, ros_przyzy, ros_lowka, ros_zoons, ros_arcy, ros_renio, ros_krolik, ros_orla, west_tanroth, west_teza, west_magua, west_przyzy, west_lowka, west_zoons, west_arcy, west_renio, west_krolik
    ros_tanroth_count = 0
    ros_teza_count = 0
    ros_magua_count = 0
    ros_przyzy_count = 0
    ros_lowka_count = 0
    ros_zoons_count = 0
    ros_arcy_count = 0
    ros_renio_count = 0
    ros_krolik_count = 0
    ros_orla_count = 0
    west_tanroth_count = 0
    west_teza_count = 0
    west_magua_count = 0
    west_przyzy_count = 0
    west_lowka_count = 0
    west_zoons_count = 0
    west_arcy_count = 0
    west_renio_count = 0
    west_krolik_count = 0

    try:
        URL = "https://public-api.margonem.pl/info/online/narwhals.json"
        r = requests.get(url = URL)
        data = r.json()
    except Exception as e:
        print(e)
        data = []

    current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    date_today = dt.strptime(current_daytime, "%Y-%m-%d %H:%M:%S")
    try:
        for i in data:
            nickname = i['n']
            account_id = i['a']
            char_id = i['c']
            if(df_players_online_run_forever.loc[df_players_online_run_forever['Nickname'] == nickname].any().all()):
                df_minutes = df_players_online_run_forever.loc[df_players_online_run_forever['Nickname'] == nickname]
                minutes = df_minutes['Minutes_online'].to_string(index=False)
                df_players_online_run_forever.loc[df_players_online_run_forever['Nickname'] == nickname, ['Minutes_online']] = int(minutes) + 1
            else:
                df_players_online_run_forever = df_players_online_run_forever.append({'Nickname':nickname, 'Minutes_online':int(1), 'Account_id':int(account_id), 'Char_id':int(char_id)}, ignore_index=True)
            if(int(date_today.hour) <= 7):
                if(nickname in ros_tanroth):
                    ros_tanroth_count = ros_tanroth_count+1
                if(nickname in ros_teza):
                    ros_teza_count = ros_teza_count+1
                if(nickname in ros_magua):
                    ros_magua_count = ros_magua_count+1
                if(nickname in ros_przyzy):
                    ros_przyzy_count = ros_przyzy_count+1
                #if(nickname in ros_lowka):
                #    ros_lowka_count = ros_lowka_count+1
                if(nickname in ros_zoons):
                    ros_zoons_count = ros_zoons_count+1
                #if(nickname in ros_arcy):
                #    ros_arcy_count = ros_arcy_count+1
                if(nickname in ros_renio):
                    ros_renio_count = ros_renio_count+1
                #if(nickname in ros_krolik):
                #    ros_krolik_count = ros_krolik_count+1
                #if(nickname in ros_orla):
                #    ros_orla_count = ros_orla_count+1
                if(nickname in west_tanroth):
                    west_tanroth_count = west_tanroth_count+1
                if(nickname in west_teza):
                    west_teza_count = west_teza_count+1
                if(nickname in west_magua):
                    west_magua_count = west_magua_count+1
                if(nickname in west_przyzy):
                    west_przyzy_count = west_przyzy_count+1
                #if(nickname in west_lowka):
                #    west_lowka_count = west_lowka_count+1
                if(nickname in west_zoons):
                    west_zoons_count = west_zoons_count+1
                #if(nickname in west_arcy):
                #    west_arcy_count = west_arcy_count+1
                if(nickname in west_renio):
                    west_renio_count = west_renio_count+1
                #if(nickname in west_krolik):
                #    west_krolik_count = west_krolik_count+1
        
        #print(df_players_online_run_forever)
        #print(ros_tanroth_count, ros_teza_count, ros_magua_count, ros_przyzy_count, ros_lowka_count, ros_zoons_count, ros_arcy_count, ros_renio_count, ros_krolik_count, ros_orla_count, west_tanroth_count, west_teza_count, west_magua_count, west_przyzy_count, west_lowka_count, west_zoons_count, west_arcy_count, west_renio_count, west_krolik_count)
        
        players_online_to_ping = 5
        channel = await interactions.get(bot, interactions.Channel, object_id=1081942227867140217)

        if(int(date_today.hour) >= 10):
            if(ros_tanroth_count >= 7):
                msg = "Możliwy Tanroth, " + str(ros_tanroth_count) + " rosów online"
                await channel.send(content=msg)
        else:
            if(ros_tanroth_count >= players_online_to_ping):
                msg = "Możliwy Tanroth, " + str(ros_tanroth_count) + " rosów online"
                await channel.send(content=msg)
        if(ros_teza_count >= players_online_to_ping):
            msg = "Możliwa Teza, " + str(ros_teza_count) + " rosów online"
            await channel.send(content=msg)
        if(ros_magua_count >= players_online_to_ping):
            msg = "Możliwy Magua, " + str(ros_magua_count) + " rosów online"
            await channel.send(content=msg)
        if(ros_przyzy_count >= players_online_to_ping):
            msg = "Możliwy Przyzy, " + str(ros_przyzy_count) + " rosów online"
            await channel.send(content=msg)
        #if(ros_lowka_count >= players_online_to_ping):
        #    msg = "Możliwa Łowka, " + str(ros_lowka_count) + " rosów online"
        #    await channel.send(content=msg)
        if(ros_zoons_count >= players_online_to_ping):
            msg = "Możliwy(a) Zoons/Łowka, " + str(ros_zoons_count) + " rosów online"
            await channel.send(content=msg)
        #if(ros_arcy_count >= players_online_to_ping):
        #    msg = "Możliwy Arcy, " + str(ros_arcy_count) + " rosów online"
        #    await channel.send(content=msg)
        if(ros_renio_count >= players_online_to_ping):
            msg = "Możliwy Renio, " + str(ros_renio_count) + " rosów online"
            await channel.send(content=msg)
        #if(ros_krolik_count >= players_online_to_ping):
        #    msg = "Możliwy Kr ólik, " + str(ros_krolik_count) + " rosów online"
        #    await channel.send(content=msg)
        #if(ros_orla_count >= players_online_to_ping):
        #    msg = "Możliwa Orla, " + str(ros_orla_count) + " rosów online"
        #    await channel.send(content=msg)
        if(west_tanroth_count >= players_online_to_ping):
            msg = "Możliwy Tanroth, " + str(west_tanroth_count) + " westów online"
            await channel.send(content=msg)
        if(west_teza_count >= players_online_to_ping):
            msg = "Możliwa Teza, " + str(west_teza_count) + " westów online"
            await channel.send(content=msg)
        if(west_magua_count >= players_online_to_ping):
            msg = "Możliwy Magua, " + str(west_magua_count) + " westów online"
            await channel.send(content=msg)
        if(west_przyzy_count >= players_online_to_ping):
            msg = "Możliwy Przyzy, " + str(west_przyzy_count) + " westów online"
            await channel.send(content=msg)
        #if(west_lowka_count >= players_online_to_ping):
        #    msg = "Możliwa Łowka, " + str(west_lowka_count) + " westów online"
        #    await channel.send(content=msg)
        if(west_zoons_count >= players_online_to_ping):
            msg = "Możliwy(a) Zoons/Łowka, " + str(west_zoons_count) + " westów online"
            await channel.send(content=msg)
        #if(west_arcy_count >= players_online_to_ping):
        #    msg = "Możliwy Arcy, " + str(west_arcy_count) + " westów online"
        #    await channel.send(content=msg)
        if(west_renio_count >= players_online_to_ping):
            msg = "Możliwy Renio, " + str(west_renio_count) + " westów online"
            await channel.send(content=msg)
        #if(west_krolik_count >= players_online_to_ping):
        #    msg = "Możliwy Królik, " + str(west_krolik_count) + " westów online"
        #    await channel.send(content=msg)

        if(int(date_today.minute) == 59):
            #Zapis do bazy
            hour_str = int(date_today.hour)
            if(len(str(hour_str)) == 1):
                hour_str = "0" + str(hour_str)

            path = 'database.db'
            con = sqlite3.connect(path)
            cur = con.cursor()
            for index, row in df_players_online_run_forever.iterrows():
                #print(row['c1'], row['c2'])
                data = (int(row['Account_id']), row['Nickname'], row['Char_id'], row['Minutes_online'], int(date_today.day), int(date_today.month), int(date_today.year), hour_str)
                sql = ''' INSERT INTO players_online(account_id, nickname, char_id, minutes_online, day, month, year, hour)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                cur.execute(sql, data)
                con.commit()
            #reset df
            df_players_online_run_forever = df_players_online_run_forever.iloc[0:0]
    except Exception as e:
        print(e)


async def select_players_online(nickname):
    current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    date_today = dt.strptime(current_daytime, "%Y-%m-%d %H:%M:%S")
    data = (nickname, int(date_today.year), int(date_today.month), int(date_today.day))
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    sql = ''' SELECT *
              FROM players_online
              WHERE nickname = ? AND year = ? AND month = ? AND day = ?
              ORDER BY year DESC, month DESC, day DESC, hour DESC'''
    res = cur.execute(sql, data)
    #print(res.fetchone()[0])
    return await df_players_online_operations(res.fetchall())


async def df_players_online_operations(data_list):
    df = pd.DataFrame (data_list, columns = ['account_id', 'nickname', 'char_id', 'minutes_online', 'day', 'month', 'year', 'hour'])
    #print(df)
    try:
        nickname = df['nickname'][0]
    except:
        return 0
    for i in range(1, 24):
        if(df.loc[df['hour'].astype(int) == i].any().all()):
            print(str(i) + " exists")
        else:
            hour_str = i
            if(len(str(i)) == 1):
                hour_str = "0" + str(i)
            df = df.append({'minutes_online':0, 'hour':hour_str, 'day':df['day'][0], 'month':df['month'][0], 'year':df['year'][0]}, ignore_index=True)
    df['date'] = df['year'].astype(str) + "-" + df['month'].astype(str) + "-" + df['day'].astype(str) + " " + df['hour'].astype(str)
    df['minutes_online']=df['minutes_online'].astype(int)
    #df.rename(columns={"minutes_online": "Minuty online"})
    #del df['year']
    #del df['month']
    #del df['day']
    #del df['hour']
    del df['account_id']
    del df['char_id']
    del df['nickname']


    del df['year']
    del df['month']
    del df['day']
    del df['hour']
    #print(df)
    df.date = pd.to_datetime(df['date'], format='%Y-%m-%d %H')
    df.set_index(['date'],inplace=True)
    #print(df)
    df.plot()
    plt.title("Wykres aktywności gracza " + nickname)
    #plt.xticks(range(1, 24))
    #print(df)
    plt.savefig('img/df_data/df_data.png')
    return 1
    #plt.show()


async def clan_members(ctx, klan):
    if(klan == "ros"):
        klan_url = "https://www.margonem.pl/guilds/view,Narwhals,1057"
    elif(klan == "west"):
        klan_url = "https://www.margonem.pl/guilds/view,Narwhals,1829"
    elif(klan == "bod"):
        klan_url = "https://www.margonem.pl/guilds/view,Narwhals,1834"
    odpowiedz = requests.get(klan_url)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    table = soup.find('table', class_='table--separators w-100')
    table = table.find('tbody')
    #print(table)

    df_clan_members_col = ({'Nick':["temp"], 'Lvl':[1]})
    df_clan_members = pd.DataFrame(df_clan_members_col)
    df_clan_members = df_clan_members.drop(df_clan_members.index[[0]])

    tanroth = ""
    teza = ""
    magua = ""
    przyzy = ""
    lowka = ""
    zoons = ""
    arcy = ""
    renio = ""
    krolik = ""
    orla = ""

    try:
        length = len(table.find_all('tr'))
    except:
        length = 0
    if(length>1):
        for i in table.find_all('tr'):
            data = i.find_all("td")
            nickname = data[1].a.string[10:-8]
            lvl = int(data[2].string[9:-7])
            if(lvl >= 285):
                tanroth = tanroth + '"' + nickname + '", '
            if(lvl >= 245 and lvl <= 271):
                teza = teza + '"' + nickname + '", '
            if(lvl >= 218 and lvl <= 244):
                magua = magua + '"' + nickname + '", '
            if(lvl >= 191 and lvl <= 217):
                przyzy = przyzy + '"' + nickname + '", '
            if(lvl >= 164 and lvl <= 190):
                lowka = lowka + '"' + nickname + '", '
            if(lvl >= 145 and lvl <= 167):
                zoons = zoons + '"' + nickname + '", '
            if(lvl >= 118 and lvl <= 144):
                arcy = arcy + '"' + nickname + '", '
            if(lvl >= 88 and lvl <= 114):
                renio = renio + '"' + nickname + '", '
            if(lvl >= 57 and lvl <= 83):
                krolik = krolik + '"' + nickname + '", '
            if(lvl >= 38 and lvl <= 64):
                orla = orla + '"' + nickname + '", '

        if(klan == "ros"):
            klan_url = "https://www.margonem.pl/guilds/view,Narwhals,1909"
            odpowiedz = requests.get(klan_url)
            soup = BeautifulSoup(odpowiedz.text, 'html.parser')
            table = soup.find('table', class_='table--separators w-100')
            table = table.find('tbody')
            #print(table)

            try:
                length = len(table.find_all('tr'))
            except:
                length = 0
            if(length>1):
                for i in table.find_all('tr'):
                    data = i.find_all("td")
                    nickname = data[1].a.string[10:-8]
                    lvl = int(data[2].string[9:-7])
                    if(lvl >= 285):
                        tanroth = tanroth + '"' + nickname + '", '
                    if(lvl >= 245 and lvl <= 271):
                        teza = teza + '"' + nickname + '", '
                    if(lvl >= 218 and lvl <= 244):
                        magua = magua + '"' + nickname + '", '
                    if(lvl >= 191 and lvl <= 217):
                        przyzy = przyzy + '"' + nickname + '", '
                    if(lvl >= 164 and lvl <= 190):
                        lowka = lowka + '"' + nickname + '", '
                    if(lvl >= 145 and lvl <= 167):
                        zoons = zoons + '"' + nickname + '", '
                    if(lvl >= 118 and lvl <= 144):
                        arcy = arcy + '"' + nickname + '", '
                    if(lvl >= 88 and lvl <= 114):
                        renio = renio + '"' + nickname + '", '
                    if(lvl >= 57 and lvl <= 83):
                        krolik = krolik + '"' + nickname + '", '
                    if(lvl >= 38 and lvl <= 64):
                        orla = orla + '"' + nickname + '", '


        tanroth = "[" + tanroth[:-2] + "]"
        teza = "[" + teza[:-2] + "]"
        magua = "[" + magua[:-2] + "]"
        przyzy = "[" + przyzy[:-2] + "]"
        lowka = "[" + lowka[:-2] + "]"
        zoons = "[" + zoons[:-2] + "]"
        arcy = "[" + arcy[:-2] + "]"
        renio = "[" + renio[:-2] + "]"
        krolik = "[" + krolik[:-2] + "]"
        orla = "[" + orla[:-2] + "]"

        print("Tanroth:\n" + tanroth + "\n")
        print("Teza:\n" + teza + "\n")
        print("Magua:\n" + magua + "\n")
        print("Przyzy:\n" + przyzy + "\n")
        print("Lowka:\n" + lowka + "\n")
        print("Zoons:\n" + zoons + "\n")
        print("Arcy:\n" + arcy + "\n")
        print("Renio:\n" + renio + "\n")
        print("Krolik:\n" + krolik + "\n")
        print("Orla:\n" + orla + "\n")

            #print(nickname, lvl, len(nickname), len(str(lvl)))



#async def quiz_admin():

async def quiz_UI(ctx):
    button_start = Button(
        style=ButtonStyle.SUCCESS,
        custom_id="start_quiz",
        label="Rozpocznij quiz"
    )
    button1 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="add_quiz",
        label="Dodaj zagadkę"
    )
    button2 = Button(
        style=ButtonStyle.DANGER,
        custom_id="delete_one",
        label="Usuń zagadkę"
    )
    button3 = Button(
        style=ButtonStyle.DANGER,
        custom_id="delete_all",
        label="Usuń wszystkie zagadki"
    )
    response = await get_data_in_db_quiz(int(ctx.guild_id))
    response_str = ""
    #print(response)
    #print(response[0][0])
    #print(len(response))
    if(len(response) == 0):
        await ctx.send("Obecnie nie ma ustawionej zagadki", components=[button1])
    else:
        for i in range(len(response)):
            response_str = response_str + "Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "\n"
        response_str = response_str[:-1]
        await ctx.send(response_str, components=[button_start, button1, button2, button3])

async def quiz_UI_started(ctx):
    global current_riddle, current_answer
    button1 = Button(
        style=ButtonStyle.DANGER,
        custom_id="stop_quiz",
        label="Zatrzymaj quiz"
    )
    response = await get_data_in_db_quiz(int(ctx.guild_id))
    response_str = ""
    #print(response)
    #print(response[0][0])
    #print(len(response))
    if(len(response) == 0):
        await ctx.send("Obecnie nie ma ustawionej zagadki", components=[button1])
    else:
        for i in range(len(response)):
            if(response[i][0] == current_riddle):
                response_str = response_str + "**Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "**\n"
            else:
                response_str = response_str + "Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "\n"
        response_str = response_str[:-1]
        await ctx.send(response_str, components=[button1])



async def quiz_sleep(ctx, response_riddles):
    global has_quiz_started, quiz_cd, current_riddle, current_answer, quiz_number, quiz_task
    #msg = store[ctx.author.user.id]
    #await msg.delete()
    #for i in range(len(respone_zagadki)):
    current_riddle = response_riddles[quiz_number][0]
    try:
        odp_temp = response_riddles[quiz_number][1].lower()
        odp_temp = unidecode(odp_temp)
        odp_temp = odp_temp.split("/")
        current_answer = odp_temp
    except:
        current_answer = response_riddles[quiz_number][1].lower()
    if(has_quiz_started == 0):
        #await ctx.send("Zakończono quiz", ephemeral=True)
        return
    #await ctx.send(current_riddle + " - " + current_answer, ephemeral=True)
    if(has_quiz_started == 1):
        msg = store_quiz_server[ctx.guild.id]
        await msg.delete()

        await quiz_UI_started(ctx)

        store_quiz_server[ctx.guild.id] = ctx

    print('Start')
    try:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
        await channel_quiz_start.send(content="Pojawiła się nowa zagadka, czas na odpowiedź: 1min")
    except:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
        await channel_quiz_start.send(content="Pojawiła się nowa zagadka, czas na odpowiedź: 1min")

    try:
        await asyncio.sleep(quiz_cd)
    except asyncio.CancelledError:
        print('Stop')
        try:
            channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
            await channel_quiz_start.send(content="Quiz został ręcznie zakończony w trakcie trwania")
        except:
            channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
            await channel_quiz_start.send(content="Quiz został ręcznie zakończony w trakcie trwania")

        has_quiz_started = 0
        msg = store_quiz_server[ctx.guild.id]
        await msg.delete()
        await ctx.send(str(ctx.author.user.username) + " zakończył(a) ręcznie quiz")
        if(has_quiz_started == 1):
            await quiz_UI_started(ctx)
        else:
            await quiz_UI(ctx)
        store_quiz_server[ctx.guild.id] = ctx
    else:
        print('Koniec')
        quiz_number = quiz_number + 1
        if(quiz_number <= len(response_riddles)-1):
            await reset_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), "won")
            quiz_task = asyncio.create_task(quiz_sleep(ctx, response_riddles))
        else:
            has_quiz_started = 0
            msg = store_quiz_server[ctx.guild.id]
            await msg.delete()
            await ctx.send("Zakończono quiz")

            try:
                channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
                await channel_quiz_start.send(content="Quiz zakończył się")
            except:
                channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
                await channel_quiz_start.send(content="Quiz zakończył się")

            quiz_result = await get_data_in_db_quiz_results(int(ctx.guild_id))
            #print(quiz_result)
            #print(len(quiz_result))
            quiz_result_str = ""
            #print(response)
            #print(response[0][0])
            #print(len(response))
            if(len(quiz_result) == 0):
                #print("Nikt...")
                await ctx.send("Nikt nie brał udział w zagadkach")
            else:
                #print("CMON")
                for i in range(len(quiz_result)):
                    #print(i)
                    #print(quiz_result)
                    #print(quiz_result[i][2])
                    quiz_result_str = quiz_result_str + str(quiz_result[i][2]) + "#" + str(quiz_result[i][3]) + " - Punkty: " + str(quiz_result[i][5]) + ", Próby: " + str(quiz_result[i][4]) + "\n"
                quiz_result_str = quiz_result_str[:-1]
                #print("quiz_result_str ->" + quiz_result_str + "<-")
                await ctx.send(quiz_result_str)

            if(has_quiz_started == 1):
                await quiz_UI_started(ctx)
            else:
                await quiz_UI(ctx)
            store_quiz_server[ctx.guild.id] = ctx


async def save_logs(guild_id, user_id, nickname, hash_code, command):
    current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    #async with aiofiles.open('logs.txt', mode='w') as f:
    #    await f.write(str(guild_id) + " | " + str(user_id) + "(" + nickname + "#" + str(hash_code) + ") | " + command)
    f = open("logs.txt", "a")
    f.write(str(guild_id) + " | " + str(user_id) + "(" + nickname + "#" + str(hash_code) + ") | " + command + " | " + current_daytime + "\n")
    f.close()


@bot.event
async def on_start():
    global channel_quiz
    print('Online')
    #print(bot._presence)
    try:
        channel_quiz = await interactions.get(bot, interactions.Channel, object_id=1083376240783785985)
    except:
        channel_quiz = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
    my_task.start()


@bot.command(
    name="say_something",
    description="say something!",
    scope= [
        dc_discord_bot_testy
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="text",
            description="What you want to say",
            required=True,
        ),
    ],
)
async def say_something(ctx: interactions.CommandContext, text: str):
    #await ctx.send(text)
    print(ctx.author.roles)
    if(1084883485736583248 in ctx.author.roles):
        print("Yess")

'''
@bot.command(
    name="count",
    description="Oblicza statystyki bić zadanego potwora",
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="mob",
            description="Link do moba na lootlogu",
            required=True,
        ),
    ],
)
async def count(ctx: interactions.CommandContext, mob: str):
    global bicia, uni, hera, legi
    #urlOriginal = arg
    if str(mob).find("https://grooove.pl/")>=0:
        await get_data(mob, mob)
        embed=interactions.Embed(title="Statystyki:", color=1)
        embed.add_field(name="Bicia:", value=bicia, inline=False)
        embed.add_field(name="Unikaty:", value=uni, inline=False)
        embed.add_field(name="Heroiki:", value=hera, inline=False)
        embed.add_field(name="Legendy:", value=legi, inline=False)
        await ctx.send(embeds=embed)
        bicia = 0
        uni = 0
        hera = 0
        legi = 0 
    else:
        embed=interactions.Embed(title="Niepoprawny adres!", description = "Upewnij sie ze podany adres prowadzi do podstrony grooove.pl", color=200)
        await ctx.send(embeds=embed)

@bot.command(
    name="wakacje2022",
    description="Oblicza statystyki bić potworów z eventu wakacje 2022",
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def wakacje2022(ctx: interactions.CommandContext, klan: str):
    embed=interactions.Embed(title="Statystyki:")
    link = await setLink(klan)
    if(link == "BRAK"):
        await ctx.send("Niepoprawna nazwa klanu")
    else:
        await ctx.send("Zbieram dane...")
        #35
        await getMobData(embed, link, "Laleczka Kogula", "35")
        #160
        await getMobData(embed, link, "Soucouya", "160")
        #210
        await getMobData(embed, link, "Papa Legba", "210")
        await ctx.send(embeds=embed)

@bot.command(
    name="halloween2022",
    description="Oblicza statystyki bić potworów z eventu halloween 2022",
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def halloween2022(ctx: interactions.CommandContext, klan: str):
    embed=interactions.Embed(title="Statystyki Halloween 2022:")
    link = await setLink(klan)
    if(link == "BRAK"):
        await ctx.send("Niepoprawna nazwa klanu")
    else:
        await ctx.send("Zbieram dane...")
        #80
        await getMobData(embed, link, "Cristian Flores", "80")
        #105
        await getMobData(embed, link, "Antonella Lozano", "105")
        #195
        await getMobData(embed, link, "Emilio de la Rosa", "195")
        #295
        await getMobData(embed, link, "Olvidada Silva", "295")
        await ctx.send(embeds=embed)

@bot.command(
    name="gwiazdka2022",
    description="Oblicza statystyki bić potworów z eventu gwiazdka 2022",
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def gwiazdka2022(ctx: interactions.CommandContext, klan: str):
    embed=interactions.Embed(title="Statystyki Gwiazdka 2022:")
    link = await setLink(klan)
    if(link == "BRAK"):
        await ctx.send("Niepoprawna nazwa klanu")
    else:
        await ctx.send("Zbieram dane...")
        await getMobData(embed, link, "Pan Cane", "55")
        await getMobData(embed, link, "Pianka", "120")
        await getMobData(embed, link, "Słodka Ewa", "140")
        await getMobData(embed, link, "Gleter", "225")
        await getMobData(embed, link, "Niesłodki Adam", "270")
        await ctx.send(embeds=embed)
'''

@bot.command(
    name="skarpetka",
    description="Informacje o Skarpecie",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def skarpetka(ctx: interactions.CommandContext):
    #embed=interactions.Embed(title="Skarpeta, znany tez jako Skarpeciasty Kox", description = "Pierwszy i najlepszy tester discordowych bocikow\nDzentelmen, filantrop, czlowiek kultury\nKoxem jest ogolnie")
    #await ctx.send(embeds=embed)
    await command_send(ctx, content = "Skarpeta, znany też jako Skarpeciasty Kox, pierwszy i najlepszy tester discordowych bocików, najlepszy gracz Tarhuny i całego Margonem, dżentelmen, filantrop, człowiek kultury, dobrodziej, wspomożyciel, koxem jest ogolnie. Mówię to ja, Neeyo podpisany, z własnej i nieprzymuszonej woli.", files=interactions.File("img/Skieta/terror_skiety.png"))


@bot.command(
    name="top",
    description="Oblicza ranking graczy z najwieksza iloscia RN",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.INTEGER,
            name="liczba",
            description="Liczba osob do wyswietlenia",
            required=True,
        ),
    ],
)
async def top(ctx: interactions.CommandContext, liczba: int):
    await ctx.send("Zbieram dane...")
    await resetWyniki()
    await get_data_darro()
    if(int(liczba) > len(wynikiNick)):
        embed=interactions.Embed(title="Blad, za duzy zakres")
        await ctx.send(embeds=embed)
        return
    embed=interactions.Embed(title="TOP "+str(liczba)+" posiadanych RN na serwerze Narwhals: ", url="https://narwhals.darro.eu/?t=currency")
    for x in range(int(liczba)):
        embed.add_field(name=wynikiRank[x] + ". " + wynikiNick[x] + "   id: " + wynikiId[x] + "   " + str(wynikiProfil[x]), value="RN: " + wynikiRN[x], inline=False)
    await ctx.send(embeds=embed)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "top")

@bot.command(
    name="find",
    description="Wyswietla ranking RN gracza o podanym ID konta",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="liczba",
            description="ID konta",
            required=True,
        ),
    ],
)
async def find(ctx: interactions.CommandContext, liczba: str):
    await ctx.send("Zbieram dane...")
    await resetWyniki()
    await get_data_darro()
    if(liczba in wynikiId):
        embed=interactions.Embed(title="Znaleziono gracza")
        embed.add_field(name=wynikiRank[wynikiId.index(liczba)] + ". " + wynikiNick[wynikiId.index(liczba)] + "   id: " + wynikiId[wynikiId.index(liczba)] + "   " + str(wynikiProfil[wynikiId.index(liczba)]), value="RN: " + wynikiRN[wynikiId.index(liczba)], inline=False)
        await ctx.send(embeds=embed)
    else:
        embed=interactions.Embed(title="Blad, brak danych")
        await ctx.send(embeds=embed)
        await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "find")
'''
@bot.command(
    name="nieaktywnosc",
    description="Podaje  najdluzej nieaktywne osoby na danym swiecie",
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="swiat",
            description="Swiat z którego zostaną pobrane dane",
            required=True,
        ),
    ],
)
async def nieaktywnosc(ctx: interactions.CommandContext, swiat: str):
    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    #embed=interactions.Embed(title="Nieaktywnosci(wlasnie pobrane):")
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page=1"

    await ctx.send("Zbieram dane...")
    if(await check_data_in_db_absency_last(swiat, ctx)):
        await get_data_absency(ctx, df, swiat, link)
        #await ctx.send(embeds=embed)
        #df = df.iloc[0:0]
        del df
    #for index, row in df.iterrows():
     #   print(row['Nickname'], row['Lvl'], row['Last online'])
    #await ctx.interaction.response.defer(ephemeral= True)
    #await ctx.interaction.followup.send(embeds=embed, ephemeral = True)
    #await ctx.send(embeds=embed)
    ############################
    #await check_data_in_db_absency_last(swiat)
'''

@bot.command(
    name="nieaktywnosc",
    description="Podaje najdluzej nieaktywne osoby na danym swiecie, aktualizacja raz na 6 godzin",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def nieaktywnosc(ctx: interactions.CommandContext):
    if(int(ctx.guild_id) == dc_discord_bot_testy or int(ctx.guild_id) == dc_bod):
        button1 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="nieaktywnosc1",
            label="Narwhals"
        )
        button2 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="nieaktywnosc2",
            label="Stoners"
        )
        await ctx.send("Wybierz swiat", components=[button1, button2])
    elif(ctx.guild_id == dc_sm):
        button2 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="nieaktywnosc2",
            label="Stoners"
        )
        await ctx.send("Wybierz swiat", components=[button2])
    else:
        await ctx.send("Błąd, nie udało sie pobrac id serwera")
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc")

@bot.component("nieaktywnosc1")
async def button_response(ctx):
    swiat = "Narwhals"

    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
    page = 1

    await ctx.defer()
    if(await check_data_in_db_absency_last(swiat, ctx)):
        await get_data_absency(ctx, df, swiat, link, page)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc - Narwhals")

@bot.component("nieaktywnosc2")
async def button_response(ctx):
    swiat = "Stoners"
    
    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
    page = 1

    await ctx.defer()
    if(await check_data_in_db_absency_last(swiat, ctx)):
        await get_data_absency(ctx, df, swiat, link, page)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc - Stoners")

'''
@bot.command(
    name="embed",
    description="Test",
)
async def embed(ctx: interactions.CommandContext):
    embed = interactions.Embed(
    title="your title",
    description="your description")
    await ctx.send(embeds = embed)

@bot.command(
    name = "przycisk_test",
    description="Komenda testujaca przyciski"
)
async def przycisk_test(ctx: interactions.CommandContext):
    button = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="primary",
        label="Przycisk test"
    )
    await ctx.send("Przykladowy przycisk", components=button)

@bot.component("primary")
async def button_response(ctx):
    button2 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="primary2",
        label="Chwal Neeya"
    )
    button3 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="primary3",
        label="Hejtuj Neeya"
    )
    await ctx.send("Przykladowy przycisk", components=[button2, button3])

@bot.component("primary2")
async def button_response(ctx):
    await ctx.send("Chwała Neeyom")

@bot.component("primary3")
async def button_response(ctx):
    await ctx.send("Tak nie wolno, chwała Neeyom")
'''



@bot.command(
    name="stworz_baze",
    description="Tworzy baze danych, funkcja tymczasowa do testów",
    scope= [
        dc_discord_bot_testy
    ],
)
async def stworz_baze(ctx: interactions.CommandContext):
    await ctx.send("Tworzę baze danych...")
    try:
        await create_database()
        await ctx.send("Baza danych została utworzona")
    except:
        await ctx.send("Baza danych już istnieje")


@bot.command(
    name="tanroth",
    description="Losuje drop z Tanrotha",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def tanroth(ctx: interactions.CommandContext):
    print(int(ctx.author.user.id))
    response = await check_data_in_db_tanroth_last_update(int(ctx.author.user.id))
    if( response == 1):
        await command_send(ctx, files=interactions.File("img/Tanroth/" + await random_tanroth_item(int(ctx.guild_id), int(ctx.author.user.id)) + ".png"))
    else:
        if(isinstance(response, float)):
            time_left = 600 - response
            if(time_left > 60):
                time_left = int(time_left/60)
                if(time_left >= 5):
                    embed=interactions.Embed(title="Od ostatniego losowania nie minelo 10 minut, zaczekaj jeszcze okolo " + str(time_left) + " minut")
                elif(time_left >= 2):
                    embed=interactions.Embed(title="Od ostatniego losowania nie minelo 10 minut, zaczekaj jeszcze okolo " + str(time_left) + " minuty")
                else:
                    embed=interactions.Embed(title="Od ostatniego losowania nie minelo 10 minut, zaczekaj jeszcze okolo " + str(time_left) + " minute")
            else:
                embed=interactions.Embed(title="Od ostatniego losowania nie minelo 10 minut, zaczekaj jeszcze " + str(int(time_left)) + " sekund")
            await ctx.send(embeds=embed)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "tanroth")


@bot.command(
    name="online",
    description="Gracze online na wybranym świecie",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="swiat",
            description="Swiat z którego zostaną pobrane dane",
            required=True,
        ),
    ],
)
async def online(ctx: interactions.CommandContext, swiat: str):
    #embed=interactions.Embed(title="Gracze online na swiecie " + swiat)
    result = await players_online(ctx, swiat)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online")
    #await ctx.send("**Gracze online na swiecie " + swiat + "**\n" + result)

@bot.command(
    name="online_przycisk",
    description="Gracze online na wybranym swiecie ale z przyciskiem",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def online_przycisk(ctx: interactions.CommandContext):
    button1 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="online1",
        label="Narwhals"
    )
    button2 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="online2",
        label="Stoners"
    )
    button3 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="online3",
        label="Tarhuna"
    )
    button4 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="online4",
        label="Fobos"
    )
    button5 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="online5",
        label="Unia"
    )
    await ctx.send("Wybierz swiat", components=[button1, button2, button3, button4, button5])
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk")

@bot.component("online1")
async def button_response(ctx):
    swiat = "Narwhals"
    await players_online(ctx, swiat)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Narwhals")

@bot.component("online2")
async def button_response(ctx):
    swiat = "Stoners"
    await players_online(ctx, swiat)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Stoners")

@bot.component("online3")
async def button_response(ctx):
    swiat = "Tarhuna"
    await players_online(ctx, swiat)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Tarhuna")

@bot.component("online4")
async def button_response(ctx):
    swiat = "Fobos"
    await players_online(ctx, swiat)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Fobos")

@bot.component("online5")
async def button_response(ctx):
    swiat = "Unia"
    await players_online(ctx, swiat)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Unia")

@bot.command(
    name="rejestracja",
    description="Rejestracja konta w Margonem do systemu powiadomień",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def rejestracja(ctx: interactions.CommandContext):
    #await ctx.send("Test..")
    #print(ctx.guild_id)
    modal = Modal(
        custom_id = "register_modal",
        title = "Podaj id konta w Margonem",
        components = [
            TextInput(
                style = TextStyleType.SHORT,
                custom_id = "register_text_input",
                label = "ID konta",
                placeholder = "np. 1234567",
                min_length = 7,
                max_length = 7,
                required = True
            )
        ]
    )
    await ctx.popup(modal)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "rejestracja")

@bot.modal("register_modal")
async def modal_response(ctx, response: str):
    try:
        int(response)
    except:
        await ctx.send("Niepoprawne ID", ephemeral=True)
        return
    register_response = requests.get("https://www.margonem.pl/profile/view," + response)
    register_soup = BeautifulSoup(register_response.text, 'html.parser')
    nickname = register_soup.find('div', class_='brown-box profile-header mb-4')
    nickname = nickname.find('h2')
    nickname = nickname.find('span')
    nickname = nickname.string[17:-12]
    print(nickname)
    await update_characters_in_game_temp(ctx.author.user.id, nickname)
    button1 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="register_button_1",
        label="Tak, zapisz"
    )
    button2 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="register_button_2",
        label="Nie"
    )
    await ctx.send("Czy twój nick to " + nickname + "?", components=[button1, button2], ephemeral=True)
    store[ctx.author.user.id] = ctx

@bot.component("register_button_1")
async def button_response1(ctx):
    msg = store[ctx.author.user.id]
    await msg.delete()
    result = await check_data_in_characters_in_game(ctx.guild_id, ctx.author.user.id, await select_characters_in_game_temp(ctx.author.user.id))
    if(result == 1):
        await ctx.send("Zrobione", ephemeral=True)
    else:
        button3 = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="register_button_3",
        label="Tak, zaktualizuj"
        )
        button4 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="register_button_4",
            label="Nie, zostaw obecne"
        )
        await ctx.send("Do konta na Discordzie przypisano już konto w grze o nicku " + str(result)+ ". Zaktualizowac dane?", components=[button3, button4], ephemeral=True)
    store[ctx.author.user.id] = ctx

@bot.component("register_button_2")
async def button_response2(ctx):
    msg = store[ctx.author.user.id]
    await msg.delete()
    modal = Modal(
        custom_id = "register_modal",
        title = "Podaj id konta w Margonem",
        components = [
            TextInput(
                style = TextStyleType.SHORT,
                custom_id = "register_text_input",
                label = "ID konta",
                placeholder = "np. 1234567",
                min_length = 7,
                max_length = 7,
                required = True
            )
        ]
    )
    await ctx.popup(modal)
    store[ctx.author.user.id] = ctx

@bot.component("register_button_3")
async def button_response3(ctx):
    msg = store[ctx.author.user.id]
    await msg.delete()
    await update_characters_in_game(ctx.guild_id, ctx.author.user.id, str(await select_characters_in_game_temp(ctx.author.user.id)))
    await ctx.send("Dane zaktualizowane", ephemeral=True)

@bot.component("register_button_4")
async def button_response3(ctx):
    msg = store[ctx.author.user.id]
    await msg.delete()
    await ctx.send("Zmiany odrzucone", ephemeral=True)


@bot.command(
    name="moje_dropy",
    description="Wyswietla licznik dropów z serwerowego Tanrotha",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def moje_dropy(ctx: interactions.CommandContext):
    try: 
        result = await select_all_tanroth_drops(ctx.guild_id, ctx.author.user.id)
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.author.user.username + "#" + ctx.author.user.discriminator, value="Unikaty: " + str(result[0]) + "\n" + "Heroiki: " + str(result[1]) + "\n" + "Legendy: " + str(result[2]), inline=False)
        await ctx.send(embeds=embed)
    except:
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.author.user.username + "#" + ctx.author.user.discriminator, value="Unikaty: " + str(0) + "\n" + "Heroiki: " + str(0) + "\n" + "Legendy: " + str(0), inline=False)
        await ctx.send(embeds=embed)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "moje_dropy")


@bot.user_command(
    name="Dropy gracza",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def dropy_gracza(ctx: interactions.CommandContext):
    try: 
        result = await select_all_tanroth_drops(ctx.guild_id, ctx.target.user.id)
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.target.user.username + "#" + ctx.target.user.discriminator, value="Unikaty: " + str(result[0]) + "\n" + "Heroiki: " + str(result[1]) + "\n" + "Legendy: " + str(result[2]), inline=False)
        await ctx.send(embeds=embed)
    except:
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.target.user.username + "#" + ctx.target.user.discriminator, value="Unikaty: " + str(0) + "\n" + "Heroiki: " + str(0) + "\n" + "Legendy: " + str(0), inline=False)
        await ctx.send(embeds=embed)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "Dropy gracza")


@create_task(IntervalTrigger(60))
async def my_task():
    await players_online_run_forever("Narwhals")

@create_task(IntervalTrigger(3))
async def zagadka_delay():
    zagadka_delay.stop()


@bot.command(
    name="online_wykres",
    description="Wykres graczy online z dzisiaj",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="nickname",
            description="Nazwa gracza",
            required=True,
        ),
    ],
)
async def online_wykres(ctx: interactions.CommandContext, nickname: str):
    if(await select_players_online(nickname)):
        await command_send(ctx, files=interactions.File("img/df_data/df_data.png"))
    else:
        await ctx.send("Brak danych gracza " + nickname)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_wykres")


@bot.command(
    name="timery",
    description="Timery herosów i tytanów na lootlogu",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def timery(ctx: interactions.CommandContext):
    embed=interactions.Embed(title="Timery herosów i tytanów")
    await get_timer_alt(embed)
    await ctx.send(embeds=embed)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery")


@bot.command(
    name="timery_alt",
    description="Timery herosów i tytanów na lootlogu",
    scope= [
        dc_discord_bot_testy
    ],
)
async def timery_alt(ctx: interactions.CommandContext):
    embed=interactions.Embed(title="Timery herosów i tytanów")
    await get_timer_alt(embed)
    await ctx.send(embeds=embed)
    await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery_alt")


@bot.command(
    name="dodaj_timer",
    description="Dodaje timer na lootlog",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="mob",
            description="Nazwa potwora",
            required=True,
            autocomplete=True,
        ),
    ],
)
async def dodaj_timer(ctx: interactions.CommandContext, mob: str):
    if(await add_timer(ctx, mob) == 1):
        await ctx.send("Dodano timer potwora " + mob)
    elif(await add_timer(ctx, mob) == 2):
        await ctx.send("Brak uprawnień do użycia komendy, tymczasowo ograniczone")
    elif(await add_timer(ctx, mob) == 3):
        await ctx.send("Wystąpił błąd")
    #await save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery")

@dodaj_timer.autocomplete("mob")
async def dodaj_timer_autocomplete(ctx: interactions.CommandContext, user_input: str = ""):
    items = ["Domina Ecclesiae", "Mietek Żul", "Mroczny Patryk", "Karmazynowy Mściciel", "Złodziej", "Zły Przewodnik", "Piekielny Kościej", "Opętany Paladyn", 
             "Kochanka Nocy", "Ksiaze Kasim", "Baca bez łowiec", "Lichwiarz Grauhaz", "Obłąkany łowca orków", "Czarująca Atalia", "Święty Braciszek", "Viviana Nandin", 
             "Mulher Ma", "Demonis Pan Nicości", "Vapor Veneno", "Dęborożec", "Tepeyollotl", "Negthotep Czarny Kapłan", "Młody smok"]
    choices = [
        interactions.Choice(name=item, value=item) for item in items if user_input in item 
    ] 
    await ctx.populate(choices)


@bot.command(
    name="czlonkowie_klanow",
    description="Wypisuje w konsoli czlonkow kazdego z klanów na dany przedzial",
    scope= [
        dc_discord_bot_testy
    ],
    options = [
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def czlonkowie_klanow(ctx: interactions.CommandContext, klan: str):
    await clan_members(ctx, klan)


@bot.command(
    name="test_ping",
    description="Testowy ping",
    scope= [
        dc_discord_bot_testy
    ],
)
async def test_ping(ctx: interactions.CommandContext):
    channel = await interactions.get(bot, interactions.Channel, object_id=987410864946679861)
    msg = "Możliwy Tanroth, " + str(1) + " rosów online"
    await channel.send(content=msg)


@bot.command(
    name="zagadka_admin",
    description="Panel admina do tworzenia zagadek",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def zagadka_admin(ctx: interactions.CommandContext):
    global has_quiz_started
    if(int(ctx.author.user.id) not in {349851438228439040, 372381114809188362, 546751756323913754}):
        await ctx.send("Brak uprawnień", ephemeral=True)
        return
    if(int(ctx.channel.id) not in {1085193552864235591, 1083376240783785985}):
        await ctx.send("Użyj komendy w przeznaczonym do tego kanale", ephemeral=True)
        return
    try:
        msg = store_quiz_server[ctx.guild.id]
        await msg.delete()
    except:
        print("Whatever")
    if(has_quiz_started == 1):
        await quiz_UI_started(ctx)
    else:
        await quiz_UI(ctx)
    store_quiz_server[ctx.guild.id] = ctx

@bot.component("add_quiz")
async def button_response(ctx):
    #await ctx.send("Dodanie zagadki", ephemeral=True)

    modal = Modal(
        custom_id = "add_quiz_modal",
        title = "Panel dodania nowej zagadki",
        components = [
            TextInput(
                style = TextStyleType.PARAGRAPH,
                custom_id = "add_quiz_modal_zagadka",
                label = "Zagadka",
                placeholder = "Tu wpisz zagadkę",
                required = True
            ),
            TextInput(
                style = TextStyleType.SHORT,
                custom_id = "add_quiz_modal_odpowiedz",
                label = "Prawidłowa odpowiedź",
                placeholder = "Tu wpisz odpowiedź",
                required = True
            )
        ]
    )
    await ctx.popup(modal)

@bot.modal("add_quiz_modal")
async def modal_response(ctx, zagadka: str, odpowiedz: str):
    global has_quiz_started
    msg = store_quiz_server[ctx.guild.id]
    await msg.delete()
    #await ctx.send(zagadka, ephemeral=True)
    #await ctx.send(odpowiedz, ephemeral=True)
    try:
        await add_data_in_db_quiz(int(ctx.guild_id), zagadka, odpowiedz)
        await ctx.send(str(ctx.author.user.username) + " pomyślnie dodał(a) zagadkę: " + zagadka)
    except:
        await ctx.send(str(ctx.author.user.username) + " nie udało sie dodać zagadki: " + zagadka)

    if(has_quiz_started == 1):
        await quiz_UI_started(ctx)
    else:
        await quiz_UI(ctx)
    store_quiz_server[ctx.guild.id] = ctx


@bot.component("delete_one")
async def button_response(ctx):
    global has_quiz_started
    #respone_zagadki = await get_data_in_db_quiz(int(ctx.guild_id))
    #for i in range(len(response)):
    #    response_str = response_str + "Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "\n"
    msg = store_quiz_server[ctx.guild.id]
    await msg.delete()
    respone_zagadki = await get_data_in_db_quiz(int(ctx.guild_id))
    if(len(respone_zagadki) != 0):
        modal = Modal(
            custom_id = "delete_zagadka_modal",
            title = "Panel usuwania wybranej zagadki",
            components = [
                TextInput(
                    style = TextStyleType.SHORT,
                    custom_id = "delete_one_modal_odpowiedz",
                    label = "Numer zagadki którą chcesz usunąć",
                    placeholder = "Tu wpisz numer",
                    required = True
                )
            ]
        )
        await ctx.popup(modal)
    else:
        await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    if(has_quiz_started == 1):
        await quiz_UI_started(ctx)
    else:
        await quiz_UI(ctx)
    store_quiz_server[ctx.guild.id] = ctx


@bot.modal("delete_zagadka_modal")
async def modal_response(ctx, numer: str):
    global has_quiz_started
    msg = store_quiz_server[ctx.guild.id]
    await msg.delete()

    respone_zagadki = await get_data_in_db_quiz(int(ctx.guild_id))
    zagadka = respone_zagadki[int(numer)-1][0]
    odpowiedz = respone_zagadki[int(numer)-1][1]
    response = await delete_data_in_db_quiz(int(ctx.guild_id), zagadka, odpowiedz)
    if(response == 1):
         await ctx.send(str(ctx.author.user.username) + " Upomyślnie usunął(ęła) zagadkę: " + zagadka)
    elif(response == 2):
         await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    
    if(has_quiz_started == 1):
        await quiz_UI_started(ctx)
    else:
        await quiz_UI(ctx)
    store_quiz_server[ctx.guild.id] = ctx


@bot.component("delete_all")
async def button_response(ctx):
    global has_quiz_started
    msg = store_quiz_server[ctx.guild.id]
    await msg.delete()

    response = await delete_all_data_in_db_quiz(int(ctx.guild_id))
    if(response == 1):
         await ctx.send(str(ctx.author.user.username) + " pomyślnie usunął(ęła) wszystkie zagadki")
    elif(response == 2):
         await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    
    if(has_quiz_started == 1):
        await quiz_UI_started(ctx)
    else:
        await quiz_UI(ctx)
    store_quiz_server[ctx.guild.id] = ctx


@bot.component("start_quiz")
async def button_response(ctx):
    global has_quiz_started, quiz_cd, current_riddle, current_answer, quiz_number, quiz_task, riddles
    quiz_number = 0
    has_quiz_started = 1
    riddles = await get_data_in_db_quiz(int(ctx.guild_id))

    await reset_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), "all")

    response_riddles = await get_data_in_db_quiz(int(ctx.guild_id))
    await ctx.send(str(ctx.author.user.username) + " rozpoczął(ęła) quiz")

    try:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
        await channel_quiz_start.send(content="Quiz rozpoczął się")
    except:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
        await channel_quiz_start.send(content="Quiz rozpoczął się")
    #quiz_task = asyncio.create_task(quiz_sleep(ctx, response_riddles)) #works

    if(has_quiz_started == 0):
        return
    if(has_quiz_started == 1):
        msg = store_quiz_server[ctx.guild.id]
        await msg.delete()
        await quiz_UI_started(ctx)
        store_quiz_server[ctx.guild.id] = ctx

    #zagadka_delay.start()

    #msg = store[ctx.author.user.id]
    #await msg.delete()


@bot.component("stop_quiz")
async def button_response(ctx):
    global has_quiz_started, quiz_task
    #msg = store[ctx.author.user.id]
    #await msg.delete()

    #quiz_task.cancel() #works

    has_quiz_started = 0
    msg = store_quiz_server[ctx.guild.id]
    await msg.delete()
    await ctx.send("Zakończono quiz")

    try:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
        await channel_quiz_start.send(content="Quiz zakończył się")
    except:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
        await channel_quiz_start.send(content="Quiz zakończył się")

    quiz_result = await get_data_in_db_quiz_results(int(ctx.guild_id))
    quiz_result_str = ""
    if(len(quiz_result) == 0):
        await ctx.send("Nikt nie brał udział w zagadkach")
    else:
        for i in range(len(quiz_result)):
            quiz_result_str = quiz_result_str + str(quiz_result[i][2]) + "#" + str(quiz_result[i][3]) + " - Punkty: " + str(quiz_result[i][5]) + "\n"
        quiz_result_str = quiz_result_str[:-1]
        await ctx.send(quiz_result_str)

    if(has_quiz_started == 1):
        await quiz_UI_started(ctx)
    else:
        await quiz_UI(ctx)
    store_quiz_server[ctx.guild.id] = ctx

    #msg = store[ctx.author.user.id]
    #await msg.delete()



@bot.command(
    name="zagadka",
    description="Zagadki",
    scope= [
        dc_discord_bot_testy,
        dc_bod
    ],
)
async def zagadka(ctx: interactions.CommandContext):
    global has_quiz_started, current_answer, riddles, channel_quiz
    if(1084883485736583248 in ctx.author.roles or 1084925145195491410 in ctx.author.roles):
        if(has_quiz_started == 1):
            '''
            has_won = await check_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), ctx.author.user.username, int(ctx.author.user.discriminator))
            #print(has_won)
            if(has_won == 0):
                modal = Modal(
                    custom_id = "answer_quiz_modal",
                    title = "Formularz odpowiedzi na zagadkę",
                    components = [
                        TextInput(
                            style = TextStyleType.SHORT,
                            custom_id = "answer_quiz_modal_odpowiedz",
                            label = current_riddle,
                            placeholder = "Miejsce na odpowiedź",
                            required = True
                        ),
                    ]
                )
                await ctx.popup(modal)
            else:
                await ctx.send("Odgadłeś już hasło, zaczekaj na nową zagadkę", ephemeral=True)'''
            
            whatever_dude = await check_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), ctx.author.user.username, int(ctx.author.user.discriminator))
            user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            #print(user_data)
            user_data = user_data[0]
            #tried = int(user_data[4])
            wins = int(user_data[6])
            losts = int(user_data[7])

            if(wins + losts <= len(riddles)-1):
                modal = Modal(
                    custom_id = "answer_quiz_modal",
                    title = "Formularz odpowiedzi na zagadkę",
                    components = [
                        TextInput(
                            style = TextStyleType.SHORT,
                            custom_id = "answer_quiz_modal_odpowiedz",
                            label = riddles[wins + losts][0],
                            placeholder = "Miejsce na odpowiedź",
                            required = True
                        ),
                    ]
                )
                await ctx.popup(modal)
            else:
                await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
                quiz_result = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
                quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
                await channel_quiz.send(content=quiz_result_str)


        else:
            await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)
        #store[ctx.author.user.id] = ctx
    else:
        await ctx.send("Nie masz uprawnień do wzięcia udziału w zagadce", ephemeral=True)

@bot.modal("answer_quiz_modal")
async def modal_response(ctx, odp: str):
    global current_answer, channel_quiz, riddles
    '''
    try:
        odp_temp = odp.lower()
        odp_temp = unidecode(odp_temp)
    except:
        odp_temp = odp.lower()
    user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
    user_data = user_data[0]
    await channel_quiz.send(content=str(ctx.author.user.username) + " odpowiedział(a) na obecną zagadkę: " + odp)
    if(odp_temp in current_answer):
        await ctx.send("Prawidłowa odpowiedź", ephemeral=True)
        await channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
        #print(user_data)
        await update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), int(user_data[4]) + 1, int(user_data[5]) + 1, int(user_data[6]) + 1, int(user_data[7]))
    else:
        button_restart = Button(
            style=ButtonStyle.DANGER,
            custom_id="restart_quiz",
            label="Spróbuj ponownie"
        )
        await ctx.send("Niepoprawna odpowiedź", components=[button_restart], ephemeral=True)
        await update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), int(user_data[4]) + 1, int(user_data[5]), int(user_data[6]), int(user_data[6]) + 1)

        store_quiz_user[ctx.author.user.id] = ctx
        #await ctx.send("Niepoprawna odpowiedź", ephemeral=True)
    '''

    user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
    user_data = user_data[0]
    tried = int(user_data[4])
    points = int(user_data[5])
    wins = int(user_data[6])
    losts = int(user_data[7])
    try:
        odp_temp = odp.lower()
        odp_temp = unidecode(odp_temp)
    except:
        odp_temp = odp.lower()
    
    try:
        answer = riddles[wins + losts][1].lower()
        answer = unidecode(answer)
        answer = answer.split("/")
    except:
        answer = riddles[wins + losts][1].lower()
    await channel_quiz.send(content=str(ctx.author.user.username) + " odpowiedział(a): " + odp)
    tried = tried + 1
    if(odp_temp in answer):
        tried = 0
        points = points + 1
        wins = wins + 1

        button_next_riddle = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="next_riddle",
            label="Następna zagadka"
        )

        await ctx.send("Prawidłowa odpowiedź", components=[button_next_riddle], ephemeral=True)
        await channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
        #print(user_data)
        await update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
    else:
        if(tried >= 3):
            tried = 0
            losts = losts + 1
            button_next_riddle = Button(
                style=ButtonStyle.PRIMARY,
                custom_id="next_riddle",
                label="Następna zagadka"
            )
            await ctx.send("Nieprawidłowa odpowiedź, limit prób przekroczony", components=[button_next_riddle], ephemeral=True)
            await update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
        else:
            button_restart = Button(
                style=ButtonStyle.PRIMARY,
                custom_id="restart_quiz",
                label="Spróbuj ponownie"
            )
            button_next_riddle_abandon = Button(
                style=ButtonStyle.PRIMARY,
                custom_id="next_riddle_abandon",
                label="Następna zagadka"
            )
            await ctx.send("Nieprawidłowa odpowiedź", components=[button_restart, button_next_riddle_abandon], ephemeral=True)
            await update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

    store_quiz_user[ctx.author.user.id] = ctx
        #await ctx.send("Niepoprawna odpowiedź", ephemeral=True)

@bot.component("restart_quiz")
async def button_response(ctx):
    global has_quiz_started, current_answer, channel_quiz

    msg = store_quiz_user[ctx.author.user.id]
    await msg.delete()

    if(has_quiz_started == 1):
        '''
        has_won = await check_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), ctx.author.user.username, int(ctx.author.user.discriminator))
        #print(has_won)
        if(has_won == 0):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = current_riddle,
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Odgadłeś już hasło, zaczekaj na nową zagadkę", ephemeral=True)
        '''

        user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(riddles)-1):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = riddles[wins + losts][0],
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)



@bot.component("next_riddle")
async def button_response(ctx):
    global has_quiz_started, current_answer, channel_quiz

    msg = store_quiz_user[ctx.author.user.id]
    await msg.delete()

    if(has_quiz_started == 1):
        user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(riddles)-1):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = riddles[wins + losts][0],
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)



@bot.component("next_riddle_abandon")
async def button_response(ctx):
    global has_quiz_started, current_answer, channel_quiz

    msg = store_quiz_user[ctx.author.user.id]
    await msg.delete()

    if(has_quiz_started == 1):
        user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        tried = 0
        points = int(user_data[5])
        wins = int(user_data[6])
        losts = int(user_data[7])
        losts = losts + 1
        await update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

        user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(riddles)-1):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = riddles[wins + losts][0],
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)

bot.start()