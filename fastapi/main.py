from fastapi import FastAPI
import sys
sys.path.append('../')
import my_utils as u

app = FastAPI()

my_test_dict = {
    ''
    'neeyo': {
        'id': 1,
        'username': 'Neeyo',
        'lvl': 400,
        'prof': 'h'
        },
    'skieta': {
        'id': 2,
        'username': 'Skieta',
        'lvl': 30,
        'prof': 'h'
        },
    'hanys': {
        'id': 3,
        'username': 'Hanys',
        'lvl': 150,
        'prof': 'b'
        },
}

async def get_players_online():
    data_dict = {}
    data = await u.get_data_in_db_players_online_on_titans(path = '../database.db')
    for single_data in data:
        clan = single_data[0]
        titan = single_data[1]
        players = single_data[2]
        if ',' in players:
            players = players.split(",")
        else:
            players = [players]
        try:
            data_dict[clan].update({titan: players})
        except:
            data_dict.update({clan: {titan: players}})
    return data_dict

players_absency = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test():
    return my_test_dict

@app.get("/test/id/{id}")
async def test_by_id(id: int):
    return (my_test_dict[user_data] for user_data in my_test_dict if my_test_dict[user_data]['id'] == id)

@app.get("/test/nickname/{nickname}")
async def test_by_nickname(nickname: str):
    return my_test_dict[nickname]

@app.get("/nieaktywnosc")
async def absency():
    i = 0
    for player in await u.get_data_in_db_absency("Narwhals", "../database.db"):
        players_absency[i] = {'nickname': player[0], 'lvl': int(player[1]), 'days_offline': player[2]}
        i = i + 1
    return players_absency

@app.get("/online")
async def online():
    data = await get_players_online()
    return data

@app.get("/online/{clan}")
async def online_by_clan(clan: str):
    data = await get_players_online()
    return data[clan]