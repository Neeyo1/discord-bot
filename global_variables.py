import pandas as pd
def init():
    global bicia, uni, hera, legi, rok, TanrothLegi, TanrothHera, TanrothUni, wynikiNick, wynikiId, wynikiRN, wynikiProfil, wynikiRank, page, position, store, store_quiz_user, store_quiz_server, has_quiz_started, quiz_cd, current_riddle, current_answer, quiz_task, quiz_number, channel_quiz, riddles, mob_lvl_heros, mob_lvl_tytan, mob_name_tytan, df_players_online_run_forever, ros_tanroth, ros_teza, ros_magua, ros_przyzy, ros_lowka, ros_zoons, ros_arcy, ros_renio, ros_krolik, ros_orla, west_tanroth, west_teza, west_magua, west_przyzy, west_lowka, west_zoons, west_arcy, west_renio, west_krolik, west_orla, bot

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
    
    #players_online_run_forever
    df_players_online_run_forever_col = ({'Nickname':["temp"], 'Minutes_online':[60], 'Account_id':[1111111], 'Char_id':[1111]})
    df_players_online_run_forever = pd.DataFrame(df_players_online_run_forever_col)
    df_players_online_run_forever = df_players_online_run_forever.drop(df_players_online_run_forever.index[[0]])

    #players list
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

    #dc bot
    bot = None