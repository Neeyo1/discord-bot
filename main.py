import pandas as pd
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import interactions
from interactions import Button, ButtonStyle, SelectMenu, SelectOption, ClientPresence, StatusType, PresenceActivity, PresenceActivityType, CommandContext, ComponentContext, Modal, TextInput, TextStyleType
from interactions.ext.files import command_send
from interactions.ext.tasks import IntervalTrigger, create_task

import secret_data as sd
import global_variables as g
import my_utils as u

g.init()

#bot = interactions.Client(token = sd.dc_bod_token, presence=ClientPresence(activities=[PresenceActivity(name="Margonem", type=PresenceActivityType.GAME, created_at=0)],status=StatusType.ONLINE, afk=False))
bot = interactions.Client(token = sd.dc_discord_bot_testy_token, presence=ClientPresence(activities=[PresenceActivity(name="Margonem", type=PresenceActivityType.GAME, created_at=0)],status=StatusType.ONLINE, afk=False))
g.bot = bot

@bot.event
async def on_start():
    print('Online')
    try:
        g.channel_quiz = await interactions.get(bot, interactions.Channel, object_id=1083376240783785985)
    except:
        g.channel_quiz = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
    my_task.start()


@bot.command(
    name="say_something",
    description="say something!",
    scope= [
        sd.dc_discord_bot_testy
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
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def skarpetka(ctx: interactions.CommandContext):
    await command_send(ctx, content = "Skarpeta, znany też jako Skarpeciasty Kox, pierwszy i najlepszy tester discordowych bocików, najlepszy gracz Tarhuny i całego Margonem, dżentelmen, filantrop, człowiek kultury, dobrodziej, wspomożyciel, koxem jest ogolnie. Mówię to ja, Neeyo podpisany, z własnej i nieprzymuszonej woli.", files=interactions.File("img/Skieta/terror_skiety.png"))


@bot.command(
    name="top",
    description="Oblicza ranking graczy z najwieksza iloscia RN",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
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
    await u.resetWyniki()
    await u.get_data_darro()
    if(int(liczba) > len(g.wynikiNick)):
        embed=interactions.Embed(title="Blad, za duzy zakres")
        await ctx.send(embeds=embed)
        return
    embed=interactions.Embed(title="TOP "+str(liczba)+" posiadanych RN na serwerze Narwhals: ", url="https://narwhals.darro.eu/?t=currency")
    for x in range(int(liczba)):
        embed.add_field(name=g.wynikiRank[x] + ". " + g.wynikiNick[x] + "   id: " + g.wynikiId[x] + "   " + str(g.wynikiProfil[x]), value="RN: " + g.wynikiRN[x], inline=False)
    await ctx.send(embeds=embed)
    await u.u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "top")

@bot.command(
    name="find",
    description="Wyswietla ranking RN gracza o podanym ID konta",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
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
    await u.resetWyniki()
    await u.get_data_darro()
    if(liczba in g.wynikiId):
        embed=interactions.Embed(title="Znaleziono gracza")
        embed.add_field(name=g.wynikiRank[g.wynikiId.index(liczba)] + ". " + g.wynikiNick[g.wynikiId.index(liczba)] + "   id: " + g.wynikiId[g.wynikiId.index(liczba)] + "   " + str(g.wynikiProfil[g.wynikiId.index(liczba)]), value="RN: " + g.wynikiRN[g.wynikiId.index(liczba)], inline=False)
        await ctx.send(embeds=embed)
    else:
        embed=interactions.Embed(title="Blad, brak danych")
        await ctx.send(embeds=embed)
        await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "find")
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
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def nieaktywnosc(ctx: interactions.CommandContext):
    if(int(ctx.guild_id) == sd.dc_discord_bot_testy or int(ctx.guild_id) == sd.dc_bod):
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
    elif(ctx.guild_id == sd.dc_sm):
        button2 = Button(
            style=ButtonStyle.PRIMARY,
            custom_id="nieaktywnosc2",
            label="Stoners"
        )
        await ctx.send("Wybierz swiat", components=[button2])
    else:
        await ctx.send("Błąd, nie udało sie pobrac id serwera")
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc")

@bot.component("nieaktywnosc1")
async def button_response(ctx):
    swiat = "Narwhals"

    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
    page = 1

    await ctx.defer()
    if(await u.check_data_in_db_absency_last(swiat, ctx)):
        await u.get_data_absency(ctx, df, swiat, link, page)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc - Narwhals")

@bot.component("nieaktywnosc2")
async def button_response(ctx):
    swiat = "Stoners"
    
    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
    page = 1

    await ctx.defer()
    if(await u.check_data_in_db_absency_last(swiat, ctx)):
        await u.get_data_absency(ctx, df, swiat, link, page)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc - Stoners")

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
        sd.dc_discord_bot_testy
    ],
)
async def stworz_baze(ctx: interactions.CommandContext):
    await ctx.send("Tworzę baze danych...")
    try:
        await u.create_database()
        await ctx.send("Baza danych została utworzona")
    except:
        await ctx.send("Baza danych już istnieje")


@bot.command(
    name="tanroth",
    description="Losuje drop z Tanrotha",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def tanroth(ctx: interactions.CommandContext):
    print(int(ctx.author.user.id))
    response = await u.check_data_in_db_tanroth_last_update(int(ctx.author.user.id))
    if( response == 1):
        await command_send(ctx, files=interactions.File("img/Tanroth/" + await u.random_tanroth_item(int(ctx.guild_id), int(ctx.author.user.id)) + ".png"))
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
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "tanroth")


@bot.command(
    name="online",
    description="Gracze online na wybranym świecie",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
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
    result = await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online")

@bot.command(
    name="online_przycisk",
    description="Gracze online na wybranym swiecie ale z przyciskiem",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
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
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk")

@bot.component("online1")
async def button_response(ctx):
    swiat = "Narwhals"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Narwhals")

@bot.component("online2")
async def button_response(ctx):
    swiat = "Stoners"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Stoners")

@bot.component("online3")
async def button_response(ctx):
    swiat = "Tarhuna"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Tarhuna")

@bot.component("online4")
async def button_response(ctx):
    swiat = "Fobos"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Fobos")

@bot.component("online5")
async def button_response(ctx):
    swiat = "Unia"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Unia")

@bot.command(
    name="rejestracja",
    description="Rejestracja konta w Margonem do systemu powiadomień",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def rejestracja(ctx: interactions.CommandContext):
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
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "rejestracja")

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
    await u.update_characters_in_game_temp(ctx.author.user.id, nickname)
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
    g.store[ctx.author.user.id] = ctx

@bot.component("register_button_1")
async def button_response1(ctx):
    msg = g.store[ctx.author.user.id]
    await msg.delete()
    result = await u.check_data_in_characters_in_game(ctx.guild_id, ctx.author.user.id, await u.select_characters_in_game_temp(ctx.author.user.id))
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
    g.store[ctx.author.user.id] = ctx

@bot.component("register_button_2")
async def button_response2(ctx):
    msg = g.store[ctx.author.user.id]
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
    g.store[ctx.author.user.id] = ctx

@bot.component("register_button_3")
async def button_response3(ctx):
    msg = g.store[ctx.author.user.id]
    await msg.delete()
    await u.update_characters_in_game(ctx.guild_id, ctx.author.user.id, str(await u.select_characters_in_game_temp(ctx.author.user.id)))
    await ctx.send("Dane zaktualizowane", ephemeral=True)

@bot.component("register_button_4")
async def button_response3(ctx):
    msg = g.store[ctx.author.user.id]
    await msg.delete()
    await ctx.send("Zmiany odrzucone", ephemeral=True)


@bot.command(
    name="moje_dropy",
    description="Wyswietla licznik dropów z serwerowego Tanrotha",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def moje_dropy(ctx: interactions.CommandContext):
    try: 
        result = await u.select_all_tanroth_drops(ctx.guild_id, ctx.author.user.id)
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.author.user.username + "#" + ctx.author.user.discriminator, value="Unikaty: " + str(result[0]) + "\n" + "Heroiki: " + str(result[1]) + "\n" + "Legendy: " + str(result[2]), inline=False)
        await ctx.send(embeds=embed)
    except:
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.author.user.username + "#" + ctx.author.user.discriminator, value="Unikaty: " + str(0) + "\n" + "Heroiki: " + str(0) + "\n" + "Legendy: " + str(0), inline=False)
        await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "moje_dropy")


@bot.user_command(
    name="Dropy gracza",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def dropy_gracza(ctx: interactions.CommandContext):
    try: 
        result = await u.select_all_tanroth_drops(ctx.guild_id, ctx.target.user.id)
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.target.user.username + "#" + ctx.target.user.discriminator, value="Unikaty: " + str(result[0]) + "\n" + "Heroiki: " + str(result[1]) + "\n" + "Legendy: " + str(result[2]), inline=False)
        await ctx.send(embeds=embed)
    except:
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.target.user.username + "#" + ctx.target.user.discriminator, value="Unikaty: " + str(0) + "\n" + "Heroiki: " + str(0) + "\n" + "Legendy: " + str(0), inline=False)
        await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "Dropy gracza")


@create_task(IntervalTrigger(60))
async def my_task():
    await u.players_online_run_forever("Narwhals")

@create_task(IntervalTrigger(3))
async def zagadka_delay():
    zagadka_delay.stop()


@bot.command(
    name="online_wykres",
    description="Wykres graczy online z dzisiaj",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
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
    if(await u.select_players_online(nickname)):
        await command_send(ctx, files=interactions.File("img/df_data/df_data.png"))
    else:
        await ctx.send("Brak danych gracza " + nickname)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_wykres")


@bot.command(
    name="timery",
    description="Timery herosów i tytanów na lootlogu",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def timery(ctx: interactions.CommandContext):
    embed=interactions.Embed(title="Timery herosów i tytanów")
    await u.get_timer_alt(embed)
    await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery")


@bot.command(
    name="timery_alt",
    description="Timery herosów i tytanów na lootlogu",
    scope= [
        sd.dc_discord_bot_testy
    ],
)
async def timery_alt(ctx: interactions.CommandContext):
    embed=interactions.Embed(title="Timery herosów i tytanów")
    await u.get_timer_alt(embed)
    await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery_alt")


@bot.command(
    name="dodaj_timer",
    description="Dodaje timer na lootlog",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
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
    if(await u.add_timer(ctx, mob) == 1):
        await ctx.send("Dodano timer potwora " + mob)
    elif(await u.add_timer(ctx, mob) == 2):
        await ctx.send("Brak uprawnień do użycia komendy, tymczasowo ograniczone")
    elif(await u.add_timer(ctx, mob) == 3):
        await ctx.send("Wystąpił błąd")
    #await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery")

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
        sd.dc_discord_bot_testy
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
    await u.clan_members(ctx, klan)


@bot.command(
    name="test_ping",
    description="Testowy ping",
    scope= [
        sd.dc_discord_bot_testy
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
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def zagadka_admin(ctx: interactions.CommandContext):
    #global g.has_quiz_started
    if(int(ctx.author.user.id) not in {349851438228439040, 372381114809188362, 546751756323913754}):
        await ctx.send("Brak uprawnień", ephemeral=True)
        return
    if(int(ctx.channel.id) not in {1085193552864235591, 1083376240783785985}):
        await ctx.send("Użyj komendy w przeznaczonym do tego kanale", ephemeral=True)
        return
    try:
        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete()
    except:
        print("Whatever")
    if(g.has_quiz_started == 1):
        await u.quiz_UI_started(ctx)
    else:
        await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx

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
    #global g.has_quiz_started
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete()
    #await ctx.send(zagadka, ephemeral=True)
    #await ctx.send(odpowiedz, ephemeral=True)
    try:
        await u.add_data_in_db_quiz(int(ctx.guild_id), zagadka, odpowiedz)
        await ctx.send(str(ctx.author.user.username) + " pomyślnie dodał(a) zagadkę: " + zagadka)
    except:
        await ctx.send(str(ctx.author.user.username) + " nie udało sie dodać zagadki: " + zagadka)

    if(g.has_quiz_started == 1):
        await u.quiz_UI_started(ctx)
    else:
        await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx


@bot.component("delete_one")
async def button_response(ctx):
    #global g.has_quiz_started
    #respone_zagadki = await get_data_in_db_quiz(int(ctx.guild_id))
    #for i in range(len(response)):
    #    response_str = response_str + "Zagadka " + str(i + 1) + ": " + response[i][0] + " - " + response[i][1] + "\n"
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete()
    respone_zagadki = await u.get_data_in_db_quiz(int(ctx.guild_id))
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
    if(g.has_quiz_started == 1):
        await u.quiz_UI_started(ctx)
    else:
        await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx


@bot.modal("delete_zagadka_modal")
async def modal_response(ctx, numer: str):
    #global g.has_quiz_started
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete()

    respone_zagadki = await u.get_data_in_db_quiz(int(ctx.guild_id))
    zagadka = respone_zagadki[int(numer)-1][0]
    odpowiedz = respone_zagadki[int(numer)-1][1]
    response = await u.delete_data_in_db_quiz(int(ctx.guild_id), zagadka, odpowiedz)
    if(response == 1):
         await ctx.send(str(ctx.author.user.username) + " Upomyślnie usunął(ęła) zagadkę: " + zagadka)
    elif(response == 2):
         await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    
    if(g.has_quiz_started == 1):
        await u.quiz_UI_started(ctx)
    else:
        await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx


@bot.component("delete_all")
async def button_response(ctx):
    #global g.has_quiz_started
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete()

    response = await u.delete_all_data_in_db_quiz(int(ctx.guild_id))
    if(response == 1):
         await ctx.send(str(ctx.author.user.username) + " pomyślnie usunął(ęła) wszystkie zagadki")
    elif(response == 2):
         await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    
    if(g.has_quiz_started == 1):
        await u.quiz_UI_started(ctx)
    else:
        await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx


@bot.component("start_quiz")
async def button_response(ctx):
    #global g.has_quiz_started, quiz_cd, g.current_riddle, g.current_answer, g.quiz_number, g.quiz_task, riddles
    g.quiz_number = 0
    g.has_quiz_started = 1
    g.riddles = await u.get_data_in_db_quiz(int(ctx.guild_id))

    await u.reset_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), "all")

    response_riddles = await u.get_data_in_db_quiz(int(ctx.guild_id))
    await ctx.send(str(ctx.author.user.username) + " rozpoczął(ęła) quiz")

    try:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
        await channel_quiz_start.send(content="Quiz rozpoczął się")
    except:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
        await channel_quiz_start.send(content="Quiz rozpoczął się")
    #g.quiz_task = asyncio.create_task(quiz_sleep(ctx, response_riddles)) #works

    if(g.has_quiz_started == 0):
        return
    if(g.has_quiz_started == 1):
        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete()
        await u.quiz_UI_started(ctx)
        g.store_quiz_server[ctx.guild.id] = ctx

    #zagadka_delay.start()

    #msg = g.store[ctx.author.user.id]
    #await msg.delete()


@bot.component("stop_quiz")
async def button_response(ctx):
    #global g.has_quiz_started, g.quiz_task
    #msg = g.store[ctx.author.user.id]
    #await msg.delete()

    #g.quiz_task.cancel() #works

    g.has_quiz_started = 0
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete()
    await ctx.send("Zakończono quiz")

    try:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1064671672822677594)
        await channel_quiz_start.send(content="Quiz zakończył się")
    except:
        channel_quiz_start = await interactions.get(bot, interactions.Channel, object_id=1085193552864235591)
        await channel_quiz_start.send(content="Quiz zakończył się")

    quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id))
    quiz_result_str = ""
    if(len(quiz_result) == 0):
        await ctx.send("Nikt nie brał udział w zagadkach")
    else:
        for i in range(len(quiz_result)):
            quiz_result_str = quiz_result_str + str(quiz_result[i][2]) + "#" + str(quiz_result[i][3]) + " - Punkty: " + str(quiz_result[i][5]) + "\n"
        quiz_result_str = quiz_result_str[:-1]
        await ctx.send(quiz_result_str)

    if(g.has_quiz_started == 1):
        await u.quiz_UI_started(ctx)
    else:
        await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx

    #msg = g.store[ctx.author.user.id]
    #await msg.delete()



@bot.command(
    name="zagadka",
    description="Zagadki",
    scope= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def zagadka(ctx: interactions.CommandContext):
    #global g.has_quiz_started, g.current_answer, riddles, channel_quiz
    if(1084883485736583248 in ctx.author.roles or 1084925145195491410 in ctx.author.roles):
        if(g.has_quiz_started == 1):
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
                            label = g.current_riddle,
                            placeholder = "Miejsce na odpowiedź",
                            required = True
                        ),
                    ]
                )
                await ctx.popup(modal)
            else:
                await ctx.send("Odgadłeś już hasło, zaczekaj na nową zagadkę", ephemeral=True)'''
            
            whatever_dude = await u.check_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), ctx.author.user.username, int(ctx.author.user.discriminator))
            user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            #print(user_data)
            user_data = user_data[0]
            #tried = int(user_data[4])
            wins = int(user_data[6])
            losts = int(user_data[7])

            if(wins + losts <= len(g.riddles)-1):
                modal = Modal(
                    custom_id = "answer_quiz_modal",
                    title = "Formularz odpowiedzi na zagadkę",
                    components = [
                        TextInput(
                            style = TextStyleType.SHORT,
                            custom_id = "answer_quiz_modal_odpowiedz",
                            label = g.riddles[wins + losts][0],
                            placeholder = "Miejsce na odpowiedź",
                            required = True
                        ),
                    ]
                )
                await ctx.popup(modal)
            else:
                await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
                quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
                quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
                await g.channel_quiz.send(content=quiz_result_str)


        else:
            await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)
        #g.store[ctx.author.user.id] = ctx
    else:
        await ctx.send("Nie masz uprawnień do wzięcia udziału w zagadce", ephemeral=True)

@bot.modal("answer_quiz_modal")
async def modal_response(ctx, odp: str):
    #global g.current_answer, channel_quiz, riddles
    '''
    try:
        odp_temp = odp.lower()
        odp_temp = unidecode(odp_temp)
    except:
        odp_temp = odp.lower()
    user_data = await get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
    user_data = user_data[0]
    await channel_quiz.send(content=str(ctx.author.user.username) + " odpowiedział(a) na obecną zagadkę: " + odp)
    if(odp_temp in g.current_answer):
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

        g.store_quiz_user[ctx.author.user.id] = ctx
        #await ctx.send("Niepoprawna odpowiedź", ephemeral=True)
    '''

    user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
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
        answer = g.riddles[wins + losts][1].lower()
        answer = unidecode(answer)
        answer = answer.split("/")
    except:
        answer = g.riddles[wins + losts][1].lower()
    await g.channel_quiz.send(content=str(ctx.author.user.username) + " odpowiedział(a): " + odp)
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
        await g.channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
        #print(user_data)
        await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
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
            await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
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
            await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

    g.store_quiz_user[ctx.author.user.id] = ctx
        #await ctx.send("Niepoprawna odpowiedź", ephemeral=True)

@bot.component("restart_quiz")
async def button_response(ctx):
    #global g.has_quiz_started, g.current_answer, channel_quiz

    msg = g.store_quiz_user[ctx.author.user.id]
    await msg.delete()

    if(g.has_quiz_started == 1):
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
                        label = g.current_riddle,
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Odgadłeś już hasło, zaczekaj na nową zagadkę", ephemeral=True)
        '''

        user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(g.riddles)-1):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = g.riddles[wins + losts][0],
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await g.channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)



@bot.component("next_riddle")
async def button_response(ctx):
    #global g.has_quiz_started, g.current_answer, channel_quiz

    msg = g.store_quiz_user[ctx.author.user.id]
    await msg.delete()

    if(g.has_quiz_started == 1):
        user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(g.riddles)-1):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = g.riddles[wins + losts][0],
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await g.channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)



@bot.component("next_riddle_abandon")
async def button_response(ctx):
    #global g.has_quiz_started, g.current_answer, channel_quiz

    msg = g.store_quiz_user[ctx.author.user.id]
    await msg.delete()

    if(g.has_quiz_started == 1):
        user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        tried = 0
        points = int(user_data[5])
        wins = int(user_data[6])
        losts = int(user_data[7])
        losts = losts + 1
        await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

        user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(g.riddles)-1):
            modal = Modal(
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
                components = [
                    TextInput(
                        style = TextStyleType.SHORT,
                        custom_id = "answer_quiz_modal_odpowiedz",
                        label = g.riddles[wins + losts][0],
                        placeholder = "Miejsce na odpowiedź",
                        required = True
                    ),
                ]
            )
            await ctx.popup(modal)
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await g.channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)


@bot.command(
    name="generuj_obrazek",
    description="Generuje obrazek z wynikami losowania",
    scope= [
        sd.dc_discord_bot_testy,
    ],
)
async def generuj_obrazek(ctx: interactions.CommandContext):
    await u.generate_image()

bot.start()