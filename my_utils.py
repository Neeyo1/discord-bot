import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
import requests
import pandas as pd
import time
import sqlite3
import datetime
import random
import os.path
from unidecode import unidecode
from datetime import datetime as dt
from bs4 import BeautifulSoup
import time
import aiofiles
import asyncio
import matplotlib.pyplot as plt
from html2image import Html2Image
#import socketio
#import websockets
from websocket import create_connection
import json
import math
from asyncio import sleep
from PIL import Image, ImageDraw, ImageFont
#from discord.ext import commands
import interactions
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ClientPresence, StatusType, PresenceActivity, PresenceActivityType, CommandContext, ComponentContext, Modal, TextInput, TextStyleType
from interactions.ext.paginator import Page, Paginator
from interactions.ext.files import command_send
from interactions.ext.tasks import IntervalTrigger, create_task

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import secret_data as sd
import global_variables as g

async def get_data(arg, argOrig):
    #global bicia, uni, hera, legi, rok
    odpowiedz = requests.get(arg, cookies=sd.cookies, headers=sd.headers)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    soup.find_all('div', class_='item col-md-12 row-shadow')
    g.bicia += len(soup.find_all('div', class_='item col-md-12 row-shadow'))

    for i in soup.find_all('div', class_='item col-md-12 row-shadow'):
        g.rok = i.find_all('div', class_='col-md-1')

        for j in i.find_all('img'):
            if str(j).find("unique")>0:
                g.uni += 1
            elif str(j).find("heroic")>0:
                g.hera += 1
            elif str(j).find("legendary")>0:
                g.legi += 1
    print(str(g.bicia) + " | " + str(g.uni) + " | " + str(g.hera) + " | " + str(g.legi))

    if len(soup.find_all('a', class_='btn next')) > 0:
        for i in soup.find_all('a', class_='btn next'):
            await get_data(argOrig+str(i['href'])[str(i['href']).find(","):], argOrig)

async def get_timer(embed):
    try:
        #global sd.mob_lvl_heros, sd.mob_lvl_tytan, sd.mob_name_tytan
        odpowiedz = requests.get(sd.bodLL + "/timer", cookies=sd.cookies, headers=sd.headers)
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

            if(mob in g.mob_name_tytan):
                df_timer_tytani = df_timer_tytani.append({'Mob':mob, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(g.mob_lvl_tytan[mob])}, ignore_index=True)
            elif(g.mob_lvl_heros[mob]):
                df_timer_herosi = df_timer_herosi.append({'Mob':mob, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(g.mob_lvl_heros[mob])}, ignore_index=True)
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
    #global sd.groove_headers, sd.groove_cookies
    groove_cookie_string = "; ".join([str(x)+"="+str(y) for x,y in sd.groove_cookies.items()])

    #if(int(ctx.author.user.id) == 349851438228439040 or int(ctx.author.user.id) == 372381114809188362):
    try:
        ws = create_connection(sd.groove_websocket, header = sd.groove_headers, cookie = groove_cookie_string)
        ws.send('42' + json.dumps(["data",{"name":mob_name,"action":"addhottimer","clan":"blade_of_destiny_narwhals","clanID":1834,"aid":"5897579"}]))
        ws.close()
        return 1
    except:
        return 3
    #else:
    #    return 2
    

async def get_timer_alt(embed):
    #global sd.groove_headers, sd.groove_cookies, sd.mob_lvl_heros, sd.mob_lvl_tytan, sd.mob_name_tytan
    groove_cookie_string = "; ".join([str(x)+"="+str(y) for x,y in sd.groove_cookies.items()])
    ws = create_connection(sd.groove_websocket, header = sd.groove_headers, cookie = groove_cookie_string)
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
                if(mob in g.mob_name_tytan):
                    df_timer_tytani = df_timer_tytani.append({'Mob':s, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(g.mob_lvl_tytan[mob])}, ignore_index=True)
                elif(mob in g.mob_lvl_heros):
                    df_timer_herosi = df_timer_herosi.append({'Mob':s, 'Resp_min':int(resp_min), 'Resp_max':int(resp_max), 'Lvl':int(g.mob_lvl_heros[mob])}, ignore_index=True)
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
    #global sd.bodLL, sd.midgardLL, sd.smLL
    if arg.lower() == "bod":
        return sd.bodLL
    elif arg.lower() == "midgard":
        return sd.midgardLL
    elif arg.lower() == "sm":
        return sd.smLL
    else:
        return "BRAK"

async def getMobData(argEmbed, argLink, argMobName, argMobLvl):
    #global bicia, uni, hera, legi
    await get_data(argLink + "monster-" + argMobName, argLink + "monster-" + argMobName)
    sumaBic = g.uni + g.hera + g.legi
    if sumaBic == 0:
        sumaBic = 1
    argEmbed.add_field(name=argMobName + "(" + argMobLvl + " lvl):", value="**Bicia: **" + str(g.bicia) + "\t**Unikaty: **" + str(g.uni) + "\t**Heroiki: **" + str(g.hera) + "\t**Legendy: **" + str(g.legi) + "\n**Procentowy udzial legend: **" + str(round(float(g.legi)/float(sumaBic)*100, 2)) + "%", inline=False)
    g.bicia = 0
    g.uni = 0
    g.hera = 0
    g.legi = 0

async def resetWyniki():
    #global page, position
    g.wynikiNick.clear()
    g.wynikiId.clear()
    g.wynikiRN.clear()
    g.wynikiProfil.clear()
    g.wynikiRank.clear()
    g.page = 1
    g.position = 1

async def get_data_darro():
    #global page, position
    odpowiedz = requests.get("https://narwhals.darro.eu/?t=currency&page=" + str(g.page))
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    print(g.page)
    print(len(soup.find_all('td'))/2)
    if (len(soup.find_all('td'))>0):
        for i in soup.find_all("td"):
            if len(i)>=5:
                g.wynikiNick.append(i.a.string)
                g.wynikiProfil.append(i.a['href'])
                g.wynikiId.append(i.a['href'].replace('https://www.margonem.pl/?task=profile&id=', ''))
                g.wynikiRank.append(str(g.position))
                g.position+=1
            else:
                g.wynikiRN.append(i.string)
        g.page += 1
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
        client = g.bot,
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
        print("Wylosowales: " + g.TanrothLegi[random.randint(0,len(g.TanrothLegi)-1)])
        await check_data_in_tanroth_drops(server_id, user_id, "lega")
        return g.TanrothLegi[random.randint(0,len(g.TanrothLegi)-1)]
    elif(random_number >= 6 and random_number <= 405):          #40%
        print("Wylosowales: " + g.TanrothHera[random.randint(0,len(g.TanrothHera)-1)])
        await check_data_in_tanroth_drops(server_id, user_id, "hero")
        return g.TanrothHera[random.randint(0,len(g.TanrothHera)-1)]
    else:
        print("Wylosowales: " + g.TanrothUni[random.randint(0,len(g.TanrothUni)-1)])
        await check_data_in_tanroth_drops(server_id, user_id, "uni")
        return g.TanrothUni[random.randint(0,len(g.TanrothUni)-1)]
    

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


async def get_data_in_db_last_item(clan):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = [clan]
    sql = ''' SELECT item_id
              FROM last_item
              WHERE clan = ?'''
    res = cur.execute(sql, data)
    res2 = res.fetchone()
    if(res2 is None):
        return None
    else:
        return res2[0]

async def update_data_in_db_last_item(clan, item_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (str(item_id), clan)
    sql = ''' UPDATE last_item
              SET item_id = ?
              WHERE clan = ?'''
    cur.execute(sql, data)
    con.commit()

async def add_data_in_db_last_item(clan, item_id):
    path = 'database.db'
    con = sqlite3.connect(path)
    cur = con.cursor()
    data = (clan, int(item_id))
    sql = ''' INSERT INTO last_item(clan, item_id)
              VALUES(?, ?)'''
    cur.execute(sql, data)
    con.commit()


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
    #global g.df_players_online_run_forever, ros_tanroth, ros_teza, ros_magua, ros_przyzy, ros_lowka, ros_zoons, ros_arcy, ros_renio, ros_krolik, ros_orla, west_tanroth, west_teza, west_magua, west_przyzy, west_lowka, west_zoons, west_arcy, west_renio, west_krolik
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
            if(g.df_players_online_run_forever.loc[g.df_players_online_run_forever['Nickname'] == nickname].any().all()):
                df_minutes = g.df_players_online_run_forever.loc[g.df_players_online_run_forever['Nickname'] == nickname]
                minutes = df_minutes['Minutes_online'].to_string(index=False)
                g.df_players_online_run_forever.loc[g.df_players_online_run_forever['Nickname'] == nickname, ['Minutes_online']] = int(minutes) + 1
            else:
                g.df_players_online_run_forever = g.df_players_online_run_forever.append({'Nickname':nickname, 'Minutes_online':int(1), 'Account_id':int(account_id), 'Char_id':int(char_id)}, ignore_index=True)
            if(True):
                if(nickname in g.ros_tanroth):
                    ros_tanroth_count = ros_tanroth_count+1
                if(nickname in g.ros_teza):
                    ros_teza_count = ros_teza_count+1
                if(nickname in g.ros_magua):
                    ros_magua_count = ros_magua_count+1
                if(nickname in g.ros_przyzy):
                    ros_przyzy_count = ros_przyzy_count+1
                #if(nickname in g.ros_lowka):
                #    ros_lowka_count = ros_lowka_count+1
                if(nickname in g.ros_zoons):
                    ros_zoons_count = ros_zoons_count+1
                #if(nickname in g.ros_arcy):
                #    ros_arcy_count = ros_arcy_count+1
                if(nickname in g.ros_renio):
                    ros_renio_count = ros_renio_count+1
                #if(nickname in g.ros_krolik):
                #    ros_krolik_count = ros_krolik_count+1
                #if(nickname in g.ros_orla):
                #    ros_orla_count = ros_orla_count+1
                if(nickname in g.west_tanroth):
                    west_tanroth_count = west_tanroth_count+1
                if(nickname in g.west_teza):
                    west_teza_count = west_teza_count+1
                if(nickname in g.west_magua):
                    west_magua_count = west_magua_count+1
                if(nickname in g.west_przyzy):
                    west_przyzy_count = west_przyzy_count+1
                #if(nickname in g.west_lowka):
                #    west_lowka_count = west_lowka_count+1
                if(nickname in g.west_zoons):
                    west_zoons_count = west_zoons_count+1
                #if(nickname in g.west_arcy):
                #    west_arcy_count = west_arcy_count+1
                if(nickname in g.west_renio):
                    west_renio_count = west_renio_count+1
                #if(nickname in g.west_krolik):
                #    west_krolik_count = west_krolik_count+1
        
        #print(g.df_players_online_run_forever)
        #print(ros_tanroth_count, ros_teza_count, ros_magua_count, ros_przyzy_count, ros_lowka_count, ros_zoons_count, ros_arcy_count, ros_renio_count, ros_krolik_count, ros_orla_count, west_tanroth_count, west_teza_count, west_magua_count, west_przyzy_count, west_lowka_count, west_zoons_count, west_arcy_count, west_renio_count, west_krolik_count)
        
        players_online_to_ping = 5
        channel = await interactions.get(g.bot, interactions.Channel, object_id=1081942227867140217)

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
            for index, row in g.df_players_online_run_forever.iterrows():
                #print(row['c1'], row['c2'])
                data = (int(row['Account_id']), row['Nickname'], row['Char_id'], row['Minutes_online'], int(date_today.day), int(date_today.month), int(date_today.year), hour_str)
                sql = ''' INSERT INTO players_online(account_id, nickname, char_id, minutes_online, day, month, year, hour)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
                cur.execute(sql, data)
                con.commit()
            #reset df
            g.df_players_online_run_forever = g.df_players_online_run_forever.iloc[0:0]
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
    #global g.current_riddle, g.current_answer
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
            if(response[i][0] == g.current_riddle):
                response_str = response_str + "**Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "**\n"
            else:
                response_str = response_str + "Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "\n"
        response_str = response_str[:-1]
        await ctx.send(response_str, components=[button1])



async def quiz_sleep(ctx, response_riddles):
    #global g.has_quiz_started, quiz_cd, g.current_riddle, g.current_answer, g.quiz_number, g.quiz_task
    #msg = g.store[ctx.author.user.id]
    #await msg.delete()
    #for i in range(len(respone_zagadki)):
    g.current_riddle = response_riddles[g.quiz_number][0]
    try:
        odp_temp = response_riddles[g.quiz_number][1].lower()
        odp_temp = unidecode(odp_temp)
        odp_temp = odp_temp.split("/")
        g.current_answer = odp_temp
    except:
        g.current_answer = response_riddles[g.quiz_number][1].lower()
    if(g.has_quiz_started == 0):
        #await ctx.send("Zakończono quiz", ephemeral=True)
        return
    #await ctx.send(g.current_riddle + " - " + g.current_answer, ephemeral=True)
    if(g.has_quiz_started == 1):
        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete()

        await quiz_UI_started(ctx)

        g.store_quiz_server[ctx.guild.id] = ctx

    print('Start')
    try:
        channel_quiz_start = await interactions.get(g.bot, interactions.Channel, object_id=1064671672822677594)
        await channel_quiz_start.send(content="Pojawiła się nowa zagadka, czas na odpowiedź: 1min")
    except:
        channel_quiz_start = await interactions.get(g.bot, interactions.Channel, object_id=1085193552864235591)
        await channel_quiz_start.send(content="Pojawiła się nowa zagadka, czas na odpowiedź: 1min")

    try:
        await asyncio.sleep(g.quiz_cd)
    except asyncio.CancelledError:
        print('Stop')
        try:
            channel_quiz_start = await interactions.get(g.bot, interactions.Channel, object_id=1064671672822677594)
            await channel_quiz_start.send(content="Quiz został ręcznie zakończony w trakcie trwania")
        except:
            channel_quiz_start = await interactions.get(g.bot, interactions.Channel, object_id=1085193552864235591)
            await channel_quiz_start.send(content="Quiz został ręcznie zakończony w trakcie trwania")

        g.has_quiz_started = 0
        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete()
        await ctx.send(str(ctx.author.user.username) + " zakończył(a) ręcznie quiz")
        if(g.has_quiz_started == 1):
            await quiz_UI_started(ctx)
        else:
            await quiz_UI(ctx)
        g.store_quiz_server[ctx.guild.id] = ctx
    else:
        print('Koniec')
        g.quiz_number = g.quiz_number + 1
        if(g.quiz_number <= len(response_riddles)-1):
            await reset_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), "won")
            g.quiz_task = asyncio.create_task(quiz_sleep(ctx, response_riddles))
        else:
            g.has_quiz_started = 0
            msg = g.store_quiz_server[ctx.guild.id]
            await msg.delete()
            await ctx.send("Zakończono quiz")

            try:
                channel_quiz_start = await interactions.get(g.bot, interactions.Channel, object_id=1064671672822677594)
                await channel_quiz_start.send(content="Quiz zakończył się")
            except:
                channel_quiz_start = await interactions.get(g.bot, interactions.Channel, object_id=1085193552864235591)
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

            if(g.has_quiz_started == 1):
                await quiz_UI_started(ctx)
            else:
                await quiz_UI(ctx)
            g.store_quiz_server[ctx.guild.id] = ctx


async def generate_image():
    empty_slots_pos = [
        [93, 220], [197, 220], [301, 220], [405, 220], [509, 220],
        [93, 266], [197, 266], [301, 266], [405, 266], [509, 266],
        [93, 312], [197, 312], [301, 312], [405, 312], [509, 312],
        [93, 358], [197, 358], [301, 358], [405, 358], [509, 358],
        [93, 404], [197, 404], [301, 404], [405, 404], [509, 404],
        [93, 450], [197, 450], [301, 450], [405, 450], [509, 450]
    ]
    #myFont = ImageFont.truetype('Roboto-Regular.ttf', 16)
    image = Image.open("img/random_pick/template.png") 
    W, H = image.size
    print(W, H)
    #image = Image.new('RGB', size, bgColor)
    draw = ImageDraw.Draw(image)

    myMessage = 'TEST MESSAGE'
    myFont = ImageFont.truetype("arial.ttf", 35)
    w, h = draw.textsize(myMessage, font=myFont)
    x1, y1, x2, y2 = [0, 40, W, 80]
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    draw.text((x, y), myMessage, align='center', font=myFont, fill='black')

    myMessage = 'DATE'
    myFont = ImageFont.truetype("arial.ttf", 25)
    w, h = draw.textsize(myMessage, font=myFont)
    x1, y1, x2, y2 = [0, 130, W, 170]
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    draw.text((x, y), myMessage, align='center', font=myFont, fill='black')

    for i in range(30):
        myMessage = str(i + 1)
        myFont = ImageFont.truetype("arial.ttf", 25)
        w, h = draw.textsize(myMessage, font=myFont)
        x1, y1, x2, y2 = [empty_slots_pos[i][0], empty_slots_pos[i][1], empty_slots_pos[i][0] + 104, empty_slots_pos[i][1] + 46]
        x = (x2 - x1 - w)/2 + x1
        y = (y2 - y1 - h)/2 + y1
        draw.text((x, y), myMessage, align='center', font=myFont, fill='black')

        myFont = ImageFont.truetype("arial.ttf", 15)
        w, h = draw.textsize(myMessage, font=myFont)
        x1, y1, x2, y2 = [empty_slots_pos[i][0], empty_slots_pos[i][1], empty_slots_pos[i][0] + 20, empty_slots_pos[i][1] + 20]
        x = (x2 - x1 - w)/2 + x1
        y = (y2 - y1 - h)/2 + y1
        draw.text((x, y), myMessage, align='center', font=myFont, fill='black')
        draw.rectangle([x1, y1, x2, y2], outline = 'black')

    image.save('img/random_pick/test.png', "PNG")
    #return image


async def save_logs(guild_id, user_id, nickname, hash_code, command):
    current_daytime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    #async with aiofiles.open('logs.txt', mode='w') as f:
    #    await f.write(str(guild_id) + " | " + str(user_id) + "(" + nickname + "#" + str(hash_code) + ") | " + command)
    f = open("logs.txt", "a")
    f.write(str(guild_id) + " | " + str(user_id) + "(" + nickname + "#" + str(hash_code) + ") | " + command + " | " + current_daytime + "\n")
    f.close()


async def get_google_sheets_data(ctx, embed):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    creds = None
    if(os.path.exists('token.json')):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if(not creds or not creds.valid):
        if(creds and creds.expired and creds.refresh_token):
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sd.SPREADSHEET_ID, range="B7:H30").execute()
        values = result.get('values', [])

        if(not values):
            embed.add_field(name="Wystąpił błąd", value="Nie mozna odczytac danych", inline=False)
            return
        
        embed_str = ""
        embed_last_update = ""

        for row in values:
            if(len(row) == 0):
                continue
            if(len(row) >= 2 and row[2] == '-'):
                break
            elif(len(row) >= 2 and row[2] == 'Gracz'):
                continue
            elif("Ostatnia aktualizacja" in row[0]):
                embed_last_update = row[0]
            else:
                embed_str = embed_str + row[0] + ". " + row[2] + ": " + row[4] + "pkt, " + row[6] + "RN\n"
            print(row)
        embed_str = embed_str[:-1]
        embed.add_field(name=embed_last_update, value=embed_str, inline=False)
        embed.url = "https://docs.google.com/spreadsheets/d/" + sd.SPREADSHEET_ID
    except HttpError as err:
        print(err)


async def generate_image_from_html(link, lvl):
    hti = Html2Image()

    respond = requests.get(link)
    soup = BeautifulSoup(respond.text, 'html.parser')
    data = str(soup.find('div', class_='item item-tip-')['data-stat'])
    datatemp = str(soup.find('div', class_='item item-tip-'))
    print(datatemp)
    data = data.split(";")
    item_name = str(soup.find('div', class_='item item-tip-')['data-name'])
    print(data)

    data_dict = {}
    for i in data:
        if "rarity=" in i:
            data_dict['item_rarity'] = i[7:]
            continue
        if "resfire=" in i:
            data_dict['item_res_fire'] = i[8:]
            continue
        elif "fire=" in i:
            data_dict['item_fire_dmg'] = i[5:]
            continue
        if "da=" in i:
            data_dict['item_wc'] = i[3:]
            continue
        if "manabon=" in i:
            data_dict['item_mana'] = i[8:]
            continue
        if "sa=" in i:
            data_dict['item_sa'] = i[3:]
            continue
        if "lvl=" in i:
            data_dict['item_lvl'] = i[4:]
            continue
        if "reqp=" in i:
            data_dict['item_prof'] = i[5:]
            continue
        if "contra=" in i:
            data_dict['item_contra'] = i[7:]
            continue
        if "resfrost=" in i:
            data_dict['item_res_frost'] = i[9:]
            continue
        elif "frost=" in i:
            data_temp = i[6:].split(",")
            data_dict['item_frost_slow'] = data_temp[0]
            data_dict['item_frost_dmg'] = data_temp[1]
            continue
        if "resdmg=" in i:
            data_dict['item_res'] = i[7:]
            continue
        elif "acdmg=" in i:
            data_dict['item_low_ac'] = i[6:]
            continue
        elif "dmg=" in i:
            data_dict['item_dmg'] = i[4:]
            continue
        if "dz=" in i:
            data_dict['item_zr'] = i[3:]
            continue
        if "hp=" in i:
            data_dict['item_hp'] = i[3:]
            continue
        if "act=" in i:
            data_dict['item_res_poison'] = i[4:]
            continue
        if "poison=" in i:
            data_temp = i[7:].split(",")
            data_dict['item_poison_slow'] = data_temp[0]
            data_dict['item_poison_dmg'] = data_temp[1]
            continue
        if "lowcrit=" in i:
            data_dict['item_low_crit'] = i[8:]
            continue
        elif "crit=" in i:
            data_dict['item_crit'] = i[5:]
            continue
        if "critmval=" in i:
            data_dict['item_crit_m_val'] = i[9:]
            continue
        if "heal=" in i:
            data_dict['item_heal'] = i[5:]
            continue
        if "reslight=" in i:
            data_dict['item_res_light'] = i[9:]
            continue
        elif "light=" in i:
            data_dict['item_light_dmg'] = i[6:]
            continue
        if "critval=" in i:
            data_dict['item_crit_val'] = i[8:]
            continue
        if "energybon=" in i:
            data_dict['item_energy'] = i[10:]
            continue
        if "lowevade=" in i:
            data_dict['item_low_evade'] = i[9:]
            continue
        elif "evade=" in i:
            data_dict['item_evade'] = i[6:]
            continue
        if "absorb=" in i:
            data_dict['item_absorb'] = i[7:]
            continue
        if "absorbm=" in i:
            data_dict['item_absorb_m'] = i[8:]
            continue
        if "ac=" in i:
            data_dict['item_ac'] = i[3:]
            continue
        if "di=" in i:
            data_dict['item_int'] = i[3:]
            continue
        if "heal=" in i:
            data_dict['item_heal'] = i[5:]
            continue
        if "endest=" in i:
            data_dict['item_low_energy'] = i[7:]
            continue
        if "manadest=" in i:
            data_dict['item_low_mana'] = i[9:]
            continue
        if "ds=" in i:
            data_dict['item_str'] = i[3:]
            continue
        if "hpbon=" in i:
            data_dict['item_hp_bon'] = i[6:]
            continue
        if "blok=" in i:
            data_dict['item_blok'] = i[5:]
            continue
        if "pierceb=" in i:
            data_dict['item_pierceb'] = i[8:]
            continue
        if "wound=" in i:
            data_temp = i[6:].split(",")
            data_dict['item_wound_chance'] = data_temp[0]
            data_dict['item_wound_dmg'] = data_temp[1]
            continue
    
    print(data_dict)

    html_page = '<div class="item-tip tip t_item"><b class="item-name">' + item_name + '</b>'
    if 'item_rarity' in data_dict:
        html_page = html_page + '<b class="' + data_dict['item_rarity'] + '"><br/>* ' + data_dict['item_rarity'] + ' *</b>'
    if 'item_dmg' in data_dict:
        html_page = html_page + '<br/>Atak: ' + data_dict['item_dmg']
    if 'item_fire_dmg' in data_dict:
        html_page = html_page + '<br/>Obrażenia od ognia: ~' + data_dict['item_fire_dmg']
    if 'item_frost_dmg' in data_dict:
        html_page = html_page + '<br/>Obrażenia od zimna: +' + data_dict['item_frost_dmg']
    if 'item_frost_slow' in data_dict:
        html_page = html_page + '<br/>oraz spowalnia cel o ' + str(0.01 * int(data_dict['item_frost_slow'])) + ' SA'
    if 'item_light_dmg' in data_dict:
        html_page = html_page + '<br/>Obrażenia od błyskawic: ' + data_dict['item_light_dmg']
    if 'item_poison_dmg' in data_dict:
        html_page = html_page + '<br/>Obrażenia od trucizny: +' + data_dict['item_poison_dmg']
    if 'item_poison_slow' in data_dict:
        html_page = html_page + '<br/>oraz spowalnia cel o ' + str(0.01 * int(data_dict['item_poison_slow'])) + ' SA'    
    if 'item_contra' in data_dict:
        html_page = html_page + '<br/+'  + data_dict['item_contra'] + '% szans na kontrę po krytyku'
    if 'item_ac' in data_dict:
        html_page = html_page + '<br/>Pancerz: ' + data_dict['item_ac']
    if 'item_res_poison' in data_dict:
        html_page = html_page + '<br/>Odporność na truciznę +' + data_dict['item_res_poison'] + '%'
    if 'item_res_fire' in data_dict:
        html_page = html_page + '<br/>Odporność na ogień +' + data_dict['item_res_fire'] + '%'
    if 'item_res_frost' in data_dict:
        html_page = html_page + '<br/>Odporność na zimno +' + data_dict['item_res_frost'] + '%'
    if 'item_res_light' in data_dict:
        html_page = html_page + '<br/>Odporność na błyskawice +' + data_dict['item_res_light'] + '%'
    if 'item_absorb' in data_dict:
        html_page = html_page + '<br/>Absorbuje do ' + data_dict['item_absorb'] + ' obrażeń fizycznych'
    if 'item_absorb_m' in data_dict:
        html_page = html_page + '<br/>Absorbuje do ' + data_dict['item_absorb_m'] + ' obrażeń magicznych'
    if 'item_blok' in data_dict:
        html_page = html_page + '<br/>Blok: +' + data_dict['item_blok']
    if 'item_low_ac' in data_dict:
        html_page = html_page + '<br/>Niszczy ' + data_dict['item_low_ac'] +' punktów pancerza podczas ciosu'  
    if 'item_crit' in data_dict:
        html_page = html_page + '<br/>Cios krtytyczny: +' + data_dict['item_crit'] + '%'
    if 'item_crit_val' in data_dict:
        html_page = html_page + '<br/>Siła krytyka fizycznego: +' + data_dict['item_crit_val'] + '%'
    if 'item_crit_m_val' in data_dict:
        html_page = html_page + '<br/>Siła krytyka magicznego: +' + data_dict['item_crit_m_val'] + '%'
    if 'item_wc' in data_dict:
        html_page = html_page + '<br/>Wszystkie cechy: +' + data_dict['item_wc']
    if 'item_str' in data_dict:
        html_page = html_page + '<br/>Siła: +' + data_dict['item_str']
    if 'item_zr' in data_dict:
        html_page = html_page + '<br/>Zręczność: +' + data_dict['item_zr']
    if 'item_int' in data_dict:
        html_page = html_page + '<br/>Intelekt: +' + data_dict['item_int']
    if 'item_heal' in data_dict:
        html_page = html_page + '<br/>Przywraca ' + data_dict['item_heal'] + ' punktów życia podczas walki'
    if 'item_low_crit' in data_dict:
        html_page = html_page + '<br/>Podczas obrony szansa na cios krytyczny przeciwnika jest mniejsza o ' + data_dict['item_low_crit'] + ' punkty procentowe'    
    if 'item_energy' in data_dict:
        html_page = html_page + '<br/>Energia: +' + data_dict['item_energy']
    if 'item_mana' in data_dict:
        html_page = html_page + '<br/>Mana: +' + data_dict['item_mana']
    if 'item_low_energy' in data_dict:
        html_page = html_page + '<br/>Podczas obrony niszczy ' + data_dict['item_low_energy'] + ' energii'
    if 'item_evade' in data_dict:
        html_page = html_page + '<br/>Unik: +' + data_dict['item_evade']
    if 'item_hp' in data_dict:
        html_page = html_page + '<br/>Życie: +' + data_dict['item_hp']
    if 'item_hp_bon' in data_dict:
        html_page = html_page + '<br/>+' + data_dict['item_hp_bon'] + ' życia za 1 pkt siły'  
    if 'item_low_evade' in data_dict:
        html_page = html_page + '<br/>Podczas ataku unik przeciwnika jest mniejszy o ' + data_dict['item_low_evade']
    if 'item_low_mana' in data_dict:
        html_page = html_page + '<br/>Podczas obrony niszczy ' + data_dict['item_low_mana'] + ' many'  
    if 'item_pierceb' in data_dict:
        html_page = html_page + '<br/>' + data_dict['item_pierceb'] + ' szans na zablokowanie przebicia'    
    if 'item_sa' in data_dict:
        html_page = html_page + '<br/>SA: +' + str(round(0.01 * int(data_dict['item_sa']), 2))
    if 'item_res' in data_dict:
        html_page = html_page + '<br/>Niszczenie odporności magicznych o ' + data_dict['item_res'] + '% podczas ciosu'
    if 'item_wound_dmg' in data_dict:
        html_page = html_page + '<br/>Głęboka rana, ' + data_dict['item_wound_chance'] + '% szans na +' + data_dict['item_wound_dmg'] + 'obrażeń'
    if 'item_lvl' in data_dict:
        html_page = html_page + '<br/>Wymagany poziom: ' + data_dict['item_lvl']
    if 'item_prof' in data_dict:
        html_page = html_page + '<br/>Wymagana profesja: ' + data_dict['item_prof']
    html_page = html_page + '</div>'

    #await pancerz(data_dict['item_prof'], data_dict['item_type'], data_dict['item_rarity'], int(data_dict['item_lvl']), lvl)
    await symulator_pancerz(data_dict)
    #await symulator_unik(data_dict)
    await symulator_abs_fiz(data_dict)
    await symulator_abs_mag(data_dict)

    #html_page = '<div class="item-tip tip t_item"><b class="item-name">Trupia torba III</b><b class="legendary">* legendarny *</b><span class="type-text">Typ:  Torby</span><br>Mieści 42 przedmioty<br>Nieznany stat: rarity<br><i class="idesc">Nie ma dziur, materiał też niczego sobie... Chyba tobie bardziej się przyda niż umarłym.<br><br>Halloween 2022 r.</i>Wartość: 10</div>'
    #first_br = html_page.find("*")
    #second_br = html_page.find("Typ")
    #third_br = html_page.find("Wartość")
    #html = html_page[:first_br] + '<br/>' + html_page[first_br:second_br] + '<br/>' + html_page[second_br:third_br] + '<br/>' + html_page[third_br:]
    #html = '<html><head></head><body>' + html_page + '</body></html>'
    css = 'body {color: #839496; background: #121620;}'
    hti.screenshot(html_str=html_page, css_str=css, save_as='page.png')


def set_variables(type, rarity, lvl, upgrade_lvl):
    if type == 'tarcza':
        p = 0.75
    elif type == 'helm':
        p = 0.33
    elif type == 'buty':
        p = 0.3
    elif type == 'rekawice':
        p = 0.25
    else:
        p = 1.0

    if rarity == 'normal':
        r = 0
    elif rarity == 'unique':
        r = 1
    elif rarity == 'enhanced':
        r = 2
    elif rarity == 'heroic':
        r = 2
    elif rarity == 'legendary':
        r = 3
    elif rarity == 'artefact':
        r = 4

    x_before = lvl
    R_before = x_before*x_before + (130 + math.ceil(10*r/3))*x_before + (130 + 390*r)

    x_after = lvl + upgrade_lvl * round(0.03 * lvl)
    R_after = x_after*x_after + (130 + math.ceil(10*r/3))*x_after + (130 + 390*r)
    
    return p, r, x_before, R_before, x_after, R_after

async def symulator_pancerz(data_dict):
    prof = data_dict['item_prof']
    type = 'zbroja'
    rarity = 'legendary'
    lvl = int(data_dict['item_lvl'])
    upgrade_lvl = 5

    p, r, x_before, R_before, x_after, R_after = set_variables(type, rarity, lvl, upgrade_lvl)

    if prof == 'w':
        c = 1.4
    elif prof == 'p':
        c = 1.0
    elif prof == 'b':
        c = 0.9
    elif prof == 'm':
        c = 0.5
    elif prof == 't':
        c = 0.7
    elif prof == 'h':
        c = 0.8
    elif all([x in prof for x in ['w', 'p', 'b', 'm', 't', 'h']]):
        c = 0.9
    elif all([x in prof for x in ['p', 'm', 't']]):
        c = 0.75
    elif all([x in prof for x in ['b', 't', 'h']]):
        c = 0.8
    elif all([x in prof for x in ['w', 'p']]):
        c = 1.2
    elif all([x in prof for x in ['w', 'b']]):
        c = 1.15
    elif all([x in prof for x in ['p', 't']]):
        c = 0.85
    elif all([x in prof for x in ['p', 'm']]):
        c = 0.75
    elif all([x in prof for x in ['b', 'h']]):
        c = 0.85
    elif all([x in prof for x in ['m', 't']]):
        c = 0.6
    elif all([x in prof for x in ['t', 'h']]):
        c = 0.75
    else:
        c= 1.0
    
    pancerz_before = round(0.02 * p * c * R_before)
    print(pancerz_before)
    pancerz_after = round(0.02 * p * c * R_after)

    if pancerz_before == int(data_dict['item_ac']):
        print(pancerz_after)
    else:
        pancerz_addictional_before = int(data_dict['item_ac']) - pancerz_before
        for i in range(10):
            pancerz_temp = round(0.003 * i * p * (x_before * x_before + 130 * x_before))
            print(pancerz_temp)
            if pancerz_temp == pancerz_addictional_before:
                n = i
                break
        pancerz_addictional_after = round(0.003 * n * p * (x_after * x_after + 130 * x_after))
        print(pancerz_after + pancerz_addictional_after)

async def symulator_abs_fiz(data_dict):
    prof = data_dict['item_prof']
    type = 'zbroja'
    rarity = 'legendary'
    lvl = int(data_dict['item_lvl'])
    upgrade_lvl = 5

    p, r, x_before, R_before, x_after, R_after = set_variables(type, rarity, lvl, upgrade_lvl)

    if prof == 'm':
        c = 6.0
    if prof == 't':
        c = 4.0
    elif all([x in prof for x in ['p', 'm', 't']]):
        c = 3.4
    elif all([x in prof for x in ['p', 'm']]):
        c = 3.0
    elif all([x in prof for x in ['m', 't']]):
        c = 5.0
    else:
        c = 0
    
    if(type in ['zbroja', 'tarcza', 'helm', 'rekawice', 'buty']):
        value_base_before = round(0.01 * p * c * R_before)
        value_base_after = round(0.01 * p * c * R_after)
    else:
        value_base_before = 0
        value_base_after = 0

    if value_base_before == int(data_dict['item_absorb']):
        print(value_base_after)
    else:
        value_addictional_before = int(data_dict['item_absorb']) - value_base_before
        for n in range(10):
            value_temp = round(0.12 * n * (x_before * x_before + 130 * x_before))
            if value_temp == value_addictional_before:
                value_addictional_after = round(0.12 * n * (x_after * x_after + 130 * x_after))
                break
        print(value_base_after + value_addictional_after)
    
async def symulator_abs_mag(data_dict):
    prof = data_dict['item_prof']
    type = 'zbroja'
    rarity = 'legendary'
    lvl = int(data_dict['item_lvl'])
    upgrade_lvl = 5

    p, r, x_before, R_before, x_after, R_after = set_variables(type, rarity, lvl, upgrade_lvl)

    if prof == 'm':
        c = 6.0
    if prof == 't':
        c = 4.0
    elif all([x in prof for x in ['p', 'm', 't']]):
        c = 3.4
    elif all([x in prof for x in ['p', 'm']]):
        c = 3.0
    elif all([x in prof for x in ['m', 't']]):
        c = 5.0
    else:
        c = 0
    
    if(type in ['zbroja', 'tarcza', 'helm', 'rekawice', 'buty']):
        value_base_before = round(0.005 * p * c * R_before)
        value_base_after = round(0.005 * p * c * R_after)
    else:
        value_base_before = 0
        value_base_after = 0

    if value_base_before == int(data_dict['item_absorb_m']):
        print(value_base_after)
    else:
        value_addictional_before = int(data_dict['item_absorb_m']) - value_base_before
        for n in range(10):
            value_temp = round(0.12 * n * (x_before * x_before + 130 * x_before))
            if value_temp == value_addictional_before:
                value_addictional_after = round(0.12 * n * (x_after * x_after + 130 * x_after))
                break
        print(value_base_after + value_addictional_after)

async def symulator_unik(data_dict):
    prof = data_dict['item_prof']
    type = 'zbroja'
    rarity = 'legendary'
    lvl = int(data_dict['item_lvl'])
    upgrade_lvl = 5

    p, r, x_before, R_before, x_after, R_after = set_variables(type, rarity, lvl, upgrade_lvl)

    if prof == 'b':
        c = 1
    else:
        c = 0
    
    if(type == 'zbroja'):
        unik_base_before = round(1/3 * c * x_before)
        unik_base_after = round(1/3 * c * x_after)
    else:
        unik_base_before = 0
        unik_base_after = 0

    if unik_base_before == int(data_dict['item_evade']):
        print(unik_base_after)
    else:
        unik_addictional_before = int(data_dict['item_evade']) - unik_base_before
        for i in range(10):
            unik_temp = round(0.1 * i * x_before)
            if unik_temp == unik_addictional_before:
                n = i
                break
        unik_addictional_after = round(0.1 * n * x_after)
        print(unik_base_after + unik_addictional_after)


async def follow_posts(link):
    odpowiedz = requests.get(link)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    table = soup.find('table', id_='posts')
    table = soup.find('tbody')
    print(table)


async def listen_for_new_items(link, clan):
    legendary_items = []
    first_item_id = 0

    try:
        last_item = await get_data_in_db_last_item(clan)
    except Exception as e:
        print(e)
        path = 'database.db'
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("CREATE TABLE last_item(clan, item_id)")
        last_item = str(await get_data_in_db_last_item(clan))
    #print(last_item)

    odpowiedz = requests.get(link, cookies=sd.cookies, headers=sd.headers)
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    items = soup.find_all('div', class_='item col-md-12 row-shadow')

    for i in items:
        #print(i)
        try:
            item_id = str(i.find('a', class_='itemborder')['href'])[7:]
        except:
            item_id = str(i.find('a', class_='empty-replacer hastip')['href'])[7:]
        if(first_item_id == 0):
            first_item_id = item_id
        #print(first_item_id)
        #print(item_id)

        if(last_item is None):
            await add_data_in_db_last_item(clan, item_id)
            return
        if(last_item == first_item_id):
            print("Dane aktualne")
            return
        if(last_item == item_id):
            await update_data_in_db_last_item(clan, first_item_id)
            print("Dane zaktualizowane")
            return
        #print(str(item_id))
        #if(item_id == await get
        #print(i)
        for item in i.find_all('img'):
            data = str(item["data-stats"])
            data = data.split(";")
            item_name = data[0]
            item_name = item_name[:item_name.find("||")]
            #print(item_name)
            #print(data)
            for single_data in data:
                if "rarity=" in single_data:
                    item_rarity = single_data[7:]
                    if('heroic' in item_rarity):
                        legendary_items.append(item_name)
                    break
            #print(item_rarity)
        #print(str(len(legendary_items)))
        if(len(legendary_items) > 0):
            mob_name = i.find('a', class_='hastip').string
            for e2_name in g.mob_name_e2:
                if(unidecode(e2_name.lower()) in unidecode(mob_name.lower())):
                    #print(unidecode(e2_name.lower()))
                    #print(unidecode(mob_name.lower()))
                    #print(e2_name)
                    mob_name = e2_name
                    break
            else:
                mob_name = mob_name[27:mob_name.find("(")]
            #print(mob_name)

            players = len(i.find_all('div', class_='player hastip'))
            #print(str(players))
            if(players == 1):
                player_nickname = i.find('div', class_='player hastip')["data-tip"]
                player_nickname = player_nickname[:player_nickname.find(" (")]
                try:
                    channel_last_item = await interactions.get(g.bot, interactions.Channel, object_id=1064671672822677594)
                except:
                    channel_last_item = await interactions.get(g.bot, interactions.Channel, object_id=1085193552864235591)
                await channel_last_item.send(content=player_nickname + " zdobył(a) " + item_name + " z potwora " + mob_name + " w grupie 1-osobowej")
                print(player_nickname + " zdobył(a) " + item_name + " z potwora " + mob_name + " w grupie 1-osobowej")
            else:
                time.sleep(0.5)
                odpowiedz = requests.get(link + "item-" + str(item_id), cookies=sd.cookies, headers=sd.headers)
                soup2 = BeautifulSoup(odpowiedz.text, 'html.parser')
                #print(soup2)

                for item_drop in soup2.find_all('p', class_='divide catcher'):
                    item_drop = str(item_drop)
                    item_catched = item_drop[26:item_drop.find(' <b class="color">')]
                    who_cathced = item_drop[item_drop.find('</b>')+5:item_drop.find('</p>')]
                    #print(item_catched)
                    #print(who_cathced)
                    if item_catched in legendary_items:
                        try:
                            channel_last_item = await interactions.get(g.bot, interactions.Channel, object_id=1064671672822677594)
                        except:
                            channel_last_item = await interactions.get(g.bot, interactions.Channel, object_id=1085193552864235591)
                        await channel_last_item.send(content=who_cathced + " zdobył(a) " + item_catched + " z potwora " + mob_name + " w grupie " + str(players) + "-osobowej")
                        print(who_cathced + " zdobył(a) " + item_catched + " z potwora " + mob_name + " w grupie " + str(players) + "-osobowej")
            
            legendary_items.clear()

    #IN CASE LAST ITEM IS NOT ON FIRST PAGE        
    await update_data_in_db_last_item(clan, first_item_id)
    print("Dane zaktualizowane, nie znaleziono ostatniego itemu")

    #print(str(len(soup.find_all('a', class_='btn next'))))
    #print(str(soup.find('a', class_='btn next')['href']))
    #if len(soup.find_all('a', class_='btn next')) > 0:
    #    await listen_for_new_items(link + str(soup.find('a', class_='btn next')['href']), clan)

async def e2_list():
    odpowiedz = requests.get("https://margohelp.pl/elity-ii")
    soup = BeautifulSoup(odpowiedz.text, 'html.parser')
    e2 = soup.find_all('div', class_='heros-box')
    for i in e2:
        mob_name = str(i.find('b'))
        mob_name = mob_name[3:mob_name.find(" (")]
        print("'" + mob_name + "',")