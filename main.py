import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
from unidecode import unidecode
import interactions
from interactions import listen, slash_command, SlashContext, AutocompleteContext, message_context_menu, user_context_menu, component_callback, ComponentContext, ModalContext, Task

import secret_data as sd
import global_variables as g
import my_utils as u

g.init()

my_token = sd.dc_discord_bot_testy_token
#my_token = sd.dc_bod_token

#bot = interactions.Client(token = sd.dc_bod_token, presence=ClientPresence(activities=[PresenceActivity(name="Margonem", type=PresenceActivityType.GAME, created_at=0)],status=StatusType.ONLINE, afk=False))

#bot = interactions.Client(token = sd.dc_discord_bot_testy_token, presence=interactions.ClientPresence(since=0, activities=[interactions.PresenceActivity(name="Margonem", type=interactions.PresenceActivityType.GAME, created_at=0)], status=interactions.StatusType.ONLINE, afk=False))
bot = interactions.Client(activity=interactions.Activity(name="Margonem", type=interactions.ActivityType.GAME, created_at=time.time()))
bot.send_command_tracebacks = False

@listen()
async def on_startup():
    g.bot = bot
    print('Online')
    my_task.start()
    look_for_new_item.start()
    look_for_new_bans.start()
    present_new_bans.start()


@slash_command(
    name="say_something",
    description="say something!",
    scopes= [
        sd.dc_discord_bot_testy
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="text",
            description="What you want to say",
            required=True,
        ),
    ],
    
)
async def say_something(ctx: SlashContext, text: str):
    print(ctx.author.roles)
    if(1084883485736583248 in ctx.author.roles):
        print("Yess")

'''
@slash_command(
    name="count",
    description="Oblicza statystyki bić zadanego potwora",
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="mob",
            description="Link do moba na lootlogu",
            required=True,
        ),
    ],
)
async def count(ctx: SlashContext, mob: str):
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

@slash_command(
    name="wakacje2022",
    description="Oblicza statystyki bić potworów z eventu wakacje 2022",
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def wakacje2022(ctx: SlashContext, klan: str):
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

@slash_command(
    name="halloween2022",
    description="Oblicza statystyki bić potworów z eventu halloween 2022",
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def halloween2022(ctx: SlashContext, klan: str):
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

@slash_command(
    name="gwiazdka2022",
    description="Oblicza statystyki bić potworów z eventu gwiazdka 2022",
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def gwiazdka2022(ctx: SlashContext, klan: str):
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

@slash_command(
    name="skarpetka",
    description="Informacje o Skarpecie",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def skarpetka(ctx: SlashContext):
    await ctx.send(content = "Skarpeta, znany też jako Skarpeciasty Kox, pierwszy i najlepszy tester discordowych bocików, najlepszy gracz Tarhuny i całego Margonem, dżentelmen, filantrop, człowiek kultury, dobrodziej, wspomożyciel, koxem jest ogolnie. Mówię to ja, Neeyo podpisany, z własnej i nieprzymuszonej woli.", files=interactions.File("img/Skieta/terror_skiety.png"))


@slash_command(
    name="top",
    description="Oblicza ranking graczy z najwieksza iloscia RN",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.INTEGER,
            name="liczba",
            description="Liczba osob do wyswietlenia",
            required=True,
        ),
    ],
)
async def top(ctx: SlashContext, liczba: int):
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

@slash_command(
    name="find",
    description="Wyswietla ranking RN gracza o podanym ID konta",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="liczba",
            description="ID konta",
            required=True,
        ),
    ],
)
async def find(ctx: SlashContext, liczba: str):
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
@slash_command(
    name="nieaktywnosc",
    description="Podaje  najdluzej nieaktywne osoby na danym swiecie",
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="swiat",
            description="Swiat z którego zostaną pobrane dane",
            required=True,
        ),
    ],
)
async def nieaktywnosc(ctx: SlashContext, swiat: str):
    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    #embed=interactions.Embed(title="Nieaktywnosci(wlasnie pobrane):")
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page=1"

    await ctx.send("Zbieram dane...")
    if(await check_data_in_db_absency_last(swiat, ctx)):
        await get_data_absency(ctx, bot, df, swiat, link)
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

@slash_command(
    name="nieaktywnosc",
    description="Podaje najdluzej nieaktywne osoby na danym swiecie, aktualizacja raz na 6 godzin",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def nieaktywnosc(ctx: SlashContext):
    if(int(ctx.guild_id) == sd.dc_discord_bot_testy or int(ctx.guild_id) == sd.dc_bod):
        components = [
            interactions.ActionRow(
                interactions.Button(
                    style=interactions.ButtonStyle.PRIMARY,
                    custom_id="nieaktywnosc1",
                    label="Narwhals"
                ),
                interactions.Button(
                    style=interactions.ButtonStyle.PRIMARY,
                    custom_id="nieaktywnosc2",
                    label="Stoners"
                )
            )
        ]
        await ctx.send("Wybierz swiat", components=components)
    elif(ctx.guild_id == sd.dc_sm):
        components = [
            interactions.ActionRow(
                interactions.Button(
                    style=interactions.ButtonStyle.PRIMARY,
                    custom_id="nieaktywnosc2",
                    label="Stoners"
                )
            )
        ]
        await ctx.send("Wybierz swiat", components=components)
    else:
        await ctx.send("Błąd, nie udało sie pobrac id serwera")
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc")

@component_callback("nieaktywnosc1")
async def button_response_1(ctx: ComponentContext):
    swiat = "Narwhals"

    df_col = ({'Nickname':["temp"], 'Lvl':[1000], 'Last online':[5]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
    page = 1
    print("Aa")
    await ctx.defer()
    if(await u.check_data_in_db_absency_last(swiat, ctx)):
        await u.get_data_absency(ctx, df, swiat, link, page)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "nieaktywnosc - Narwhals")

@component_callback("nieaktywnosc2")
async def button_response_2(ctx: ComponentContext):
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
@slash_command(
    name="embed",
    description="Test",
)
async def embed(ctx: SlashContext):
    embed = interactions.Embed(
    title="your title",
    description="your description")
    await ctx.send(embeds = embed)

@slash_command(
    name = "przycisk_test",
    description="Komenda testujaca przyciski"
)
async def przycisk_test(ctx: SlashContext):
    button = Button(
        style=ButtonStyle.PRIMARY,
        custom_id="primary",
        label="Przycisk test"
    )
    await ctx.send("Przykladowy przycisk", components=button)

@component_callback("primary")
async def button_response(ctx: ComponentContext):
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

@component_callback("primary2")
async def button_response(ctx: ComponentContext):
    await ctx.send("Chwała Neeyom")

@component_callback("primary3")
async def button_response(ctx: ComponentContext):
    await ctx.send("Tak nie wolno, chwała Neeyom")
'''



@slash_command(
    name="stworz_baze",
    description="Tworzy baze danych, funkcja tymczasowa do testów",
    scopes= [
        sd.dc_discord_bot_testy
    ],
)
async def stworz_baze(ctx: SlashContext):
    await ctx.send("Tworzę baze danych...")
    try:
        await u.create_database()
        await ctx.send("Baza danych została utworzona")
    except:
        await ctx.send("Baza danych już istnieje")


@slash_command(
    name="tanroth",
    description="Losuje drop z Tanrotha",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def tanroth(ctx: SlashContext):
    print(int(ctx.author.user.id))
    response = await u.check_data_in_db_tanroth_last_update(int(ctx.author.user.id))
    if( response == 1):
        await ctx.send(files=interactions.File("img/Tanroth/" + await u.random_tanroth_item(int(ctx.guild_id), int(ctx.author.user.id)) + ".png"))
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


@slash_command(
    name="online",
    description="Gracze online na wybranym świecie",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="swiat",
            description="Swiat z którego zostaną pobrane dane",
            required=True,
        ),
    ],
)
async def online(ctx: SlashContext, swiat: str):
    result = await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online")

@slash_command(
    name="online_przycisk",
    description="Gracze online na wybranym swiecie ale z przyciskiem",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def online_przycisk(ctx: SlashContext):
    components = [
        interactions.ActionRow(
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="online1",
                label="Narwhals"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="online2",
                label="Stoners"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="online3",
                label="Tarhuna"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="online4",
                label="Fobos"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="online5",
                label="Unia"
            )
        )
    ]
    await ctx.send("Wybierz swiat", components=components)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk")

@component_callback("online1")
async def button_response_online1(ctx: ComponentContext):
    swiat = "Narwhals"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Narwhals")

@component_callback("online2")
async def button_response_online2(ctx: ComponentContext):
    swiat = "Stoners"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Stoners")

@component_callback("online3")
async def button_response_online3(ctx: ComponentContext):
    swiat = "Tarhuna"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Tarhuna")

@component_callback("online4")
async def button_response_online4(ctx: ComponentContext):
    swiat = "Fobos"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Fobos")

@component_callback("online5")
async def button_response_online5(ctx: ComponentContext):
    swiat = "Unia"
    await u.players_online(ctx, swiat)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_przycisk - Unia")

@slash_command(
    name="rejestracja",
    description="Rejestracja konta w Margonem do systemu powiadomień",
    scopes= [
        sd.dc_discord_bot_testy
    ],
)
async def rejestracja(ctx: SlashContext):
    modal = interactions.Modal(
        interactions.ShortText(label="ID konta", custom_id="register_text_input", placeholder="np. 1234567", min_length = 7, max_length = 7, required=True),
        custom_id = "register_modal",
        title = "Podaj id konta w Margonem",
    )
    await ctx.send_modal(modal=modal)

    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
    #await modal_ctx.send(f"""You input {modal_ctx.responses["short_text"]} and {modal_ctx.responses["long_text"]}""")

    try:
        int(modal_ctx.responses["register_text_input"])
    except:
        await modal_ctx.send("Niepoprawne ID", ephemeral=True)
        return
    register_response = requests.get("https://www.margonem.pl/profile/view," + modal_ctx.responses["register_text_input"])
    register_soup = BeautifulSoup(register_response.text, 'html.parser')
    nickname = register_soup.find('div', class_='brown-box profile-header mb-4')
    nickname = nickname.find('h2')
    nickname = nickname.find('span')
    nickname = nickname.string[17:-12]
    print(nickname)
    await u.update_characters_in_game_temp(ctx.author.user.id, nickname)
    components = [
        interactions.ActionRow(
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="register_button_1",
                label="Tak, zapisz"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="register_button_2",
                label="Nie"
            )
        )
    ]
    ctx_msg = await modal_ctx.send("Czy twój nick to " + nickname + "?", components=components, ephemeral=True)
    g.store[ctx.author.user.id] = ctx_msg, ctx

    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "rejestracja")


@component_callback("register_button_1")
async def button_response_register_button1(ctx: ComponentContext):
    msg = g.store[ctx.author.user.id][0]
    ctx_to_delete = g.store[ctx.author.user.id][1]
    await msg.delete(context= ctx_to_delete)
    result = await u.check_data_in_characters_in_game(ctx.guild_id, ctx.author.user.id, await u.select_characters_in_game_temp(ctx.author.user.id))
    if(result == 1):
        ctx_msg = await ctx.send("Zrobione", ephemeral=True)
    else:
        components = [
            interactions.ActionRow(
                interactions.Button(
                    style=interactions.ButtonStyle.PRIMARY,
                    custom_id="register_button_3",
                    label="Tak, zaktualizuj"
                ),
                interactions.Button(
                    style=interactions.ButtonStyle.PRIMARY,
                    custom_id="register_button_4",
                    label="Nie, zostaw obecne"
                )
            )
        ]
        ctx_msg = await ctx.send("Do konta na Discordzie przypisano już konto w grze o nicku " + str(result)+ ". Zaktualizowac dane?", components=components, ephemeral=True)
    g.store[ctx.author.user.id] = ctx_msg, ctx

@component_callback("register_button_2")
async def button_response_register_button2(ctx: ComponentContext):
    msg = g.store[ctx.author.user.id][0]
    ctx_to_delete = g.store[ctx.author.user.id][1]
    await msg.delete(context= ctx_to_delete)
    modal = interactions.Modal(
        interactions.ShortText(label="ID konta", custom_id="register_text_input", placeholder="np. 1234567", min_length = 7, max_length = 7, required=True),
        custom_id = "register_modal",
        title = "Podaj id konta w Margonem",
    )
    await ctx.send_modal(modal=modal)

    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)

    try:
        int(modal_ctx.responses["register_text_input"])
    except:
        await modal_ctx.send("Niepoprawne ID", ephemeral=True)
        return
    register_response = requests.get("https://www.margonem.pl/profile/view," + modal_ctx.responses["register_text_input"])
    register_soup = BeautifulSoup(register_response.text, 'html.parser')
    nickname = register_soup.find('div', class_='brown-box profile-header mb-4')
    nickname = nickname.find('h2')
    nickname = nickname.find('span')
    nickname = nickname.string[17:-12]
    print(nickname)
    await u.update_characters_in_game_temp(ctx.author.user.id, nickname)
    components = [
        interactions.ActionRow(
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="register_button_1",
                label="Tak, zapisz"
            ),
            interactions.Button(
                style=interactions.ButtonStyle.PRIMARY,
                custom_id="register_button_2",
                label="Nie"
            )
        )
    ]
    ctx_msg = await modal_ctx.send("Czy twój nick to " + nickname + "?", components=components, ephemeral=True)
    g.store[ctx.author.user.id] = ctx_msg, ctx

@component_callback("register_button_3")
async def button_response_register_button3(ctx: ComponentContext):
    msg = g.store[ctx.author.user.id][0]
    ctx_to_delete = g.store[ctx.author.user.id][1]
    await msg.delete(context= ctx_to_delete)
    await u.update_characters_in_game(ctx.guild_id, ctx.author.user.id, str(await u.select_characters_in_game_temp(ctx.author.user.id)))
    await ctx.send("Dane zaktualizowane", ephemeral=True)

@component_callback("register_button_4")
async def button_response_register_button4(ctx: ComponentContext):
    msg = g.store[ctx.author.user.id][0]
    ctx_to_delete = g.store[ctx.author.user.id][1]
    await msg.delete(context= ctx_to_delete)
    await ctx.send("Zmiany odrzucone", ephemeral=True)


@slash_command(
    name="moje_dropy",
    description="Wyswietla licznik dropów z serwerowego Tanrotha",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def moje_dropy(ctx: SlashContext):
    try: 
        result = await u.select_all_tanroth_drops(ctx.guild_id, ctx.author.user.id)
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.author.user.username, value="Unikaty: " + str(result[0]) + "\n" + "Heroiki: " + str(result[1]) + "\n" + "Legendy: " + str(result[2]), inline=False)
        await ctx.send(embeds=embed)
    except:
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.author.user.username, value="Unikaty: " + str(0) + "\n" + "Heroiki: " + str(0) + "\n" + "Legendy: " + str(0), inline=False)
        await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "moje_dropy")


@user_context_menu(
    name="Dropy gracza",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def dropy_gracza(ctx: SlashContext):
    try: 
        result = await u.select_all_tanroth_drops(ctx.guild_id, ctx.target.user.id)
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.target.user.username, value="Unikaty: " + str(result[0]) + "\n" + "Heroiki: " + str(result[1]) + "\n" + "Legendy: " + str(result[2]), inline=False)
        await ctx.send(embeds=embed)
    except:
        embed=interactions.Embed(title="Licznik dropów z serwerowego Tanrotha")
        embed.add_field(name="Użytkownik: " + ctx.target.user.username, value="Unikaty: " + str(0) + "\n" + "Heroiki: " + str(0) + "\n" + "Legendy: " + str(0), inline=False)
        await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "Dropy gracza")


@Task.create(interactions.IntervalTrigger(minutes=1))
async def my_task():
    await u.players_online_run_forever("Narwhals")

@Task.create(interactions.IntervalTrigger(minutes=1))
async def look_for_new_item():
    try:
        await u.listen_for_new_items("https://grooove.pl/blade_of_destiny_narwhals/", "bod")
    except:
        pass

@Task.create(interactions.TimeTrigger(hour=9))
async def look_for_new_bans():
    try:
        swiat = "Narwhals"
        df_col = ({'Id':["temp"]})
        df = pd.DataFrame(df_col)
        df = df.drop(df.index[[0]])
        link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
        page = 1
        embed_value = await u.get_data_bans(df, swiat, link, page)
        g.store_bans[sd.dc_bod] = embed_value
    except:
        g.store_bans[sd.dc_bod] = ""

@Task.create(interactions.TimeTrigger(hour=10))
async def present_new_bans():
    embed_value = g.store_bans[sd.dc_bod]
    if(embed_value == ""):
        return
    embed=interactions.Embed(title="Lista ukaranych graczy")
    swiat = "Narwhals"
    try:
        embed.add_field(name="Świat " + swiat, value=embed_value, inline=False)
        channel = bot.get_channel(channel_id=1118856852332085329)
        try:
            await channel.send(embeds = embed)
        except:
            pass
    except:
        try:
            await channel.send(content="Jakiś błąd, prawdopodobnie błąd serwera")
        except:
            pass

@Task.create(interactions.IntervalTrigger(seconds=3))
async def zagadka_delay():
    zagadka_delay.stop()


@slash_command(
    name="online_wykres",
    description="Wykres graczy online z dzisiaj",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="nickname",
            description="Nazwa gracza",
            required=True,
        ),
    ],
)
async def online_wykres(ctx: SlashContext, nickname: str):
    if(await u.select_players_online(nickname)):
        await ctx.send(files=interactions.File("img/df_data/df_data.png"))
    else:
        await ctx.send("Brak danych gracza " + nickname)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "online_wykres")


@slash_command(
    name="timery",
    description="Timery herosów i tytanów na lootlogu",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def timery(ctx: SlashContext):
    embed=interactions.Embed(title="Timery herosów i tytanów")
    try:
        await u.get_timer_alt(embed)
        await ctx.send(embeds=embed)
    except:
        await ctx.send(content="Bład, nie udało się połączyc z serwerem timerów")
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery")


@slash_command(
    name="timery_alt",
    description="Timery herosów i tytanów na lootlogu",
    scopes= [
        sd.dc_discord_bot_testy
    ],
)
async def timery_alt(ctx: SlashContext):
    embed=interactions.Embed(title="Timery herosów i tytanów")
    await u.get_timer_alt(embed)
    await ctx.send(embeds=embed)
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery_alt")


@slash_command(
    name="dodaj_timer",
    description="Dodaje timer na lootlog",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="mob",
            description="Nazwa potwora",
            required=True,
            autocomplete=True
        ),
    ],
)
async def dodaj_timer(ctx: SlashContext, mob: str):
    response = await u.add_timer(ctx, mob)
    if(response == 1):
        await ctx.send("Dodano timer potwora " + mob)
    elif(response == 2):
        await ctx.send("Brak uprawnień do użycia komendy, tymczasowo ograniczone")
    elif(response == 3):
        await ctx.send("Wystąpił błąd")
    #await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "timery")

@dodaj_timer.autocomplete("mob")
async def autocomplete(ctx: AutocompleteContext):
    items = ["Domina Ecclesiae", "Mietek Żul", "Mroczny Patryk", "Karmazynowy Mściciel", "Złodziej", "Zły Przewodnik", "Piekielny Kościej", "Opętany Paladyn", 
             "Kochanka Nocy", "Ksiaze Kasim", "Baca bez łowiec", "Lichwiarz Grauhaz", "Obłąkany łowca orków", "Czarująca Atalia", "Święty Braciszek", "Viviana Nandin", 
             "Mulher Ma", "Demonis Pan Nicości", "Vapor Veneno", "Dęborożec", "Tepeyollotl", "Negthotep Czarny Kapłan", "Młody smok", "Dziewicza Orlica", "Zabojczy Krolik",
             "Renegat Baulus", "Piekielny Arcymag", "Versus Zoons", "Łowczyni Wspomnien", "Przyzywacz Demonow", "Maddok Magua", "Tezcatlipoca", "Barbatos Smoczy Straznik",
             "Tanroth"
             ]
    choices = []
    for item in items:
        if(len(choices) >= 25):
            break
        if ctx.input_text.lower() in item.lower():
            choices.append({"name": item, "value": item})
    await ctx.send(choices=choices)


@slash_command(
    name="czlonkowie_klanow",
    description="Wypisuje w konsoli czlonkow kazdego z klanów na dany przedzial",
    scopes= [
        sd.dc_discord_bot_testy
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="klan",
            description="Nazwa klanu",
            required=True,
        ),
    ],
)
async def czlonkowie_klanow(ctx: SlashContext, klan: str):
    await u.clan_members(ctx, klan)


@slash_command(
    name="test_ping",
    description="Testowy ping",
    scopes= [
        sd.dc_discord_bot_testy
    ],
)
async def test_ping(ctx: SlashContext):
    channel = bot.get_channel(channel_id=987410864946679861)
    msg = "Możliwy Tanroth, " + str(1) + " rosów online"
    await channel.send(content=msg)


@slash_command(
    name="zagadka_admin",
    description="Panel admina do tworzenia zagadek",
    scopes= [
        sd.dc_discord_bot_testy
    ],
)
async def zagadka_admin(ctx: SlashContext):
    #global g.has_quiz_started
    if(int(ctx.author.user.id) not in {349851438228439040, 372381114809188362, 546751756323913754}):
        await ctx.send("Brak uprawnień", ephemeral=True)
        return
    if(int(ctx.channel.id) not in {1085193552864235591, 1083376240783785985}):
        await ctx.send("Użyj komendy w przeznaczonym do tego kanale", ephemeral=True)
        return
    try:
        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete(ctx)
    except:
        print("Whatever")
    if(g.has_quiz_started == 1):
        ctx_msg = await u.quiz_UI_started(ctx)
    else:
        ctx_msg = await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx

@component_callback("add_quiz")
async def button_response_add_quiz(ctx: ComponentContext):
    modal = interactions.Modal(
        interactions.ParagraphText(label="Zagadka", custom_id="add_quiz_modal_zagadka", placeholder="Tu wpisz zagadkę", required=True),
        interactions.ShortText(label="Prawidłowa odpowiedź", custom_id="add_quiz_modal_odpowiedz", placeholder="Tu wpisz odpowiedź", required=True),
        custom_id = "add_quiz_modal",
        title = "Panel dodania nowej zagadki",
    )
    await ctx.send_modal(modal=modal)

    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)

    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete(ctx)
    zagadka = modal_ctx.responses["add_quiz_modal_zagadka"]
    odpowiedz = modal_ctx.responses["add_quiz_modal_odpowiedz"]
    try:
        await u.add_data_in_db_quiz(int(ctx.guild_id), zagadka, odpowiedz)
        await ctx.send(str(ctx.author.user.username) + " pomyślnie dodał(a) zagadkę: " + zagadka)
    except:
        await ctx.send(str(ctx.author.user.username) + " nie udało sie dodać zagadki: " + zagadka)

    if(g.has_quiz_started == 1):
        ctx_msg = await u.quiz_UI_started(ctx)
    else:
        ctx_msg = await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx


@component_callback("delete_one")
async def button_response_delete_one(ctx: ComponentContext):
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete(ctx)
    respone_zagadki = await u.get_data_in_db_quiz(int(ctx.guild_id))
    if(len(respone_zagadki) != 0):
        modal = interactions.Modal(
            interactions.ShortText(label="Numer zagadki którą chcesz usunąć", custom_id="delete_one_modal_odpowiedz", placeholder="Tu wpisz numer", required=True),
            custom_id = "delete_zagadka_modal",
            title = "Panel usuwania wybranej zagadki",
        )
        await ctx.send_modal(modal=modal)

        modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
        numer = modal_ctx.responses["delete_one_modal_odpowiedz"]

        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete(ctx)

        respone_zagadki = await u.get_data_in_db_quiz(int(ctx.guild_id))
        zagadka = respone_zagadki[int(numer)-1][0]
        odpowiedz = respone_zagadki[int(numer)-1][1]
        response = await u.delete_data_in_db_quiz(int(ctx.guild_id), zagadka, odpowiedz)
        if(response == 1):
            await ctx.send(str(ctx.author.user.username) + " Upomyślnie usunął(ęła) zagadkę: " + zagadka)
        elif(response == 2):
            await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
        
        if(g.has_quiz_started == 1):
            ctx_msg = await u.quiz_UI_started(ctx)
        else:
            ctx_msg = await u.quiz_UI(ctx)
        g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx
    else:
        await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    if(g.has_quiz_started == 1):
        ctx_msg = await u.quiz_UI_started(ctx)
    else:
        ctx_msg = await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx


@component_callback("delete_all")
async def button_response_delete_all(ctx: ComponentContext):
    #global g.has_quiz_started
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete(ctx)

    response = await u.delete_all_data_in_db_quiz(int(ctx.guild_id))
    if(response == 1):
         await ctx.send(str(ctx.author.user.username) + " pomyślnie usunął(ęła) wszystkie zagadki")
    elif(response == 2):
         await ctx.send(str(ctx.author.user.username) + " próbował(a) usunąć nieistniejącą zagadkę")
    
    if(g.has_quiz_started == 1):
        ctx_msg = await u.quiz_UI_started(ctx)
    else:
        ctx_msg = await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx


@component_callback("start_quiz")
async def button_response_start_quiz(ctx: ComponentContext):
    #global g.has_quiz_started, quiz_cd, g.current_riddle, g.current_answer, g.quiz_number, g.quiz_task, riddles
    g.quiz_number = 0
    g.has_quiz_started = 1
    g.riddles = await u.get_data_in_db_quiz(int(ctx.guild_id))

    await u.reset_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), "all")

    response_riddles = await u.get_data_in_db_quiz(int(ctx.guild_id))
    await ctx.send(str(ctx.author.user.username) + " rozpoczął(ęła) quiz")

    channel_quiz_start = g.bot.get_channel(channel_id=1064671672822677594)
    if(channel_quiz_start is None):
        channel_quiz_start = g.bot.get_channel(channel_id=1085193552864235591)
    await channel_quiz_start.send(content="Quiz rozpoczął się")
    #g.quiz_task = asyncio.create_task(quiz_sleep(ctx, bot, response_riddles)) #works

    if(g.has_quiz_started == 0):
        return
    if(g.has_quiz_started == 1):
        msg = g.store_quiz_server[ctx.guild.id]
        await msg.delete(ctx)
        ctx_msg = await u.quiz_UI_started(ctx)
        g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx

    #zagadka_delay.start()

    #msg = g.store[ctx.author.user.id]
    #await msg.delete(ctx)


@component_callback("stop_quiz")
async def button_response_stop_quiz(ctx: ComponentContext):
    #global g.has_quiz_started, g.quiz_task
    #msg = g.store[ctx.author.user.id]
    #await msg.delete(ctx)

    #g.quiz_task.cancel() #works

    g.has_quiz_started = 0
    msg = g.store_quiz_server[ctx.guild.id]
    await msg.delete(ctx)
    await ctx.send("Zakończono quiz")

    channel_quiz_start = g.bot.get_channel(channel_id=1064671672822677594)
    if(channel_quiz_start is None):
        channel_quiz_start = g.bot.get_channel(channel_id=1085193552864235591)
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
        ctx_msg = await u.quiz_UI_started(ctx)
    else:
        ctx_msg = await u.quiz_UI(ctx)
    g.store_quiz_server[ctx.guild.id] = ctx_msg, ctx

    #msg = g.store[ctx.author.user.id]
    #await msg.delete(ctx)



@slash_command(
    name="zagadka",
    description="Zagadki",
    scopes= [
        sd.dc_discord_bot_testy
    ],
)
async def zagadka(ctx: SlashContext):
    #global g.has_quiz_started, g.current_answer, riddles, channel_quiz
    if(1084883485736583248 in ctx.author.roles or 1084925145195491410 in ctx.author.roles):
        if(g.has_quiz_started == 1):
            '''
            has_won = await check_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), ctx.author.user.username, int(ctx.author.user.discriminator))
            #print(has_won)
            if(has_won == 0):
                modal = interactions.Modal(
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
                modal = interactions.Modal(
                    interactions.ShortText(label=g.riddles[wins + losts][0], custom_id="answer_quiz_modal_odpowiedz", placeholder = "Miejsce na odpowiedź", required=True),
                    custom_id = "answer_quiz_modal",
                    title = "Formularz odpowiedzi na zagadkę",
                )
                await ctx.send_modal(modal=modal)
                modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
                odp = modal_ctx.responses["answer_quiz_modal_odpowiedz"]

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

                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle",
                                label="Następna zagadka"
                            )
                        )
                    ]

                    await ctx.send("Prawidłowa odpowiedź", components=components, ephemeral=True)
                    await g.channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
                    #print(user_data)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
                else:
                    if(tried >= 3):
                        tried = 0
                        losts = losts + 1
                        components = [
                            interactions.ActionRow(
                                interactions.Button(
                                    style=interactions.ButtonStyle.PRIMARY,
                                    custom_id="next_riddle",
                                    label="Następna zagadka"
                                )
                            )
                        ]
                        await ctx.send("Nieprawidłowa odpowiedź, limit prób przekroczony", components=components, ephemeral=True)
                        await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
                    else:
                        components = [
                            interactions.ActionRow(
                                interactions.Button(
                                    style=interactions.ButtonStyle.PRIMARY,
                                    custom_id="restart_quiz",
                                    label="Spróbuj ponownie"
                                ),
                                interactions.Button(
                                    style=interactions.ButtonStyle.PRIMARY,
                                    custom_id="next_riddle_abandon",
                                    label="Następna zagadka"
                                )
                            )
                        ]
                        await ctx.send("Nieprawidłowa odpowiedź", components=components, ephemeral=True)
                        await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

                g.store_quiz_user[ctx.author.user.id] = ctx

            else:
                await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
                quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
                quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
                await g.channel_quiz.send(content=quiz_result_str)


        else:
            await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)
        #g.store[ctx.author.user.id] = ctx_msg
    else:
        await ctx.send("Nie masz uprawnień do wzięcia udziału w zagadce", ephemeral=True)

@component_callback("restart_quiz")
async def button_response_restart_quiz(ctx: ComponentContext):
    msg = g.store_quiz_user[ctx.author.user.id]
    await msg.delete(ctx)

    if(g.has_quiz_started == 1):
        user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(g.riddles)-1):
            modal = interactions.Modal(
                interactions.ShortText(label=g.riddles[wins + losts][0], custom_id="answer_quiz_modal_odpowiedz", placeholder = "Miejsce na odpowiedź", required = True),
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
            )
            await ctx.send_modal(modal=modal)
            modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
            odp = modal_ctx.responses["answer_quiz_modal_odpowiedz"]

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

                components = [
                    interactions.ActionRow(
                        interactions.Button(
                            style=interactions.ButtonStyle.PRIMARY,
                            custom_id="next_riddle",
                            label="Następna zagadka"
                        )
                    )
                ]

                await ctx.send("Prawidłowa odpowiedź", components=components, ephemeral=True)
                await g.channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
                #print(user_data)
                await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
            else:
                if(tried >= 3):
                    tried = 0
                    losts = losts + 1
                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle",
                                label="Następna zagadka"
                            )
                        )
                    ]
                    await ctx.send("Nieprawidłowa odpowiedź, limit prób przekroczony", components=components, ephemeral=True)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
                else:
                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="restart_quiz",
                                label="Spróbuj ponownie"
                            ),
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle_abandon",
                                label="Następna zagadka"
                            )
                        )
                    ]
                    await ctx.send("Nieprawidłowa odpowiedź", components=components, ephemeral=True)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

            g.store_quiz_user[ctx.author.user.id] = ctx

        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await g.channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)



@component_callback("next_riddle")
async def button_response_next_riddle(ctx: ComponentContext):
    #global g.has_quiz_started, g.current_answer, channel_quiz

    msg = g.store_quiz_user[ctx.author.user.id]
    await msg.delete(ctx)

    if(g.has_quiz_started == 1):
        user_data = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
        user_data = user_data[0]
        #tried = int(user_data[4])
        wins = int(user_data[6])
        losts = int(user_data[7])

        if(wins + losts <= len(g.riddles)-1):
            modal = interactions.Modal(
                interactions.ShortText(label=g.riddles[wins + losts][0], custom_id="answer_quiz_modal_odpowiedz", placeholder = "Miejsce na odpowiedź", required = True),
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
            )
            await ctx.send_modal(modal=modal)
            modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
            odp = modal_ctx.responses["answer_quiz_modal_odpowiedz"]

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

                components = [
                    interactions.ActionRow(
                        interactions.Button(
                            style=interactions.ButtonStyle.PRIMARY,
                            custom_id="next_riddle",
                            label="Następna zagadka"
                        )
                    )
                ]

                await ctx.send("Prawidłowa odpowiedź", components=components, ephemeral=True)
                await g.channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
                #print(user_data)
                await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
            else:
                if(tried >= 3):
                    tried = 0
                    losts = losts + 1
                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle",
                                label="Następna zagadka"
                            )
                        )
                    ]
                    await ctx.send("Nieprawidłowa odpowiedź, limit prób przekroczony", components=components, ephemeral=True)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
                else:
                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="restart_quiz",
                                label="Spróbuj ponownie"
                            ),
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle_abandon",
                                label="Następna zagadka"
                            )
                        )
                    ]
                    await ctx.send("Nieprawidłowa odpowiedź", components=components, ephemeral=True)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

            g.store_quiz_user[ctx.author.user.id] = ctx
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await g.channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)



@component_callback("next_riddle_abandon")
async def button_response_next_riddle_abandon(ctx: ComponentContext):
    #global g.has_quiz_started, g.current_answer, channel_quiz

    msg = g.store_quiz_user[ctx.author.user.id]
    await msg.delete(ctx)

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
            modal = interactions.Modal(
                interactions.ShortText(label=g.riddles[wins + losts][0], custom_id="answer_quiz_modal_odpowiedz", placeholder = "Miejsce na odpowiedź", required = True),
                custom_id = "answer_quiz_modal",
                title = "Formularz odpowiedzi na zagadkę",
            )
            await ctx.send_modal(modal=modal)
            modal_ctx: ModalContext = await ctx.bot.wait_for_modal(modal)
            odp = modal_ctx.responses["answer_quiz_modal_odpowiedz"]

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

                components = [
                    interactions.ActionRow(
                        interactions.Button(
                            style=interactions.ButtonStyle.PRIMARY,
                            custom_id="next_riddle",
                            label="Następna zagadka"
                        )
                    )
                ]

                await ctx.send("Prawidłowa odpowiedź", components=components, ephemeral=True)
                await g.channel_quiz.send(content=str(ctx.author.user.username) + " udzielił(a) poprawnej odpowiedzi, + 1 punkt")
                #print(user_data)
                await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
            else:
                if(tried >= 3):
                    tried = 0
                    losts = losts + 1
                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle",
                                label="Następna zagadka"
                            )
                        )
                    ]
                    await ctx.send("Nieprawidłowa odpowiedź, limit prób przekroczony", components=components, ephemeral=True)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)
                else:
                    components = [
                        interactions.ActionRow(
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="restart_quiz",
                                label="Spróbuj ponownie"
                            ),
                            interactions.Button(
                                style=interactions.ButtonStyle.PRIMARY,
                                custom_id="next_riddle_abandon",
                                label="Następna zagadka"
                            )
                        )
                    ]
                    await ctx.send("Nieprawidłowa odpowiedź", components=components, ephemeral=True)
                    await u.update_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id), tried, points, wins, losts)

            g.store_quiz_user[ctx.author.user.id] = ctx
        else:
            await ctx.send("Udzieliłeś(aś) odpowiedzi na wszystkie zagadki", ephemeral=True)
            quiz_result = await u.get_data_in_db_quiz_results(int(ctx.guild_id), int(ctx.author.user.id))
            quiz_result_str = str(quiz_result[0][2]) + "#" + str(quiz_result[0][3]) + " - Punkty: " + str(quiz_result[0][5])
            await g.channel_quiz.send(content=quiz_result_str)

    else:
        await ctx.send("Żaden quiz nie jest obecnie aktywny", ephemeral=True)


@slash_command(
    name="generuj_obrazek",
    description="Generuje obrazek z wynikami losowania",
    scopes= [
        sd.dc_discord_bot_testy,
    ],
)
async def generuj_obrazek(ctx: SlashContext):
    await u.generate_image()


@slash_command(
    name="konkurs",
    description="Wyniki konkursu Łowcy herosów",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
)
async def konkurs(ctx: SlashContext):
    embed=interactions.Embed(title="Wyniki konkursu Łowcy herosów")
    await u.get_google_sheets_data(ctx, embed)
    await ctx.send(embeds=embed)


@slash_command(
    name="hti",
    description="HTML to image",
    scopes= [
        sd.dc_discord_bot_testy
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="link",
            description="Link do przedmiotu ze strony margohelp.pl",
            required=True,
        ),
        interactions.SlashCommandOption(
            type=interactions.OptionType.INTEGER,
            name="poziom",
            description="Poziom na który ulepszyć przedmiot",
            required=True,
        ),
    ],
)
async def hti(ctx: SlashContext, link: str, poziom: int):
    await u.generate_image_from_html(link, poziom)


@slash_command(
    name="posty",
    description="Posty",
    scopes= [
        sd.dc_discord_bot_testy,
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="link",
            description="Link",
            required=True,
        ),
    ]
)
async def posty(ctx: SlashContext, link: str):
    await u.follow_posts(link)


@slash_command(
    name="nowe_itemy",
    description="Nowe itemy",
    scopes= [
        sd.dc_discord_bot_testy,
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="link",
            description="Link",
            required=True,
        ),
    ]
)
async def nowe_itemy(ctx: SlashContext, link: str):
    await u.listen_for_new_items(link, "bod")


@slash_command(
    name="e2_lista",
    description="Lista e2",
    scopes= [
        sd.dc_discord_bot_testy,
    ],
)
async def e2_lista(ctx: SlashContext):
    await u.e2_list()


@slash_command(
    name="obrazek_legenda",
    description="Obrazek legenda",
    scopes= [
        sd.dc_discord_bot_testy,
    ],
)
async def obrazek_legenda(ctx: SlashContext):
    await u.generate_image_when_legendary("Neeyo", "Jakas legenda", "Jakis potwor", 5)
    channel_last_item = g.bot.get_channel(channel_id=1064671672822677594)
    if(channel_last_item is None):
        channel_last_item = g.bot.get_channel(channel_id=1085193552864235591)
    await channel_last_item.send(files=interactions.File("img/legendary/" + "Neeyo" + ".png"))


@slash_command(
    name="kary",
    description="Wyświetla liste ukaranych graczy na świecie",
    scopes= [
        sd.dc_discord_bot_testy,
    ],
)
async def kary(ctx: SlashContext):
    swiat = "Narwhals"

    df_col = ({'Id':["temp"]})
    df = pd.DataFrame(df_col)
    df = df.drop(df.index[[0]])
    link = "https://www.margonem.pl/ladder/players,"+ swiat +"?page="
    page = 1

    await ctx.send("Przez zlagowane serwery proces może zająć wiele minut, odpowiem gdy skończę")

    embed=interactions.Embed(title="Lista ukaranych graczy")
    try:
        embed_value = await u.get_data_bans(df, swiat, link, page)
        embed.add_field(name="Świat " + swiat, value=embed_value, inline=False)
        try:
            channel = bot.get_channel(channel_id=1085193552864235591)
            await channel.send(embeds = embed)
        except:
            pass
    except:
        try:
            channel = bot.get_channel(channel_id=1085193552864235591)
            await channel.send(content="Jakiś błąd, prawdopodobnie błąd serwera")
        except:
            pass
    await u.save_logs(ctx.guild_id, ctx.author.user.id, ctx.author.user.username, ctx.author.user.discriminator, "kary - Narwhals")


@slash_command(
    name="dodaj_wiadomosc_przez_ll",
    description="Dodaje wiadomosc przez ll",
    scopes= [
        sd.dc_discord_bot_testy,
        sd.dc_bod
    ],
    options = [
        interactions.SlashCommandOption(
            type=interactions.OptionType.STRING,
            name="message",
            description="Wiadomość",
            required=True
        ),
    ],
)
async def dodaj_wiadomosc_przez_ll(ctx: SlashContext, message: str):
    response = await u.send_message_via_ll(ctx, message)
    if(response == 1):
        await ctx.send("Pomyślnie wysłano wiadomość: " + message)
    elif(response == 2):
        await ctx.send("Brak uprawnień do użycia komendy, tymczasowo ograniczone")
    elif(response == 3):
        await ctx.send("Wystąpił błąd")



bot.start(token = my_token)