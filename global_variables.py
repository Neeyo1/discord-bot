import pandas as pd
def init():
    global bicia, uni, hera, legi, rok, TanrothLegi, TanrothHera, TanrothUni, wynikiNick, wynikiId, wynikiRN, wynikiProfil, wynikiRank, page, position, store, store_quiz_user, store_quiz_server, store_bans, has_quiz_started, quiz_cd, current_riddle, current_answer, quiz_task, quiz_number, channel_quiz, riddles, mob_lvl_heros, mob_lvl_tytan, mob_name_tytan, mob_name_e2, df_players_online_run_forever, clan_members_ros, clan_members_west, bot, is_muted

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

    #store
    store = {}
    store_quiz_user = {}
    store_quiz_server = {}
    store_bans = {}

    #quiz
    has_quiz_started = 0
    quiz_cd = 20
    current_riddle = ""
    current_answer = []
    quiz_task = None
    quiz_number = 0
    channel_quiz = None
    riddles = None

    #mobs
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
    
    mob_name_e2 = [
        'Mushita',
        'Kotołak Tropiciel',
        'Shae Phu',
        'Zorg Jednooki Baron',
        'Władca Rzek',
        'Gobbos',
        'Tyrtajos',
        'Tollok Shimger',
        'Szczęt alias Gładki',
        'Razuglag Oklash',
        'Agar',
        'Foverk Turrim',
        'Owadzia Matka',
        'Vari Kruger',
        'Furruk Kozug',
        'Jotun',
        'Tollok Atamatu',
        'Tollok Utumutu',
        'Goplana',
        'Choukker',
        'Wyznawca ciemnych mocy',
        'Mazurnik Przybrzeżny',
        'Łowca czaszek',
        'Grabarz świątynny',
        'Podły zbrojmistrz',
        'Nieumarły krzyżowiec',
        'Szkielet władcy żywiołów',
        'Grubber Ochlaj',
        'Morthen',
        'Żelazoręki Ohydziarz',
        'Kambion',
        'Miłośnik Łowców',
        'Miłośnik rycerzy',
        'Miłośnik magii',
        'Młody Jack Truciciel',
        'Wójt Fistuła',
        'Krab pustelnik',
        'Królowa śniegu',
        'Teściowa Rumcajsa',
        'Pogromca gryfów',
        'Pogromczyni Mantikor',
        'Poskramiacz hydr',
        'Sheba Orcza Szamanka',
        'Burkog Lorulk',
        'Jertek Moxos',
        'Berserker Amuno',
        'Stworzyciel',
        'Fodug Zolash',
        'Mistrz Worundriel',
        'Goons Asterus',
        'Adariel',
        'Duch władcy klanów',
        'Ogr Stalowy Pazur',
        'Bragarth myśliwy dusz',
        'Fursharag pożeracz umysłów',
        'Ziuggrael strażnik królowej',
        'Lusgrathera królowa pramatka',
        'Borgoros Garamir III',
        'Chryzoprenia',
        'Cerasus',
        'Czempion Furboli',
        'Torunia Ankelwald',
        'Breheret żelazny łeb',
        'Mysiur myświórowy król',
        'Sadolia nadzorczyni Hurys',
        'Gothardus kolekcjoner głów',
        'Sataniel skrytobójca',
        'Bergermona krwawa hrabina',
        'Annaniel wysysacz marzeń',
        'Zufulus smakosz serc',
        'Marlloth Malignitas',
        'Mocny Maddoks',
        'Rycerz z za małym mieczem',
        'Arachniregina Colosseus',
        'Pancerny Maddok',
        'Silvanasus',
        'Dendroculus',
        'Tolypeutes',
        'Cuaitl Citlalin',
        'Pogardliwa Sybilla',
        'Yaotl',
        'Quetzalcoatl',
        'Chopesz',
        'Neferkar Set',
        'Chaegd Agnrakh',
        'Vaenra Charkhaam',
        'Terrozaur',
        'Nymphemonia',
        'Zorin',
        'Artenius',
        'Furion'
        ]
    
    #players_online_run_forever
    df_players_online_run_forever_col = ({'Nickname':["temp"], 'Minutes_online':[60], 'Account_id':[1111111], 'Char_id':[1111]})
    df_players_online_run_forever = pd.DataFrame(df_players_online_run_forever_col)
    df_players_online_run_forever = df_players_online_run_forever.drop(df_players_online_run_forever.index[[0]])

    #players list
    clan_members_ros = None
    clan_members_west = None

    #dc bot
    bot = None

    #information about players online
    is_muted = 0